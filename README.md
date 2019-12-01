Clone of Densepose for webcam inference

Please refer to the original repository for installation and syntax.

To run:
1. Download the models
2. python tools/infer_webcam2.py --cfg configs/DensePose_ResNet101_FPN_s1x-e2e.yaml --wts models/DensePose_ResNet101_FPN_s1x-e2e.pkl


Lambda Notes

```
cd docker
docker build -t densepose-webcam:c2-cuda9-cudnn7 . 

nvidia-docker run -v /home/ubuntu/densepose-webcam/DensePoseData:/denseposedata -v /home/ubuntu/data/coco:/coco -it densepose-webcam:c2-cuda9-cudnn7 bash

mv /densepose-webcam/DensePoseData /densepose-webcam/DensePoseDataLocal
ln -s /denseposedata DensePoseData

ln -s /coco /densepose-webcam/detectron/datasets/data/coco
ln -s /densepose-webcam/DensePoseData/DensePose_COCO/densepose_coco_2014_minival.json /densepose-webcam/detectron/datasets/data/coco/annotations/
ln -s /densepose-webcam/DensePoseData/DensePose_COCO/densepose_coco_2014_train.json /densepose-webcam/detectron/datasets/data/coco/annotations/
ln -s /densepose-webcam/DensePoseData/DensePose_COCO/densepose_coco_2014_valminusminival.json /densepose-webcam/detectron/datasets/data/coco/annotations/

# exit


docker commit $(docker ps --last 1 -q) densepose:c2-cuda9-cudnn7-wdata

xhost + 

nvidia-docker run --rm -v /home/ubuntu/densepose-webcam/DensePoseData:/denseposedata -v /home/ubuntu/data/coco:/coco -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix --device=/dev/video0:/dev/video0 --env QT_X11_NO_MITSHM=1 -it densepose:c2-cuda9-cudnn7-wdata 

# Turing GPU seems to be problematic
CUDA_VISIBLE_DEVICES=1 python tools/infer_webcam2.py --cfg configs/DensePose_ResNet101_FPN_s1x-e2e.yaml --wts https://dl.fbaipublicfiles.com/densepose/DensePose_ResNet101_FPN_s1x-e2e.pkl
```