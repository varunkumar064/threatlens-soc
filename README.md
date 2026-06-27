# 🛡️ ThreatLens

<h3 align="center">
Security Operations Center (SOC) Monitoring Platform
</h3>

<p align="center">
  Detect • Analyze • Monitor • Report
</p>

---

## 📖 Overview

ThreatLens is a Security Operations Center (SOC) monitoring platform built using Python and Flask.

The platform analyzes log files, detects suspicious activities, maps attacks to the MITRE ATT&CK framework, performs threat intelligence checks, stores alerts in a database, and visualizes security incidents through an interactive dashboard.

This project was developed to simulate real-world SOC workflows and incident monitoring processes.

---

## 🚀 Features

### 🚨 Threat Detection

* Brute Force Attack Detection
* Port Scan Detection
* Suspicious Login Detection
* Severity Classification
* Threat Scoring

### 🧠 Threat Intelligence

* Known Malicious IP Detection
* Threat Enrichment
* Risk Scoring

### 🗺 MITRE ATT&CK Mapping

* T1110 – Brute Force
* T1046 – Network Service Discovery
* T1078 – Valid Accounts

### 📊 Dashboard

* Total Alert Statistics
* High Severity Alerts
* Threat Distribution Chart
* Threat Score Analysis
* Search Functionality

### 📄 Reporting

* PDF Incident Reports
* Alert Documentation
* Security Event Tracking

---

## 🏗️ Architecture

```text
Log Files
    │
    ▼
Detection Engine
    │
    ├── Brute Force Detection
    ├── Port Scan Detection
    └── Suspicious Login Detection
    │
    ▼
MITRE ATT&CK Mapping
    │
    ▼
Threat Intelligence
    │
    ▼
SQLite Database
    │
    ▼
Flask Backend
    │
    ▼
SOC Dashboard
```

---

## 🔍 Detection Modules

### Brute Force Detection

Detects repeated failed login attempts from the same IP address.

Example:

```text
FAILED_LOGIN 192.168.1.101
FAILED_LOGIN 192.168.1.101
FAILED_LOGIN 192.168.1.101
FAILED_LOGIN 192.168.1.101
FAILED_LOGIN 192.168.1.101
```

---

### Port Scan Detection

Detects network scanning activity.

Example:

```text
PORT_SCAN 10.10.10.10
```

---

### Suspicious Login Detection

Detects potentially unauthorized login attempts.

Example:

```text
SUSPICIOUS_LOGIN 203.0.113.50
```

---

## 🛠️ Technologies Used

### Backend

* Python
* Flask
* SQLite

### Frontend

* HTML
* CSS
* Chart.js
* Jinja2

### Reporting

* ReportLab

### Security Concepts

* SOC Operations
* Threat Detection
* Threat Intelligence
* MITRE ATT&CK Framework
* Incident Monitoring

---

## 📂 Project Structure

```text
ThreatLens/
│
├── app.py
│
├── detection/
│   ├── detector.py
│   ├── brute_force.py
│   ├── port_scan.py
│   └── suspicious_login.py
│
├── database/
│   └── db.py
│
├── mitre/
│   └── attack_mapping.py
│
├── threat_intel/
│   └── intel_checker.py
│
├── reports/
│   └── report_generator.py
│
├── dashboard/
│   ├── templates/
│   └── static/
│
├── logs/
│   └── auth.log
│
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/varunkumar0164/ThreatLens.git
cd ThreatLens-SOC-Platform
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate the virtual environment:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install flask
pip install reportlab
```

Run the application:

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## 📸 Screenshots

Add screenshots of:

* Dashboard
* Alerts Page
* Threat Intelligence Page
* Reports Page

---

## 🎯 Learning Outcomes

This project helped me gain practical experience in:

* Log Analysis
* Threat Detection
* SOC Operations
* MITRE ATT&CK Mapping
* Threat Intelligence
* Incident Reporting
* Flask Development
* Database Management

---

## 🔮 Future Improvements

* Real-Time Monitoring
* Email Alerting
* External Threat Intelligence Feeds
* ELK Stack Integration
* Splunk Integration
* Machine Learning-Based Detection
* REST API Support

---

## 👨‍💻 Author

**Pavanakumara B**

GitHub: https://github.com/pavanakumarab

LinkedIn: https://www.linkedin.com/in/pavanakumarab/

