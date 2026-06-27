from detection.brute_force import detect_brute_force
from detection.port_scan import detect_port_scan
from detection.suspicious_login import detect_suspicious_login

def run_detection(log_file):

    with open(log_file, "r") as file:
        logs = file.readlines()

    alerts = []

    alerts.extend(
        detect_brute_force(logs)
    )

    alerts.extend(
        detect_port_scan(logs)
    )

    alerts.extend(
        detect_suspicious_login(logs)
    )

    return alerts
