# B — SIS Engineering & Program Integrity

**Principle defended: integrity of the safety logic (primer §2).** This is the **TRITON/TRISIS** category — the attack reached a Triconex SIS through the engineering path and attempted to alter its logic. These detect engineering sessions, program transfers, mode/key-switch changes, and logic/firmware modification against the safety controller. Any hit is SEV-1.

## Detections

| ID | Detection | Logic | Data source | ATT&CK | Severity |
|----|-----------|-------|-------------|--------|----------|
| SIS-B1 | SIS engineering-tool session | TriStation/SILworX/TIA-Safety/Studio5000 session to a safety controller | NDR (safety net) | T0868 / T0843 | high |
| SIS-B2 | SIS program download (logic change) | Program/logic download to the safety controller | NDR + SIS event log | T0843 | critical |
| SIS-B3 | SIS program upload (recon/theft) | Program/logic upload from the safety controller | NDR | T0845 | high |
| SIS-B4 | Key-switch / mode → PROGRAM or REMOTE | Safety controller mode change enabling logic changes | key-switch DI / SIS event log | T0858 | critical |
| SIS-B5 | SIS logic differs from golden baseline | Read-only logic compare mismatch vs known-good | offline compare (engineer-led) | T0889 | critical |
| SIS-B6 | SIS firmware change | Firmware version delta / firmware-update mode | SIS event log / NDR | T0839 / T0800 | critical |
| SIS-B7 | SIS engineering off-window / from new host | Engineering activity outside maintenance window or from an unexpected station | NDR + host | T0868 | high |

## Worked queries

### SIS-B2 — SIS program download (native signature + generic)
Nozomi N2QL — ride the NDR's built-in safety signatures (Guardian/Dragos flag TriStation program transfer):
```
alerts | where type_id include? "PROGRAM" OR type_id include? "TRISTATION"
     OR type_id include? "DOWNLOAD" OR type_id include? "SIS"
| select type_id ip_src ip_dst created_time | sort created_time desc
```
Generic engineering-traffic-into-SIS fallback:
```
links | where protocol == tristation OR protocol == s7 OR protocol == cip
| join nodes to ip | select from to joined_node_to_ip.label->sis_asset joined_node_to_ip.zone->to_zone protocol last_activity_time
| where to_zone include? "<SIS_ZONE>" | where from exclude? "<APPROVED_SIS_EWS_IP>"
| sort last_activity_time desc
```
**Assert:** non-empty ⇒ **critical**. A program download to a safety controller — especially from anything but the approved, in-window engineering station — is the TRITON signature.

### SIS-B4 — Key-switch / mode change to PROGRAM
Splunk SPL — historised key-switch position (safety controllers should sit in RUN):
```spl
index=ot_historian tag="*SIS*KEYSWITCH*" OR tag="*SIS*MODE*"
| sort 0 tag _time
| streamstats current=f last(value) as prev_mode by tag
| where value != prev_mode AND (value=="PROGRAM" OR value=="REMOTE")
| table _time tag prev_mode value
| sort - _time
```
Sentinel KQL:
```kql
OTHistorian_CL
| where TimeGenerated > ago(1h) and (TagName_s has "SIS" and (TagName_s has "KEYSWITCH" or TagName_s has "MODE"))
| order by TagName_s asc, TimeGenerated asc
| serialize
| extend prev_mode = iff(TagName_s == prev(TagName_s), prev(Value_s), "")
| where Value_s != prev_mode and Value_s in ("PROGRAM","REMOTE")
| project TimeGenerated, TagName_s, prev_mode, Value_s
```
**Assert:** non-empty ⇒ **critical**. Leaving RUN is what enables an online logic change; it should coincide only with an authorized, in-window maintenance activity.

### SIS-B5 — Logic compare vs golden baseline
Not a query — a **read-only** procedure: engineer uploads the running safety logic and offline-compares it to the golden baseline captured under change control. Any difference is proof of modification. (See the historian/IR libraries for the compare-to-baseline pattern; for SIS this is safety-authority-led.)

## Notes
- Prove a change from the **network capture** (B2) and **key-switch** (B4) evidence first — passively — before any controller-side action.
- SIS-B4 depends on the key-switch being wired to a monitored/historised digital input; if it isn't, that's a telemetry gap worth closing.
