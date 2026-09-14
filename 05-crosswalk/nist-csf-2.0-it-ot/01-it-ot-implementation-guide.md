# NIST CSF 2.0 IT and OT Implementation Guide

## Govern

### IT focus

Enterprise risk appetite, legal/privacy obligations, policies, business ownership, cloud/vendor governance, budgets and board reporting.

### OT focus

Process safety and production context, site accountability, engineering authority, MOC, OEM/integrator responsibilities, long equipment lifecycles, remote vendors, spare parts and compensating controls.

### Evidence

Approved cybersecurity strategy; IT/OT RACI; risk criteria; policies; exception register; governance minutes; supplier requirements; site KPIs; MOC integration.

## Identify

### IT focus

Servers, endpoints, applications, identities, cloud resources, business data, vulnerabilities and third parties.

### OT focus

DCS/PLC/SIS/SCADA assets; firmware and logic versions; industrial protocols; process criticality; safety dependencies; zones/conduits; serial and silent assets; engineering workstations; gateways; network paths and recovery dependencies.

### Evidence

Authoritative inventory reconciled with passive discovery; network/Purdue and zone diagrams; data-flow/conduit register; risk assessments; vulnerability decisions; lessons/actions register.

## Protect

### IT focus

IAM/MFA, endpoint protection, secure configuration, encryption, awareness, patching, backups and network security.

### OT focus

Controlled engineering access; jump hosts; vendor-session approval; DCS/SIS role separation; application allowlisting; removable media; tested patch windows; backups of logic/configuration; allowlisted conduits; physical access; safe failover.

### Evidence

RBAC matrix; firewall rules; remote-access logs; configuration baselines; backup/restore tests; training; exception approvals; patch validation; asset-owner acceptance.

## Detect

### IT focus

EDR, SIEM, cloud monitoring, identity analytics, email/network detections and threat intelligence.

### OT focus

Passive network monitoring; new assets/links; logic downloads; controller mode changes; unexpected writes; SIS access; vendor activity; protocol anomalies; process/reliability deviations; monitoring-health alarms.

### Evidence

Nozomi coverage and health; detection catalog; SIEM mappings; validation records; tuning register; alert-to-case tests; capture-point assurance; coverage metrics.

## Respond

### IT focus

Incident triage, containment, eradication, notification, legal/privacy communications and coordination.

### OT focus

Joint SOC–operations validation, process consequence assessment, safety authority, control-room communications, MOC/emergency change, evidence preservation and safe containment. Cybersecurity does not independently trip or isolate process assets.

### Evidence

OT incident plan; playbooks; decision authority; contact trees; exercises; case timelines; communication templates; evidence chain; regulatory criteria.

## Recover

### IT focus

Restore services and data, validate integrity, communicate status and improve resilience.

### OT focus

Restore process in a safe sequence; validate controller logic/configuration, interlocks, SIS independence, historian/time, network visibility and production quality. Coordinate with operations, process safety and vendors.

### Evidence

RTO/RPO by service; offline backups; golden builds; spare strategy; restore tests; startup approval; post-incident review; improvement tracking.

## IT versus OT decision rules

| Question | IT tendency | OT requirement |
|---|---|---|
| Patch immediately? | Often desirable | Test compatibility and schedule with operations/OEM |
| Isolate endpoint? | Common containment | Assess process/safety consequence first |
| Active scan? | Routine when authorized | Validate device tolerance and obtain MOC |
| Reboot? | Standard recovery step | May stop control or lose process state |
| Confidentiality priority? | Often high | Availability, integrity and safety may dominate |
| Asset discovery | Agent/scanner/API | Passive first; supplement carefully |
| Backup success | Job completed | Restore must prove controller/config/process usability |
| Network monitoring | North-south/east-west | Include industrial operations and capture health |

## Program metrics

- Critical assets with owner, process, zone and recovery plan.
- Critical conduits with bidirectional monitoring.
- Priority detections safely validated.
- Remote/vendor sessions approved and reviewed.
- Time to detect, validate with operations and escalate.
- Backups with successful restore evidence.
- High-risk exceptions and compensating controls.
- Monitoring blind spots and aged remediation.
- Exercises completed and lessons closed.
