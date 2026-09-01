# Chapter 04 — Safety Instrumented Systems and the Safety Lifecycle

> Part I · Foundations. Safety systems are the most consequential systems in any plant and the reason "safety-first" is more than a slogan. This chapter explains what a Safety Instrumented System is, the principles that make it trustworthy, and why those same principles are what you defend. (The companion repository `sis-safety-detection` turns this chapter into a full detection library.)

## 4.1 What an SIS is, and why it is separate

A **Safety Instrumented System (SIS)** is an independent layer whose only job is to take the process to a **safe state** when something goes dangerously wrong — regardless of what the control system is doing. It is deliberately kept **separate from the Basic Process Control System (BPCS = the DCS/PLC layer)**, so that it remains effective *even when the control system fails or is compromised.*

This separation is the core idea of **layers of protection**. The control system runs the process day to day. If control fails and the process heads toward a hazard, the SIS is the independent guardian that trips the process to safe. If the SIS were just a feature of the control system, a single failure or a single attacker could take out both at once — which is exactly what independence exists to prevent.

The governing standards are **IEC 61511** (process-industry functional safety, the practitioner's standard) and its parent **IEC 61508**.

## 4.2 The direction of trust: read up, never write down

Communication across the BPCS↔SIS boundary is deliberately **asymmetric**:

- **SIS → BPCS is read-mostly.** The SIS publishes its status, trip states, and diagnostics *up* to the DCS/SCADA/historian so operators can see what safety is doing. This is normal and expected.
- **BPCS → SIS is tightly restricted.** The control system must **not** be able to write the SIS's logic, trip setpoints, or outputs. At most it may make a non-safety, access-controlled request (like a reset) that the SIS logic itself decides whether to honor.

State this as a rule you will detect against: **the DCS may read the safety system but must never command it.** Any control-to-safety write is a boundary violation and a top-severity event.

## 4.3 The Safety Instrumented Function (SIF) chain

The SIS delivers one or more **Safety Instrumented Functions (SIFs)**, each a complete protective loop:

```
  [ dedicated safety sensor ] ──▶ [ logic solver ] ──▶ [ final element ]
       measures the hazard        certified safety      valve/breaker moves
       (its own transmitter)       logic vs trip limit   process to safe state
```

Three things distinguish a SIF from ordinary control:

1. Its sensors are **dedicated and safety-rated**, wired directly into the safety logic solver — not shared with control (see 4.6).
2. Its trip limits come from the **process hazard analysis and SIL determination**, not from the DCS.
3. It acts **autonomously** — it does not wait for or depend on the control system to reach the safe state.

Logic solvers you will meet: **Triconex** (the TRITON target), **HIMA**, **Siemens S7 F-Series**, **Rockwell GuardLogix**.

## 4.4 SIL — how much protection

**Safety Integrity Level (SIL 1–4)** expresses how much risk reduction a SIF provides, quantified as a **Probability of Failure on Demand (PFD)** — the chance the SIF fails to act when needed. Higher SIL = lower PFD = more protection (and more cost/complexity). SIL is determined by hazard analysis (often via **LOPA — Layers of Protection Analysis**), which credits each independent protection layer. The security-relevant point: **anything that quietly degrades a SIF — a bypassed channel, a defeated trip, a manipulated input — erodes the SIL the plant's risk assessment depends on**, even if the process keeps running.

## 4.5 Fail-safe by design: de-energize-to-trip

Most SIS final-element circuits are **de-energize-to-trip**: the outputs are *energized* during normal operation and **de-energize to reach the safe state** on a trip. This elegant choice makes failures fail *safe*: loss of power, a cut wire, or a dead output module all drop the circuit to the safe position, and line-monitoring detects the open circuit. Combined with continuous **self-diagnostics** (on a detected dangerous fault, the solver trips to safe), de-energize-to-trip is what lets a SIF carry a low PFD and hold its SIL. For a defender, the corollary is that **loss of line monitoring, an unexpected energize where de-energize is expected, or a diagnostic fault** are all erosions of the fail-safe property worth watching.

## 4.6 Voting and the shared-sensor rule

To balance **spurious trips** (nuisance shutdowns that hurt availability) against **dangerous failures** (missed trips that hurt safety), SIFs use **voting** across redundant channels:

- **1oo1** — one channel; simplest, no tolerance.
- **1oo2** — either of two can trip; safe but prone to spurious trips.
- **2oo2** — both must agree to trip; fewer spurious trips, less safe.
- **2oo3** — two of three agree; the sweet spot — tolerates one failed/deviating channel without a spurious trip while still protecting.

**Voting degradation** (a 2oo3 group dropping to a lesser configuration) lowers the effective SIL even while the process runs — a quiet, important signal.

The **shared-sensor rule (IEC 61511-1, clause 11.2)** is the sharpest independence principle: a device may **not** be shared between control and safety such that its failure *both* causes the demand on the SIF *and* disables the SIF's response. That single common-cause is precisely the trap independence exists to prevent. Best practice is **dedicated safety sensors** with voting; if a device is shared, it becomes part of the SIS (managed to SIL) and the common-cause failure must be accounted for in the PFD.

## 4.7 Bypasses, overrides and forces

Maintenance legitimately takes a SIF or channel out of service temporarily using **bypasses / overrides / maintenance-override switches (MOS)** and **forces** — under strict procedure (authorization, a time limit, and compensating measures). Each active bypass is a hole in the protection. Unauthorized, overdue, or clustered bypasses are both a safety problem and a security signal.

## 4.8 Why safety principles are security controls

Notice that independence, fail-safe, voting, and bypass discipline are **safety** properties — and each is also a **security** control. A safety-targeting attack (the TRITON class) works by defeating one of them: reaching the engineering path to change safety logic, or manipulating inputs and bypasses so the SIF won't act when it's needed. Therefore **monitoring these properties is simultaneously safety assurance and attack detection**, and any event touching the SIS is treated as **SEV-1** and routed to the safety authority.

## Chapter summary

- The SIS is an **independent protection layer** that trips the process to a safe state regardless of the control system; independence is the whole point.
- Trust flows **up** (SIS→BPCS read) and never **down** (BPCS must not command the SIS).
- A **SIF** is sensor → logic solver → final element, with dedicated sensors, hazard-derived trip limits, and autonomous action.
- **SIL/PFD** quantify protection; quiet degradation erodes it.
- **De-energize-to-trip** makes failures fail safe; **voting (2oo3)** balances spurious vs dangerous failure; the **shared-sensor rule** forbids common-cause between demand and response.
- Safety principles are security controls — any SIS event is SEV-1.

## Cross-references
- Chapter 12 (ICS malware) covers TRITON in depth.
- Chapter 25 (incident response) defines the safety-authority escalation and veto.
- Companion repository: `sis-safety-detection` (boundary, engineering/program, trip, voting, bypass, and diagnostics detections).
