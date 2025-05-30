# Microsoft Sentinel KQL Queries

This document contains pre-built KQL (Kusto Query Language) queries for Microsoft Sentinel to help you detect potential threats.

## Sample Query 1: Suspicious Login Attempts
```kusto
SigninLogs
| where ResultType == "50126"
| summarize Count = count() by UserPrincipalName, IPAddress, bin(TimeGenerated, 1h)
| order by Count desc
```

## Sample Query 2: Failed Login Analysis
```kusto
SigninLogs
| where ResultType != 0
| summarize FailCount = count() by IPAddress, bin(TimeGenerated, 1h)
| order by FailCount desc
```

