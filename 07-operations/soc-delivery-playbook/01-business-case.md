# 01 — Business Case

OT security is funded when it's framed as **operational resilience and safety**, not "cyber." Boards fund uptime, safety, and compliance — lead with those.

## Why now (the drivers)
- **Threat landscape has proven physical impact.** Stuxnet, the Ukraine grid attacks, TRITON/TRISIS (safety system), Colonial Pipeline (operational shutdown from IT ransomware), Oldsmar (setpoint manipulation). OT is targeted, and consequences are physical.
- **IT/OT convergence & digitalization.** Remote access, cloud analytics, IIoT, and flat legacy networks have erased the air gap that used to be the control.
- **Regulation & standards.** NIS2 (EU), NERC CIP (electric), TSA directives (pipeline), IEC 62443, NIST 800-82; in the GCC, UAE Information Assurance / NESA and KSA NCA (ECC/OTCC) increasingly mandate OT security and incident reporting.
- **Insurance & liability.** Cyber insurers now require OT controls; boards face personal accountability for safety.

## Business drivers to anchor on
| Driver | Board language |
|--------|----------------|
| **Safety** | Preventing a cyber-induced safety event (harm to people/environment) |
| **Availability / production** | Avoiding unplanned downtime and lost production |
| **Compliance** | Meeting regulatory and contractual obligations, avoiding penalties |
| **Reputation** | Avoiding the headline and the customer/market fallout |
| **Insurability** | Meeting insurer requirements; managing premiums |

## Quantifying the risk (consequence-based)
OT risk is **consequence-driven**, not data-driven. Frame it as:
`Risk = likelihood × consequence`, where consequence is measured in **safety, environmental, production, and equipment** terms — not records breached.
- Estimate **cost of downtime** (per hour of the affected process) and a credible worst-case incident (safety event, extended outage, equipment damage).
- Compare against the **cost of the program** (below). The ratio is usually stark — a single day of unplanned downtime often exceeds the annual monitoring cost.

## Cost model
- **Capex / one-time:** NDR sensors (per site/segment), SIEM integration, design & deployment services, initial detection engineering.
- **Opex / recurring:** MSS monitoring (or internal analyst staffing for 24/7), sensor licences, tuning & detection lifecycle, threat intel.
- **Phased funding:** fund Crawl (visibility + quick wins) first — it's the cheapest, highest-value tranche and de-risks the larger spend.

## The board narrative (one paragraph)
> Our industrial processes are increasingly connected and increasingly targeted, and a cyber event here isn't a data breach — it's a safety and production event we can't undo. For a fraction of the cost of a single day of unplanned downtime, an OT SOC gives us continuous visibility of our control networks, early detection of manipulation before it reaches the process, and a rehearsed response that keeps operations and safety in control. It also puts us ahead of tightening regulation and insurer requirements.

## Cost of inaction
Make it concrete: the affected process's downtime cost per hour, the regulatory penalty exposure, the insurer's stance without OT controls, and the fact that a safety-targeting attack (TRITON class) is designed to defeat the last line of protection. Inaction is a decision with a price.
