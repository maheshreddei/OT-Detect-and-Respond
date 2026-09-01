# Chapter 25 — OT Incident Response

> Part V · Response & Forensics. Responding to an OT incident is not IT incident response with different assets — the authority, the goals, and the containment options are fundamentally different. This chapter is how you run an OT incident from confirmed finding to safe recovery.

## 25.1 The goal is a safe process, not eradication

In IT, the response goal is to eradicate the threat and restore service. In OT, the primary goal is a **safe process state**. Eradication is secondary to safety and availability. A response action that eliminates the malware but trips the plant or defeats a safety function is a *failure*, not a success. Every decision runs through the question: *does this keep the process safe?*

## 25.2 Authority: operations decides, safety vetoes

The single most important structural fact of OT IR:

- **Operations decides for the process.** The control engineers who own the plant decide what response actions are safe to take, because only they understand the physical consequences.
- **The safety authority holds a veto.** Anything touching a safety function requires the plant's safety authority.
- **Security advises.** The SOC/IR team provides the threat picture and recommends options; it does not unilaterally isolate or shut down OT assets.

This **authority-to-act matrix** must be agreed *before* an incident. The middle of a crisis is the wrong time to discover that no one knows who can authorize isolating a controller.

## 25.3 The adapted lifecycle

The familiar NIST lifecycle applies — **prepare → detect/analyze → contain → eradicate → recover → lessons learned** — but each phase is constrained by OT reality:

- **Prepare** — OT-specific playbooks, the authority matrix, known-good baselines, contact trees including operations and safety, and pre-agreed containment options ranked by process impact.
- **Detect/analyze** — using the network, host, and historian telemetry of Part II; confirm the physical impact, not just the digital indicator.
- **Contain** — the hard part (below).
- **Eradicate/recover** — restore logic/config from known-good backups, revalidate the process with engineering, and return to service under operations' control.
- **Lessons learned** — feed findings back into detections, playbooks, and baselines.

## 25.4 Containment is constrained

In IT you isolate or power off freely. In OT you often **cannot**:

- Isolating a live controller can blind operators or trip the process.
- Powering off is frequently impossible without a safe, planned shutdown.
- "Pull the network cable" may be exactly the wrong move.

So containment is a **consequence-ranked negotiation with operations**, choosing the option with the least process impact that still limits the threat:

- Network isolation **at the boundary** (cut the attacker's path in) rather than at the controller.
- **Disabling remote access** and tightening allow-lists.
- Increased monitoring while planning a safe shutdown window, where an immediate action would be more dangerous than the threat.

Passive-before-active applies to response, not just monitoring.

## 25.5 Evidence before action

Because you frequently cannot take systems offline and may have to act fast, **capture volatile evidence before you change anything** — network captures, host memory/artifacts on the EWS/HMI, controller state, and historian data around the event. Once you've contained or restored, that evidence is gone. This is doubly important because OT incidents can become **safety and regulatory investigations** (Chapter 26 develops the forensics).

## 25.6 Escalation paths

Pre-define who is called for each scenario. In particular, **any safety-system (SIS) finding routes to the safety authority** and is treated as SEV-1. Wire your detections so a safety alert reaches the right people directly, not just the cyber on-call.

## Chapter summary
- The OT IR goal is a **safe process state**, not eradication.
- **Operations decides; safety vetoes; security advises** — agree the authority matrix in advance.
- The NIST lifecycle applies but **containment is constrained** — a consequence-ranked negotiation, boundary-first, passive-before-active.
- **Capture volatile evidence before acting**; OT incidents can become safety/regulatory investigations.
- Pre-define escalation; **SIS findings are SEV-1** to the safety authority.

## Cross-references
- Chapter 04 (SIS/safety), Chapter 26 (forensics), Chapter 24 (hunting → IR handoff).
- Companion: `it-ot-incident-response` (full IR plan, investigation SOPs, evidence guides, playbooks, RACI).
