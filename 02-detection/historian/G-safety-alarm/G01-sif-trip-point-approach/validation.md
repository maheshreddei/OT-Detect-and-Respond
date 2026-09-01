# Validation — G01 SIF Trip-Point Approach

Tag: `PLANT1.U200.PIC220.PV`, SIF-201, trip_direction=high, trip_value=11.0,
prealarm_value=10.0, safe_margin=2.0 barg. (Normal run ≈ 7.9.)
"Inside safe margin" means value > 9.0 (i.e. margin < 2.0).

| # | Type | Scenario | Value trajectory | Expected |
|---|------|----------|------------------|----------|
| 1 | Positive | Steady approach to trip | 8.0 → 9.2 → 9.6 → 9.9 | Alert: margin<2, margin_rate<0, severity high |
| 2 | Positive | Approach past pre-alarm | 9.5 → 10.1 → 10.4 | Alert: severity critical (>= prealarm 10.0) |
| 3 | Negative | Normal operation | 7.8 → 7.9 → 8.0 | No alert (margin >= 2.0) |
| 4 | Negative | Stable close-but-constant offset | 9.3 → 9.3 → 9.3 | No alert (inside margin but not approaching) |
| 5 | Negative | Receding from trip | 9.4 → 9.0 → 8.6 | No alert (margin_rate > 0) |
| 6 | Edge | Noise around stable offset | 9.3 ± 0.05 | No alert (rate within deadband) |
| 7 | Edge | Low-direction SIF | tag AT301, pH 4.0 → 3.6 → 3.2 (trip low 3.0) | Alert (approaching low trip) |
| 8 | Edge | Bad quality during approach | approach samples quality=Bad | Ignored |

## Deceptive-approach enrichment (if companion tags wired)
Case 9 (Positive, high value): PV approaches trip AND no BPCS process alarm present
for the loop → severity escalated, tagged "control-normal" — the TRITON-style
deceptive signature. Requires companion alarm-state tag; document the mapping.

## Test data generation
```
_time,tag,value,quality,mode,source
2026-01-14T08:00:00Z,PLANT1.U200.PIC220.PV,8.0,Good,run,hmi_historian
2026-01-14T08:01:00Z,PLANT1.U200.PIC220.PV,9.2,Good,run,hmi_historian
2026-01-14T08:02:00Z,PLANT1.U200.PIC220.PV,9.6,Good,run,hmi_historian
2026-01-14T08:03:00Z,PLANT1.U200.PIC220.PV,9.9,Good,run,hmi_historian
```

## Result log
| Date | Version | Pass/Fail | Notes | Approver |
|------|---------|-----------|-------|----------|
|      | 0.1.0   |           |       |          |
