from ultralytics import YOLO

YOLO("yolo26s-pose-best.pt").predict(
    source=0,
    show=True,
    save=True,
    project="webcam",
    name="test",
)
