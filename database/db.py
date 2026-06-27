import sqlite3
import uuid

DB_PATH = "database/alerts.db"


def create_table():

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alerts (

        alert_id TEXT PRIMARY KEY,

        ip TEXT,

        attack_type TEXT,

        severity TEXT,

        attempts INTEGER,

        score INTEGER,

        mitre_id TEXT,

        threat_intel TEXT,

        timestamp TEXT,

        status TEXT

    )
    """)

    conn.commit()
    conn.close()


def alert_exists(ip, attack_type):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM alerts
        WHERE ip=?
        AND attack_type=?
        """,
        (
            ip,
            attack_type
        )
    )

    count = cursor.fetchone()[0]

    conn.close()

    return count > 0


def save_alert(alert):

    create_table()

    if alert_exists(
        alert["ip"],
        alert["attack_type"]
    ):
        return

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    alert_id = (
        "ALT-" +
        str(uuid.uuid4())[:8]
    )

    cursor.execute(
        """
        INSERT INTO alerts
        (
            alert_id,
            ip,
            attack_type,
            severity,
            attempts,
            score,
            mitre_id,
            threat_intel,
            timestamp,
            status
        )

        VALUES
        (
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
        )
        """,
        (
            alert_id,
            alert["ip"],
            alert["attack_type"],
            alert["severity"],
            alert["attempts"],
            alert["score"],
            alert["mitre_id"],
            alert["threat_intel"],
            alert["timestamp"],
            "Open"
        )
    )

    conn.commit()
    conn.close()


def get_alerts():

    create_table()

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT

            alert_id,
            ip,
            attack_type,
            severity,
            attempts,
            score,
            mitre_id,
            threat_intel,
            timestamp,
            status

        FROM alerts

        ORDER BY timestamp DESC
        """
    )

    rows = cursor.fetchall()

    conn.close()

    alerts = []

    for row in rows:

        alerts.append({

            "alert_id": row[0],

            "ip": row[1],

            "attack_type": row[2],

            "severity": row[3],

            "attempts": row[4],

            "score": row[5],

            "mitre_id": row[6],

            "threat_intel": row[7],

            "timestamp": row[8],

            "status": row[9]

        })

    return alerts


def update_status(
    alert_id,
    status
):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE alerts

        SET status=?

        WHERE alert_id=?
        """,
        (
            status,
            alert_id
        )
    )

    conn.commit()
    conn.close()


def delete_alert(
    alert_id
):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM alerts

        WHERE alert_id=?
        """,
        (
            alert_id,
        )
    )

    conn.commit()
    conn.close()
