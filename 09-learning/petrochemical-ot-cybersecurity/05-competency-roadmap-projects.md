# Competency Roadmap and Practical Projects

## Capability levels

### Level 1 — Plant-aware analyst

Can describe ammonia/urea flow, identify major equipment, read simple PFD/P&ID, distinguish DCS/PLC/SIS/SCADA, explain Purdue and basic protocols, navigate Nozomi assets/alerts and escalate safely.

Evidence: annotated process diagram, 50-term glossary, system inventory, ten alert triages and shift handover.

### Level 2 — OT SOC analyst

Can analyze PCAPs, map communications, reconcile assets, investigate engineering/remote-access behavior, validate SPAN/TAP health, write SIEM searches and produce process-aware cases.

Evidence: protocol workbook, baseline matrix, six playbooks, asset reconciliation, packet-loss test and end-to-end alert test.

### Level 3 — Detection engineer

Can translate process risks into use cases, validate telemetry, tune with approvals, measure efficacy and run hunts across Nozomi/SIEM/endpoint/network sources.

Evidence: 20 use cases, safe validation results, tuning register, hunt reports, MITRE ATT&CK for ICS mapping and metrics dashboard.

### Level 4 — OT security architect

Can conduct IEC 62443 risk assessment, design zones/conduits and target security levels, produce HLD/LLD/firewall/monitoring design, size NDR, design HA/DR and lead acceptance.

Evidence: complete site architecture pack, conduit register, risk assessment, BOM/sizing, MOC, FAT/SAT, recovery exercise and as-built handover.

## Twelve-week plan

| Weeks | Focus | Deliverable |
|---|---|---|
| 1–2 | Process, equipment, tags, PFD/P&ID | Process map and glossary |
| 3–4 | DCS/PLC/SIS/SCADA and operations | System-role and dependency matrix |
| 5–6 | Networking and industrial protocols | Traffic baseline and PCAP analysis |
| 7 | IEC 62443 zones/conduits | HLD and conduit register |
| 8 | Nozomi architecture/coverage | Monitoring-point and interface design |
| 9 | Detection engineering | Ten priority use cases |
| 10 | Investigation/hunting | Three case reports and two hunts |
| 11 | MOC, backup, HA/DR | Implementation and recovery runbook |
| 12 | Tabletop and interview | Portfolio review and presentation |

## Portfolio projects

### Project 1 — Process cyber-criticality map

Map each unit operation to controller, HMI/EWS, SIS function, utilities, protocols, owner, consequence and recovery dependency.

### Project 2 — Asset and communication baseline

Build an inventory and approved-flow matrix: source, destination, zone, protocol/function, direction, frequency, owner and monitoring point.

### Project 3 — IEC 62443 architecture

Produce HLD, LLD, zone/conduit register, data-flow diagram, firewall matrix, remote-access design and security-requirements specification.

### Project 4 — Nozomi deployment

Create capture-point survey, SPAN/TAP/broker choice, PPS/Mbps sizing, port/cable schedule, management flow matrix, HA/DR and SAT tests. Use the repository Nozomi package.

### Project 5 — Detection catalogue

Create use cases for engineering changes, SIS access, remote vendor activity, unknown assets, conduit bypass, scanning, malware indicators, external connections, time changes and monitoring failures.

### Project 6 — Incident tabletop

Scenario: vendor access is followed by an unauthorized controller change and compressor trip indication. Build timeline, roles, evidence, safe options, communications, recovery and lessons. Do not simulate on production.

## Knowledge checks

You are ready for plant support when you can answer:

- What does this unit make and which utilities can stop it?
- Which controller and safety layer protect it?
- What traffic should exist between the zones?
- Is the observed function a read, write, download or mode change?
- Was it approved and is the evidence trustworthy?
- What process consequence is plausible?
- Who can authorize containment?
- How will we know the process and monitoring recovered?

## Certifications and references

Useful structured learning includes ISA/IEC 62443 Fundamentals, Risk Assessment, Design and Maintenance; vendor Nozomi training; network/packet analysis; SIEM-specific training; and process-safety awareness provided by the employer. Certifications supplement—not replace—supervised plant experience.

## Experience log

For every exercise or real approved task record scope, role, tools, assumptions, evidence, result, safety/MOC involvement, lesson and what you would improve. In interviews, distinguish “performed,” “supported,” “observed” and “lab-practiced.”
