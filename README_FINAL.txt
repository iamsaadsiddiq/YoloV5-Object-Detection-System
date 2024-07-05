YOLOv5 Object Detection System:

YOLOv5 Object Detection System is an advanced solution for detecting and quantifying objects across various media formats including images, videos, directories, webcams, and streaming sources. Powered by Ultralytics YOLOv5, this system employs deep learning techniques and convolutional neural networks (CNNs) for accurate and real-time object detection.

Features
Multi-Source Compatibility: Supports images, videos, directories, webcams, and streaming sources like YouTube and RTSP streams.
Flexible Model Deployment: Compatible with PyTorch, TorchScript, ONNX, OpenVINO, and other optimized configurations.

Customizable Inference Parameters: Adjust confidence thresholds, NMS IOU thresholds, and maximum detections per image for tailored performance.

Visualization and Output Options: Visualize detections, save results in CSV and text formats, and store images and videos locally.
Advanced Post-Processing: Implements non-maximum suppression (NMS) for accurate bounding box detections and annotation.

Ensure that you have the following libraries installed:

torch
opencv-python
matplotlib
numpy
scipy
tqdm
pyyaml
tensorboard
thop

Running Inference
To run object detection on different sources (images, videos, webcams, etc.), use the detect.py script:
python detect.py --weights yolov5s.pt --source path/to/your/input --imgsz 640 --conf-thres 0.25 --iou-thres 0.45

Replace yolov5s.pt with the appropriate model weights file and adjust parameters as needed.

Configuring Options
--weights: Path to the YOLOv5 model weights file.
--source: Path to the input source (image file, video file, directory, webcam, or stream URL).
--imgsz: Inference size (height, width) in pixels.
--conf-thres: Confidence threshold for detections.
--iou-thres: IOU threshold for non-maximum suppression.
Additional options such as saving results (--save-txt, --save-csv), visualization (--view-img), and more can be configured as per your requirements.
Contributing
Contributions are welcome! Please fork the repository and create a pull request with your improvements, bug fixes, or new features.

License
This project is licensed under the AGPL-3.0 License. See the LICENSE file for more details.

Acknowledgments
This project utilizes the YOLOv5 model implementation from Ultralytics.

Special thanks to the open-source community for their contributions and support.

Contact:
For questions or feedback, please feel free to reach out via email at musaad03@gmail.com