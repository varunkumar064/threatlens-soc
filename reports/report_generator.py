from datetime import datetime


def generate_report(alert):

    filename = (
        f"reports/"
        f"{alert['alert_id']}.txt"
    )

    with open(
        filename,
        "w"
    ) as report:

        report.write(
            "SENTINELAI INCIDENT REPORT\n"
        )

        report.write(
            "=" * 40 + "\n\n"
        )

        report.write(
            f"Generated: "
            f"{datetime.now()}\n\n"
        )

        report.write(
            f"Alert ID: "
            f"{alert['alert_id']}\n"
        )

        report.write(
            f"IP Address: "
            f"{alert['ip']}\n"
        )

        report.write(
            f"Attack Type: "
            f"{alert['attack_type']}\n"
        )

        report.write(
            f"Severity: "
            f"{alert['severity']}\n"
        )

        report.write(
            f"Attempts: "
            f"{alert['attempts']}\n"
        )

        report.write(
            f"Score: "
            f"{alert['score']}\n"
        )

        report.write(
            f"MITRE ID: "
            f"{alert['mitre_id']}\n"
        )

        report.write(
            f"Threat Intel: "
            f"{alert['threat_intel']}\n"
        )

        report.write(
            f"Status: "
            f"{alert['status']}\n"
        )

    return filename
