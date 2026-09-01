# F — Availability & Diagnostics

**Principle defended: fail-safe and SIS health stay visible (primer §3).** The SIS's self-diagnostics and de-energize-to-trip design are what let it hold its SIL. Loss of view of the SIS, diagnostic faults, restarts, and clock skew all degrade either the protection or your ability to trust the record. Any hit is SEV-1.

## Detections

| ID | Detection | Logic | Data source | ATT&CK | Severity |
|----|-----------|-------|-------------|--------|----------|
| SIS-F1 | SIS↔BPCS comm loss (loss of view of safety) | Status/heartbeat from the SIS to BPCS/historian stops | historian / gateway / NDR | T0804 / T0837 | high |
| SIS-F2 | SIS diagnostic fault / degraded module | Safety controller reports a diagnostic fault or module degradation | SIS event log | T0837 | high |
| SIS-F3 | Spurious trip-rate anomaly | Trip/demand rate rises above baseline (attack, fault, or manipulation) | historian / alarm | T0880 | medium |
| SIS-F4 | SIS controller restart / power event | Safety controller restarts or power-cycles (evidence loss / disruption) | SIS event / NDR | T0816 | high |
| SIS-F5 | SIS time / clock skew | Safety controller clock drifts from reference (SOE/sequence integrity) | SIS event / NDR | T0856 | medium |

## Worked queries

### SIS-F1 — Loss of view of the safety system
Splunk SPL — SIS heartbeat/status tag stops updating (staleness):
```spl
index=ot_historian (tag="*SIS*HEARTBEAT*" OR tag="*SIS*STATUS*" OR tag="*SIS*COMM*")
| stats latest(_time) as last_seen by tag
| eval stale_sec = now() - last_seen
| where stale_sec > <HEARTBEAT_TIMEOUT_SEC>
| eval stale_min=round(stale_sec/60,1)
| table tag last_seen stale_min
| sort - stale_min
```
Sentinel KQL:
```kql
OTHistorian_CL
| where TimeGenerated > ago(1d) and (TagName_s has "SIS" and (TagName_s has "HEARTBEAT" or TagName_s has "STATUS" or TagName_s has "COMM"))
| summarize LastSeen = max(TimeGenerated) by TagName_s
| extend StaleMin = datetime_diff('minute', now(), LastSeen)
| where StaleMin > <HEARTBEAT_TIMEOUT_MIN>
| sort by StaleMin desc
```
**Assert:** non-empty ⇒ alert. Losing view of the SIS is serious in itself and can mask activity on the safety network.

### SIS-F2 — SIS diagnostic fault
Nozomi N2QL / SIS event log — safety controller diagnostic/fault events:
```
alerts | where type_id include? "SIS" OR type_id include? "SAFETY" OR type_id include? "FAULT" OR type_id include? "DIAGNOSTIC"
| select type_id ip_src ip_dst created_time | sort created_time desc
```
**Assert:** non-empty ⇒ alert. Correlate diagnostic faults with any concurrent engineering activity (category B) — a fault plus an engineering session is more than a coincidence.

### SIS-F3 — Spurious trip-rate anomaly
Splunk SPL — trip events per day vs baseline:
```spl
index=ot_historian tag="*SIS*TRIP*" value="TRIP"
| bin _time span=1d
| stats count as trips by _time
| eventstats avg(trips) as avg_trips stdev(trips) as sd_trips
| where trips > (avg_trips + 3*sd_trips)
| table _time trips avg_trips
```
**Assert:** outlier ⇒ alert. A rise in trips can be a genuine process problem, a failing sensor, or manipulation — all worth investigating.

## Notes
- `<HEARTBEAT_TIMEOUT>` should be a small multiple of the normal status update interval.
- F4/F5 depend on SIS event/diagnostic logging being collected; a restart that clears volatile state is also an evidence-preservation trigger (see the IR library).
