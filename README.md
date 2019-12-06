Clone of Densepose for webcam inference

Please refer to the original repository for installation and syntax.

To run:
1. Download the models
2. python tools/infer_webcam2.py --cfg configs/DensePose_ResNet101_FPN_s1x-e2e.yaml --wts models/DensePose_ResNet101_FPN_s1x-e2e.pkl


## Lambda Notes

#### Install Nivida docker

```
./install_nvidia_docker.sh

sudo reboot
```

#### Build from Scratch

```
git clone https://github.com/chuanli11/densepose-webcam.git
cd densepose-webcam/DensePoseData
bash get_densepose_uv.sh

# Build docker image takes three hours on a TensorBook
cd .. 
cd docker
docker build --no-cache -t densepose-webcam:c2-cuda10-cudnn7 . 

cd ..
cd models
wget https://dl.fbaipublicfiles.com/densepose/DensePose_ResNet50_FPN_s1x-e2e.pkl
```

#### Usage


__Quick demo__

```
xhost + 

nvidia-docker run --rm -v /home/ubuntu/densepose-webcam/DensePoseData:/denseposedata -v /home/ubuntu/densepose-webcam/models:/models -v /home/ubuntu/densepose-webcam/update:/densepose-webcam/neurips -v /home/ubuntu/densepose-webcam/update:/update -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix --device=/dev/video0:/dev/video0 --env QT_X11_NO_MITSHM=1 -it densepose-webcam:c2-cuda10-cudnn7

cp /update/texture_from_SURREAL_2.png DensePoseData/demo_data/texture_from_SURREAL.png & cp /update/vis.py detectron/utils/ & cp /update/test.py detectron/core/ & python neurips/infer_webcam_fast2.py --cfg configs/DensePose_ResNet50_FPN_s1x-e2e.yaml --wts /models/DensePose_ResNet50_FPN_s1x-e2e.pkl --scaler_down 0.5 --scaler_up 1.0
```

__Change Texture__

Add new texture to `update/new_texture.png`. Overwrite the texture when running the webcam demo. 

```
cp /update/new_texture.png DensePoseData/demo_data/texture_from_SURREAL.png & cp /update/vis.py detectron/utils/ & cp /update/test.py detectron/core/ & python neurips/infer_webcam_fast2.py --cfg configs/DensePose_ResNet50_FPN_s1x-e2e.yaml --wts /models/DensePose_ResNet50_FPN_s1x-e2e.pkl --scaler_down 0.5 --scaler_up 1.0
```

For example

```
# Pen and Ink
cp /update/texture_from_SURREAL_penink.png DensePoseData/demo_data/texture_from_SURREAL.png & cp /update/vis.py detectron/utils/ & cp /update/test.py detectron/core/ & python neurips/infer_webcam_fast2.py --cfg configs/DensePose_ResNet50_FPN_s1x-e2e.yaml --wts /models/DensePose_ResNet50_FPN_s1x-e2e.pkl --scaler_down 0.5 --scaler_up 1.0

# Color painting
cp /update/texture_from_SURREAL_color.png DensePoseData/demo_data/texture_from_SURREAL.png & cp /update/vis.py detectron/utils/ & cp /update/test.py detectron/core/ & python neurips/infer_webcam_fast2.py --cfg configs/DensePose_ResNet50_FPN_s1x-e2e.yaml --wts /models/DensePose_ResNet50_FPN_s1x-e2e.pkl --scaler_down 0.5 --scaler_up 1.0

# Simple Texture
cp /update/texture_from_SURREAL_simple.png DensePoseData/demo_data/texture_from_SURREAL.png & cp /update/vis.py detectron/utils/ & cp /update/test.py detectron/core/ & python neurips/infer_webcam_fast2.py --cfg configs/DensePose_ResNet50_FPN_s1x-e2e.yaml --wts /models/DensePose_ResNet50_FPN_s1x-e2e.pkl --scaler_down 0.5 --scaler_up 1.0
```

Notice the `update` folder on the host is mounted as the `neurips` folder in the container. The change automatically takes effect without exiting the running container.

__Change Detection Resolution__


Simply change the `scaler_down` (default 0.5) and `scaler_up` (default 1.0) parameters to run the script. For example, setting `scaler_down=0.5` and `scaler_up=2.0` will downsample the image by a factor of 0.5, then upsample the rendered result by a factor of `2.0 / 0.5 = 4`.

```
cp /update/new_texture.png DensePoseData/demo_data/texture_from_SURREAL.png & cp /update/vis.py detectron/utils/ & cp /update/test.py detectron/core/ & python neurips/infer_webcam_fast2.py --cfg configs/DensePose_ResNet50_FPN_s1x-e2e.yaml --wts /models/DensePose_ResNet50_FPN_s1x-e2e.pkl --scaler_down 0.5 --scaler_up 2.0
```
