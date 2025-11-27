"""
Interface Segregation Principle (ISP)

Big Interface ❌  
Small, Focused Interfaces ✔

Do not force a class to implement methods it doesn't need.
"""

# ============================================================
# ❌ BAD EXAMPLE — Violates ISP
# ============================================================

class CameraInterfaceBad:
    """Big interface — forces all methods on all cameras"""
    def start(self): pass
    def stop(self): pass
    def zoom(self): pass
    def ptz(self): pass
    def capture(self): pass


class USBCameraBad(CameraInterfaceBad):
    """USB camera cannot do PTZ, but forced to implement it"""
    def start(self): print("[USB] Started")
    def stop(self): print("[USB] Stopped")
    def zoom(self): print("[USB] Zoomed")
    def ptz(self): print("[USB] Cannot PTZ! ❌")  # Violation
    def capture(self): print("[USB] Captured frame")


# ============================================================
# ✅ GOOD EXAMPLE — Follows ISP
# ============================================================

# Small, focused interfaces

class BaseCamera:
    """Common methods for all cameras"""
    def start(self): pass
    def stop(self): pass
    def capture(self): pass


class PTZCamera(BaseCamera):
    """Optional PTZ interface for cameras that support it"""
    def zoom(self): pass
    def ptz(self): pass


# ------------------------------------------------------------
# Concrete Implementations
# ------------------------------------------------------------

class USBWebcam(BaseCamera):
    def start(self): print("[USB] Started")
    def stop(self): print("[USB] Stopped")
    def capture(self): print("[USB] Captured frame")
    # No PTZ methods needed — perfectly fine


class ONVIFCamera(PTZCamera):
    def start(self): print("[ONVIF] Started")
    def stop(self): print("[ONVIF] Stopped")
    def capture(self): print("[ONVIF] Captured frame")
    def zoom(self): print("[ONVIF] Zooming...")
    def ptz(self): print("[ONVIF] PTZ moved")


# ------------------------------------------------------------
# Demo Usage
# ------------------------------------------------------------

if __name__ == "__main__":
    print("=== BAD EXAMPLE (Violates ISP) ===")
    usb_bad = USBCameraBad()
    usb_bad.start()
    usb_bad.ptz()  # ❌ Forced method

    print("\n=== GOOD EXAMPLE (Follows ISP) ===")
    usb = USBWebcam()
    usb.start()
    # usb.ptz() → Does not exist, no violation

    onvif = ONVIFCamera()
    onvif.start()
    onvif.ptz()   # ✔ Only cameras that support PTZ implement it
