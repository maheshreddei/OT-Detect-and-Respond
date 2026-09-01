# PLAYBOOK-OT-09 — Process data anomaly (historian-detected)

**Trigger.** A historian-based detection fires: a tag breaching its operating envelope, a
frozen or replayed value, an impossible state combination, divergence between the historian
and the controller, or a redundant-sensor correlation break.

Catalog references: `HIST-A01` (tag out of envelope), `HIST-B01` (setpoint outside range),
`HIST-C01` (frozen value / replay), `HIST-D02` (impossible state combination),
`HIST-E01` (historian↔PLC divergence), `SIGMA:it-dmz-ot-crosszone/22` (redundant sensor
divergence), `SIS-D*` (sensor voting integrity).

**Severity guide.** **Medium** by default — process data is noisy and instrument faults are
far more common than attacks. Escalate to **High** if the anomaly is a frozen/replayed value
(a classic manipulation-masking pattern), if the historian and controller disagree, or if
the affected tag feeds a protective function. Escalate to **Critical** if a safety-related
measurement is involved — hand off to `PLAYBOOK-OT-05`.

**Safety check.** **The most likely explanation is an instrument problem, not an attack —
and an instrument problem is still an operational hazard.** Establish with the control room
whether operators trust the reading, whether the loop is in manual, and whether a
transmitter is known faulty or under calibration. A frozen value may be a stuck sensor or a
replay attack; both need attention, but only one needs the SOC. Also check for startup,
shutdown, or grade-change transients — these routinely produce out-of-envelope values that
are entirely legitimate.

## Investigate (passive) — every step here is read-only

1. Characterise the anomaly precisely: which tag, what pattern (breach, freeze,
   divergence), duration, and magnitude against the validated envelope.
2. Check the tag's quality flags and the instrument's maintenance/calibration record.
3. Corroborate against an independent source: a redundant transmitter, a related loop that
   should move with it, or the controller's own value versus the historian's.
4. Determine whether the process actually moved or only the *reported* value moved — this
   is the distinction between a real process event and a data-integrity event.
5. Check for a corresponding control action: was there a write, setpoint change, or logic
   change in the same window that explains the movement?
6. Check whether a mode change or MOC-driven operating-point change occurred that should
   have triggered a re-baseline.

**Decide.** Three branches:

- **Instrument fault or legitimate process transient** → close as false positive; route the
  instrument finding to maintenance. If it was a post-MOC operating change, trigger a
  detection re-baseline.
- **Unclear** → contact the loop owner and process engineer; **do not conclude manipulation
  from historian data alone** — it is the weakest single source for attribution.
- **Data-integrity anomaly with a corresponding control action** → escalate; correlate with
  `PLAYBOOK-OT-02` (setpoint) or `PLAYBOOK-OT-07` (control command). A reported value that
  diverges from the controller's value while the process moves is the signature worth
  escalating hardest.

**Respond (only with sign-off).** There is normally **no security response to a historian
alert on its own** — this playbook usually terminates in corroboration or escalation, not
containment. Any action affecting the loop is operations'. Do not "correct" historian data.

**Close.** Record the tag, the pattern, the corroborating sources checked, and the
conclusion. Where the cause was a legitimate operating-point change, trigger the re-baseline
so the detection does not keep firing. Where the historian and controller disagreed, raise a
data-integrity finding regardless of the security outcome.
