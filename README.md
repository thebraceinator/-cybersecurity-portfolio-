# Cybersecurity Portfolio – Log Alerting System

Welcome to my cybersecurity portfolio! This repository features a Python-based **log alerting system** that simulates core Security Operations Center (SOC) tasks — specifically, identifying suspicious activity such as brute-force login attempts and anomalous logins.

## Project Overview

This project demonstrates my ability to:
- Write clean and modular Python code
- Work with JSON-formatted log data
- Detect security anomalies using custom logic
- Send **automated email alerts** via SMTP (Gmail)
- Apply real-world thinking to cybersecurity monitoring

## Features

- Brute-force login detection (5+ failed attempts from same IP)
- Suspicious login detection (e.g., logins at odd hours)
- Email alerting via Gmail using Python's `smtplib`
- Upcoming: Slack alerts, file output, log dashboard (future phase)

## Files Included

- `analyze_logs.py` – Base version for log detection
- `analyze_logs_with_email.py` – Version that sends email alerts
- `simulated_logs.json` – Sample log data for testing

## Tech Stack

- Python 3.8+
- JSON
- Gmail SMTP (for email alerts)

## How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/thebraceinator/cybersecurity-portfolio.git
   cd cybersecurity-portfolio
2. Install dependencies (if any are added)
3. Run: python3 analyze_logs_with_email.py
4. View alerts in your email inbox (configured in script)
      sender = "your-email@gmail.com"
      recipient = "recipient-email@gmail.com"
      app_password = "your-app-password"

## About Me

I’m Wayne Bracy — a QA engineer transitioning into cybersecurity with hands-on projects like this one. I’ve completed the Google Cybersecurity Certificate and am currently preparing to sut for the CompTIA Security+ exam. 

Let’s connect on LinkedIn or see more of my work on GitHub.
