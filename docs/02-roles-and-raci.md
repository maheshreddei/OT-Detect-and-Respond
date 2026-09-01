# Roles & RACI

OT incident response is a joint cyber + engineering + operations effort. The single most common failure mode is a SOC analyst taking an action on an OT asset without operations in the loop. This RACI prevents that.

## Roles

| Role | Who | Core responsibility |
|------|-----|---------------------|
| **Incident Commander (IC)** | Senior SOC / OT Security Lead | Owns the incident end to end; final call on non-safety decisions; coordinates all parties |
| **OT Security Analyst / Investigator** | SOC (OT-capable) | Evidence collection, analysis, timeline, technical containment recommendations |
| **Controls / Automation Engineer** | Plant/site engineering | Owns controller & process knowledge; performs or supervises any action on L0-L2; golden-baseline compare |
| **Operations / Shift Supervisor** | Control room | Owns the running process; authority over process-affecting actions; can order controlled shutdown |
| **Plant Safety Authority** | Process safety / HSE | Final veto on any action affecting safety; owns the safety case |
| **IT Security / SOC** | Enterprise SOC | IT-side containment, identity, boundary firewall, enterprise forensics |
| **Comms / Legal / Compliance** | Legal, PR, compliance | Regulatory reporting, external comms, legal hold, law-enforcement liaison |
| **Executive Sponsor** | CISO / Plant Manager | Business decisions, major shutdown authorization, resourcing |

## RACI — key activities

R responsible · A accountable · C consulted · I informed

| Activity | IC | OT Analyst | Controls Eng | Operations | Safety | IT Sec | Legal |
|----------|----|-----------|--------------|------------|--------|--------|-------|
| Declare incident & severity | A/R | C | C | C | I | C | I |
| Preserve volatile evidence (network/historian/logs) | A | **R** | C | I | I | C | I |
| Acquire evidence from L0-L2 (controller/HMI) | A | C | **R** | C | C | I | I |
| IT-side / boundary containment | A | C | I | I | I | **R** | I |
| Process-affecting containment (isolate HMI, go manual) | A | C | C | **R** | **C/veto** | I | I |
| Controlled process shutdown | C | I | C | **A/R** | **C/veto** | I | I |
| Identity / credential response | A | C | I | C | I | **R** | I |
| Eradication & rebuild of OT hosts | A | C | **R** | C | C | C | I |
| Restore controller logic from golden baseline | A | C | **R** | C | C | I | I |
| Regulatory / external reporting | C | I | I | I | I | C | **A/R** |
| Recovery validation (process within safe envelope) | A | C | C | **R** | C | I | I |
| Post-incident review | **A/R** | R | C | C | C | C | C |

## Authority-to-act matrix (the critical one)

| Proposed action | Who can authorize |
|-----------------|-------------------|
| Block external IP / disable IT account / isolate IT host | SOC (pre-authorized) |
| Tighten IT↔OT boundary firewall rule | IC + IT Sec |
| Cut a specific cross-zone / vendor-access flow | IC + Operations |
| Isolate an HMI / EWS / historian | IC + **Operations** |
| Move a control loop to manual / local | **Operations** + Controls Eng |
| Power-cycle / reboot a controller | **Operations + Controls Eng + Safety** (rarely; capture first) |
| Controlled process shutdown | **Operations** (with Safety), informed by IC |
| Any action that could affect safety | **Plant Safety Authority holds veto** |

> Rule of thumb: **anything at Purdue Level 2 and below requires operations/engineering authorization.** The SOC recommends; operations decides for the process.

## Out-of-band comms
Maintain a communication path that does not depend on potentially-compromised infrastructure (separate messaging, phone tree, physical control-room presence). Assume email/AD may be untrusted during an incident.
