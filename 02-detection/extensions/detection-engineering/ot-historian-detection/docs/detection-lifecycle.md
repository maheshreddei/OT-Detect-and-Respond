# Detection Lifecycle (MSS Delivery)

How a historian detection moves from idea to production and stays healthy, framed for managed-service delivery. Aligns to NIST CSF 2.0 (Identify/Protect/Detect/Respond/Govern) and IEC 62443.

## Lifecycle stages

```
  Propose ──▶ Design ──▶ Build ──▶ Validate ──▶ Deploy ──▶ Tune ──▶ Retire
     │           │          │          │           │         │         │
   use case   baseline    SPL/KQL   test cases   prod +    FP/MTTD   supersede
   + risk     spec +      + yml     (val.md)     shadow    review    or remove
   rationale  data model            pass                   cadence
```

Each detection folder is the artifact of this lifecycle: `README.md` (Propose/Design), `detection.yml` + `splunk.spl`/`sentinel.kql` (Build), `validation.md` (Validate). Nothing promotes to Deploy without a passing `validation.md`.

## RACI

Roles: **DE** Detection Engineer · **OTL** OT Security Lead · **SOC** SOC Analyst (L1/L2) · **PE** Process/Controls Engineer (customer) · **SO** Service Owner / Delivery Manager.

| Activity | DE | OTL | SOC | PE | SO |
|----------|----|-----|-----|----|----|
| Propose use case & risk rationale | R | A | C | C | I |
| Approve clean baseline window | C | A | I | **R** | I |
| Define data model / onboarding | R | A | I | C | I |
| Author detection (SPL/KQL + yml) | **R** | A | I | I | I |
| Author validation cases | R | A | C | C | I |
| Execute validation | R | A | C | **C** | I |
| Approve promotion to production | C | **A/R** | I | C | I |
| Triage alerts in production | I | C | **R** | C | I |
| Confirm true/false positive | C | A | R | **C** | I |
| Re-baseline (scheduled / post-MOC) | R | A | I | **C** | I |
| FP/MTTD KPI review | C | **A/R** | C | I | C |
| Retire / supersede detection | R | **A** | I | C | I |

`R` responsible · `A` accountable · `C` consulted · `I` informed.

The **Process Engineer is consulted at every physics-touching step** — baseline windows, validation, re-baselining. Historian detection without process-engineering input produces confident nonsense.

## KPI cadence

| KPI | Definition | Target | Cadence |
|-----|------------|--------|---------|
| **False-positive rate** | FP alerts ÷ total alerts, per detection | < 15% per detection; < 5% portfolio | Weekly |
| **MTTD** | Deviation onset → alert raised | < 5 min (near-real-time detections) | Weekly |
| **MTTT** | Alert raised → triage complete | < 30 min | Weekly |
| **Coverage** | Built detections ÷ prioritized catalog | Trend up | Monthly |
| **Baseline freshness** | % of tags baselined within cadence window | > 95% | Monthly |
| **Validation currency** | % of prod detections with passing validation in last quarter | 100% | Quarterly |
| **Detection efficacy** | True positives + purple-team catches ÷ known test injections | Trend up | Quarterly |

## Promotion gates

A detection may move to the next stage only when:

- **Build → Validate:** `detection.yml` complete (id, ATT&CK, baseline spec, level, response); query runs clean against sample data.
- **Validate → Deploy:** every case in `validation.md` passes; FP rate on the validation dataset within target; OTL sign-off recorded.
- **Deploy (shadow) → Deploy (active):** minimum 2-week shadow period; FP rate within target on live data; SOC runbook (the `Response` section of the README) reviewed with L1/L2.

## Shadow deployment

New detections run in **shadow mode** first — alerts routed to the DE/OTL, not to the live SOC queue — for a tuning window (default 2 weeks). This prevents an unvalidated FP rate from degrading the production queue while real-world baseline gaps surface. Promotion to the active queue is a gated, recorded decision.

## Change control

- The **baseline lookup is version-controlled**. Every re-baseline is a recorded change with approver and rollback point.
- Detection logic changes follow the same Build→Validate→Deploy path as new detections; a logic change re-opens validation.
- Retirement requires a superseding detection or a documented rationale, approved by the OTL.
