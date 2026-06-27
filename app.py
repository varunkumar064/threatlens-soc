from core.socket_manager import socketio

import threading
from realtime.monitor import start_monitor
from flask import (
    Flask,
    render_template,
    request,
    send_file
)

from datetime import datetime

from detection.detector import run_detection

from database.db import (
    save_alert,
    get_alerts
)

from mitre.attack_mapping import (
    get_mitre_mapping
)

from threat_intel.intel_checker import (
    is_malicious
)

from reports.report_generator import (
    generate_report
)

app = Flask(
    __name__,
    template_folder="dashboard/templates",
    static_folder="dashboard/static"
)
socketio.init_app(app)

@app.route("/")
def dashboard():

    search = request.args.get(
        "search",
        ""
    )

    alerts = get_alerts()

    alerts = sorted(
        alerts,
        key=lambda x: x["timestamp"],
        reverse=True
    )

    if search:

        alerts = [

            alert

            for alert in alerts

            if search.lower()
            in str(alert).lower()

        ]

    return render_template(
        "index.html",
        alerts=alerts,
        search=search
    )

@app.route("/alerts")
def alerts_page():

    alerts = get_alerts()

    alerts = sorted(
        alerts,
        key=lambda x: x["timestamp"],
        reverse=True
    )

    return render_template(
        "alerts.html",
        alerts=alerts
    )


@app.route("/threat-intel")
def threat_intel_page():

    alerts = get_alerts()

    malicious_alerts = [

        alert

        for alert in alerts

        if alert["threat_intel"] == "Known Malicious"

    ]

    malicious_alerts = sorted(
        malicious_alerts,
        key=lambda x: x["timestamp"],
        reverse=True
    )

    return render_template(
        "threat_intel.html",
        alerts=malicious_alerts
    )


@app.route("/reports")
def reports_page():

    alerts = get_alerts()

    alerts = sorted(
        alerts,
        key=lambda x: x["timestamp"],
        reverse=True
    )

    return render_template(
        "reports.html",
        alerts=alerts
    )


@app.route("/settings")
def settings_page():

    return render_template(
        "settings.html"
    )


@app.route("/report/<alert_id>")
def report(alert_id):

    alerts = get_alerts()

    selected_alert = None

    for alert in alerts:

        if alert["alert_id"] == alert_id:

            selected_alert = alert

            break

    if selected_alert:

        filename = generate_report(
            selected_alert
        )

        return send_file(
            filename,
            as_attachment=True
        )

    return "Alert not found"


if __name__ == "__main__":

    threading.Thread(
        target=start_monitor,
        daemon=True
    ).start()

    socketio.run(
        app,
        host="0.0.0.0",
        port=5000,
        debug=False
    )

