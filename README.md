# Yolo v4, v3 and v2 for Windows and Linux

## (neural networks for object detection)

Paper YOLO v4: https://arxiv.org/abs/2004.10934

Paper Scaled YOLO v4: * **[CVPR 2021](https://openaccess.thecvf.com/content/CVPR2021/html/Wang_Scaled-YOLOv4_Scaling_Cross_Stage_Partial_Network_CVPR_2021_paper.html)**: use to reproduce results: [ScaledYOLOv4](https://github.com/WongKinYiu/ScaledYOLOv4)

More details in articles on medium:

- [Scaled_YOLOv4](https://alexeyab84.medium.com/scaled-yolo-v4-is-the-best-neural-network-for-object-detection-on-ms-coco-dataset-39dfa22fa982?source=friends_link&sk=c8553bfed861b1a7932f739d26f487c8)
- [YOLOv4](https://medium.com/@alexeyab84/yolov4-the-most-accurate-real-time-neural-network-on-ms-coco-dataset-73adfd3602fe?source=friends_link&sk=6039748846bbcf1d960c3061542591d7)

Manual: https://github.com/AlexeyAB/darknet/wiki

Fork of https://github.com/AlexeyAB/darknet

### How to compile on Linux/macOS (using `CMake`)

The `CMakeLists.txt` will attempt to find installed optional dependencies like CUDA, cudnn, ZED and build against those. It will also create a shared object library file to use `darknet` for code development.

To update CMake on Ubuntu, it's better to follow guide here: https://apt.kitware.com/ or https://cmake.org/download/

```bash
git clone https://github.com/alex1075/darknet.git
cd darknet
mkdir build_release
cd build_release
cmake ..
cmake --build . --target install --parallel 8
```
