# UC-S01-002 — Program/Logic Download Provenance

| | |
|---|---|
| **ID** | 9c4041d2-a8ec-41bc-a340-0c79c7ae3e84 |
| **Asset** | S-01 (Control/SCADA Server) as anomalous origin |
| **ATT&CK for ICS** | T0843 Program Download |
| **Streams** | Controller telemetry (Nozomi) + S-01 host process telemetry |
| **Level** | high |

## Rationale
Legitimate logic/program downloads originate from a **sanctioned engineering workstation (EWS)
during a change window** — never from the SCADA server. Any download whose origin is S-01,
or an unsanctioned host, or outside the change window, is suspect.

## 1. Controller stream — Nozomi N2QL
```n2ql
alerts
| where type_id in [
      "SIGN:S7-DOWNLOAD", "SIGN:PLC-PROGRAM-DOWNLOAD",
      "SIGN:CIP-FORWARD-OPEN-WRITE", "SIGN:ENG-SESSION-DOWNLOAD" ]
| select record_created_at, ip_src, ip_dst, protocol, type_id, name
```
> Confirm the download `type_id`s exist for your protocol packs; on some deployments logic
> download surfaces as a PROTOCOL:/VI: assertion rather than SIGN:. Adjust accordingly.

## 2. Correlation — Sentinel KQL
```kql
let S01_IP = "10.30.0.5";
let SanctionedEWS = dynamic(["10.20.0.30","10.20.0.31"]);   // PLACEHOLDER
let ChangeStart = todatetime("2026-08-12T22:00:00Z");        // wire to your change calendar
let ChangeEnd   = todatetime("2026-08-13T02:00:00Z");
Nozomi_Controller_CL
| where CommandType_s == "program_download"
| extend BadOrigin  = (SrcIp_s == S01_IP) or (SrcIp_s !in (SanctionedEWS))
| extend OutOfWindow = not(TimeGenerated between (ChangeStart .. ChangeEnd))
| where BadOrigin or OutOfWindow
| project TimeGenerated, SrcIp_s, DstIp_s, Protocol_s, BadOrigin, OutOfWindow
| extend Alert = "T0843 Program download - anomalous provenance"
// Enrich: DeviceProcessEvents on S-01 for an engineering tool spawn (e.g. Step7/TIA/Studio 5000)
```

## 3. Correlation — Splunk SPL
```spl
index=ot sourcetype=nozomi:controller CommandType=program_download
| eval bad_origin=if(SrcIp=="10.30.0.5" OR NOT (SrcIp IN ("10.20.0.30","10.20.0.31")),1,0)
| eval hour=strftime(_time,"%H"), out_of_window=if(hour>=2 AND hour<22,1,0)
| where bad_origin=1 OR out_of_window=1
| table _time, SrcIp, DstIp, Protocol, bad_origin, out_of_window
| eval Alert="T0843 Program download - anomalous provenance"
```

## Response
High-severity to control-room + engineering. Correlate with the change record; an unmatched
download to a live controller is a candidate incident, not an auto-action.
