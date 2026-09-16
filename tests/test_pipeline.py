from input.video_reader import VideoReader
from preprocessing.image_processor import ImageProcessor


def main():
    video_path = "input/test_video.mp4"

    reader = VideoReader(video_path)
    processor = ImageProcessor()

    print("Starting video preprocessing pipeline...")

    frame_count = 0

    for frame in reader.read_frames():

        results = processor.process(frame)
        frame_count += 1

        if frame_count == 1:
            print("Original frame:", frame.shape)
            print("Resized frame:", results["resized"].shape)
            print("Enhanced frame:", results["enhanced"].shape)

        if frame_count >= 10:
            break

    reader.release()

    print("Pipeline test successful")
    print("Frames processed:", frame_count)


if __name__ == "__main__":
    main()