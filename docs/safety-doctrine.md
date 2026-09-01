# Safety Doctrine

Every SOP in an OT SOC carries a safety statement. This document defines what that
statement is, why it belongs on *every* procedure rather than only the safety-related ones,
and how it differs from the fuller treatment given to safety-centric use cases.

## Two different things called "safety"

**1. The safety line (a guardrail) — belongs in every SOP.**

In OT, the responder is often a bigger risk than the alert. An analyst acting on IT
instinct — isolate the host, block the flow, kill the session, force a credential reset,
take the device offline — can trip a process, cause a loss of view or control, or actuate a
safety function, while the original alert turns out benign. The safety line is a guardrail
on the *analyst's hands*, not a statement about the alert. It therefore applies to a routine
firewall-noise procedure exactly as much as to a controller-tampering one, because both can
end with someone reaching for a containment action.

**2. Safety-centric handling (the full treatment) — belongs in safety-relevant use cases.**

Use cases where the safety function itself is the target (`OT-UC-0017`, SIS key switch in
PROGRAM mode; TRITON/XENOTIME-class activity) are not "a line". The entire procedure is
shaped around protecting the safety instrumented system: page-out on any event regardless
of volume, process/safety engineering in the loop from the first minute, and a deliberate
bias *against* unilateral network action.

Conflating the two is a common mistake. The guardrail is universal; the full treatment is
specific.

## The standard safety line

Every SOP header carries this block:

> **Safety statement.** Priority order for this procedure is **Safety → Availability →
> Integrity → Confidentiality**. Do not isolate, block, reset, or power-cycle any asset
> that participates in a running process without first confirming operational impact with
> the OT/process engineer. Where containment would affect the process, escalate rather than
> act. The SOC analyst may take [defined actions] independently; anything touching a
> controller, a safety function, or process availability requires [named authority].

Four elements, none optional:

1. **Priority order** — the AIC inversion of IT's CIA, stated explicitly so it is not
   assumed.
2. **Do-no-harm caution** — no containment mid-process.
3. **Consultation requirement** — the process engineer is in the loop before process-
   affecting action.
4. **Authority boundary** — what the analyst may do alone versus what requires the asset
   owner or operations.

This aligns with NIST SP 800-82's core principle that security controls and response
actions must not adversely affect safety or reliability.

## Avoiding boilerplate blindness

A universal statement that never changes becomes text people skim. The countermeasure is to
split it:

- **The generic guardrail** goes in the SOP header, identical everywhere. It sets the
  standing rule.
- **The specific operational impact** goes in the individual SOP body, and must be written
  fresh for each use case. Not "be careful" but *"blocking this flow drops the DNP3 poll to
  the substation and causes loss of view for the operator."*

The per-use-case field is where the real safety thinking happens. The header is the
reminder that the thinking is required.

## Where this is enforced in the repository

- `00-program/use-case-template.md` carries an **OT-specific caution** field — what an
  IT-trained analyst would get wrong on this particular use case.
- `00-program/raci-matrix.md` makes the **OT/Process Engineer responsible** for the
  safety/operational plausibility review, and that row is marked non-optional for any use
  case touching an SIS. Detection engineering does not self-certify operational impact.
- `00-program/use-case-lifecycle.md` requires the process engineering owner in the
  Validated → Production gate review for safety-relevant content.
- `01-telemetry/log-source-inventory.csv` flags the Safety Controller (`LS-07`) as
  priority-1 investigation on any event *regardless of collection difficulty or tier* —
  because onboarding tier governs the order in which sources arrive, never the priority of
  response once they do.

That last distinction is worth stating plainly, because it is easy to get backwards:

> **Tier governs onboarding order. It never governs response priority.**
