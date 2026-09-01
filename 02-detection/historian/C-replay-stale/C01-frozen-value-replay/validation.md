# Validation — C01 Frozen Value / Replay

Tag: `PLANT1.U200.FT201.PV`, mode run, max_stall_sec=20, min_variance=0.15.

| # | Type | Scenario | Injected input | Expected |
|---|------|----------|----------------|----------|
| 1 | Positive | Sensor stuck / replay hold | value=42.5 exactly, unchanged for 60s | Alert (frozen_value): stall_sec>20 |
| 2 | Positive | Variance collapse with jitter | value = 42.5 ± 0.01 over 5m window | Alert (variance_collapse): win_variance<0.15 |
| 3 | Negative | Normal noisy operation | value oscillating 41–44 | No alert (changes reset stall; variance normal) |
| 4 | Negative | Brief hold under threshold | value constant for 15s then changes | No alert (< max_stall_sec) |
| 5 | Negative | Idle mode long hold | value=0.3 in mode idle (max_stall_sec=600) | No alert (idle baseline tolerates long hold) |
| 6 | Edge | Stall boundary | constant for exactly 20s | No alert (strictly greater-than) |
| 7 | Edge | Bad quality flat | value flat but quality=Bad | Ignored |

## Test data generation
```
_time,tag,value,quality,mode,source
2026-01-14T08:00:00Z,PLANT1.U200.FT201.PV,42.5,Good,run,hmi_historian
2026-01-14T08:00:05Z,PLANT1.U200.FT201.PV,42.5,Good,run,hmi_historian
2026-01-14T08:00:10Z,PLANT1.U200.FT201.PV,42.5,Good,run,hmi_historian
2026-01-14T08:00:55Z,PLANT1.U200.FT201.PV,42.5,Good,run,hmi_historian
```

## Result log
| Date | Version | Pass/Fail | Notes | Approver |
|------|---------|-----------|-------|----------|
|      | 0.1.0   |           |       |          |
