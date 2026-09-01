# Chapter 15 — Real-World Case Studies

> Part III. Landmark OT intrusions, read as timelines with lessons. The goal is not history for its own sake — it is to extract, from each, the detection or hunt that would have caught it, and to internalize the recurring patterns.

## 15.1 How to read a case

For each incident, extract four things:
1. **Access vector** — how they got in.
2. **Pivot to OT** — how they crossed from IT to the control network.
3. **Plant-floor action** — what they did to the process.
4. **Detection opportunity** — the signal that was, or could have been, caught.

Every real case contains a missed or late signal that your telemetry could have surfaced. Turn each into a detection or a hunt hypothesis.

## 15.2 The cases and their lessons

**Stuxnet (Natanz, ~2010).** Access via removable media/IT; targeted specific S7 PLCs; modified controller logic to damage centrifuges while replaying normal readings to operators. *Lesson:* watch the **physics** (recorded/live divergence) and detect **program downloads** — the network layer alone would have missed a hidden, logic-level attack.

**Ukraine grid (2015).** Spear-phishing → corporate foothold → stolen credentials → remote access to distribution HMIs; operators watched their own cursors open breakers; KillDisk wiped systems to slow recovery. *Lesson:* **remote-access and HMI-command monitoring**; many OT attacks are human-operated over legitimate access.

**Industroyer / Ukraine (2016).** Purpose-built malware spoke grid protocols (IEC-101/104, 61850, OPC) to operate substation equipment automatically. *Lesson:* **protocol-aware detection** — the malware is a valid protocol client; you catch it by "unauthorized command from the wrong source," not by signature.

**TRITON (Saudi petrochemical, 2017).** Reached Triconex **safety** controllers via the engineering workstation and tried to reprogram them; a fault tripped the plant and exposed the attack. *Lesson:* **monitor the SIS and the engineering path**; any safety-system engineering is SEV-1. Had the plant not tripped, the last line of protection might have been silently disabled.

**Colonial Pipeline (2021).** IT-side ransomware (via a legacy VPN account without MFA) never touched OT, but the operator **shut down the pipeline** out of caution, causing regional fuel disruption. *Lesson:* **IT/OT convergence risk is operational** — an IT incident can force an OT shutdown; remote-access hygiene (MFA) and boundary segmentation are decisive.

**Oldsmar water plant (2021).** An attacker used **remote-access software** to reach an HMI and briefly raised the sodium hydroxide setpoint ~100×; an operator saw the change and reverted it. *Lesson:* **remote-access monitoring plus setpoint/historian detection** — a setpoint write outside the safe range should alert instantly, not depend on an alert operator.

**PIPEDREAM / INCONTROLLER (2022).** A modular ICS attack framework discovered **before** deployment against energy targets. *Lesson:* detect **capability staging and discovery**, not only execution — the best outcome is catching the pre-positioning.

## 15.3 The recurring patterns

Across the cases, the same themes repeat and should shape your program:

- **Access, not exploits** — remote access and the IT pivot dominate initial access.
- **Human-operated** — many attacks are hands-on-keyboard over legitimate access, not autonomous malware.
- **Legitimate operations abused** — the malicious action is usually a *valid* command from the wrong source.
- **The physical layer is decisive** — the historian and process indicators are where impact (and hidden impact) show up.
- **Safety is the ultimate target** — defeating protection is the highest-consequence move.

## Chapter summary
- Read each case for **access vector, OT pivot, plant-floor action, and the detection opportunity.**
- Stuxnet (hidden logic sabotage), Ukraine 2015 (remote-access HMI operation), Industroyer (protocol-native), TRITON (safety-system via EWS), Colonial (IT incident forcing OT shutdown), Oldsmar (remote-access setpoint change), PIPEDREAM (pre-deployment framework).
- Recurring patterns: access over exploits, human-operated, abuse of legitimate operations, the decisive physical layer, and safety as the ultimate target.

## Cross-references
- Chapter 11 (kill chain) and Chapter 12 (malware) underpin these; Chapter 16 turns cases into hunt hypotheses; Chapter 17 develops the physical-layer detections.
