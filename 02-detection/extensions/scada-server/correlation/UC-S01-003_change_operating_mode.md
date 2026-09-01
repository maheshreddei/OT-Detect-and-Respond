# UC-S01-003 — Controller Operating-Mode Change

| | |
|---|---|
| **ID** | 3973864b-ad9d-41e9-a06a-1e259f20881a |
| **Asset** | S-01 (Control/SCADA Server) as command origin |
| **ATT&CK for ICS** | T0858 Change Operating Mode |
| **Streams** | Controller telemetry (Nozomi) + maintenance/operator context |
| **Level** | high |

## Rationale
A controller key/mode transition (RUN -> PROGRAM / REMOTE / STOP) is a strong pre-manipulation
signal. Legitimate mode changes happen under maintenance; unexplained ones — especially sourced
from S-01 — precede logic or parameter tampering.

## 1. Controller stream — Nozomi N2QL
```n2ql
alerts
| where type_id in [ "SIGN:PLC-MODE-CHANGE", "SIGN:S7-PLC-STOP",
                     "SIGN:S7-PLC-START", "SIGN:CIP-MODE-CHANGE" ]
| select record_created_at, ip_src, ip_dst, protocol, type_id, name, content
```

## 2. Correlation — Sentinel KQL
```kql
let SanctionedEWS = dynamic(["10.20.0.30","10.20.0.31"]);
Nozomi_Controller_CL
| where CommandType_s == "mode_change"
| extend NewMode = column_ifexists("NewMode_s","")
| where NewMode in ("PROGRAM","REMOTE","STOP")
| extend Suspicious = (SrcIp_s !in (SanctionedEWS))
| where Suspicious
| project TimeGenerated, SrcIp_s, DstIp_s, Protocol_s, NewMode
| extend Alert = "T0858 Operating-mode change from unsanctioned source"
// Enrich: correlate against open maintenance ticket for DstIp_s; no ticket -> escalate
```

## 3. Correlation — Splunk SPL
```spl
index=ot sourcetype=nozomi:controller CommandType=mode_change (NewMode=PROGRAM OR NewMode=REMOTE OR NewMode=STOP)
| eval suspicious=if(NOT (SrcIp IN ("10.20.0.30","10.20.0.31")),1,0)
| where suspicious=1
| table _time, SrcIp, DstIp, Protocol, NewMode
| eval Alert="T0858 Operating-mode change from unsanctioned source"
```
> Optional maintenance-context join: `lookup maint_windows.csv Controller AS DstIp` and drop rows
> that fall inside an open window. Keeps false positives off scheduled work.

## Response
Notify control-room immediately; an unexplained RUN->PROGRAM on a live controller is treated as
an in-progress manipulation until the process engineer confirms otherwise.
