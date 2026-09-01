# C — Safety Function State & Trip

**Principle defended: the SIF trips correctly on deviation, and nothing suppresses it (primer §2).** These watch the safety-function chain in action — a PV approaching its trip while the BPCS looks normal, trip-setpoint tampering, missing/suppressed trips, and final-element command-vs-response mismatches. Historian-centric. Any hit is SEV-1.

## Detections

| ID | Detection | Logic | Data source | ATT&CK | Severity |
|----|-----------|-------|-------------|--------|----------|
| SIS-C1 | Safety PV trending toward trip (TRITON precursor) | Safety PV enters the trip margin and is still approaching, while BPCS view looks normal | historian (safety tags) | T0880 / T0837 | high |
| SIS-C2 | Trip setpoint / safety parameter modification | A SIF trip limit or safety parameter changes | historian / SIS event log | T0836 / T0838 | critical |
| SIS-C3 | Unexpected SIF trip / demand | A safety trip fires — record, correlate, investigate cause | historian / DCS alarm | T0880 | high |
| SIS-C4 | Expected trip absent / safety-alarm suppression | Conditions met a trip but none occurred, or the safety alarm was suppressed | historian / alarm journal | T0878 / T0837 | critical |
| SIS-C5 | Final-element command–response mismatch | SIS commanded the safe state but the final element didn't move (spoof/blocked) | historian (cmd + feedback) | T0835 / T0856 | critical |
| SIS-C6 | De-energize-to-trip circuit anomaly | Unexpected energize where de-energize is expected, or loss of line monitoring | SIS diagnostics / historian | T0837 | high |

## Worked queries

### SIS-C1 — Safety PV trending toward trip
Splunk SPL — safety PV inside its trip margin and still closing (cross-references the historian library's SIF-approach detection, scoped to safety tags):
```spl
index=ot_historian quality=Good
| lookup sif_trip_limits.csv tag OUTPUT sif_id trip_direction trip_value prealarm_value safe_margin
| where isnotnull(sif_id)
| eval margin = case(trip_direction=="high", trip_value-value, trip_direction=="low", value-trip_value)
| sort 0 tag _time
| streamstats window=10 first(margin) as m_first last(margin) as m_last range(_time) as span by tag sif_id
| eval margin_rate = (m_last-m_first)/(coalesce(span,1)/60)
| where margin < safe_margin AND margin_rate < -0.01
| eval severity=if(value>=prealarm_value OR (trip_direction=="low" AND value<=prealarm_value),"critical","high")
| table _time tag sif_id value trip_value margin margin_rate severity
| sort - _time
```
**Assert:** non-empty ⇒ high/critical. A safety PV being driven toward its trip while the BPCS shows normal is the deceptive-approach signature.

### SIS-C2 — Trip setpoint modification
Splunk SPL — change to a SIF trip limit (these should essentially never change outside a controlled MOC):
```spl
index=ot_historian (tag="*SIS*TRIP*SP*" OR tag="*SIF*SETPOINT*" OR tag="*SIS*LIMIT*")
| sort 0 tag _time
| streamstats current=f last(value) as prev_value by tag
| where value != prev_value
| table _time tag prev_value value
| sort - _time
```
**Assert:** non-empty ⇒ **critical**. A moved trip point silently reduces protection.

### SIS-C5 — Final-element command vs response mismatch
Splunk SPL — SIS commanded safe state but the valve/breaker feedback disagrees:
```spl
index=ot_historian (tag="*SIS*CMD*" OR tag="*SIS*FEEDBACK*" OR tag="*SIS*POS*")
| bin _time span=5s
| stats latest(eval(if(match(tag,"CMD"),value,null()))) as cmd
        latest(eval(if(match(tag,"FEEDBACK|POS"),value,null()))) as feedback by _time
| where isnotnull(cmd) AND isnotnull(feedback)
| eval mismatch = if(cmd=="TRIP" AND feedback!="SAFE", 1, 0)
| where mismatch==1
| table _time cmd feedback
```
**Assert:** non-empty (sustained) ⇒ **critical**. A commanded-but-not-actuated safe state means the final element was blocked, spoofed, or failed — a defeated SIF.

## Notes
- C1/C4 pair with the DCS alarm journal — a suppressed safety alarm alongside a trip-approach is the strongest TRITON-precursor signal.
- SIS-C5 depends on independent command and feedback tags being historised; without feedback you can't prove actuation.
