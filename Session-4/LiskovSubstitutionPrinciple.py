"""
Liskov Substitution Principle (LSP)

Parent Class ← Subclass (should behave the same)

Child classes should be replaceable for their parent class
without breaking the system.

Bad Example:
    BaseCamera.read() → returns frame
    IPCamera.read() → sometimes returns None → breaks LSP

Good Example:
    All subclasses maintain same signature + guarantees
"""

# ============================================================
# ❌ BAD EXAMPLE — Violates LSP
# ============================================================

class BaseCameraBad:
    """Parent camera class"""
    def read(self):
        """Always returns a frame"""
        return "frame_data"


class IPCameraBad(BaseCameraBad):
    """Child camera sometimes breaks the contract"""
    def read(self):
        """Sometimes returns None — breaks LSP"""
        import random
        if random.choice([True, False]):
            return None
        return "frame_data_from_ipcamera"


# ------------------------------------------------------------
# Demo of BAD behavior
# ------------------------------------------------------------
def process_camera_bad(cam: BaseCameraBad):
    frame = cam.read()
    if frame is None:
        print("[BAD] Error: Frame is None!")
    else:
        print("[BAD] Frame processed:", frame)


# ============================================================
# ✅ GOOD EXAMPLE — Follows LSP
# ============================================================

class BaseCamera:
    """Parent camera class (guarantees non-None frame)"""
    def read(self):
        """Always returns a frame"""
        return "frame_data"


class ONVIFCamera(BaseCamera):
    """Subclass maintains LSP contract"""
    def read(self):
        return "frame_data_from_onvif"


class IPCamera(BaseCamera):
    """Subclass maintains LSP contract"""
    def read(self):
        # Always returns valid frame
        return "frame_data_from_ipcamera"


class USBWebcam(BaseCamera):
    """Subclass maintains LSP contract"""
    def read(self):
        return "frame_data_from_usb"


# ------------------------------------------------------------
# Function that works for any BaseCamera subclass
# ------------------------------------------------------------
def process_camera(cam: BaseCamera):
    frame = cam.read()
    print("[GOOD] Frame processed:", frame)


# ============================================================
# Usage Demo
# ============================================================
if __name__ == "__main__":

    print("=== BAD EXAMPLE — Violates LSP ===")
    bad_cam = IPCameraBad()
    for _ in range(5):
        process_camera_bad(bad_cam)

    print("\n=== GOOD EXAMPLE — Follows LSP ===")
    cameras = [ONVIFCamera(), IPCamera(), USBWebcam()]
    for cam in cameras:
        process_camera(cam)
