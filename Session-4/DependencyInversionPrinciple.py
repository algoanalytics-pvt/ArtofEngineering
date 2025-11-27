"""
Dependency Inversion Principle (DIP)

Diagram:
High-Level Module
      ↑
Abstractions
      ↑
Low-Level Modules

Explanation:
High-level logic should depend on interfaces, not concrete classes.

Example:
AlertEngine → uses INotifier
INotifier → EmailNotifier / SMSNotifier / WhatsAppNotifier
"""

from abc import ABC, abstractmethod

# ============================================================
# Low-Level Modules implement the abstraction
# ============================================================

class INotifier(ABC):
    """Abstraction for notifications"""
    @abstractmethod
    def send(self, message: str):
        pass


class EmailNotifier(INotifier):
    def send(self, message: str):
        print(f"[EmailNotifier] Sending Email: {message}")


class SMSNotifier(INotifier):
    def send(self, message: str):
        print(f"[SMSNotifier] Sending SMS: {message}")


class WhatsAppNotifier(INotifier):
    def send(self, message: str):
        print(f"[WhatsAppNotifier] Sending WhatsApp message: {message}")


# ============================================================
# High-Level Module depends on abstraction, NOT concrete classes
# ============================================================

class AlertEngine:
    """High-level module"""
    def __init__(self, notifier: INotifier):
        self.notifier = notifier

    def alert(self, event: str):
        """Send alert using the injected notifier"""
        self.notifier.send(f"ALERT! {event}")


# ============================================================
# Demo Usage
# ============================================================

if __name__ == "__main__":
    print("=== DIP Example ===")

    email_notifier = EmailNotifier()
    sms_notifier = SMSNotifier()
    wa_notifier = WhatsAppNotifier()

    # High-level module uses abstraction
    alert_engine1 = AlertEngine(email_notifier)
    alert_engine2 = AlertEngine(sms_notifier)
    alert_engine3 = AlertEngine(wa_notifier)

    # Trigger alerts
    alert_engine1.alert("Camera 12 anomaly detected")
    alert_engine2.alert("Camera 15 anomaly detected")
    alert_engine3.alert("Camera 22 anomaly detected")
