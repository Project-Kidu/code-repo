# SageMaker PyTorch image
FROM 763104351884.dkr.ecr.ap-south-1.amazonaws.com/pytorch-inference:1.12.1-cpu-py38-ubuntu20.04-sagemaker

WORKDIR /opt/ml

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt && rm -rf /root/.cache/pip
