# Log Source Validation Template

Evidence that a source is not just arriving but usable for detection. Fill one per source
before moving it to live.

---

- **Source ID:** LS-NN
- **Source:** 
- **Validator:** 
- **Date:** 

## 1. Completeness

| Check | Expected | Result |
|-------|----------|--------|
| Events arriving continuously | No gaps > X min | |
| Volume vs estimate | Within +/- tolerance | |
| All in-scope instances reporting | Count matches inventory | |

## 2. Parsing fidelity

| Field | Extracts correctly? | Notes |
|-------|---------------------|-------|
| Timestamp / timezone | | |
| Source / destination identity | | |
| Action / event type | | |
| Protocol-specific fields (passive) | | |
| Nozomi type_id (passive) | | |
| ATT&CK-for-ICS technique (passive) | | |

## 3. Normalization

- [ ] Mapped to the correct data model(s)
- [ ] Field aliases resolve in a data-model search
- [ ] No parsing errors / line-breaking issues on sampled events

## 4. Detection readiness

- [ ] A use case from `detection-linkage.csv` returns results against this feed
- [ ] A deliberately generated test event produces the expected detection
- [ ] No unexplained high-volume benign trigger (tune before go-live)

## 5. Outcome

- **Result:** Pass / Conditional / Fail
- **Blocking issues:** 
- **Approved for go-live:** Yes / No
