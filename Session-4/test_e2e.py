"""
🌐 Slide 16 — E2E Testing

Arrow Diagram:
User Action → System Flow → Final Output

Example:
User opens dashboard → live feed loads → alert triggers → mobile notification arrives
"""

import pytest

# -----------------------------
# Mock system modules
# -----------------------------

class Dashboard:
    def load_live_feed(self):
        return "live_feed_loaded"

class AlertEngine:
    def trigger_alert(self, event):
        return f"Alert triggered: {event}"

class MobileNotifier:
    def notify(self, message):
        return f"Mobile notification sent: {message}"

# -----------------------------
# E2E Test
# -----------------------------

def test_dashboard_alert_flow():
    dashboard = Dashboard()
    alert_engine = AlertEngine()
    mobile = MobileNotifier()

    # Simulate user action
    feed_status = dashboard.load_live_feed()
    assert feed_status == "live_feed_loaded"

    # System flow
    alert_status = alert_engine.trigger_alert("Camera anomaly")
    assert alert_status == "Alert triggered: Camera anomaly"

    # Final output
    mobile_status = mobile.notify(alert_status)
    assert mobile_status == "Mobile notification sent: Alert triggered: Camera anomaly"
