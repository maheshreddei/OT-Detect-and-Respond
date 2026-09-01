# Validation — D02 Impossible State Combination

Rule: `PLANT1.U200.P101.RUN` == 0 (off) AND `PLANT1.U200.FT201.PV` > 5 m³/h ⇒ impossible.

| # | Type | Scenario | P101.RUN | FT201.PV | Expected |
|---|------|----------|----------|----------|----------|
| 1 | Positive | Spoofed pump status or spoofed flow | 0 | 42.5 (2+ bins) | Alert: violation, high |
| 2 | Negative | Normal running | 1 | 42.5 | No alert (pump on) |
| 3 | Negative | Normal stopped | 0 | 0.2 | No alert (no flow) |
| 4 | Negative | Stop transient (residual flow, 1 bin) | 0 | 20 for 1 bin then 0.2 | No alert (dwell not met) |
| 5 | Edge | Flow just above threshold | 0 | 5.1 (2+ bins) | Alert |
| 6 | Edge | Flow at threshold | 0 | 5.0 | No alert (strictly greater-than) |
| 7 | Edge | One tag missing in bin | 0 | (missing) | No evaluation (both required) |
| 8 | Edge | Bad quality | 0 | 42.5 quality=Bad | Ignored |

## Test data generation
```
_time,tag,value,quality,mode,source
2026-01-14T08:00:00Z,PLANT1.U200.P101.RUN,0,Good,run,hmi_historian
2026-01-14T08:00:00Z,PLANT1.U200.FT201.PV,42.5,Good,run,hmi_historian
2026-01-14T08:00:10Z,PLANT1.U200.P101.RUN,0,Good,run,hmi_historian
2026-01-14T08:00:10Z,PLANT1.U200.FT201.PV,42.4,Good,run,hmi_historian
```

## Result log
| Date | Version | Pass/Fail | Notes | Approver |
|------|---------|-----------|-------|----------|
|      | 0.1.0   |           |       |          |
