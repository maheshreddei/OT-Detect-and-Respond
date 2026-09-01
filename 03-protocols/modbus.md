# Modbus (TCP)

## Snapshot
| Property | Value |
|----------|-------|
| Port/transport | TCP/502 |
| Purdue | L1–L2 (PLCs, RTUs, I/O) |
| Auth | **None** — no authentication, authorization, or encryption |
| Telemetry | Zeek `modbus.log` (+ICSNPP), NDR, pcap |

## What it is
The simplest and most widespread industrial protocol. A master reads and writes numbered data items (coils, discrete inputs, holding/input registers) on slave devices by **function code**. That simplicity is why it's everywhere — and why it has no security.

## What it really means for a defender
Modbus is the textbook unauthenticated protocol: **any host that can reach TCP/502 can read or write any register.** The good news for defenders is that Modbus makes the recon/impact split *explicit in the function code* — reads and writes are different codes, so you can alert on writes precisely. The whole detection strategy is: baseline which master(s) talk to which slaves, then alert on writes from anyone else, on diagnostic/identification functions (recon and disruption), and on any Modbus at all crossing a zone boundary.

## Attacker actions (recon → impact)
- **Discover:** probe TCP/502; read device identification (FC 43/0x2B) for vendor/product/version.
- **Read (recon):** enumerate registers/coils (FC 1–4) to map the process.
- **Write (impact):** change coils/registers (FC 5, 6, 15, 16) — flip an output, alter a setpoint value held in a register ("ShockPLC"-style manipulation).
- **Disrupt:** diagnostics (FC 8) sub-functions (e.g. restart comms, force listen-only mode).

## Detections you can build
| Detection | Signal / logic | Log source | ATT&CK ICS |
|-----------|----------------|------------|------------|
| Write from unauthorized source | Write FCs (5/6/15/16) from a host not in the master baseline | `modbus.log` | T0836 Modify Parameter, T0831 |
| Any write to a critical slave/register | Write to a safety/critical register range | `modbus.log` + tag map | T0836 |
| Device-ID reconnaissance | FC 43/0x2B from unexpected source | `modbus.log` | T0846, T0888 |
| Diagnostic abuse | FC 8 sub-functions (restart/listen-only) | `modbus.log` | T0814 Denial of Service |
| Function-code scan | Many distinct/invalid FCs or unit IDs from one source | `modbus.log` | T0846 |
| Cross-zone Modbus | Any TCP/502 crossing IT→OT boundary | firewall/NDR | T0885 Commonly Used Port |
| New Modbus master | First-time source issuing function codes | NDR + baseline | T0836 |

## Log sources & telemetry
Zeek `modbus.log` / ICSNPP gives function code, unit id, reference address, and quantity — enough for all of the above. NDRs alert on unauthorized writes natively. pcap confirms the exact register and value written (pair with historian to confirm impact).

## Functions/services to watch
**Reads (recon):** FC 1 (coils), 2 (discrete inputs), 3 (holding regs), 4 (input regs). **Writes (impact):** FC 5 (single coil), 6 (single reg), 15/0x0F (multi coils), 16/0x10 (multi regs). **Recon/disrupt:** FC 43/0x2B (device ID), FC 8 (diagnostics sub-functions).

## ATT&CK mapping
T0836 Modify Parameter · T0831 Manipulation of Control · T0846 Remote System Discovery · T0888 Remote System Information Discovery · T0814 Denial of Service · T0885 Commonly Used Port.
