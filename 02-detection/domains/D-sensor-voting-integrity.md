# D — Sensor & Voting Integrity

**Principle defended: valid inputs, voting, and independence (primer §4–5).** The SIF is only as trustworthy as its inputs. These detect voting degradation, redundant-transmitter disagreement, frozen/replayed inputs, and the loss-of-independence that the shared-sensor rule exists to prevent. Any hit is SEV-1.

## Detections

| ID | Detection | Logic | Data source | ATT&CK | Severity |
|----|-----------|-------|-------------|--------|----------|
| SIS-D1 | Voting degradation | A voted group (e.g. 2oo3) drops a channel / runs degraded | historian (voting status) | T0837 | high |
| SIS-D2 | Redundant safety-sensor disagreement | Redundant transmitters diverge beyond tolerance | historian (redundant PVs) | T0856 | high |
| SIS-D3 | Frozen / replayed safety input | A safety PV holds perfectly constant beyond its stall limit | historian (safety PV) | T0856 | high |
| SIS-D4 | Loss of independence (shared/BPCS-sourced input) | A safety PV tracks a BPCS-path value suspiciously, or is sourced from the BPCS | historian (two sources) | T0856 / T0835 | high |
| SIS-D5 | Safety input bad-quality spike | Surge of Bad/Uncertain quality on safety inputs | historian (quality) | T0815 | medium |

## Worked queries

### SIS-D2 — Redundant safety-sensor disagreement
Splunk SPL — two redundant transmitters for the same safety measurement diverge:
```spl
index=ot_historian quality=Good (tag="*SIS*XMTR_A*" OR tag="*SIS*XMTR_B*")
| bin _time span=5s
| stats latest(eval(if(match(tag,"XMTR_A"),value,null()))) as a
        latest(eval(if(match(tag,"XMTR_B"),value,null()))) as b by _time
| where isnotnull(a) AND isnotnull(b)
| eval diff=abs(a-b)
| where diff > <TOLERANCE>
| table _time a b diff
| sort - _time
```
**Assert:** sustained divergence ⇒ alert. Disagreeing redundant safety transmitters mean one is faulty or spoofed — and voting can mask it until it's too late.

### SIS-D1 — Voting degradation
Splunk SPL — voted-group status leaves its healthy state (e.g. 2oo3 → 1oo2):
```spl
index=ot_historian (tag="*SIS*VOTE*" OR tag="*SIS*CHANNEL*STATUS*")
| sort 0 tag _time
| streamstats current=f last(value) as prev by tag
| where value != prev AND value != "HEALTHY" AND value != "2oo3"
| table _time tag prev value
| sort - _time
```
**Assert:** non-empty ⇒ alert. Degraded voting lowers the effective SIL even while the process still runs.

### SIS-D4 — Loss of independence (safety input tracking a BPCS source)
Concept + SPL — compare the safety PV against the BPCS measurement of the same variable; suspicious near-identical tracking (or a safety tag literally sourced from the BPCS path) indicates lost independence:
```spl
index=ot_historian quality=Good (tag="<SIS_SAFETY_PV>" OR tag="<BPCS_SAME_VAR_PV>")
| bin _time span=5s
| stats latest(eval(if(tag=="<SIS_SAFETY_PV>",value,null()))) as sis
        latest(eval(if(tag=="<BPCS_SAME_VAR_PV>",value,null()))) as bpcs by _time
| where isnotnull(sis) AND isnotnull(bpcs)
| eval delta=abs(sis-bpcs)
| stats avg(delta) as avg_delta stdev(sis-bpcs) as jitter
| eval independence_suspect=if(avg_delta<0.01 AND jitter<0.01, 1, 0)
```
**Assert / review:** near-zero delta and jitter across time suggests the "independent" safety input is not independent — a design/common-cause finding (primer §5) as much as a security one.

## Notes
- `<TOLERANCE>` comes from the transmitter accuracy and the SIF design, not statistics.
- D3 reuses the historian library's frozen-value logic, scoped to safety tags; D4 reuses its divergence logic to test *independence* rather than spoofing.
