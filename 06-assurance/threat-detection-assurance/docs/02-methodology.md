# 02 — TDA Methodology

The five goals and four process steps, turned into a repeatable method with roles, cadence, and clear pass/fail criteria.

## The process, step by step

### Step 1 — Scope definition
Choose the specific threat scenarios and use cases to test. Drive scope from:
- **Risk / threat model** — the techniques most relevant to your environment and sector.
- **ATT&CK coverage** — prioritize techniques you claim to cover; test the crown-jewel detections first.
- **Change triggers** — every new detection, every platform/parser change, every log-source onboarding.
Output: a prioritized list of test cases (each maps to a use case, a detection rule, and an ATT&CK technique).

### Step 2 — Attack simulation
Emulate the chosen threat vector — manually or with automation (Atomic Red Team, Caldera; for OT, lab replication or pcap replay). Record the **exact time** the simulated action ran (this anchors MTTD). Keep it safe and authorized (see `03`; for OT see `05`). Output: executed simulation with a timestamped action log.

### Step 3 — Alert validation
Verify the SOC receives the expected alert. Check four things, not just "did something fire":
1. **Data present** — the required log/telemetry arrived (log validation).
2. **Rule fired** — the correct detection triggered (logic).
3. **Fidelity** — the alert has the right entities/fields to be actionable, and isn't lost in false positives.
4. **Speed** — measure MTTD = alert time − simulation time.
Output: a pass/partial/fail result with MTTD and evidence.

### Step 4 — Remediation & retesting
For any failed or partial detection, fix the **root cause** — then retest to prove the fix:
- No data → onboard/repair the log source (log-validation failure).
- No rule / wrong logic → write or fix the detection.
- Too noisy → tune thresholds/allow-lists (FP reduction).
- Too slow → address pipeline latency or scheduling.
- No coverage at all → record a **blind spot** and add to the detection backlog.
Output: remediation logged, retest passed, coverage updated.

### Step 5 — Report (close the loop)
Score the cycle, update the coverage map, trend MTTD and pass-rate over time (see `04`).

## Detection health states (the result of Step 3)
| State | Meaning |
|-------|---------|
| **Pass** | Data present, rule fired, actionable, within MTTD target |
| **Partial** | Fired but late, low-fidelity, or noisy — needs tuning |
| **Fail — no rule** | Technique executed, nothing fired → detection to build |
| **Fail — no data** | Rule exists but the log source isn't feeding → log-validation gap |
| **Blind spot** | No data *and* no rule — completely unseen |
| **FP-prone** | Fires on normal activity → threshold/allow-list work |

## Roles (RACI)
| Activity | Detection Eng | Red/Purple | SOC | Platform |
|----------|:-------------:|:----------:|:---:|:--------:|
| Scope | A/R | C | C | I |
| Simulate | C | R | I | I |
| Validate | R | C | A | C |
| Remediate | R | C | C | C |
| Report | R/A | C | C | I |

## Cadence
- **Per new detection** — no rule goes to production un-validated (a release gate).
- **On change** — after platform upgrades, parser changes, or log-source onboarding (regression).
- **Periodic** — a rolling schedule so every priority use case is re-validated (e.g. quarterly), because detections decay.
- **Continuous (BAS)** — where automation allows, run the simulation step continuously.

## Pass/fail definition (agree up front)
A test **passes** when: required data present **AND** correct rule fired **AND** alert is actionable **AND** MTTD ≤ target **AND** FP rate acceptable. Anything else is partial/fail with a tracked remediation. Define MTTD targets and acceptable FP rate per severity before testing.
