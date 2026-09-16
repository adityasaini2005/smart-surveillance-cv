import cv2


class MotionDetector:
    """Detects motion between consecutive video frames."""

    def __init__(
        self,
        threshold=25,
        pixel_threshold=500
    ):
        self.threshold = threshold
        self.pixel_threshold = pixel_threshold

        self.previous_frame = None

    def detect(self, frame):
        """
        Detects whether motion is present
        between the current and previous frame.
        """

        # Convert frame to grayscale
        gray = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2GRAY
        )

        # Reduce image noise
        gray = cv2.GaussianBlur(
            gray,
            (5, 5),
            0
        )

        # First frame cannot be compared
        if self.previous_frame is None:

            self.previous_frame = gray

            return False

        # Calculate absolute difference
        difference = cv2.absdiff(
            self.previous_frame,
            gray
        )

        # Apply threshold
        _, thresholded = cv2.threshold(
            difference,
            self.threshold,
            255,
            cv2.THRESH_BINARY
        )

        # Count changed pixels
        motion_pixels = cv2.countNonZero(
            thresholded
        )

        # Update previous frame
        self.previous_frame = gray

        # Determine whether motion occurred
        return motion_pixels > self.pixel_threshold