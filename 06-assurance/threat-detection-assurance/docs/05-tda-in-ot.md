# 05 — TDA in OT/ICS

OT changes *how* you simulate, not *whether* you assure. The five goals and four steps are identical; the attack-simulation step must be **passive and safe** because you cannot run live attacks against a running plant or a safety system.

## The hard rule
**Never run attack simulations against a live OT process, and never against a Safety Instrumented System.** A simulated Modbus write or program download on a live controller can move the physical process or trip a plant. OT TDA proves the detection without touching the controller.

## Three safe methods
1. **Lab replication (preferred).** Reproduce the detection in an isolated lab (the `ot-security-lab`: OpenPLC/Conpot + Zeek+ICSNPP + SIEM). Run the real technique there with pymodbus / ISF / Metasploit ICS. This validates the full chain end-to-end with zero production risk, and doubles as your demo environment.
2. **PCAP replay to the sensor.** Replay a captured or crafted malicious pcap to the NDR/Zeek sensor with `tcpreplay` on a mirror interface. This validates the **passive detection chain** (pcap → ICSNPP parse → SIEM rule → alert) without any traffic reaching a controller — safe even alongside production if replayed onto an isolated span.
3. **Event/log injection.** Inject a representative NDR or historian event into the SIEM to validate the SIEM-side rule, pipeline, and MTTD — when you only need to test the detection logic, not the sensor parsing.

## What to validate per OT detection type
| Detection type | Safe simulation | Validates |
|----------------|-----------------|-----------|
| Protocol write/command (Modbus/S7/DNP3…) | lab technique or pcap replay | ICSNPP parse + rule fire |
| Physics / historian (baseline & deviation) | inject historian values crossing the threshold | baseline logic + alert |
| SIS / safety (key-switch, program) | **event injection only** (never live) | SIEM rule + escalation path |
| Boundary / zone-crossing | pcap replay or lab traffic | firewall/NDR rule |

## Extra checks that matter in OT
- **Passive-chain integrity** — is the SPAN/tap feeding the sensor? A dead tap is a silent blind spot; log-validation here means verifying the mirror is alive.
- **Safety escalation path** — for SIS detections, validate not just that the alert fires but that it routes to the **safety authority** (SEV-1 path), via a tabletop if a live test is unsafe.
- **No operational impact** — confirm the TDA activity itself caused none (that's the whole point).

## OT TDA cadence
Validate OT detections in the lab on the same triggers as IT (new detection, parser/platform change, periodic regression), plus whenever the plant's protocol/asset baseline changes — because OT detections are baseline-sensitive and drift as the environment changes.
