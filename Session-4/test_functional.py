"""
🔧 Slide 15 — Functional Testing

Arrow Diagram:
Module → Run Scenario → Verify output

Example:
End-to-end frame → model → anomaly detection → alert
Validate correct JSON output
"""

import pytest
import json

# -----------------------------
# Sample functional modules
# -----------------------------

class FrameReader:
    def read(self):
        return "frame_data"

class ObjectDetector:
    def detect(self, frame):
        return ["person"] if frame == "frame_data" else []

class AlertService:
    def send_alert(self, objects):
        return json.dumps({"alert": objects})

# -----------------------------
# Functional Test
# -----------------------------

def test_frame_to_alert():
    reader = FrameReader()
    detector = ObjectDetector()
    alert_service = AlertService()

    frame = reader.read()
    detected_objects = detector.detect(frame)
    alert_json = alert_service.send_alert(detected_objects)

    # Verify output is correct JSON
    parsed = json.loads(alert_json)
    assert "alert" in parsed
    assert parsed["alert"] == ["person"]
