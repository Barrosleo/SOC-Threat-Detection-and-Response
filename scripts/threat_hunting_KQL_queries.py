#!/usr/bin/env python3
"""
Threat Hunting KQL Queries

This script contains advanced KQL queries for threat hunting in Microsoft Sentinel.
"""

def query_for_lateral_movement():
    query = """
    SecurityEvent
    | where EventID == 4624
    | where AccountType == "User"
    | summarize count() by Computer, Account
    """
    return query

if __name__ == "__main__":
    print("Threat Hunting Query for Lateral Movement:")
    print(query_for_lateral_movement())
