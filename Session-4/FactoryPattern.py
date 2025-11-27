# -------------------------------
# Product Classes (Models)
# -------------------------------

class YoloONNX:
    """Concrete Product A"""
    def load(self):
        return "YOLO ONNX model loaded"

class SSD:
    """Concrete Product B"""
    def load(self):
        return "SSD model loaded"

class MobileNet:
    """Concrete Product C"""
    def load(self):
        return "MobileNet model loaded"


# -------------------------------
# Factory Function
# -------------------------------

def model_factory(model_type):
    """
    Factory Function:
    Returns a model object based on input type.
    Hides the object creation logic from the user.
    """

    if model_type == "yolo":
        return YoloONNX()
    elif model_type == "ssd":
        return SSD()
    elif model_type == "mobilenet":
        return MobileNet()
    else:
        raise ValueError(f"Unknown model type: {model_type}")


# -------------------------------
# Example Usage
# -------------------------------
if __name__ == "__main__":
    # Input
    model_type = "yolo"

    # Factory creates the correct model
    model = model_factory(model_type)

    # Using the created product
    print("Created:", type(model).__name__)
    print(model.load())
