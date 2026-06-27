import sqlite3

conn = sqlite3.connect("database/alerts.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS alerts (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    alert_id TEXT,

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

print("Database initialized.")
