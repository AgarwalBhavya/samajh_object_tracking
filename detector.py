# detector.py
from ultralytics import YOLO

class YOLODetector:
    def __init__(self, model_path='yolov8n.pt'):
        self.model = YOLO(model_path)

    def detect(self, frame):
        results = self.model(frame)[0]
        detections = []
        for box in results.boxes.data:
            x1, y1, x2, y2, score, cls = box[:6]
            detections.append(([int(x1), int(y1), int(x2 - x1), int(y2 - y1)], score.item(), int(cls.item())))
        return detections

