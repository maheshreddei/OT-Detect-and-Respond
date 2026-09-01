# Use Case Lifecycle RACI

Roles are defined for a managed OT SOC / MSS delivery model. In a single-owner internal
team, one person may hold several roles, but the accountabilities should still be
explicit so nothing falls between detection engineering and process engineering - the gap
where OT detection programs most often fail.

## Roles

- **OT Detection Engineer (DE)** - authors and tests detection content.
- **OT SOC Analyst (SA)** - triages resulting alerts; owns the runbook.
- **Threat Intel (TI)** - supplies actor/technique context and IOCs.
- **OT/Process Engineer (PE)** - validates operational safety and plausibility.
- **SOC / Detection Lead (LD)** - approves promotion to production; owns coverage.
- **Customer / Asset Owner (CO)** - approves change in their environment (MSS context).

## Matrix

| Activity | DE | SA | TI | PE | LD | CO |
|----------|----|----|----|----|----|----|
| Identify threat / propose UC | C | C | R | C | A | I |
| Populate catalog record (actor, ATT&CK, sector, data source) | R | I | C | I | A | I |
| Confirm data source availability | R | I | I | C | A | C |
| Author detection logic (Sigma / N2QL / native) | R | I | C | I | A | I |
| Write validation test plan | R | C | I | C | A | I |
| Execute validation (benign + malicious) | R | C | I | C | A | I |
| Safety/operational plausibility review | C | I | I | R | A | C |
| Approve promotion to production | I | I | I | C | R/A | C |
| Deploy to platform + author runbook | R | C | I | I | A | I |
| Triage live alerts | I | R | C | C | A | I |
| Tune thresholds / allowlists | R | C | I | C | A | I |
| Retire / supersede UC | C | I | C | I | R/A | I |

R = Responsible, A = Accountable, C = Consulted, I = Informed.

## Notes

- The **PE row on safety/operational plausibility review is non-optional** for any UC in
  the Safety category or touching an SIS (e.g. OT-UC-0017). Detection engineering does not
  self-certify operational impact.
- The **Lead is Accountable across the board** because coverage is a program property, not
  a per-rule property. One well-written rule with no production path is not coverage.
- In an MSS engagement the **Customer approves change** in their zone; the SOC owns the
  content. Keeping content in this repository (not only in the customer's console) is what
  makes the offering portable across tenants.
