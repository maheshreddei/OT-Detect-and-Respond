# Pre-Deployment Document Package

Before deploying any cybersecurity solution — especially in OT/ICS — security architects, engineers, and SOC teams rely on a package of documents and diagrams. They ensure the deployment is **secure, meets operational requirements, and doesn't disrupt the industrial process.** This is the package to assemble before a Nozomi / Microsoft Sentinel / OT-SIEM rollout.

## Who relies on each document

Legend: ✅ primary user (relies on it directly) · ⚠️ secondary / situational.

| Document | Security Team | SOC | Engineers |
|----------|:---:|:---:|:---:|
| Network Architecture | ✅ | ✅ | ✅ |
| Purdue / Zone & Conduit Diagram | ✅ | ✅ | ✅ |
| Asset Inventory | ✅ | ✅ | ✅ |
| Communication Matrix | ✅ | ✅ | ✅ |
| Firewall Rules | ✅ | ✅ | ✅ |
| Data Flow Diagram | ✅ | ✅ | ✅ |
| P&ID | ⚠️ | ✅ | ✅ |
| Cause & Effect Matrix | ⚠️ | ✅ | ✅ |
| PLC I/O List | ⚠️ | ✅ | ✅ |
| HLD (High-Level Design) | ✅ | ⚠️ | ✅ |
| LLD (Low-Level Design) | ✅ | ⚠️ | ✅ |
| Risk Assessment | ✅ | ⚠️ | ✅ |
| Incident Response Playbooks | ✅ | ✅ | ⚠️ |
| Log Source Matrix | ✅ | ✅ | ⚠️ |
| Historian Tag List | ✅ | ✅ | ⚠️ |

## Why each document matters for monitoring deployment

**Network Architecture Diagram** — physical and logical topology. Determines **where sensors, SPAN/TAP, and collectors go**, what each vantage point can and can't see, and the chokepoints worth instrumenting. Without it, sensor placement is guesswork.

**Purdue / Zone & Conduit Diagram** — Purdue levels and IEC 62443 zones/conduits. Defines **where the boundaries are** (so you can build zone-crossing detections) and which conduits carry the traffic to watch. Drives Tier-1 firewall/switch onboarding.

**Asset Inventory** — devices with IP, role, vendor, criticality, and Purdue level. The **baseline for asset-based detections** (new/rogue asset), and what you need to scope collectors and size sensor licensing. An incomplete inventory is the most common cause of blind spots.

**Communication Matrix** — the authorized source↔destination↔protocol↔port flows. The **"allowed pair" baseline** that turns raw traffic into detections (anything off-matrix is a candidate alert), and the reference for validating firewall rules and scoping protocol monitoring.

**Firewall Rule Matrix** — the actual ruleset at the IT/OT and inter-zone boundaries. Validates segmentation, provides the **allow/deny baseline**, and is itself a Tier-1 log source. Reveals where the real cross-zone paths are.

**Data Flow Diagram** — how data moves across zones, including to the historian, DMZ, and any cloud/analytics egress. Identifies **the ingress/egress to watch** and informs data-gateway and historian onboarding.

**P&ID (Piping & Instrumentation Diagram)** — the process design: equipment, instruments, and their tags. Ties telemetry to the **physical process** so analysts understand consequence and context. Essential for engineers; security-relevant for impact analysis and historian tag interpretation.

**Cause & Effect Matrix** — which process conditions trigger which trips/interlocks/shutdown actions. Effectively the **safety/SIS logic map** — critical for understanding impact, prioritizing safety-related detections, and interpreting what a manipulated value could cause.

**PLC I/O List** — the I/O points per controller. Maps signals to the process and supports **detection tuning and historian tag mapping** (which register/point means what).

**HLD (High-Level Design)** — the monitoring solution's architecture: sensor/collector placement, data flows, integrations, high-level sizing. The **primary deployment blueprint**.

**LLD (Low-Level Design)** — the build detail: IPs, ports, SPAN sessions, sensor specs, rulesets, integration configs. The **document the deployment is actually built from**.

**Risk Assessment** — threats, crown-jewel assets, consequences, and (in OT) SIL/LOPA context. **Prioritizes what to detect and protect** — detection engineering should follow the risk, not the tooling defaults.

**Incident Response Playbooks / Procedures** — how the SOC responds when a detection fires, including OT-safe containment and escalation. Ensures **every detection has an actionable, safe response** rather than an alert nobody can act on.

**Log Source Matrix** — the prioritized list of which sources to onboard, in what order, at what effort (see [`../log-onboarding/onboarding-guide.md`](../log-onboarding/onboarding-guide.md)). The bridge from context to telemetry.

**Historian Tag List** — the process tags available for **baseline-and-deviation (physics) detections**. Essential for historian-based detection — you can't detect a setpoint manipulation or a trip-point approach without knowing the tags.

## Using this package
- **Security & SOC** lean on architecture, Purdue, assets, comms, firewall, data flow, IR, and log/tag sources — the context for placement and detection.
- **Engineers** additionally own P&ID, Cause & Effect, PLC I/O, HLD/LLD — the process and build detail that keeps the deployment safe.
- The ✅/⚠️ split shows where a document is a primary working reference vs. a situational consult. Gather the ✅-heavy rows first (see [`priority-request-list.md`](priority-request-list.md)).
