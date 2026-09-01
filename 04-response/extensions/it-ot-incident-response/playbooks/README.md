# Incident Response Playbooks

Per-scenario response guides. Each follows the same shape: **indicators → severity → immediate triage → evidence to collect (with what it proves) → analysis → OT-safe containment → eradication & recovery → proof-artifact checklist.**

Playbooks reference the [evidence guides](../evidence/) for collection detail and the [SOPs](../sop/) for procedure. They do not replace the [authority-to-act matrix](../docs/02-roles-and-raci.md) — any OT action still routes through operations.

| Playbook | Scenario | Min severity |
|----------|----------|--------------|
| [pb-01](pb-01-unauthorized-plc-logic-change.md) | Unauthorized PLC / controller logic change | SEV-1 |
| [pb-02](pb-02-unauthorized-setpoint-change.md) | Unauthorized setpoint change | SEV-2 |
| [pb-03](pb-03-safety-system-manipulation.md) | Safety instrumented system (SIS) manipulation | SEV-1 |
| [pb-04](pb-04-malware-ransomware-on-ot-host.md) | Malware / ransomware on an OT host | SEV-2 |
| [pb-05](pb-05-suspicious-remote-access.md) | Suspicious remote / vendor access into OT | SEV-2 |
