def detect_port_scan(log_lines):

    alerts = []

    for line in log_lines:

        if "PORT_SCAN" in line:

            ip = line.strip().split()[-1]

            alerts.append({
                "ip": ip,
                "attack_type": "Port Scan",
                "severity": "Medium",
                "attempts": 1,
                "score": 70
            })

    return alerts

