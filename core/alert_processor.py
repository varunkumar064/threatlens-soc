from datetime import datetime
from core.socket_manager import socketio
from detection.detector import run_detection
from database.db import save_alert
from mitre.attack_mapping import get_mitre_mapping
from threat_intel.intel_checker import is_malicious


def process_alerts():

    detected_alerts = run_detection(
        "logs/auth.log"
    )

    for alert in detected_alerts:

        alert["timestamp"] = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        mapping = get_mitre_mapping(
            alert["attack_type"]
        )

        alert["mitre_id"] = mapping["id"]

        if is_malicious(alert["ip"]):

            alert["threat_intel"] = "Known Malicious"

            alert["score"] += 20

            if alert["severity"] == "Medium":
                alert["severity"] = "High"

        else:

            alert["threat_intel"] = "Clean"

        try:

            save_alert(alert)
            socketio.emit(
                "new_alert",
                alert
            )

        except Exception as e:

            print(
                "Alert Save Error:",
                e
            )