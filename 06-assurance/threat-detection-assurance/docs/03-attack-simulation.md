# 03 — Attack Simulation

The "simulate" step, done safely and repeatably. The goal is to trigger the technique the detection claims to catch — with a recorded timestamp for MTTD — not to cause damage.

## Simulation approaches
| Approach | When | Tools |
|----------|------|-------|
| **Automated atomic tests** | Per-technique logic testing at scale | **Atomic Red Team** (Invoke-AtomicRedTeam), mapped to ATT&CK T-codes |
| **Adversary emulation** | Multi-step chains / campaigns | **MITRE Caldera**, Prelude Operator |
| **Manual / bespoke** | Techniques without an atomic, or environment-specific | scripts, red-team tooling in a lab |
| **Log / telemetry injection** | When you can't run the live technique (prod, OT) | craft & inject a representative log event or replay a pcap |
| **Cloud** | Cloud control-plane techniques | **Stratus Red Team** |

## IT examples (map technique → atomic)
- **T1110 Brute Force** → repeated failed logons then success (validates IAM-01/02/03).
- **T1059.001 PowerShell** → encoded command execution (validates EDR-01).
- **T1071.004 DNS / T1048 exfil** → high-volume/long-label DNS queries (validates OUT-01).
- **T1003.001 LSASS** → credential-access simulation on a lab host (validates EDR-03).

Atomic Red Team ships tests for most of these; run on an instrumented lab host, capture the run timestamp, then validate.

## OT/ICS simulation — safety first
**Never run attack simulations against a live process, and never against a Safety Instrumented System.** OT TDA is done one of three safe ways (detail in `05`):
1. **Lab replication** — reproduce the detection in the `ot-security-lab` (OpenPLC/Conpot + Zeek+ICSNPP + SIEM) and simulate there with pymodbus / ISF / Metasploit ICS modules.
2. **PCAP replay** — replay a captured or crafted malicious pcap **to the sensor** (`tcpreplay`), validating the passive detection chain without touching any controller.
3. **Log/event injection** — inject a representative NDR/historian event to validate the SIEM-side rule and pipeline.

OT technique → simulation:
- **T0836 Modify Parameter** → Modbus write function code (5/6/16) from an unauthorized source (validates MOD-01).
- **T0843 Program Download** → S7 program-transfer in the lab / pcap replay (validates S7-02).
- **T0858 Change Operating Mode** → key-switch/mode change event injection (validates SIS-B4).

## Recording for MTTD
Every simulation must log **the exact time the malicious action executed**. MTTD = (alert generated) − (action executed). Automate the timestamp capture where possible; a manual test still records it in the test-case result.

## Safety & authorization rules
- Simulations run in a **lab or under explicit written authorization**.
- **Isolate** attacker tooling (host-only/internal networks, no bridge to production/internet).
- **Never** target production OT/SIS with live attacks — use replay/injection.
- Clean up artifacts (created accounts, files, tasks) after IT atomics.
- Log every simulation for auditability.
