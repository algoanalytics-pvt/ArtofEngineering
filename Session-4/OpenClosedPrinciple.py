"""
Open/Closed Principle (OCP)

Extend ✔
Modify ❌

System should allow adding NEW features without MODIFYING existing code.

Bad:
    if model == "yolo5":
    elif model == "yolo8":

Good (Plug-in):
    ModelInterface
         ↓
    YoloV5   YoloV8   YoloONNX
"""


# ============================================================
# ❌ BAD EXAMPLE — Violates OCP
# ============================================================

def run_model_bad(model_type, frame):
    """
    BAD:
    Adding a new model requires MODIFYING this function.
    Violates OCP.
    """
    if model_type == "yolov5":
        print("[YOLOv5] Running inference...")
        return "v5_result"

    elif model_type == "yolov8":
        print("[YOLOv8] Running inference...")
        return "v8_result"

    # Every new model adds more elif statements (BAD!)
    # elif model_type == "yolov10":
    #     ...


# ============================================================
# ✅ GOOD EXAMPLE — Follows OCP (Plugin Architecture)
# ============================================================

from abc import ABC, abstractmethod


# ------------------------------------------------------------
# Abstract Interface — system depends on this, not on models
# ------------------------------------------------------------
class ModelInterface(ABC):
    """Defines required methods for all model plugins."""

    @abstractmethod
    def run(self, frame):
        pass


# ------------------------------------------------------------
# Concrete Implementations (Plugins)
# ------------------------------------------------------------
class YoloV5(ModelInterface):
    def run(self, frame):
        print("[YOLOv5] Running inference...")
        return "yolov5_result"


class YoloV8(ModelInterface):
    def run(self, frame):
        print("[YOLOv8] Running inference...")
        return "yolov8_result"


class YoloONNX(ModelInterface):
    def run(self, frame):
        print("[YOLO ONNX] Running inference...")
        return "onnx_result"


# ------------------------------------------------------------
# Factory (EXTENDABLE without modifying old code)
# ------------------------------------------------------------
class ModelFactory:
    """
    Plugin factory.
    New models can be registered WITHOUT modifying existing logic.
    """
    registry = {}

    @classmethod
    def register(cls, name, model_class):
        cls.registry[name] = model_class

    @classmethod
    def create(cls, name):
        if name not in cls.registry:
            raise ValueError(f"Unknown model: {name}")
        return cls.registry[name]()   # Instantiate the model


# Register available models (EXTENSION POINT)
ModelFactory.register("yolov5", YoloV5)
ModelFactory.register("yolov8", YoloV8)
ModelFactory.register("yolonnx", YoloONNX)


# ============================================================
# Usage Demo
# ============================================================
if __name__ == "__main__":

    print("=== BAD EXAMPLE — Violates OCP ===")
    print(run_model_bad("yolov5", "frame1"))
    print(run_model_bad("yolov8", "frame1"))

    print("\n=== GOOD EXAMPLE — Follows OCP ===")
    model = ModelFactory.create("yolov8")   # Select model dynamically
    result = model.run("frame1")
    print("Result:", result)

    print("\nAdd new model? → Just register a new class ✔ No code modification ❌")
