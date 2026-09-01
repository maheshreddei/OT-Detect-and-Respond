# Prioritization Methodology

The tiering in this repository is not arbitrary. Each source is scored on four axes, and
the tier is derived from how those axes trade off. This document makes the derivation
explicit so the model can be applied consistently to sources not yet in the inventory.

## The four axes

**Log Ease** — how hard it is to get usable logs off the source. Values: Easy (native
syslog or Windows event log), Medium (agent deployment or filtering required), Hard
(limited/no native logging; needs a passive proxy), Nightmare (no practical direct
collection). This is the effort axis.

**Noise** — event volume and signal-to-noise once collecting. Values: Low, Medium, High,
Nightmare. High-noise critical sources (engineering workstations) are still Tier 1, but the
axis flags where tuning effort must be budgeted before go-live.

**Source Count** — how many instances typically exist. Values: Very Few, Few, Moderate,
Many, Very Many. This drives licensing/volume planning and whether per-instance onboarding
is realistic or whether a fleet approach (passive monitoring) is required.

**Importance** — security value of the source. Values: Low, Medium, High, Critical. This is
the value axis and the dominant input to tiering.

## How tier is derived

The tier balances **value against effort**, with two safety-driven overrides:

1. **Value first.** Critical and High importance sources are candidates for Tier 1-2; Medium
   for Tier 3; Low for Tier 4.
2. **Effort demotes.** A Critical source that is Hard to collect (PLC, PAC, Safety
   Controller) drops from Tier 1 to Tier 2-3, because the practical collection path
   (passive monitoring) is itself a project. High effort is why Network Traffic sits in
   Tier 3 despite being the most detection-rich source.
3. **Safety override.** Any source whose events carry safety consequence (Safety
   Controller) is always treated as page-out on event, regardless of tier or collection
   difficulty. Tier governs *onboarding order*, never *response priority*.
4. **Redundancy demotes to zero.** A source whose state is fully represented by another
   already-collected source (Field I/O, covered by PLC/RTU/historian) is Tier 4 — do not
   collect. Marginal detection value, not raw importance, decides this.

## Worked examples

- **Firewall (OT):** Easy + Critical, low instance count -> Tier 1. Highest value-per-effort
  ratio in the whole inventory; it is the cheapest confirmation of Purdue zone crossing.
- **Engineering Workstation:** Critical but High noise -> still Tier 1 (value wins), with an
  explicit note to budget aggressive tuning. Noise delays *nothing* here; it shapes the
  onboarding work.
- **PLC:** Critical but Hard -> Tier 2. The demotion is entirely about the collection path:
  you onboard it via passive monitoring (Network Traffic), not by instrumenting the
  controller.
- **Network Traffic:** High value, Nightmare noise, Medium ease -> Tier 3. It underpins all
  protocol-level detection but is gated on SPAN/TAP architecture and DPI tuning, so it is
  sequenced after the quick wins.
- **Field I/O:** Low importance, redundant -> Tier 4. Not collected.

## Applying the model to a new source

Score the four axes, then: start from Importance for the candidate tier, demote by one tier
for Hard/Nightmare Log Ease, apply the safety override for anything with safety
consequence, and drop to Tier 4 if another collected source already represents its state.
