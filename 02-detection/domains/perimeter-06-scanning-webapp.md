# 06 — Outbound Scanning & Web-App Attacks

Two related surfaces: an internal host scanning **external** IP ranges (recon/compromise), and attacks against **public web applications** (the T1190 exploit path). Detections run on firewall/flow and WAF/web-server logs.

## Detections

| ID | Detection | Logic | Data source | ATT&CK | Severity |
|----|-----------|-------|-------------|--------|----------|
| SCN-01 | Outbound scanning to external ranges | Internal host → many external IPs on one port (horizontal) | firewall/flow | T1595.001 | high |
| SCN-02 | Outbound vertical scan | Internal host → many ports on one external host | firewall/flow | T1595.001 | medium |
| SCN-03 | High outbound deny rate | One internal source generating many firewall denies outbound | firewall | T1595 | medium |
| WEB-01 | Web login brute force | Many auth failures (401/403 or app-login) then success, one source | WAF / IIS / app | T1110 | high |
| WEB-02 | Directory / endpoint enumeration | Burst of 404s / many distinct paths from one source | WAF / IIS | T1595.003 | medium |
| WEB-03 | Injection patterns (SQLi/XSS/cmd) | Request contains SQLi/XSS/traversal/command signatures | WAF / web | T1190 | high |
| WEB-04 | High 5xx / error spike | Surge of server errors (exploitation / fuzzing) | web / LB | T1190 | medium |
| WEB-05 | Suspicious user-agent / tool | scanner/tool user-agents (sqlmap, nikto, nmap, curl bursts) | WAF / web | T1595 | medium |
| WEB-06 | Web shell indicators | Requests to newly-created script paths; POST to odd endpoints | web / EDR | T1505.003 | critical |

## Worked queries

### SCN-01 — Outbound horizontal scan to external ranges

**Splunk (SPL)**:
```spl
index=firewall direction=outbound earliest=-10m
| search NOT dest_ip IN (10.0.0.0/8,172.16.0.0/12,192.168.0.0/16)
| stats dc(dest_ip) as ext_targets values(dest_port) as ports by src_ip dest_port
| where ext_targets > 100
| sort - ext_targets
```

**Sentinel (KQL)**:
```kql
CommonSecurityLog
| where TimeGenerated > ago(10m) and Direction == "Outbound"
| where not(ipv4_is_private(DestinationIP))
| summarize ExtTargets = dcount(DestinationIP) by SourceIP, DestinationPort
| where ExtTargets > 100
| sort by ExtTargets desc
```

### WEB-02 — Directory enumeration (404 burst)

**Sentinel (KQL)** — IIS logs:
```kql
W3CIISLog
| where TimeGenerated > ago(15m)
| summarize Total = count(), NotFound = countif(scStatus == 404), Paths = dcount(csUriStem)
    by cIP
| where NotFound > 100 and Paths > 100
| extend NotFoundRatio = round(NotFound * 1.0 / Total, 2)
| sort by NotFound desc
```

**Splunk (SPL)**:
```spl
index=web earliest=-15m
| stats count as total count(eval(status==404)) as notfound dc(uri_path) as paths by clientip
| where notfound > 100 AND paths > 100
| eval nf_ratio=round(notfound/total,2)
| sort - notfound
```

### WEB-03 — Injection / traversal patterns

**Splunk (SPL)**:
```spl
index=web
| eval decoded=urldecode(uri_query)
| regex decoded="(?i)(union\s+select|or\s+1=1|<script>|onerror=|\.\./|\bexec\b|xp_cmdshell|;--|/etc/passwd|base64_decode)"
| table _time clientip method uri_path decoded status http_user_agent
| sort - _time
```

## Tuning
- Exclude sanctioned vulnerability scanners and uptime monitors from SCN-* and WEB-* (allow-list their source IPs) — otherwise they dominate.
- Prefer your WAF's own signatures for WEB-03 where present; this layer catches gaps and feeds correlation.
- WEB-06 (web shell) is near-critical; correlate new script-file creation on the web host (category 03) with anomalous POSTs.
