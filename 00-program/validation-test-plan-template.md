# Validation Test Plan Template

A use case does not reach the Validated stage without a completed copy of this plan.
Validation in OT is evidence-based and safety-bounded: emulate the technique in a lab or
non-production zone, never against live process equipment.

---

- **UC ID:** OT-UC-00NN
- **Detection reference:**
- **Tester:**
- **Date:**
- **Environment:** (lab / test zone / digital twin / replayed PCAP)

## 1. Positive test (true positive)

| Field | Value |
|-------|-------|
| Technique emulated | T0NNN - <name> |
| Emulation method | (PCAP replay / protocol client / red-team tool / manual command) |
| Source / destination | |
| Expected alert | (Sigma rule ID or Nozomi Type ID) |
| Fired? | Yes / No |
| Time to alert | |
| Evidence | (screenshot, alert ID, log excerpt path) |

If the rule did not fire, the UC returns to In-Development. Do not promote on intent.

## 2. Negative test (false-positive assessment)

| Benign scenario | Traffic used | Alert fired? | Action if fired |
|-----------------|--------------|--------------|-----------------|
| Normal operation baseline | | | |
| Scheduled maintenance / commissioning | | | |
| Backup control center / secondary master | | | |
| Authorized scanner / monitoring poll | | | |

Document every benign trigger as either an allowlist entry or a tuning change. An
unexplained benign trigger blocks promotion.

## 3. Data source and field validation

- [ ] Required log source confirmed present in the target platform
- [ ] Field mapping verified (rule fields resolve against real events)
- [ ] Nozomi Type ID observed in syslog/CEF export (if applicable)
- [ ] ATT&CK for ICS technique tag present on the resulting alert

## 4. Peer review

- **Reviewer:**
- **Detection logic sound?** Yes / No
- **OT/process plausibility confirmed (PE)?** Yes / No / N/A
- **Runbook exists and is linked?** Yes / No

## 5. Outcome

- **Result:** Pass / Fail / Conditional
- **Promote to:** Validated / Production / (return to In-Development)
- **Notes:**
