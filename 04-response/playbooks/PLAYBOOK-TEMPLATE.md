# Playbook Template

Every playbook in `04-response/playbooks/` follows this structure. The sections are not
optional — each one exists because an OT SOC gets a specific thing wrong without it.

---

# PLAYBOOK-OT-NN — <Short descriptive title>

**Trigger.** Which KQL, SPL, Sigma, or platform detection fires this playbook, and what
condition it represents. Name the `OTD-####` IDs so the playbook and the detection catalog
stay wired together.

**Severity guide.** The default severity, plus the specific conditions that escalate it.
Escalation criteria must be concrete and checkable — "if the connecting host is not the
asset's normal engineering workstation", not "if it looks suspicious".

**Safety check.** *Asked before investigation begins.* Is there a legitimate operational
explanation — maintenance window, commissioning, emergency repair, vendor visit — that was
not logged? Check the shift log and call the control room before assuming malicious intent.
This section exists because **most hits on most OT playbooks are legitimate work with
missing paperwork**, and because an analyst who skips it is one step from a disruptive
response to a non-event.

**Investigate (passive).** A numbered sequence in which **every step is read-only**. Pull
logs, compare against approved lists, examine network telemetry, read controller audit
trails. Nothing in this section changes state on any OT asset. If a step would write,
reset, or disconnect, it belongs in Respond, not here.

**Decide.** Explicit branches — typically three:
- **Confirmed legitimate** → close as false positive, route the process gap to its owner.
- **Unclear** → contact the asset owner and shift engineer directly; **do not proceed
  until you have a human answer**.
- **Unauthorised or unexplained** → escalate, naming the specific playbook or IR process.

**Respond (only with sign-off).** Every containment action, with the authority required for
it. State *why* sign-off is needed in operational terms — e.g. an abrupt disconnect can
leave a controller in an undefined online-edit state.

**Close.** What gets recorded, where, and what routing happens for process gaps found
during the investigation.

---

## Standing safety statement

Every playbook operates under the program safety doctrine (`docs/safety-doctrine.md`):

> Priority order is **Safety → Availability → Integrity → Confidentiality**. Do not
> isolate, block, reset, or power-cycle any asset participating in a running process
> without confirming operational impact with the OT/process engineer. Where containment
> would affect the process, escalate rather than act.

The header statement is the standing rule. The **Safety check** section is where that rule
becomes specific to the situation in front of you — write it fresh for every playbook.
