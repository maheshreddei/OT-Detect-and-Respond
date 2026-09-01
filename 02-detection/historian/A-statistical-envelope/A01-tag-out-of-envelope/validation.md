# Validation — A01 Tag Out of Operating Envelope

Baseline used for these cases: `PLANT1.U200.FT201.PV`, mode `run`,
p01=38.1, p99=46.9, ll=35.0, hl=50.0 (so effective band = 35.0–50.0), mean=42.5, std=1.8.

| # | Type | Scenario | Injected input (mode=run) | Expected result |
|---|------|----------|---------------------------|-----------------|
| 1 | Positive | Sustained high excursion | value=52.0 for 3+ consecutive samples | Alert: breach=above, sigma_off≈+5.3, severity medium |
| 2 | Positive | Extreme excursion | value=62.0 for 3+ samples | Alert: severity high (>6σ) |
| 3 | Negative | Normal operation | value oscillating 41–44 | No alert |
| 4 | Negative | Single-sample spike | value=52.0 for exactly 1 sample, then back in band | No alert (dwell not met) |
| 5 | Negative | Legitimate mode change | value=0.3 with mode=idle | No alert (idle baseline band applies) |
| 6 | Negative | Legitimate mode change, wrong band | value=0.3 with mode=run | Alert fires — this is the mode-tag-accuracy failure mode; document as tuning dependency |
| 7 | Edge | Dwell boundary | value=52.0 for exactly 2 samples | No alert (needs 3) |
| 8 | Edge | Bad quality | value=99.0, quality=Bad | Ignored (filtered pre-stats) |
| 9 | Edge | At the limit | value=50.0 (== hl) | No alert (band is inclusive) |

## Test data generation
Replay from a historian test archive, or synthesize a CSV matching the data model and
ingest to a test index/table:

```
_time,tag,value,quality,mode,source
2026-01-14T08:00:00Z,PLANT1.U200.FT201.PV,42.4,Good,run,hmi_historian
2026-01-14T08:00:05Z,PLANT1.U200.FT201.PV,52.0,Good,run,hmi_historian
2026-01-14T08:00:10Z,PLANT1.U200.FT201.PV,52.3,Good,run,hmi_historian
2026-01-14T08:00:15Z,PLANT1.U200.FT201.PV,52.1,Good,run,hmi_historian
```

## Result log
| Date | Version | Pass/Fail | Notes | Approver |
|------|---------|-----------|-------|----------|
|      | 0.1.0   |           |       |          |
