import cv2

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
from tracking.object_tracker import ObjectTracker
from motion.motion_detector import MotionDetector
from logging_module.event_logger import EventLogger
from analytics.analytics import SurveillanceAnalytics


def main():

    # --------------------------------
    # 1. INITIALIZE MODULES
    # --------------------------------

    reader = VideoReader(
        VIDEO_PATH
    )

    processor = ImageProcessor()

    tracker = ObjectTracker(
        model_name=MODEL_PATH
    )

    motion_detector = MotionDetector(
        threshold=MOTION_THRESHOLD,
        pixel_threshold=MOTION_PIXEL_THRESHOLD
    )

    logger = EventLogger(
        file_path=EVENT_LOG_PATH
    )

    # --------------------------------
    # 2. GET VIDEO PROPERTIES
    # --------------------------------

    properties = reader.get_properties()

    original_width = properties["width"]
    original_height = properties["height"]
    fps = properties["fps"]

    # Preserve original aspect ratio
    output_width = OUTPUT_WIDTH

    output_height = int(
        original_height *
        (
            output_width /
            original_width
        )
    )

    # --------------------------------
    # 3. CREATE OUTPUT VIDEO
    # --------------------------------

    fourcc = cv2.VideoWriter_fourcc(
        *"mp4v"
    )

    writer = cv2.VideoWriter(
        OUTPUT_VIDEO_PATH,
        fourcc,
        fps,
        (
            output_width,
            output_height
        )
    )

    # Validate output writer
    if not writer.isOpened():

        reader.release()

        raise RuntimeError(
            "Could not create output video: "
            f"{OUTPUT_VIDEO_PATH}"
        )

    print(
        "Starting Smart Surveillance System..."
    )

    frame_number = 0

    # --------------------------------
    # 4. PROCESS VIDEO FRAMES
    # --------------------------------

    for frame in reader.read_frames():

        frame_number += 1

        # ----------------------------
        # IMAGE PREPROCESSING
        # ----------------------------

        processed = processor.process(
            frame
        )

        resized_frame = processed[
            "resized"
        ]

        # ----------------------------
        # OBJECT TRACKING
        # ----------------------------

        result = tracker.track(
            resized_frame
        )

        tracks = tracker.get_tracks(
            result
        )

        # ----------------------------
        # MOTION DETECTION
        # ----------------------------

        motion = motion_detector.detect(
            resized_frame
        )

        # ----------------------------
        # DRAW TRACKED OBJECTS
        # ----------------------------

        for track in tracks:

            x1, y1, x2, y2 = map(
                int,
                track["box"]
            )

            label = (
                f"ID {track['track_id']} "
                f"{track['class_name']} "
                f"{track['confidence']:.2f}"
            )

            # Draw bounding box
            cv2.rectangle(
                resized_frame,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

            # Draw object label
            cv2.putText(
                resized_frame,
                label,
                (
                    x1,
                    max(y1 - 10, 20)
                ),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 255, 0),
                2
            )

            # ------------------------
            # EVENT LOGGING
            # ------------------------

            if motion:

                logger.log_event(
                    frame_number=frame_number,
                    event_type="Motion Detected",
                    object_id=track["track_id"],
                    object_class=track["class_name"],
                    confidence=track["confidence"]
                )

        # --------------------------------
        # 5. DISPLAY MOTION STATUS
        # --------------------------------

        if motion:

            status = "MOTION DETECTED"

            status_color = (
                0,
                0,
                255
            )

        else:

            status = "NO MOTION"

            status_color = (
                255,
                255,
                255
            )

        cv2.putText(
            resized_frame,
            status,
            (20, 35),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            status_color,
            2
        )

        # --------------------------------
        # 6. SAVE OUTPUT FRAME
        # --------------------------------

        writer.write(
            resized_frame
        )

        # Display processed video
        cv2.imshow(
            "Smart Surveillance System",
            resized_frame
        )

        # Press Q to stop
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # --------------------------------
    # 7. RELEASE RESOURCES
    # --------------------------------

    reader.release()

    writer.release()

    cv2.destroyAllWindows()

    # --------------------------------
    # 8. GENERATE ANALYTICS
    # --------------------------------

    analytics = SurveillanceAnalytics(
        event_file=EVENT_LOG_PATH
    )

    summary = analytics.analyze()

    # --------------------------------
    # 9. DISPLAY SUMMARY
    # --------------------------------

    print(
        "\n========== SURVEILLANCE SUMMARY =========="
    )

    print(
        "Frames processed:",
        frame_number
    )

    print(
        "Total events:",
        summary["total_events"]
    )

    print(
        "Unique objects:",
        summary["unique_objects"]
    )

    print(
        "Average confidence:",
        summary["average_confidence"]
    )

    print(
        "\nObject types:"
    )

    for object_type, count in summary[
        "object_types"
    ].items():

        print(
            f"{object_type}: {count}"
        )

    print(
        "=========================================="
    )

    print(
        "\nOutput video:",
        OUTPUT_VIDEO_PATH
    )

    print(
        "Event log:",
        EVENT_LOG_PATH
    )


if __name__ == "__main__":
    main()