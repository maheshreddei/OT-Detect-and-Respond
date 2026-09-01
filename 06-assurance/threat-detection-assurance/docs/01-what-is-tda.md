# 01 — What is TDA

**Threat Detection Assurance (TDA)** is a validation process used to measure and verify the effectiveness of security threat-detection rules and use cases. It replaces the assumption that a deployed rule works with evidence that it does.

## The problem TDA solves
Detections degrade silently. A log source stops feeding, a field name changes after a platform upgrade, a rule was written but never fired, a threshold is so loose it never alerts or so tight it floods the SOC. None of this is visible until an incident is missed. TDA surfaces it deliberately, on a schedule, before an attacker does.

## The five goals (what TDA measures)
- **Log validation** — confirm the necessary log sources feed properly into the SIEM/NDR. If the data isn't arriving, no rule can fire.
- **Logic testing** — confirm the detection rule correctly triggers during a simulated attack.
- **Blind-spot discovery** — find missing coverage or absent data streams (techniques you can't see at all).
- **False-positive reduction** — tune thresholds so normal behavior is filtered out.
- **Speed tracking** — measure the real-life **Mean Time to Detect (MTTD)**.

## Where TDA sits
TDA is the **assurance layer** over detection engineering:

```
  detection engineering  →  deploy rule  →  [ TDA validates ]  →  trust the coverage
                                               ↑                        │
                                               └──── retest ────────────┘
```

It's a purple-team discipline — red-team technique meets blue-team measurement — run continuously and at gates (every new detection, after platform changes, periodically for regression).

## What "good" looks like
For any use case in scope, you can state, with evidence:
- the log source is feeding (log validation ✓),
- the rule fired on the simulated attack (logic ✓),
- it wasn't buried in false positives (FP rate ✓),
- it fired within an acceptable MTTD (speed ✓),
- and any gap has a tracked remediation.

## TDA vs. related activities
| Activity | Question it answers |
|----------|---------------------|
| **TDA** | Do our detections actually fire, with the right data, fast, without noise? |
| Penetration test | Can an attacker get in? |
| Red team | Can we detect & respond to a full campaign? |
| BAS (breach & attack simulation) | Automated, continuous version of the "simulate" step |
| Detection engineering | Building the rules TDA validates |

TDA is narrower and more measurable than a red team: it's the systematic, per-use-case proof that the detection layer works.
