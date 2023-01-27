# SageMaker PyTorch image
FROM 763104351884.dkr.ecr.ap-south-1.amazonaws.com/pytorch-inference:1.12.1-cpu-py38-ubuntu20.04-sagemaker

WORKDIR /opt/ml
ENV PATH="/opt/ml/model/code:${PATH}"

# this environment variable is used by the SageMaker PyTorch container to determine our user code directory.
ENV SAGEMAKER_SUBMIT_DIRECTORY /opt/ml/model/code

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt && rm -rf /root/.cache/pip
COPY infer.py model/code/

# Defines cifar10.py as script entrypoint
ENV SAGEMAKER_PROGRAM infer.py
