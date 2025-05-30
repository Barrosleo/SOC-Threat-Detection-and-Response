#!/usr/bin/env python3
"""
SOC Alert Prioritization

This script simulates prioritizing SOC alerts based on severity scores.
"""

def prioritize_alerts():
    alerts = [
        {"id": "Alert1", "severity": "High"},
        {"id": "Alert2", "severity": "Medium"},
        {"id": "Alert3", "severity": "Low"}
    ]
    sorted_alerts = sorted(alerts, key=lambda x: {"High": 1, "Medium": 2, "Low": 3}[x["severity"]])
    print("Prioritized alerts:")
    for alert in sorted_alerts:
        print(alert)

if __name__ == "__main__":
    prioritize_alerts()
