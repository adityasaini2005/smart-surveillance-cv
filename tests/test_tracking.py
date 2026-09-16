from input.video_reader import VideoReader
from tracking.object_tracker import ObjectTracker


def main():
    video_path = "input/test_video.mp4"

    reader = VideoReader(video_path)
    tracker = ObjectTracker()

    print("Loading tracking model...")
    print("Testing object tracking...")

    frame_count = 0

    for frame in reader.read_frames():
        result = tracker.track(frame)
        tracks = tracker.get_tracks(result)

        frame_count += 1

        print(f"\nFrame {frame_count}")
        print("Objects tracked:", len(tracks))

        for track in tracks:
            print(
                f"ID: {track['track_id']} | "
                f"{track['class_name']} | "
                f"Confidence: {track['confidence']:.2f}"
            )

        if frame_count >= 10:
            break

    reader.release()

    print("\nTracking test completed.")
    print("Frames tested:", frame_count)


if __name__ == "__main__":
    main()