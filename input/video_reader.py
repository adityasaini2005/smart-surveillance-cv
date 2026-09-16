import cv2
import os


class VideoReader:
    """Reads video frames from a file."""

    def __init__(self, video_path):
        self.video_path = video_path

        # Validate video path
        if not os.path.exists(video_path):
            raise FileNotFoundError(
                f"Video file not found: {video_path}"
            )

        self.cap = cv2.VideoCapture(video_path)

        # Validate video opening
        if not self.cap.isOpened():
            raise ValueError(
                f"Could not open video: {video_path}"
            )

    def get_properties(self):
        """Returns basic video properties."""

        width = int(
            self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        )

        height = int(
            self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        )

        fps = self.cap.get(
            cv2.CAP_PROP_FPS
        )

        frame_count = int(
            self.cap.get(cv2.CAP_PROP_FRAME_COUNT)
        )

        # Validate video properties
        if width <= 0 or height <= 0:
            raise ValueError(
                "Invalid video dimensions."
            )

        if fps <= 0:
            raise ValueError(
                "Invalid video FPS."
            )

        return {
            "width": width,
            "height": height,
            "fps": fps,
            "frame_count": frame_count
        }

    def read_frames(self):
        """Yields valid video frames."""

        while True:

            success, frame = self.cap.read()

            if not success:
                break

            if frame is None or frame.size == 0:
                continue

            yield frame

    def release(self):
        """Releases the video resource."""

        if self.cap is not None:
            self.cap.release()