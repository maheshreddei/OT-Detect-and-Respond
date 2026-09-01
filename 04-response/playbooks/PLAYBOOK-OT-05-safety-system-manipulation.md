# PLAYBOOK-OT-05 — Safety instrumented system manipulation

**Trigger.** A detection fires on the safety layer: a write or command from a BPCS/control
zone source into the SIS zone, an SIS key switch in PROGRAM mode, a forced or overridden
safety point, a bypass that exceeds its permitted duration, or a voting/sensor-divergence
anomaly.

Catalog references: `OTD-0017` (SIS key switch in PROGRAM mode), the full `SIS-A*`
(boundary), `SIS-B*` (engineering/program), `SIS-D*` (sensor voting), `SIS-E*`
(bypass/override) families, and `HIST-G01` (SIF trip-point approach).

ATT&CK for ICS: T0858 Change Operating Mode, T0855 Unauthorized Command Message,
T0880 Loss of Safety. Precedent: TRITON/TRISIS (XENOTIME).

**Severity guide.** **Critical (SEV-1) on any hit. There is no default-Medium branch in
this playbook.** The safety layer exists to be independent; any evidence that its
independence, logic, or voting has been touched is treated as a potential loss-of-safety
event until an engineer proves otherwise. Escalate to plant leadership and the safety
authority immediately — this is one of the few OT detections where notification precedes
investigation.

**Safety check.** This section inverts here. Elsewhere the safety check asks *"is this
legitimate work?"* — here it asks **"is the safety function currently able to do its job?"**
Establish with the safety authority and operations: is the SIF available, is any bypass
currently active and authorised, and is the process operating inside the envelope that
assumes that SIF works? A legitimate proof-test or authorised bypass is common and must be
confirmed against the bypass register — but confirmation is required *before* standing
down, never assumed. If the safety function is degraded, operations decides whether the
process continues to run. That decision is theirs, and it outranks the investigation.

## Investigate (passive) — every step here is read-only

1. Confirm the current state of the safety function: bypass register, forced-point list,
   key-switch position, and whether a proof test or MOC is in progress.
2. Identify the source of the activity — zone, host, account — and whether it sits in the
   BPCS zone (a boundary violation by definition) or the sanctioned SIS engineering path.
3. Pull the SIS engineering workstation logs and the safety-application audit trail: who
   connected, with what tool, and what operation was performed.
4. Pull NDR telemetry at the BPCS↔SIS boundary: protocol, direction, function code, and
   whether traffic traversed the sanctioned gateway.
5. Compare the running safety logic against the validated baseline — **engineer-led,
   read-only.** Export the SOE (sequence-of-events) recorder for the window.
6. Check sensor voting integrity: divergence between redundant transmitters, or a voted
   input behaving inconsistently with its peers.

**Decide.** Three branches:

- **Confirmed authorised safety work** (proof test, MOC-approved change, registered bypass)
  → close as false positive **with the safety authority's explicit confirmation recorded**,
  not the SOC's own judgement.
- **Unclear** → maintain SEV-1; contact the safety authority and controls engineering
  directly. **Do not stand down a safety alert on ambiguity.**
- **Unauthorised or unexplained** → major incident. Assume potential loss of safety;
  operations determines whether the process continues to run.

**Respond (only with sign-off).** No network action against SIS assets without the safety
authority's approval — isolating a safety controller can itself create the hazard the SIF
exists to prevent. Removing an unauthorised bypass or restoring safety logic is an
engineering action performed under MOC, never a SOC action. Security's role here is
evidence, attribution, and closing the access path.

**Close.** Record the safety-function state throughout, the authorisation status of every
change found, and the full identity chain. Any finding routes to both the incident record
and the functional-safety management system. Where an unauthorised change reached the SIS,
a full proof test is required before the SIF is credited again — that is the safety
authority's call and must be recorded as a closure condition.
