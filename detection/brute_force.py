from collections import Counter

def detect_brute_force(log_lines):

    failed_ips = []

    for line in log_lines:

        if "FAILED_LOGIN" in line:

            ip = line.strip().split()[-1]
            failed_ips.append(ip)

    counts = Counter(failed_ips)

    alerts = []

    for ip, count in counts.items():

        if count >= 5:

            alerts.append({
                "ip": ip,
                "attack_type": "Brute Force Attack",
                "severity": "High",
                "attempts": count,
                "score": 90
            })

    return alerts
