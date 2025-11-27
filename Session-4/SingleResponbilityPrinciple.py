"""
Single Responsibility Principle (SRP)

One Class → One Reason to Change
"""


# ============================================================
# ❌ BAD EXAMPLE — Violates SRP
# ============================================================

class CameraManager:
    """
    BAD:
    This class does TOO MANY THINGS:
    - Loads RTSP stream
    - Decodes frames
    - Detects objects
    - Logs events

    Multiple responsibilities → multiple reasons to change → violates SRP.
    """

    def load_rtsp(self, url):
        print(f"[CameraManager] Loading RTSP stream from {url}")
        return "raw_frame"

    def decode_frame(self, raw_frame):
        print("[CameraManager] Decoding frame...")
        return "decoded_frame"

    def detect_objects(self, frame):
        print("[CameraManager] Detecting objects...")
        return ["person"]

    def log_event(self, event):
        print(f"[CameraManager] Logging event: {event}")


# ============================================================
# ✅ GOOD EXAMPLE — Follows SRP
# ============================================================

class RTSPLoader:
    """Responsible ONLY for pulling RTSP stream"""
    def load(self, url):
        print(f"[RTSPLoader] Loading stream from: {url}")
        return "raw_frame_data"


class FrameDecoder:
    """Responsible ONLY for decoding raw frames"""
    def decode(self, raw_frame):
        print("[FrameDecoder] Decoding frame...")
        return "decoded_frame"


class ObjectDetector:
    """Responsible ONLY for object detection"""
    def detect(self, frame):
        print("[ObjectDetector] Detecting objects...")
        return ["person", "car"]


class AlertService:
    """Responsible ONLY for sending alerts"""
    def send_alert(self, objects):
        print(f"[AlertService] ALERT! Objects detected: {objects}")


# ------------------------------------------------------------
# OPTIONAL: Coordinator (does not break SRP)
# ------------------------------------------------------------

class CameraPipeline:
    """
    Coordinates the SRP classes.
    Does NOT do detection/decoding itself.
    """
    def __init__(self):
        self.loader = RTSPLoader()
        self.decoder = FrameDecoder()
        self.detector = ObjectDetector()
        self.alert = AlertService()

    def run(self, url):
        raw = self.loader.load(url)
        frame = self.decoder.decode(raw)
        objs = self.detector.detect(frame)
        self.alert.send_alert(objs)


# ============================================================
# Usage Demo
# ============================================================

if __name__ == "__main__":
    print("\n=== BAD EXAMPLE (Violates SRP) ===")
    bad = CameraManager()
    raw = bad.load_rtsp("rtsp://cam/live")
    frame = bad.decode_frame(raw)
    objs = bad.detect_objects(frame)
    bad.log_event(f"Objects found: {objs}")

    print("\n=== GOOD EXAMPLE (Follows SRP) ===")
    pipeline = CameraPipeline()
    pipeline.run("rtsp://cam/live")
