# TDA-<LAYER>-<NNN> — <title>

| Field | Value |
|-------|-------|
| Use case | <what threat/behavior> |
| Detection tested | <rule ID> |
| ATT&CK | <technique ID(s)> |
| TDA goals | <log validation / logic / blind-spot / FP / speed> |
| Layer / severity | <IT|OT> / <domain> · <severity> |
| Environment | <lab / authorized / injection-only> |

## Objective
<one sentence: what this test proves>

## Preconditions (log validation)
- <required log source(s) feeding the SIEM/NDR>
- <rule deployed/enabled; baseline built if needed>
- <OT: SPAN/tap alive>

## Attack simulation
<method: automated atomic / manual / pcap replay / injection>. **Record the action timestamp** (anchors MTTD).
```
<command / steps — lab-safe; OT never against live process>
```

## Expected detection
<rule logic summary> → <expected alert>. Expected fields: <entities/fields that make it actionable>.

## Validation criteria
- [ ] Data present — <required telemetry arrived>
- [ ] Rule fired — <correct detection triggered>
- [ ] Fidelity — <right fields/entities present; not buried in FPs>
- [ ] Speed — MTTD ≤ <target>
- [ ] FP — <normal activity does not trigger>

## Result (fill in)
State: ☐ Pass ☐ Partial ☐ Fail-no-rule ☐ Fail-no-data ☐ Blind-spot ☐ FP-prone
MTTD: ____ · Evidence: ____ · Tester / date: ____ · Notes:

## Remediation (if failed)
- No data → <onboard/repair source>
- Rule miss/wrong logic → <fix rule>
- Too slow → <pipeline/schedule>
- Too noisy → <tune threshold/allow-list>
- No coverage → <log blind spot → detection backlog>
Retest result: ☐ Pass · date: ____
