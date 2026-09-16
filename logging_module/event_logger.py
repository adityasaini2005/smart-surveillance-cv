import csv
import os
from datetime import datetime


class EventLogger:
    """Stores detected surveillance events in a CSV file."""

    def __init__(self, file_path="output/events.csv", reset=True):
        self.file_path = file_path

        # Create output directory if it does not exist
        directory = os.path.dirname(self.file_path)

        if directory:
            os.makedirs(directory, exist_ok=True)

        # Create a fresh log file for every new run
        if reset:
            self._create_new_file()
        elif not os.path.exists(self.file_path):
            self._create_new_file()

    def _create_new_file(self):
        """Creates a new CSV file with column headers."""

        with open(
            self.file_path,
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

    def log_event(
        self,
        frame_number,
        event_type,
        object_id,
        object_class,
        confidence
    ):
        """Adds a surveillance event to the CSV file."""

        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        with open(
            self.file_path,
            "a",
            newline=""
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                timestamp,
                frame_number,
                event_type,
                object_id,
                object_class,
                round(confidence, 2)
            ])