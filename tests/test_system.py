def main():
    print("Running Smart Surveillance System Test...")

    try:
        from config.config import (
            VIDEO_PATH,
            OUTPUT_VIDEO_PATH,
            EVENT_LOG_PATH,
            MODEL_PATH,
            OUTPUT_WIDTH,
            MOTION_THRESHOLD,
            MOTION_PIXEL_THRESHOLD
        )

        from input.video_reader import VideoReader
        from preprocessing.image_processor import ImageProcessor
        from detection.object_detector import ObjectDetector
        from tracking.object_tracker import ObjectTracker
        from motion.motion_detector import MotionDetector
        from logging_module.event_logger import EventLogger
        from analytics.analytics import SurveillanceAnalytics

        assert VIDEO_PATH
        assert OUTPUT_VIDEO_PATH
        assert EVENT_LOG_PATH
        assert MODEL_PATH
        assert OUTPUT_WIDTH > 0
        assert MOTION_THRESHOLD >= 0
        assert MOTION_PIXEL_THRESHOLD >= 0

        assert VideoReader
        assert ImageProcessor
        assert ObjectDetector
        assert ObjectTracker
        assert MotionDetector
        assert EventLogger
        assert SurveillanceAnalytics

        print("All required modules imported successfully.")
        print("Configuration values validated.")
        print("System test passed.")

    except Exception as error:
        print("System test failed.")
        print("Error:", error)
        raise


if __name__ == "__main__":
    main()