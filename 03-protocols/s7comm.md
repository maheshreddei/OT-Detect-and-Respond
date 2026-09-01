# S7comm (Siemens S7)

## Snapshot
| Property | Value |
|----------|-------|
| Port/transport | TCP/102 (TPKT/COTP); S7comm-Plus on newer CPUs |
| Purdue | L1–L2 (Siemens S7-300/400/1200/1500) |
| Auth | Legacy S7comm none; S7comm-Plus adds integrity/anti-replay (still bypass-researched) |
| Telemetry | Zeek `s7comm.log` (ICSNPP), NDR, pcap |

## What it is
The proprietary Siemens protocol used by STEP 7 / TIA Portal to talk to S7 PLCs — reading and writing variables, and performing **engineering actions**: start/stop the CPU, and upload/download program blocks. It's the protocol behind the most consequential Siemens attacks.

## What it really means for a defender
S7comm carries the operations that *change the controller itself*, not just its data: **STOP the CPU, and download logic.** Those are the crown-jewel events — a program download or a CPU STOP from anything other than the sanctioned engineering workstation is close to a true-positive incident. Reads of the system status list (SZL) are the reconnaissance that precedes them. The defensive priority is unambiguous: baseline the one/few engineering stations, and alarm hard on PLC-control and program-transfer functions from anywhere else.

## Attacker actions (recon → impact)
- **Discover/recon:** connect on TCP/102; read SZL / system info (CPU type, firmware) — device fingerprinting.
- **Read (recon):** read variables/data blocks to understand the process.
- **Write (impact):** write variables/data blocks — manipulate values.
- **Control (high impact):** PLC STOP / START (loss of control).
- **Program (max impact):** upload (steal logic) or **download** (replace logic) program blocks — the Stuxnet class.

## Detections you can build
| Detection | Signal / logic | Log source | ATT&CK ICS |
|-----------|----------------|------------|------------|
| PLC STOP/START | S7 PLC-control function from any source | `s7comm.log` | T0813 Denial of Control, T0800 |
| Program download | Block download (PLC program transfer) | `s7comm.log` | T0843 Program Download |
| Program upload | Block upload (logic theft) | `s7comm.log` | T0845 Program Upload |
| Write from non-engineering source | Write-var function from a host outside the EWS baseline | `s7comm.log` | T0836 Modify Parameter |
| SZL / system recon | Read SZL / system-status from unexpected source | `s7comm.log` | T0888 Remote System Information Discovery |
| New S7 client | First-time source speaking S7comm to a PLC | NDR + baseline | T0843 |
| Cross-zone S7 | TCP/102 crossing IT→OT boundary | firewall/NDR | T0885 |

## Log sources & telemetry
Zeek `s7comm.log` / ICSNPP exposes ROSCTR (job/ack/userdata), function, and subfunction — enough to distinguish read/write/control/upload/download. NDRs ship S7-specific policies (STOP, download) — enable them. Pair a download/STOP alert with the controller diagnostic buffer (records mode changes/downloads) and the historian (process impact).

## Functions/services to watch
**Recon:** SZL/system-status reads, setup communication. **Read/Write:** read var / write var (data blocks, memory areas). **Control:** PLC STOP / START / restart. **Program transfer:** block download / upload. (S7comm-Plus obfuscates some of this — rely on NDR parsers that decode it.)

## ATT&CK mapping
T0843 Program Download · T0845 Program Upload · T0813 Denial of Control · T0836 Modify Parameter · T0888 Remote System Information Discovery · T0885 Commonly Used Port.
