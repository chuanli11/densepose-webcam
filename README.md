Clone of Densepose for webcam inference

Please refer to the original repository for installation and syntax.

To run:
1. Download the models
2. python tools/infer_webcam2.py --cfg configs/DensePose_ResNet101_FPN_s1x-e2e.yaml --wts models/DensePose_ResNet101_FPN_s1x-e2e.pkl


Lambda Notes



Build from Scratch

```
git clone https://github.com/chuanli11/densepose-webcam.git
cd densepose-webcam/DensePoseData
bash get_densepose_uv.sh

cd .. 
cd docker
docker build --no-cache -t densepose-webcam:c2-cuda10-cudnn7 . 

cd ..
cd models
wget https://dl.fbaipublicfiles.com/densepose/DensePose_ResNet50_FPN_s1x-e2e.pkl


xhost + 

nvidia-docker run --rm -v /home/ubuntu/densepose-webcam/DensePoseData:/denseposedata -v /home/ubuntu/densepose-webcam/models:/models -v /home/ubuntu/densepose-webcam/update:/densepose-webcam/neurips -v /home/ubuntu/densepose-webcam/update:/update -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix --device=/dev/video0:/dev/video0 --env QT_X11_NO_MITSHM=1 -it densepose-webcam:c2-cuda10-cudnn7

cp /update/texture_from_SURREAL_2.png DensePoseData/demo_data/texture_from_SURREAL.png & cp /update/vis.py detectron/utils/ & cp /update/test.py detectron/core/ & python neurips/infer_webcam_fast2.py --cfg configs/DensePose_ResNet50_FPN_s1x-e2e.yaml --wts /models/DensePose_ResNet50_FPN_s1x-e2e.pkl

22:18 start
```



```
cd docker
docker build -t densepose-webcam:c2-cuda10-cudnn7 . 

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

nvidia-docker run --rm -v /home/ubuntu/densepose-webcam/DensePoseData:/denseposedata -v /home/ubuntu/densepose-webcam/models:/models -v /home/ubuntu/densepose-webcam/update:/update -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix --device=/dev/video0:/dev/video0 --env QT_X11_NO_MITSHM=1 -it densepose:c2-cuda9-cudnn7-wdata 

python tools/infer_webcam2.py --cfg configs/DensePose_ResNet50_FPN_s1x-e2e.yaml --wts https://dl.fbaipublicfiles.com/densepose/DensePose_ResNet50_FPN_s1x-e2e.pkl




python tools/infer_webcam2.py --cfg configs/DensePose_ResNet50_FPN_s1x-e2e.yaml --wts /models/DensePose_ResNet50_FPN_s1x-e2e.pkl

# To update, edit the script in the update folder on host, then recopy to tools in the container
cp /update/infer_webcam2.py tools/
```



nvidia-docker run --rm -v /home/ubuntu/densepose-webcam/DensePoseData:/denseposedata -v /home/ubuntu/densepose-webcam/models:/models -v /home/ubuntu/densepose-webcam/update:/densepose-webcam/neurips -v /home/ubuntu/densepose-webcam/update:/update -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix --device=/dev/video0:/dev/video0 --env QT_X11_NO_MITSHM=1 -it densepose:c2-cuda9-cudnn7-wdata 

python neurips/infer_webcam_fast2.py --cfg configs/DensePose_ResNet50_FPN_s1x-e2e.yaml --wts /models/DensePose_ResNet50_FPN_s1x-e2e.pkl

python neurips/infer_webcam_fast2.py --cfg configs/DensePose_ResNet50_FPN.yaml --wts /models/DensePose_ResNet50_FPN.pkl





cp /update/vis.py detectron/utils/

cp /update/test.py detectron/core/