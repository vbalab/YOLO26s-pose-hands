<div align="center">

# Hand Pose Detection

<img src="docs/hands.gif" alt="hands" width="640"/>
<img src="docs/hand-landmarks.jpg" alt="landmarks" width="640" />

<br>

</div>

## Weights

> [Download](yolo26s-pose-best.pt) YOLO26s-pose fine-tuned for hand pose detection.

## How to run yourself

Clone the repository:

```bash
git clone https://github.com/vbalab/YOLO26s-pose-hands.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the webcam test on your machine (_no GPU needed_) with your webcam:

```bash
python webcam_test.py
```

Test videos are saved to `/runs/pose/webcam/<#>.mp4`.

## How it was trained

The model itself is pretrained [Ultralytics YOLO26](https://docs.ultralytics.com/models/yolo26/#supported-tasks-and-modes) finetuned for hand pose detection using their own [dataset](https://docs.ultralytics.com/datasets/pose/hand-keypoints/).

To see details of training look at the [notebook](train.ipynb) and files of the [results](runs/pose/train/).

<div align="center">

### Enjoy!

<img src="docs/bros.gif" alt="bros" width="640"/>

</div>
