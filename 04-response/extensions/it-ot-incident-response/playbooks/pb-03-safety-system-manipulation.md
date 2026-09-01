# PB-03 — Safety Instrumented System (SIS) Manipulation

**Severity: SEV-1 always.** ATT&CK ICS: T0880 (Loss of Safety), T0837 (Loss of Protection), T0858 (Change Operating Mode). The TRITON/TRISIS class — the most consequential OT incident type.

## Indicators
SIS engineering-tool activity; SIS controller mode/key-switch change to PROGRAM; safety-PV trending toward a trip while control looks normal; unexpected/suppressed trips; SIS logic-transfer on the wire.

## Immediate actions
- **SEV-1 immediately. Engage plant safety authority, operations, controls engineering, and executive sponsor at once.**
- Treat as a potential imminent safety event. Operations + safety lead process protection; cyber supports.
- **Take no action that could affect the SIS function.** Capture only.

## Evidence to collect — and what it proves
1. **Safety-PV trend + trip records (prove approach/defeat).** Historian safety tags + trip/alarm journal → proves whether the process approached a trip and whether protection functioned. → [historian guide](../evidence/historian-and-process.md).
2. **SIS logic/config compare (prove modification) — read-only, safety-authority-led.** Compare SIS logic to golden baseline; export SIS diagnostic/event log; check key-switch/mode. → [controller guide](../evidence/plc-controller-safe-acquisition.md) (SIS section).
3. **SIS network activity (prove the transfer).** pcap/NDR of any SIS engineering traffic → proves connection to and transfer against the safety controller. → [network guide](../evidence/network-and-ot-protocols.md).
4. **EWS/engineering host (prove tool use).** Which station ran SIS engineering software, when, by whom. → [windows guide](../evidence/windows-ews-hmi-historian-host.md).
5. **Identity (prove attribution).** How the actor reached the SIS engineering path. → [identity guide](../evidence/identity-and-remote-access.md).

## Analysis
Establish whether the SIS logic was modified, whether protection was bypassed (key-switch in PROGRAM, forces), and whether a hazardous process state was approached. The TRITON pattern: BPCS looks normal while the SIS is targeted — so weight the SIS-specific and safety-PV evidence heavily.

## Containment
Process protection is operations + safety's call and may include a controlled shutdown to a safe state. Cyber containment (cut the path, isolate the SIS engineering station, disable accounts) is done **without touching the SIS function**, operations-authorized.

## Eradication & recovery
Restore verified SIS baseline logic — **only** under safety-authority control and validation, following the plant's functional-safety change process (this is not a routine rebuild). Full safety validation before the SIS is trusted again. Rebuild the SIS engineering station; close the vector.

## Proof-artifact checklist
- [ ] Safety-PV trend + trip/alarm records (hashed)
- [ ] SIS logic compare vs baseline + diagnostic/event log
- [ ] Key-switch/mode record; forces
- [ ] Network capture of SIS engineering traffic
- [ ] SIS engineering-station host artifacts + identity timeline
- [ ] Chain-of-custody complete; safety authority sign-off recorded
