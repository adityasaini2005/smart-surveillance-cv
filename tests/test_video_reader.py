from input.video_reader import VideoReader


def main():
    video_path = "input/test_video.mp4"

    reader = VideoReader(video_path)

    properties = reader.get_properties()

    print("Video opened successfully")
    print("Width:", properties["width"])
    print("Height:", properties["height"])
    print("FPS:", properties["fps"])
    print("Frame count:", properties["frame_count"])

    count = 0

    for frame in reader.read_frames():
        count += 1

        if count == 1:
            print("First frame read successfully")
            print("Frame shape:", frame.shape)

        # Only test a few frames for now
        if count >= 10:
            break

    reader.release()

    print("Frames tested:", count)


if __name__ == "__main__":
    main()