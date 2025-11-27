from abc import ABC, abstractmethod


# -------------------------------------------------------
# Abstract Class (Defines structure, not implementation)
# -------------------------------------------------------
class BaseCamera(ABC):
    """
    Abstract base class for all camera types.
    Enforces required methods for subclasses.
    """

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def get_frame(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass


# -------------------------------------------------------
# Concrete Implementations
# -------------------------------------------------------

class ONVIFCamera(BaseCamera):
    def connect(self):
        print("[ONVIF] Connected via ONVIF protocol")

    def get_frame(self):
        return "[ONVIF] Frame data"

    def disconnect(self):
        print("[ONVIF] Disconnected")


class IPCamera(BaseCamera):
    def connect(self):
        print("[IP Camera] Connected using RTSP URL")

    def get_frame(self):
        return "[IP Camera] Frame data"

    def disconnect(self):
        print("[IP Camera] Disconnected")


class USBWebcam(BaseCamera):
    def connect(self):
        print("[USB Webcam] Connected to system USB port")

    def get_frame(self):
        return "[USB Webcam] Frame data"

    def disconnect(self):
        print("[USB Webcam] Disconnected")


# -------------------------------------------------------
# Example Usage
# -------------------------------------------------------
if __name__ == "__main__":
    cameras = [
        ONVIFCamera(),
        IPCamera(),
        USBWebcam()
    ]

    # All cameras follow the same interface
    for cam in cameras:
        cam.connect()
        print("Frame:", cam.get_frame())
        cam.disconnect()
        print()
