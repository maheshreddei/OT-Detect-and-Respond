# UC-S01-001 — Operator-Intent Correlation (Unauthorized Command Message)

| | |
|---|---|
| **ID** | 0b3804be-3509-4176-8415-003a9759d9e3 |
| **Asset** | S-01 (Control/SCADA Server) |
| **ATT&CK for ICS** | T0855 Unauthorized Command Message (enrich: T0831 Manipulation of Control) |
| **Streams** | Controller telemetry (Nozomi) + SCADA operator-action log (S-01 host) |
| **Level** | high |

## Rationale
A command issued from a compromised SCADA host is *protocol-valid* and *credential-valid*,
so protocol-anomaly detection will not fire. Legitimacy is anchored to **operator intent**:
every downstream control command must correspond to a matching, authenticated operator action
on the HMI within a tight time window. Commands with no matching operator action are the signal.

## Dependency (state honestly)
Requires the SCADA platform's **operator-action / tag-write audit log** to be enabled and
forwarded. Many platforms disable this by default. If unavailable, the degraded proxy is
`HMI session active AND expected source IP` — weaker, and it must be labelled as reduced fidelity.

---
## 1. Controller stream — Nozomi N2QL
Defines the downstream command stream sourced from S-01. Verify `type_id` values and field
names against your N2OS version and enabled protocol packages — these vary by release.

```n2ql
alerts
| where ip_src == "10.30.0.5"            // S-01
| where type_id in [
      "SIGN:MODBUS-WRITE-SINGLE", "SIGN:MODBUS-WRITE-MULTIPLE",
      "SIGN:DNP3-OPERATE", "SIGN:DNP3-CROB",
      "SIGN:S7-WRITE", "SIGN:IEC104-CONTROL", "SIGN:OPCUA-WRITE" ]
| select record_created_at, ip_src, ip_dst, protocol, type_id, name, content
```

Raw-write alternative (variable-write tracking, if you export `variables`):
```n2ql
variables
| where src_ip == "10.30.0.5"
| where access == "write"
| select time, src_ip, dst_ip, protocol, name /* point/tag */, value
```

Forward this stream to the SIEM as `Nozomi_Controller_CL` (Sentinel) / `nozomi:controller` (Splunk).

---
## 2. Correlation — Sentinel KQL
```kql
let win = 5s;
let S01_IP = "10.30.0.5";
let cmds = Nozomi_Controller_CL
    | where SrcIp_s == S01_IP
    | where CommandType_s in ("write","control","operate","crob","c_sc","c_dc")
    | project CmdTime=TimeGenerated, Tag_s, Value_s, DstIp_s, Protocol_s,
              CmdId = strcat(Tag_s,"|",format_datetime(TimeGenerated,"HH:mm:ss.fff"));
let ops = Scada_OpLog_CL
    | where Authenticated_b == true
    | project OpTime=TimeGenerated, Tag_s, Operator_s, SessionId_s;
cmds
| join kind=leftouter ops on Tag_s
| extend matched = iff(isnotnull(OpTime) and abs(datetime_diff('second', CmdTime, OpTime)) <= 5, 1, 0)
| summarize hasMatch = max(matched) by CmdId, CmdTime, Tag_s, Value_s, DstIp_s, Protocol_s
| where hasMatch == 0
| extend Alert = "T0855 Unauthorized command - no matching operator intent"
// Enrichment: join host telemetry on S-01 at +/- win to attribute (injected DLL / non-operator logon / new proc)
```

---
## 3. Correlation — Splunk SPL
```spl
(index=ot sourcetype=nozomi:controller SrcIp="10.30.0.5"
   (CommandType=write OR CommandType=control OR CommandType=operate OR CommandType=crob OR CommandType=c_sc OR CommandType=c_dc))
OR (index=ot sourcetype=scada:oplog Authenticated=true)
| eval kind=if(sourcetype=="nozomi:controller","cmd","op")
| transaction Tag maxspan=5s keepevicted=true
| eval has_cmd=if(searchmatch("kind=cmd"),1,0), has_op=if(searchmatch("kind=op"),1,0)
| where has_cmd=1 AND has_op=0
| table _time, Tag, Value, SrcIp, DstIp, Protocol
| eval Alert="T0855 Unauthorized command - no matching operator intent"
```
> Cross-source absence-matching is environment-specific. Treat the KQL join and the SPL
> `transaction` as **reference implementations** — validate window behaviour against your
> data volumes before production (high tag-write rates may need per-tag bucketing / a lookup).

## Enrichment (attribution)
On a positive hit, pivot to S-01 host telemetry at `CmdTime ± 5s`:
non-operator logon session, new process spawn, DLL injected into the HMI runtime
(see `s01_unsigned_dll_hmi_runtime`), or PowerShell. Command + injected DLL at the same second
= compromised-supervisor. Command + unexpected source IP = rogue master on the segment.

## Response
Playbook: safety-first. Do **not** auto-block on the OT path. Notify process engineer /
control-room; containment (session kill, host isolation) requires process-engineer authorization.
