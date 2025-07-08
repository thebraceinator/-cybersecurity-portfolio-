# Log Alerting System

This is a simple Python-based log monitoring script designed to detect suspicious activity in server log files, such as:

- 🚫 Multiple failed login attempts from the same IP
- 🕒 Successful logins during odd hours (e.g., 12 AM – 6 AM)

## 🔧 How It Works

The script (`analyze_logs.py`) analyzes JSON-formatted logs and detects:

1. **Brute-force attempts**: More than 5 failed logins from the same user/IP within a 5-minute window.
2. **Suspicious login times**: Successful logins occurring between midnight and 6 AM.

Alerts are printed to the terminal and also written to `alerts_output.txt`.

## 📁 Files Included

- `analyze_logs.py`: Main script to run
- `simulated_logs.json`: Sample log entries for testing
- `alerts_output.txt`: Output alerts from the analysis

## ▶️ How to Run

1. Place all files in the same folder.
2. Open terminal and navigate to that folder:
   ```bash
   cd ~/Documents/log\ alerting
   ```
3. Run the script:
   ```bash
   python3 analyze_logs.py
   ```

## ✅ Sample Output

```
Multiple failed logins detected for user wayne_b from 192.168.1.12
Suspicious login at 03:00 by user john_smith from 10.0.0.5
```

## 🛠️ Skills Demonstrated

- Python scripting
- Security log analysis
- Brute-force detection
- Time-based anomaly detection
- JSON parsing and data handling

## 🚀 Next Steps (Ideas for Enhancement)

- Add severity levels to alerts
- Parse logs from real syslog/CSV files
- Add IP geolocation lookup (e.g., using IPinfo API)
- Integrate with a basic dashboard or email alert

## 📌 Author

Wayne Bracy  
Aspiring Cybersecurity Analyst | Former QA Engineer | Security+ Candidate