"""
🧪 Slide 14 — Unit Testing

Arrow Diagram:
Function → Test → Validate Logic

Example Tests:
- ObjectDetector output
- FrameReader output
- Alert throttling logic

Tools: pytest
"""

import pytest

# -----------------------------
# Sample classes to test
# -----------------------------

class FrameReader:
    def read(self):
        return "frame_data"

class ObjectDetector:
    def detect(self, frame):
        # Simulate detection
        if frame == "frame_data":
            return ["person", "car"]
        return []

class AlertService:
    def __init__(self):
        self.throttle = False

    def send_alert(self, objects):
        if self.throttle:
            return "throttled"
        return f"Alert sent for: {objects}"

# -----------------------------
# Unit Tests
# -----------------------------

def test_frame_reader():
    reader = FrameReader()
    frame = reader.read()
    assert frame == "frame_data"

def test_object_detector():
    detector = ObjectDetector()
    result = detector.detect("frame_data")
    assert "person" in result
    assert "car" in result

def test_alert_throttle():
    alert = AlertService()
    alert.throttle = True
    response = alert.send_alert(["person"])
    assert response == "throttled"
