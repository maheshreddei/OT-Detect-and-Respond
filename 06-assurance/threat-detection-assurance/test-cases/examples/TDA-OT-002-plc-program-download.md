# TDA-OT-002 — PLC program download (S7)

| Field | Value |
|-------|-------|
| Use case | Logic download to a Siemens PLC |
| Detection tested | S7-02 (ot-protocol-defense / ot-detection-engineering) |
| ATT&CK for ICS | T0843 Program Download |
| TDA goals | Log validation · Logic · Blind-spot · Speed |
| Layer / severity | OT / engineering · Critical |
| Environment | **Lab only** or pcap replay |

## Objective
Prove a program/logic download to a PLC raises a critical alert via the passive chain — the Stuxnet/TRITON-class event — without touching a production controller.

## Preconditions (log validation)
- Zeek + ICSNPP (S7comm) or NDR S7 policy feeding the SIEM.
- S7-02 rule / NDR signature enabled.
- SPAN/tap alive.

## Attack simulation (safe)
**Method A — lab technique** (S7 PLC sim / snap7 in the isolated lab): perform a block download to the lab controller using an engineering tool or snap7 in a lab scenario.
**Method B — pcap replay** (preferred if no lab S7 device): replay a captured S7 program-download pcap to the sensor:
```
sudo tcpreplay -i mirror0 s7_program_download.pcap
```
Record the timestamp.

## Expected detection
S7-02 / native "program transfer" signature fires. Fields: **src (engineering source), dst (PLC), function = program download, time**. Bonus: correlate with a key-switch change if available.

## Validation criteria
- [ ] Data present — S7comm parsed (or NDR program-transfer alert present).
- [ ] Rule fired — critical alert on the download.
- [ ] Fidelity — source + target PLC identified.
- [ ] Speed — MTTD ≤ target.
- [ ] Escalation — routed as **critical** to the right path.

## Result (fill in)
State: ☐ Pass ☐ Partial ☐ Fail-no-rule ☐ Fail-no-data · MTTD: ____ · Evidence: · Notes:

## Remediation (if failed)
- No data → S7comm not parsed → check ICSNPP/NDR S7 support and tap placement (**blind spot** if S7 is unseen).
- Rule miss → enable the native program-transfer signature / S7 function detection.
- Wrong severity/route → fix alert severity and escalation.
