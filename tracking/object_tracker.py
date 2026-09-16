from ultralytics import YOLO


class ObjectTracker:
    """Tracks detected objects across video frames using YOLO tracking."""

    def __init__(self, model_name="yolo11n.pt"):
        self.model = YOLO(model_name)

    def track(self, frame):
        results = self.model.track(
            frame,
            persist=True,
            verbose=False
        )
        return results[0]

    def get_tracks(self, result):
        tracks = []

        if result.boxes is None or result.boxes.id is None:
            return tracks

        for box, track_id, cls, conf in zip(
            result.boxes.xyxy,
            result.boxes.id,
            result.boxes.cls,
            result.boxes.conf
        ):
            tracks.append({
                "track_id": int(track_id),
                "class_id": int(cls),
                "class_name": result.names[int(cls)],
                "confidence": float(conf),
                "box": box.tolist()
            })

        return tracks