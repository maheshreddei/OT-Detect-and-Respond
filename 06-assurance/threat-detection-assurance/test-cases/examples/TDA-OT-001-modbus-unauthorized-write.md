# TDA-OT-001 — Unauthorized Modbus write

| Field | Value |
|-------|-------|
| Use case | Write to a PLC from a non-master source |
| Detection tested | MOD-01 (ot-protocol-defense) |
| ATT&CK for ICS | T0836 Modify Parameter · T0831 Manipulation of Control |
| TDA goals | Log validation · Logic · Speed |
| Layer / severity | OT / protocol · High |
| Environment | **Lab only** (`ot-security-lab`) or pcap replay |

## Objective
Prove the passive detection chain flags a Modbus write function code from an unauthorized source — **without touching any production controller**.

## Preconditions (log validation)
- Zeek + **ICSNPP** parsing Modbus on the sensor; `modbus.log` (or NDR alerts) → SIEM.
- The SPAN/tap is alive and feeding the sensor (verify — a dead tap is a silent blind spot).
- MOD-01 rule / NDR assertion deployed.

## Attack simulation (safe)
**Method A — lab technique** (OpenPLC/Conpot target in the isolated lab):
```
# Write a single register (FC6) to the lab PLC from a non-master host - LAB ONLY
python3 - <<'PY'
from pymodbus.client import ModbusTcpClient
c = ModbusTcpClient('10.10.0.11')   # lab PLC
c.write_register(0, 1234, slave=1)  # FC6 write - triggers MOD-01
c.close()
PY
```
**Method B — pcap replay** (safe even near production, onto an isolated span): replay a captured "unauthorized write" pcap to the sensor:
```
sudo tcpreplay -i mirror0 modbus_unauth_write.pcap
```
Record the action timestamp for MTTD.

## Expected detection
MOD-01: write FCs (5/6/15/16) from a source not in the master baseline → alert. Fields: **src, dst, function code, register, unit id**.

## Validation criteria
- [ ] Data present — `modbus.log` shows the write (ICSNPP parsed it).
- [ ] Rule fired — MOD-01 alert with the correct src/dst/FC.
- [ ] Fidelity — function code + target register captured.
- [ ] Speed — MTTD ≤ target (near-real-time).
- [ ] No operational impact from the test itself.

## Result (fill in)
State: ☐ Pass ☐ Partial ☐ Fail-no-rule ☐ Fail-no-data · MTTD: ____ · Evidence: · Notes:

## Remediation (if failed)
- No `modbus.log` → check SPAN/tap and ICSNPP parser on the sensor (log-validation gap).
- Rule miss → confirm write-FC list and master allow-list.
- Slow → check sensor→SIEM pipeline latency.
