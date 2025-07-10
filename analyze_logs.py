import json
from datetime import datetime, timedelta

def load_logs(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)

def parse_time(ts):
    return datetime.strptime(ts, "%Y-%m-%dT%H:%M:%S")

def detect_failed_logins(logs, threshold=5, window_minutes=5):
    alerts = []
    login_attempts = {}

    for log in logs:
        if log['event'] != 'failed_login':
            continue
        key = (log['username'], log['ip_address'])
        login_attempts.setdefault(key, []).append(parse_time(log['timestamp']))

    for key, times in login_attempts.items():
        times.sort()
        for i in range(len(times) - threshold + 1):
            if times[i + threshold - 1] - times[i] <= timedelta(minutes=5):
                alerts.append(f"Multiple failed logins detected for user {key[0]} from {key[1]}")
                break

    return alerts

def detect_odd_login_times(logs, hours=(0, 6)):
    alerts = []
    for log in logs:
        dt = parse_time(log['timestamp'])
        if log['event'] == 'successful_login' and dt.hour >= hours[0] and dt.hour < hours[1]:
            alerts.append(f"Suspicious login at {dt.strftime('%H:%M')} by user {log['username']} from {log['ip_address']}")
    return alerts

if __name__ == "__main__":
    logs = load_logs("simulated_logs.json")
    alerts = []
    alerts.extend(detect_failed_logins(logs))
    alerts.extend(detect_odd_login_times(logs))

    with open("alerts_output.txt", "w") as f:
        for alert in alerts:
            print(alert)
            f.write(alert + "\n")
