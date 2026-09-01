# Program RACI (Template)

Roles: **OTL** OT Security Lead · **ARC** Architect · **DE** Detection Engineer · **DEP** Deployment Engineer · **SOC** SOC/MSS · **ENG** Plant Engineering · **OPS** Operations · **SAF** Safety Authority · **SPON** Sponsor.

| Activity | OTL | ARC | DE | DEP | SOC | ENG | OPS | SAF | SPON |
|----------|-----|-----|----|----|-----|-----|-----|-----|------|
| Scope & business case | A | C | I | I | C | C | C | I | R |
| Assessment & risk analysis | A | R | C | I | C | C | C | C | I |
| HLD / LLD | A | R | C | C | I | C | C | I | I |
| Sensor deployment (passive) | A | C | I | R | I | C | **C** | I | I |
| Log-source onboarding | A | C | C | R | C | C | I | I | I |
| Detection engineering & tuning | A | C | R | I | C | C | I | I | I |
| Baseline sign-off (physics) | A | I | C | I | I | **R** | C | I | I |
| IR playbooks & tabletop | A | C | C | I | R | C | C | C | I |
| Authority to act on OT assets | C | I | I | I | I | C | **A/R** | **veto** | I |
| SIS-related response | C | I | I | I | I | C | C | **A/R** | I |
| Run / monitoring / triage | A | I | C | I | R | C | C | I | I |
| KPI/SLA review | A | I | C | I | C | I | I | I | C |

R responsible · A accountable · C consulted · I informed. **Operations decides for the process; safety holds veto.**
