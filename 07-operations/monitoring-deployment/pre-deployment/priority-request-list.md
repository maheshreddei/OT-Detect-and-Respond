# Priority Request List

If you're asked to review a plant before deploying Nozomi, Microsoft Sentinel, or another OT monitoring solution, these are the **highest-priority documents to request first** — the ones that unblock safe sensor placement and effective detection. Ordered by how early you need them.

Together they provide the **technical, operational, and security context** needed to deploy monitoring safely and build effective detections.

| # | Document | What it tells you / how it informs the deployment |
|---|----------|---------------------------------------------------|
| 1 | **High-Level Design (HLD)** | The intended monitoring architecture — sensor/collector placement, data flows, integrations. Your deployment blueprint; everything else validates or refines it. |
| 2 | **Low-Level Design (LLD)** | The build detail — IPs, ports, SPAN sessions, sensor specs, rulesets. What the deployment is actually configured from. |
| 3 | **Network Architecture Diagram** | Physical/logical topology — where to place SPAN/TAP and collectors, and what each vantage point can see. |
| 4 | **Purdue / Zone & Conduit Diagram** | The zone boundaries and conduits — defines zone-crossing detections and where the IT/OT line sits. |
| 5 | **Asset Inventory** | Devices, IPs, roles, criticality, Purdue level — scopes sensors/licensing and seeds new-asset detection. |
| 6 | **Communication Matrix** | Authorized flows (src↔dst↔proto↔port) — the "allowed pair" baseline for protocol detections and firewall validation. |
| 7 | **Firewall Rule Matrix** | The real boundary ruleset — validates segmentation and provides the allow/deny baseline. |
| 8 | **P&ID** | The process design — ties tags to the physical process for consequence and context. |
| 9 | **PLC I/O List** | I/O points per controller — maps signals to process; supports detection tuning and tag mapping. |
| 10 | **Historian Tag List** | The tags available for baseline-and-deviation (physics) detections — essential for historian-based detection. |
| 11 | **Risk Assessment** | Threats, crown jewels, consequences, SIL/LOPA — prioritizes what to detect and protect. |
| 12 | **Incident Response Procedures** | How the SOC responds, safely — ensures detections have an actionable, OT-safe response. |

## Why this order
- **HLD/LLD first** — you're validating and executing a design; get the design before critiquing the details.
- **Architecture → Purdue → Assets → Comms → Firewall** — this is the placement-and-baseline chain: where to watch, what the zones are, what's there, what should talk, and what the boundary allows.
- **P&ID → PLC I/O → Historian tags** — the process/detection-context chain: what the signals mean and which tags power physics detections.
- **Risk Assessment & IR last of the priority set** — not least important, but they shape *priority and response* once you know the environment; detection engineering should follow the risk.

## Practical note
Missing or stale documents are themselves a finding — an out-of-date asset inventory or communication matrix is one of the most common reasons an OT deployment produces noise instead of detections. Track requests with [`document-request-checklist.md`](document-request-checklist.md), and where a document doesn't exist, an early phase of the deployment (passive discovery, asset inventory build) often has to produce it.
