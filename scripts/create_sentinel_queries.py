#!/usr/bin/env python3
"""
Create Sentinel Queries

This script generates sample KQL queries for Microsoft Sentinel.
"""

def generate_query():
    query = """
    SigninLogs
    | where ResultType == "50126"
    | summarize Count = count() by UserPrincipalName, IPAddress, bin(TimeGenerated, 1h)
    | order by Count desc
    """
    return query

if __name__ == "__main__":
    print("Sample Microsoft Sentinel Query:")
    print(generate_query())
