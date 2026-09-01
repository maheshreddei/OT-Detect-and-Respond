# E — Bypass / Override / Inhibit

**Principle defended: protection is not silently disabled (primer §6).** Bypasses, overrides, MOS, and forces legitimately take a SIF or channel out of service for maintenance — under authorization, a time limit, and compensating measures. Each active bypass is a hole in the protection; unauthorized, overdue, or clustered bypasses are both safety and security findings. Any hit is SEV-1.

## Detections

| ID | Detection | Logic | Data source | ATT&CK | Severity |
|----|-----------|-------|-------------|--------|----------|
| SIS-E1 | SIF bypass / inhibit activated | A SIF bypass/inhibit/MOS status goes active | historian / SIS event / alarm | T0837 | high |
| SIS-E2 | Long-duration / overdue bypass | A bypass stays active beyond the approved window | historian (bypass + duration) | T0837 | high |
| SIS-E3 | Bypass from unexpected source / off-window | Bypass activated outside maintenance or from an unexpected station | SIS event / NDR + calendar | T0837 | high |
| SIS-E4 | Forced I/O on the safety controller | Safety input/output forced/overridden | SIS diagnostics / event | T0835 | critical |
| SIS-E5 | Multiple simultaneous bypasses | Several SIF bypasses active at once (defense-in-depth erosion) | historian (bypass tags) | T0837 | critical |

## Worked queries

### SIS-E1 — SIF bypass / inhibit activated
Splunk SPL:
```spl
index=ot_historian (tag="*SIS*BYPASS*" OR tag="*SIF*INHIBIT*" OR tag="*SIS*MOS*")
| sort 0 tag _time
| streamstats current=f last(value) as prev by tag
| where value != prev AND (value=="ACTIVE" OR value=="ON" OR value==1)
| table _time tag prev value
| sort - _time
```
Sentinel KQL:
```kql
OTHistorian_CL
| where TimeGenerated > ago(1h) and (TagName_s has "BYPASS" or TagName_s has "INHIBIT" or TagName_s has "MOS")
| order by TagName_s asc, TimeGenerated asc
| serialize
| extend prev = iff(TagName_s == prev(TagName_s), prev(Value_s), "")
| where Value_s != prev and Value_s in ("ACTIVE","ON","1")
| project TimeGenerated, TagName_s, prev, Value_s
```
**Assert:** non-empty ⇒ alert (route to safety authority to confirm against the authorized-work list).

### SIS-E2 — Long-duration / overdue bypass
Splunk SPL — bypass active longer than the allowed window:
```spl
index=ot_historian (tag="*SIS*BYPASS*" OR tag="*SIF*INHIBIT*")
| sort 0 tag _time
| streamstats reset_before="(value!=\"ACTIVE\" AND value!=\"ON\" AND value!=1)" earliest(_time) as start by tag
| eval active_sec = _time - start
| where (value=="ACTIVE" OR value=="ON" OR value==1) AND active_sec > <MAX_BYPASS_SEC>
| eval active_hours=round(active_sec/3600,1)
| table _time tag active_hours
| sort - active_hours
```
**Assert:** non-empty ⇒ alert. Overdue bypasses are a leading indicator of both procedural drift and deliberate protection defeat.

### SIS-E5 — Multiple simultaneous bypasses
Splunk SPL:
```spl
index=ot_historian (tag="*SIS*BYPASS*" OR tag="*SIF*INHIBIT*")
| stats latest(value) as state by tag
| where state=="ACTIVE" OR state=="ON" OR state==1
| stats count as active_bypasses values(tag) as bypassed_sifs
| where active_bypasses >= 2
```
**Assert:** count ≥ 2 ⇒ **critical**. Simultaneous bypasses erode layered protection fast.

## Notes
- Cross-check every bypass against the authorized-work / permit-to-work list; an unlisted bypass is the finding.
- `<MAX_BYPASS_SEC>` comes from your bypass procedure (e.g. one shift). Forced I/O (E4) is often the more surgical attacker technique — treat it as critical.
