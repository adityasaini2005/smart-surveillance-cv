import csv
import os
import tempfile

from logging_module.event_logger import EventLogger


def main():
    # Create a separate temporary file for testing
    with tempfile.TemporaryDirectory() as temp_dir:

        test_file = os.path.join(
            temp_dir,
            "test_events.csv"
        )

        logger = EventLogger(
            file_path=test_file
        )

        # Add sample test events
        logger.log_event(
            frame_number=1,
            event_type="Motion Detected",
            object_id=1,
            object_class="person",
            confidence=0.95
        )

        logger.log_event(
            frame_number=2,
            event_type="Motion Detected",
            object_id=2,
            object_class="car",
            confidence=0.80
        )

        # Verify the logged events
        with open(
            test_file,
            "r",
            newline=""
        ) as file:

            reader = csv.DictReader(file)
            rows = list(reader)

        assert len(rows) == 2
        assert rows[0]["object_class"] == "person"
        assert rows[1]["object_class"] == "car"

        print("Event logging test successful.")
        print("Test events saved to temporary file.")


if __name__ == "__main__":
    main()