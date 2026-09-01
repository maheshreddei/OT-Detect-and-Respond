# Onboarding Go-Live Checklist

A condensed gate for declaring a log source "onboarded". A source is not done when events
arrive — it is done when a detection consuming it is live and monitored. Use alongside the
full runbook template.

## Collection

- [ ] Raw events reaching the SIEM
- [ ] Correct sourcetype / parser assigned
- [ ] Timestamp and timezone correct
- [ ] Volume within estimate; source-health (stopped-feed) alert configured

## Parsing

- [ ] Key fields extract per `catalog/parser-mapping.csv`
- [ ] CIM / data-model normalization validated
- [ ] Passive sources: `type_id` and ATT&CK-for-ICS fields present

## Detection

- [ ] At least one use case from `catalog/detection-linkage.csv` consumes this feed
- [ ] Consuming detection tested against live data
- [ ] Alert triage guidance / runbook exists
- [ ] Safety Controller sources route to page-out on any event

## Governance

- [ ] Source marked live in `catalog/log-source-inventory.csv` (or a status field)
- [ ] Owner and SLA recorded
- [ ] Change approved (customer, in MSS context)

## Tier reminders

- **Tier 1** should be complete before Tier 2 begins — it delivers the IT-to-OT crossing
  and remote-access detections that cover the two most common compromise paths.
- **Tier 3 Network Traffic** is gated on SPAN/TAP architecture and DPI tuning; do not treat
  it as a quick win despite its detection value.
- **Tier 4 Field I/O** is intentionally never onboarded.
