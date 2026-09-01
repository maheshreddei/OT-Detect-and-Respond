# Log Source Onboarding Runbook (Template)

Copy this per source (or per source class) when onboarding. Keep the structured facts in
`catalog/log-source-inventory.csv` and `catalog/parser-mapping.csv`; use this runbook for
the operational steps and sign-off.

---

- **Source ID:** LS-NN
- **Source:** 
- **Tier:** 
- **Collection pattern:** A (host agent) / B (syslog) / C (passive)
- **Owner:** 
- **Target go-live:** 

## 1. Pre-onboarding

- [ ] Source confirmed in scope and asset-inventoried
- [ ] Collection pattern selected (A/B/C) and feasibility confirmed
- [ ] Network path to collection tier validated (firewall rule / SPAN port / syslog dest)
- [ ] Data owner / change approver identified (customer, in MSS context)
- [ ] Expected daily volume estimated (licensing / index sizing)

## 2. Collection setup

- [ ] Forwarder / syslog / sensor configured per pattern
- [ ] Transport confirmed reaching the SIEM (raw events visible)
- [ ] Correct sourcetype assigned; vendor TA / parser installed
- [ ] Timezone and timestamp parsing verified
- [ ] For high-noise sources: filtering applied at source (ship security events only)

## 3. Parsing and normalization

- [ ] Key fields extract correctly (see `parser-mapping.csv` for this source)
- [ ] CIM / data-model normalization mapped and validated
- [ ] For passive sources: Nozomi `type_id` present; ATT&CK-for-ICS fields present
- [ ] Sample events reviewed against a known-good baseline

## 4. Detection enablement

- [ ] `detection-linkage.csv` reviewed — at least one consuming use case identified
- [ ] Consuming detection(s) tested against the live feed
- [ ] Runbook / triage guidance exists for resulting alerts
- [ ] For Safety Controller: page-out routing confirmed regardless of volume

## 5. Go-live and handoff

- [ ] Volume and health monitoring in place (source stops = alert)
- [ ] Source marked live in the inventory
- [ ] Handoff to SOC complete; owner and SLA recorded

## Sign-off

- **Onboarded by:** 
- **Reviewed by:** 
- **Date:** 
- **Notes:** 
