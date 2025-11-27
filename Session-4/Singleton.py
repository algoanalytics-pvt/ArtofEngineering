class Config:
    """
    Singleton class example.
    Ensures only one instance of Config exists across the entire application.
    """

    # Class-level variable to store the single shared instance
    _instance = None

    def __init__(self):
        # Initialize configuration values here
        # (This block runs only once)
        self.settings = {
            "db_url": "localhost:27017",
            "log_level": "INFO"
        }

    @staticmethod
    def get_instance():
        """
        Static access method.
        Always returns the same Config instance.
        """
        # If no instance exists, create one
        if Config._instance is None:
            Config._instance = Config()

        # Return the existing instance
        return Config._instance


# -----------------------------
# Example Usage
# -----------------------------
if __name__ == "__main__":
    c1 = Config.get_instance()
    c2 = Config.get_instance()

    print("Are both objects same?", c1 is c2)     # True
    print("Config settings:", c1.settings)
