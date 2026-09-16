from input.video_reader import VideoReader
from detection.object_detector import ObjectDetector


def main():
    video_path = "input/test_video.mp4"

    reader = VideoReader(video_path)
    detector = ObjectDetector()

    print("Loading YOLO model...")
    print("Testing object detection on first frame...")

    for frame in reader.read_frames():
        result = detector.detect(frame)
        detections = detector.get_detections(result)

        print("Detection completed")
        print("Objects detected:", len(detections))

        for detection in detections:
            print(
                f"{detection['class_name']} "
                f"| Confidence: {detection['confidence']:.2f} "
                f"| Box: {detection['box']}"
            )

        break

    reader.release()


if __name__ == "__main__":
    main()