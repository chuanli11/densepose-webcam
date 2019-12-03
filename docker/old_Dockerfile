# Use Caffe2 image as parent image
FROM caffe2/caffe2:snapshot-py2-cuda9.0-cudnn7-ubuntu16.04

RUN mv /usr/local/caffe2 /usr/local/caffe2_build
ENV Caffe2_DIR /usr/local/caffe2_build

ENV PYTHONPATH /usr/local/caffe2_build:${PYTHONPATH}
ENV LD_LIBRARY_PATH /usr/local/caffe2_build/lib:${LD_LIBRARY_PATH}

# Clone the Detectron repository
RUN git clone https://github.com/chuanli11/densepose-webcam.git /densepose-webcam

# Install Python dependencies
RUN sed -i "s|pyyaml>=3.12|pyyaml==3.12|g" /densepose-webcam/requirements.txt
RUN pip install -r /densepose-webcam/requirements.txt

# Install the COCO API
RUN git clone https://github.com/cocodataset/cocoapi.git /cocoapi
WORKDIR /cocoapi/PythonAPI
RUN make install

# Go to Densepose root
WORKDIR /densepose-webcam

# Set up Python modules
RUN make

# [Optional] Build custom ops
RUN make ops