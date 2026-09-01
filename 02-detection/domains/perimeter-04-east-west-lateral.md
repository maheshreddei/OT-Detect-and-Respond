# 04 — East-West / Lateral Movement

After the foothold, attackers move sideways. These detect internal reconnaissance and lateral movement as **deviations from normal internal communication** plus known lateral techniques. East-west telemetry is the classic blind spot — these depend on internal flow / EDR network events.

## Detections

| ID | Detection | Logic | Data source | ATT&CK | Severity |
|----|-----------|-------|-------------|--------|----------|
| EW-01 | Internal host scanning | One internal host → many internal peers/ports in a short window | internal flow / DeviceNetworkEvents | T1046 | high |
| EW-02 | New east-west peer relationship | src→dst (or src→dst:port) pair not seen in the baseline window | flow baseline | T1021 | medium |
| EW-03 | Lateral movement — SMB admin shares | Access to ADMIN$/C$/IPC$ from non-admin/unusual source | 5140/5145 / DeviceNetworkEvents | T1021.002 | high |
| EW-04 | Lateral movement — RDP internal spread | Internal RDP (3389) from a host that doesn't normally initiate it | 4624 type 10 / flow | T1021.001 | high |
| EW-05 | Lateral movement — WMI/WinRM exec | wmic/winrm remote process creation | Sysmon 1 / DeviceProcessEvents | T1021.006 / T1047 | high |
| EW-06 | Remote service creation (PsExec-like) | Service install (7045) on remote host + SMB session | 7045 + 5145 | T1021.002 / T1569 | high |
| EW-07 | Pass-the-hash / anomalous NTLM | NTLM auth where Kerberos expected; logon type/pattern anomaly | 4624/4776 | T1550.002 | high |
| EW-08 | Kerberoasting | Burst of TGS requests (4769) with RC4 for many SPNs | 4769 | T1558.003 | high |
| EW-09 | Internal DNS/AD recon | Bulk LDAP/DNS enumeration from one host | 4662 / DNS / Sysmon | T1087 / T1018 | medium |

## Worked queries

### EW-01 — Internal host scanning

**Sentinel (KQL)** — MDE network events:
```kql
let window = 10m;
let peerThreshold = 50;
DeviceNetworkEvents
| where TimeGenerated > ago(window)
| where RemoteIPType == "Private"
| summarize Peers = dcount(RemoteIP), Ports = dcount(RemotePort), Attempts = count()
    by DeviceName, LocalIP
| where Peers > peerThreshold or Ports > 100
| sort by Peers desc
```

**Splunk (SPL)** — internal flow:
```spl
index=flow earliest=-10m
| search src_ip=10.0.0.0/8 OR src_ip=172.16.0.0/12 OR src_ip=192.168.0.0/16
| stats dc(dest_ip) as peers dc(dest_port) as ports count as attempts by src_ip
| where peers > 50 OR ports > 100
| sort - peers
```

### EW-02 — New east-west peer relationship

**Splunk (SPL)** — compare live pairs to a known-pairs lookup:
```spl
index=flow earliest=-1h
| eval pair=src_ip."->".dest_ip.":".dest_port
| stats count by pair src_ip dest_ip dest_port
| lookup known_east_west_pairs.csv pair OUTPUT first_seen
| where isnull(first_seen)
| table _time src_ip dest_ip dest_port count
| sort - count
```
> Maintain `known_east_west_pairs.csv` from a scheduled search over the baseline window (see baseline-methodology).

**Sentinel (KQL)** — new pair vs a 14-day baseline:
```kql
let lookback = 14d;
let baseline = DeviceNetworkEvents
    | where TimeGenerated between (ago(lookback) .. ago(1d)) and RemoteIPType == "Private"
    | summarize by LocalIP, RemoteIP, RemotePort;
DeviceNetworkEvents
| where TimeGenerated > ago(1d) and RemoteIPType == "Private"
| summarize Conns = count() by LocalIP, RemoteIP, RemotePort
| join kind=leftanti baseline on LocalIP, RemoteIP, RemotePort
| sort by Conns desc
```

### EW-08 — Kerberoasting

**Splunk (SPL)**:
```spl
index=wineventlog EventCode=4769 Ticket_Encryption_Type=0x17
| stats dc(Service_Name) as spns count by Account_Name Client_Address
| where spns >= 10
| sort - spns
```

## Tuning
- Exclude legitimate scanners (vuln management, asset discovery), backup servers, and monitoring hosts from EW-01/EW-02 — they are the top FP sources.
- EW-02 needs a solid baseline; start in report-only until the known-pairs set stabilizes.
- Correlate EW detections with 02 (identity) and 03 (endpoint) on the same host to promote confidence.
