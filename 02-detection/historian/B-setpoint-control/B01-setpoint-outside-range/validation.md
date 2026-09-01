# Validation — B01 Setpoint Outside Approved Range

Tag: `PLANT1.U200.TIC205.SP`, approved band ll=150.0, hl=205.0. Normal SP ≈ 188.

| # | Type | Scenario | prev → new SP | Expected |
|---|------|----------|---------------|----------|
| 1 | Positive | Malicious over-range write (Oldsmar analog) | 188 → 260 | Alert: above_max, high |
| 2 | Positive | Under-range write | 188 → 90 | Alert: below_min, high |
| 3 | Negative | Legitimate in-band change | 188 → 192 | No alert |
| 4 | Negative | No change, sits in band | 188 → 188 | No alert |
| 5 | Edge | At the limit | 188 → 205 (== hl) | No alert (inclusive band) |
| 6 | Edge | Out-of-band but unchanged (already flagged) | 260 → 260 | No alert (change-gated; avoids re-fire) |
| 7 | Edge | Bad quality write | 188 → 260 quality=Bad | Ignored |

## Test data generation
```
_time,tag,value,quality,mode,source
2026-01-14T08:00:00Z,PLANT1.U200.TIC205.SP,188.0,Good,run,hmi_historian
2026-01-14T08:05:00Z,PLANT1.U200.TIC205.SP,260.0,Good,run,hmi_historian
```

## Result log
| Date | Version | Pass/Fail | Notes | Approver |
|------|---------|-----------|-------|----------|
|      | 0.1.0   |           |       |          |
