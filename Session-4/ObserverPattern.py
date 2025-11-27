# ----------------------------------------
# Observer Interface
# ----------------------------------------
class Observer:
    def update(self, event_data):
        """
        Called when the subject (EventSource) notifies observers.
        """
        raise NotImplementedError


# ----------------------------------------
# Concrete Observers
# ----------------------------------------

class MobileAppNotifier(Observer):
    def update(self, event_data):
        print(f"[MobileApp] Push Notification sent: {event_data}")


class EventLogger(Observer):
    def update(self, event_data):
        print(f"[Logger] Event logged: {event_data}")


class AlertEngine(Observer):
    def update(self, event_data):
        print(f"[AlertEngine] Alert triggered with data: {event_data}")


# ----------------------------------------
# Subject / Event Source
# ----------------------------------------
class EventSource:
    """
    Maintains a list of observers.
    Notifies all observers when an event occurs.
    """

    def __init__(self):
        self.observers = []

    def subscribe(self, observer):
        """Add an observer to the list"""
        self.observers.append(observer)

    def unsubscribe(self, observer):
        """Remove an observer"""
        self.observers.remove(observer)

    def notify(self, event_data):
        """Notify all observers"""
        print("\n[EventSource] Event Occurred! Notifying observers...\n")
        for obs in self.observers:
            obs.update(event_data)


# ----------------------------------------
# Example Usage
# ----------------------------------------
if __name__ == "__main__":

    # Event Source
    event_source = EventSource()

    # Observers
    mobile = MobileAppNotifier()
    logger = EventLogger()
    alert = AlertEngine()

    # Subscribe observers
    event_source.subscribe(mobile)
    event_source.subscribe(logger)
    event_source.subscribe(alert)

    # Trigger event
    event_source.notify("Anomaly detected in Camera 12")
