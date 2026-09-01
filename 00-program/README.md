# 00 — Program Governance

How detection content moves from idea to production, and how log sources go live.

| File | Purpose |
|------|---------|
| `use-case-lifecycle.md` | Stages and gates: Proposed → In-Development → Validated → Production → Tuning → Retired |
| `raci-matrix.md` | Who is Responsible/Accountable/Consulted/Informed at each step |
| `use-case-template.md` | Authoring template for a new detection |
| `validation-test-plan-template.md` | Evidence required to promote a detection |
| `onboarding-runbook-template.md` | Per-source log onboarding runbook |
| `onboarding-checklist.md` | Go-live gate for a log source |
| `validation-template.md` | Log source validation evidence |

## Two rules that matter most

**A detection does not reach Production on paper.** Promotion requires a positive test (the
technique was emulated and the rule fired) and a false-positive assessment. For anything
touching a safety instrumented system, the OT/process engineer signs the review — detection
engineering does not self-certify operational impact.

**A log source is not onboarded when events arrive.** It is onboarded when a detection
consuming it is live and monitored. `05-crosswalk/detection-to-logsource.csv` names what
each source unlocks.
