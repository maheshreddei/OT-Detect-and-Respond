# 02 — Identity & Account

Where external access becomes a foothold. These cover authentication abuse (brute force, spray), the high-signal **success-after-failures** case, and privilege/permission changes. Identity is often the first place an intrusion is provable.

## Detections

| ID | Detection | Logic | Data source | ATT&CK | Severity |
|----|-----------|-------|-------------|--------|----------|
| IAM-01 | Brute force (single account) | Many auth failures against one account over a short window | auth logs / SigninLogs | T1110.001 | medium |
| IAM-02 | Password spray | One source → failures across **many** accounts (few attempts each) | auth logs / SigninLogs | T1110.003 | high |
| IAM-03 | **Success after repeated failures** | N+ failures then a success for the same account/source | auth logs / SigninLogs | T1110 | high |
| IAM-04 | Privilege / permission change | Add to privileged group, role assignment, admin grant | 4728/4732/4756; AuditLogs | T1098 / T1078 | high |
| IAM-05 | New / re-enabled account then use | Account created/enabled (4720/4722) and used shortly after | Security / AuditLogs | T1136 | medium |
| IAM-06 | Impossible travel / atypical geo | Same account authenticates from geographically impossible locations | SigninLogs | T1078 | high |
| IAM-07 | Off-hours privileged logon | Admin logon outside normal hours / from new device | auth logs | T1078 | medium |
| IAM-08 | Disabled/dormant account use | Auth success for an account long inactive or disabled | auth logs | T1078.002 | high |
| IAM-09 | MFA fatigue / repeated MFA prompts | Many MFA challenges then an approval | SigninLogs (auth detail) | T1621 | high |

## Worked queries

### IAM-03 — Success after repeated failures (brute-force success)

**Sentinel (KQL)** — Entra ID sign-ins:
```kql
let window = 1h;
let failThreshold = 10;
let signins = union SigninLogs, AADNonInteractiveUserSignInLogs
    | where TimeGenerated > ago(window)
    | project TimeGenerated, UserPrincipalName, IPAddress, ResultType;
let failures = signins | where ResultType != "0"
    | summarize Failures = count(), FirstFail = min(TimeGenerated), LastFail = max(TimeGenerated)
        by UserPrincipalName, IPAddress
    | where Failures >= failThreshold;
let successes = signins | where ResultType == "0"
    | summarize SuccessTime = min(TimeGenerated) by UserPrincipalName, IPAddress;
failures
| join kind=inner successes on UserPrincipalName, IPAddress
| where SuccessTime > LastFail
| project UserPrincipalName, IPAddress, Failures, FirstFail, LastFail, SuccessTime
| sort by Failures desc
```

**Splunk (SPL)** — Windows Security (4625 then 4624):
```spl
index=wineventlog (EventCode=4625 OR EventCode=4624)
| eval outcome=if(EventCode==4625,"fail","success")
| transaction user src_ip maxspan=1h startswith=eval(outcome=="fail") endswith=eval(outcome=="success")
| eval failures=mvcount(mvfilter(match(outcome,"fail")))
| where failures >= 10
| table _time user src_ip failures duration
| sort - failures
```

### IAM-02 — Password spray

**Splunk (SPL)**:
```spl
index=wineventlog EventCode=4625 earliest=-1h
| stats dc(user) as accounts_targeted count as attempts values(user) as users by src_ip
| where accounts_targeted >= 20 AND (attempts/accounts_targeted) < 5
| sort - accounts_targeted
```

**Sentinel (KQL)**:
```kql
union SigninLogs, AADNonInteractiveUserSignInLogs
| where TimeGenerated > ago(1h) and ResultType != "0"
| summarize Accounts = dcount(UserPrincipalName), Attempts = count() by IPAddress
| where Accounts >= 20 and (Attempts * 1.0 / Accounts) < 5
| sort by Accounts desc
```

### IAM-04 — Privilege escalation via group change

**Splunk (SPL)**:
```spl
index=wineventlog (EventCode=4728 OR EventCode=4732 OR EventCode=4756)
| eval group=Group_Name, member=Member_Name
| search group IN ("Domain Admins","Enterprise Admins","Administrators","Schema Admins")
| table _time Security_ID member group Subject_Account_Name EventCode
| sort - _time
```

## Tuning
- IAM-03/IAM-01 thresholds (10 failures) depend on lockout policy; lower for high-value accounts.
- Exclude known scanners/health-checks and service accounts with expected failure patterns — but treat **service-account** spray/success as higher, not lower, severity.
- Impossible travel (IAM-06) has native analytics in Sentinel/UEBA; prefer those and use this layer to correlate.
