import csv
import os
import tempfile

from analytics.analytics import SurveillanceAnalytics


def main():
    # Create a temporary CSV for analytics testing
    with tempfile.TemporaryDirectory() as temp_dir:

        test_file = os.path.join(
            temp_dir,
            "test_events.csv"
        )

        # Write sample events
        with open(
            test_file,
            "w",
            newline=""
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                "timestamp",
                "frame_number",
                "event_type",
                "object_id",
                "object_class",
                "confidence"
            ])

            writer.writerow([
                "2026-09-16 10:00:00",
                1,
                "Motion Detected",
                1,
                "person",
                0.90
            ])

            writer.writerow([
                "2026-09-16 10:00:01",
                2,
                "Motion Detected",
                2,
                "car",
                0.70
            ])

            writer.writerow([
                "2026-09-16 10:00:02",
                3,
                "Motion Detected",
                1,
                "person",
                0.80
            ])

        # Run analytics on the test file
        analytics = SurveillanceAnalytics(
            event_file=test_file
        )

        summary = analytics.analyze()

        # Verify expected results
        assert summary["total_events"] == 3
        assert summary["unique_objects"] == 2
        assert summary["object_types"]["person"] == 2
        assert summary["object_types"]["car"] == 1
        assert summary["average_confidence"] == 0.80

        print("Analytics test successful.")
        print("Total events:", summary["total_events"])
        print("Unique objects:", summary["unique_objects"])
        print("Average confidence:", summary["average_confidence"])
        print("Object types:", summary["object_types"])


if __name__ == "__main__":
    main()