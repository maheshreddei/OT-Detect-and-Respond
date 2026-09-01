# Validation — E01 Historian vs Live PLC Divergence

Tag: `PLANT1.U200.FT201.PV`, std=1.8. Tolerance = sigma_diff>3 (≈ >5.4 absolute) OR pct_diff>2%.

| # | Type | Scenario | hmi_historian | direct_opcua | Expected |
|---|------|----------|---------------|--------------|----------|
| 1 | Positive | View spoofed to look normal while real value drifts | 42.5 (held) | 55.0 rising | Alert after 2 bins: sigma_diff high, severity high |
| 2 | Positive | Frozen HMI, live process moving | 42.5 (frozen) | 42.5→48→52 | Alert once divergence persists 2 bins |
| 3 | Negative | Both sources agree | 42.4 | 42.6 | No alert (within tolerance) |
| 4 | Negative | Momentary collection skew | 42.4 | 44.9 for 1 bin, then agree | No alert (persistence not met) |
| 5 | Negative | Noisy tag within tolerance | 42.1 | 43.0 | No alert (sigma_diff<3, pct<2) |
| 6 | Edge | direct source Bad quality | 42.5 (Good) | 55.0 (Bad) | Ignored (dual-Good gate) — collector fault, not spoof |
| 7 | Edge | Only one source present in a bin | 42.5 | (missing) | No comparison (both required) |
| 8 | Edge | Tolerance boundary | 42.5 | 48.0 (exactly ~3σ) | Boundary — confirm inclusive/exclusive behavior |

## Independence check (deployment validation, run once at onboarding)
Before trusting this detection, prove the two sources are independent:
1. Inject a value change at the controller only; confirm `direct_opcua` moves and, if the HMI path is healthy, `hmi_historian` also moves.
2. Temporarily stall the HMI collector; confirm `direct_opcua` continues updating (proves separate path).
If both sources move together *only* because they read the same OPC endpoint, the detection is worthless — re-provision the direct read closer to the controller.

## Test data generation
Emit paired-source samples to the test index/table:
```
_time,tag,value,quality,mode,source
2026-01-14T08:00:00Z,PLANT1.U200.FT201.PV,42.5,Good,run,hmi_historian
2026-01-14T08:00:00Z,PLANT1.U200.FT201.PV,55.0,Good,run,direct_opcua
2026-01-14T08:00:10Z,PLANT1.U200.FT201.PV,42.5,Good,run,hmi_historian
2026-01-14T08:00:10Z,PLANT1.U200.FT201.PV,55.4,Good,run,direct_opcua
```

## Result log
| Date | Version | Pass/Fail | Notes | Approver |
|------|---------|-----------|-------|----------|
|      | 0.1.0   |           |       |          |
