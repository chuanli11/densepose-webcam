FROM nvidia/cuda:10.0-cudnn7-devel-ubuntu16.04

RUN apt-get -y update
RUN apt-get install -y --no-install-recommends \
      build-essential \
      git \
      libgoogle-glog-dev \
      libgtest-dev \
      libiomp-dev \
      libleveldb-dev \
      liblmdb-dev \
      libopencv-dev \
      libopenmpi-dev \
      libsnappy-dev \
      libprotobuf-dev \
      openmpi-bin \
      openmpi-doc \
      protobuf-compiler \
      python-dev \
      python-pip   
RUN pip install setuptools                       
RUN pip install --user \
      future \
      numpy==1.14.6 \
      protobuf \
      typing \
      hypothesis
RUN apt-get install -y --no-install-recommends \
      libgflags-dev \
      cmake

RUN git clone --branch master --recursive https://github.com/pytorch/pytorch.git
RUN pip install typing pyyaml
WORKDIR /pytorch
RUN git submodule update --init --recursive
RUN python setup.py install

RUN git clone https://github.com/chuanli11/densepose-webcam.git /densepose-webcam

# Install Python dependencies
RUN pip install -U pip
RUN sed -i "s|pyyaml>=3.12|pyyaml==3.12|g" /densepose-webcam/requirements.txt
RUN pip install -r /densepose-webcam/requirements.txt

# Install the COCO API
RUN git clone https://github.com/cocodataset/cocoapi.git /cocoapi
WORKDIR /cocoapi/PythonAPI

ENV PYTHONPATH /usr/local
ENV Caffe2_DIR=/usr/local/lib/python2.7/dist-packages/torch/share/cmake/Caffe2/
ENV PYTHONPATH=${PYTHONPATH}:/pytorch/build
ENV LD_LIBRARY_PATH=/usr/local/lib:${LD_LIBRARY_PATH}

ENV LD_LIBRARY_PATH=/usr/local/lib/python2.7/dist-packages/torch/lib/:${LD_LIBRARY_PATH}
ENV LIBRARY_PATH=/usr/local/lib/python2.7/dist-packages/torch/lib/:${LIBRARY_PATH}

ENV C_INCLUDE_PATH=/usr/local/lib/python2.7/dist-packages/torch/lib/include/:${C_INCLUDE_PATH}
ENV CPLUS_INCLUDE_PATH=/usr/local/lib/python2.7/dist-packages/torch/lib/include/:${CPLUS_INCLUDE_PATH}

ENV C_INCLUDE_PATH=/pytorch/:${C_INCLUDE_PATH}
ENV CPLUS_INCLUDE_PATH=/pytorch/:${CPLUS_INCLUDE_PATH}

ENV C_INCLUDE_PATH=/pytorch/build/:${C_INCLUDE_PATH}
ENV CPLUS_INCLUDE_PATH=/pytorch/build/:${CPLUS_INCLUDE_PATH}

ENV C_INCLUDE_PATH=/pytorch/torch/lib/include/:${C_INCLUDE_PATH}
ENV CPLUS_INCLUDE_PATH=/pytorch/torch/lib/include/:${CPLUS_INCLUDE_PATH}

RUN make install
WORKDIR /densepose-webcam

RUN make

RUN apt-get -y update \
    && apt-get -y install \
        wget \
        software-properties-common

WORKDIR /densepose-webcam/DensePoseData
RUN bash get_densepose_uv.sh

WORKDIR /densepose-webcam