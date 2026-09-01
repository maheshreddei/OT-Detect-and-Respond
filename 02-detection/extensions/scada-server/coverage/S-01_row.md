# S-01 Coverage Row — Update

## Before
| ID | Asset | Tier | Crit. | Difficulty | Techniques | Detections |
|----|-------|------|-------|-----------|-----------:|-----------:|
| S-01 | Control Server / SCADA Server | Tier 1 | Critical | Easy | 0 | 0 |

## After
| ID | Asset | Tier | Crit. | Difficulty | Techniques | Detections |
|----|-------|------|-------|-----------|-----------:|-----------:|
| S-01 | Control Server / SCADA Server | Tier 1 | Critical | Easy | 14 | 12 |

**Detections (12):** 9 host-side Sigma rules (one file carries 2 docs) + 3 correlation use cases.

**Techniques (14):**
Enterprise — T1021.001, T1136.001, T1098, T1543.003, T1053.005, T1059.001,
T1003.001, T1574, T1091, T1562.001, T1071 (11)
ICS — T0855, T0843, T0858 (3)  ·  enrichment references T0831.

**Data sources onboarded for this row:**
Windows Security (4624/4625/4672/4688/4697/4698/4702/4720/4728/4732/4756/1102/4719/6416),
Sysmon (1/3/7/10/11) or MDE Device* equivalents, SCADA operator-action/tag-write audit log,
Nozomi controller command/write stream (SIGN:/PROTOCOL:/VI: assertions).

**Residual gaps (document, don't hide):**
- ICS enrichment rows (UC-001/002/003) depend on the SCADA operator-action log and on the
  Nozomi controller stream being forwarded to the SIEM. Until both are onboarded, those three
  run in degraded-fidelity mode (host-only precursors still fire).
- EDR/allowlisting rows assume an agent is present; on OT supervisory hosts EDR is often
  absent or audit-only — where so, rely on Sysmon + Security channel.
