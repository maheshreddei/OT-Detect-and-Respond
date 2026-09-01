# Validation — <ID>

| # | Type | Scenario | Injected input | Expected result |
|---|------|----------|----------------|-----------------|
| 1 | Positive | Clear deviation | ... | Alert fires |
| 2 | Negative | Normal operation | ... | No alert |
| 3 | Negative | Legitimate mode change | ... | No alert (mode-gated) |
| 4 | Edge | Persistence boundary | deviation just below dwell | No alert |
| 5 | Edge | Bad-quality samples | quality=Bad | Ignored |

## Test data
How to generate/replay the samples (historian replay, synthetic CSV, etc.).

## Result log
| Date | Version | Pass/Fail | Notes | Approver |
|------|---------|-----------|-------|----------|
