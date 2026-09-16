from ultralytics import YOLO


class ObjectDetector:
    """Performs object detection using a pretrained YOLO model."""

    def __init__(self, model_name="yolo11n.pt"):
        self.model = YOLO(model_name)

    def detect(self, frame):
        results = self.model(frame, verbose=False)
        return results[0]

    def get_detections(self, result):
        detections = []

        if result.boxes is None:
            return detections

        for box in result.boxes:
            class_id = int(box.cls[0])
            confidence = float(box.conf[0])
            coordinates = box.xyxy[0].tolist()

            class_name = result.names[class_id]

            detections.append({
                "class_id": class_id,
                "class_name": class_name,
                "confidence": confidence,
                "box": coordinates
            })

        return detections