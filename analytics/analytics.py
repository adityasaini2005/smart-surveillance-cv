import csv
from collections import Counter


class SurveillanceAnalytics:
    """Generates statistics from surveillance event logs."""

    def __init__(self, event_file="output/events.csv"):
        self.event_file = event_file

    def analyze(self):
        total_events = 0
        object_types = Counter()
        object_ids = set()
        confidences = []

        with open(self.event_file, "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                total_events += 1

                object_types[row["object_class"]] += 1
                object_ids.add(row["object_id"])
                confidences.append(float(row["confidence"]))

        average_confidence = (
            sum(confidences) / len(confidences)
            if confidences else 0
        )

        return {
            "total_events": total_events,
            "unique_objects": len(object_ids),
            "object_types": dict(object_types),
            "average_confidence": round(
                average_confidence, 2
            )
        }