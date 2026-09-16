from input.video_reader import VideoReader
from motion.motion_detector import MotionDetector


def main():
    video_path = "input/test_video.mp4"

    reader = VideoReader(video_path)
    detector = MotionDetector()

    print("Testing motion detection...")

    frame_count = 0
    motion_count = 0

    for frame in reader.read_frames():
        motion = detector.detect(frame)

        frame_count += 1

        print(f"Frame {frame_count}: Motion = {motion}")

        if motion:
            motion_count += 1

        if frame_count >= 10:
            break

    reader.release()

    print("\nMotion detection test completed.")
    print("Frames tested:", frame_count)
    print("Frames with motion:", motion_count)


if __name__ == "__main__":
    main()