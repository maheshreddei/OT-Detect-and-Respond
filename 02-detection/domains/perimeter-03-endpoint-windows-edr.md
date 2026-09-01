# 03 — Endpoint: Windows & EDR

Where the foothold executes. These cover suspicious execution, credential access, persistence, and defense evasion on Windows endpoints — best served by EDR (MDE/CrowdStrike) telemetry, with Windows Security/Sysmon as the fallback.

## Detections

| ID | Detection | Logic | Data source | ATT&CK | Severity |
|----|-----------|-------|-------------|--------|----------|
| EDR-01 | Encoded / suspicious PowerShell | `-enc`/`-e`, `FromBase64String`, `IEX`, download cradles | 4104 / Sysmon 1 / DeviceProcessEvents | T1059.001 | high |
| EDR-02 | LOLBin abuse | certutil/mshta/rundll32/regsvr32/bitsadmin with network or script args | 4688 / Sysmon 1 / DeviceProcessEvents | T1218 | high |
| EDR-03 | Credential access (LSASS) | Non-system process opens/dumps lsass.exe | Sysmon 10 / DeviceEvents (MDE) | T1003.001 | critical |
| EDR-04 | Persistence — run key / startup | Registry Run-key write or startup-folder drop | Sysmon 13 / DeviceRegistryEvents | T1547.001 | high |
| EDR-05 | Persistence — service install | New service created (7045) esp. with suspicious path | 7045 / DeviceEvents | T1543.003 | high |
| EDR-06 | Persistence — scheduled task | schtasks/at task creation (4698) | 4698 / DeviceProcessEvents | T1053.005 | medium |
| EDR-07 | Defense evasion — log clearing | Security/System log cleared (1102/104) | 1102 / SecurityEvent | T1070.001 | high |
| EDR-08 | Defense evasion — AV/EDR tamper | Defender disabled / tamper, service stop | Defender events / DeviceEvents | T1562.001 | critical |
| EDR-09 | Suspicious parent-child | office/browser spawning cmd/powershell/wscript | Sysmon 1 / DeviceProcessEvents | T1059 / T1204 | high |
| EDR-10 | Masquerading binary | system-name binary from non-standard path | Sysmon 1 / DeviceProcessEvents | T1036.005 | medium |

## Worked queries

### EDR-01 — Encoded / suspicious PowerShell

**Sentinel (KQL)** — MDE process events:
```kql
DeviceProcessEvents
| where TimeGenerated > ago(1h)
| where FileName in~ ("powershell.exe","pwsh.exe")
| where ProcessCommandLine has_any ("-enc","-e ","-EncodedCommand","FromBase64String",
        "IEX","Invoke-Expression","DownloadString","DownloadFile","-nop","-w hidden","hidden")
| project TimeGenerated, DeviceName, AccountName, InitiatingProcessFileName, ProcessCommandLine
| sort by TimeGenerated desc
```

**Splunk (SPL)** — Sysmon:
```spl
index=sysmon EventCode=1 (Image="*powershell.exe" OR Image="*pwsh.exe")
| regex CommandLine="(?i)(-enc|-e\s|FromBase64String|IEX|Invoke-Expression|DownloadString|DownloadFile|-nop|-w\s?hidden)"
| table _time Computer User ParentImage Image CommandLine
| sort - _time
```

### EDR-03 — LSASS credential access

**Sentinel (KQL)**:
```kql
DeviceEvents
| where TimeGenerated > ago(1h)
| where ActionType == "ProcessAccessedLSASS" or FileName =~ "lsass.exe"
| where InitiatingProcessFileName !in~ ("wininit.exe","services.exe","svchost.exe","MsMpEng.exe","csrss.exe")
| project TimeGenerated, DeviceName, InitiatingProcessFileName, InitiatingProcessCommandLine, AccountName
| sort by TimeGenerated desc
```

**Splunk (SPL)** — Sysmon 10 (ProcessAccess to lsass):
```spl
index=sysmon EventCode=10 TargetImage="*lsass.exe"
| where NOT (SourceImage IN ("C:\\Windows\\System32\\wininit.exe","C:\\Windows\\System32\\services.exe","C:\\Program Files\\Windows Defender\\MsMpEng.exe"))
| table _time Computer SourceImage GrantedAccess TargetImage
| sort - _time
```

### EDR-07 — Windows event log cleared

**Splunk (SPL)**:
```spl
index=wineventlog (EventCode=1102 OR EventCode=104)
| table _time Computer EventCode Account_Name Message
| sort - _time
```

## Tuning
- Filter known-good admin/automation tooling (SCCM, monitoring agents) that legitimately use LOLBins/PowerShell — but keep the download-cradle and hidden-window patterns high-severity.
- EDR-03/EDR-08 are near-true-positive; route them to high/critical with minimal suppression.
- Where you have MDE/CrowdStrike, ingest their own detections too and use these as coverage for gaps / cross-tool correlation.
