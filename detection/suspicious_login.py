def detect_suspicious_login(log_lines):

    alerts = []

    for line in log_lines:

        if "SUSPICIOUS_LOGIN" in line:

            ip = line.strip().split()[-1]

            alerts.append({
                "ip": ip,
                "attack_type": "Suspicious Login",
                "severity": "Medium",
                "attempts": 1,
                "score": 60
            })

    return alerts
