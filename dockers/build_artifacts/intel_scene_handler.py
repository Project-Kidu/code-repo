import base64
import io

import torch
import torch.nn.functional as F
import torchvision.transforms as T
from PIL import Image
from ts.torch_handler.vision_handler import VisionHandler
from ts.utils.util import map_class_to_label


class ImageClassifier(VisionHandler):
    """ImageClassifier handler class.

    This handler takes an image and returns the name of object in that image.
    """

    topk = 6
    # These are the standard Imagenet dimensions
    # and statistics
    image_processing = T.Compose(
        [
            T.ToTensor(),
            T.Resize((224, 224)),
            T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ]
    )

    def set_max_result_classes(self, topk):
        self.topk = topk

    def get_max_result_classes(self):
        return self.topk

    def preprocess(self, data):
        """The preprocess function of MNIST program converts the input data to a float tensor.

        Args:
            data (List): Input data from the request is in the form of a Tensor

        Returns:
            list : The preprocess function returns the input image as a list of float tensors.
        """
        images = []

        for row in data:
            # Compat layer: normally the envelope should just return the data
            # directly, but older versions of Torchserve didn't have envelope.
            image = row.get("data") or row.get("body")

            if isinstance(image, str):
                # if the image is a string of bytesarray.
                image = base64.b64decode(image)

            # If the image is sent as bytesarray
            if isinstance(image, (bytearray, bytes)):
                image = Image.open(io.BytesIO(image))
                image = image.convert("RGB")
                image = self.image_processing(image)
            else:
                # if the image is a list
                image = torch.FloatTensor(image)

            images.append(image)

        return torch.stack(images).to(self.device)

    def postprocess(self, data):
        ps = F.softmax(data, dim=-1)
        probs, classes = torch.topk(ps, self.topk, dim=1)
        probs = probs.tolist()
        classes = classes.tolist()
        return map_class_to_label(probs, self.mapping, classes)
