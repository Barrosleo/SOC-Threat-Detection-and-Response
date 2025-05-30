#!/usr/bin/env python3
"""
Ingest SIEM Logs

This script ingests SIEM log data from a local JSON file and processes it for further analysis.
"""

import json
import sys

def ingest_logs(file_path):
    try:
        with open(file_path, "r") as f:
            logs = json.load(f)
        print(f"Ingested {len(logs)} log entries.")
    except Exception as e:
        print(f"Error ingesting logs: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ingest_siEM_logs.py <path_to_logs.json>")
        sys.exit(1)
    ingest_logs(sys.argv[1])
