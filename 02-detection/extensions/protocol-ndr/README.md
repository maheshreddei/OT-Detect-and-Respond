# OT/ICS Protocol Defender's Guide

**What each industrial protocol really means for a defender, the detections you can build against it, and the log sources that feed them.**

![Protocols](https://img.shields.io/badge/protocols-13-blue)
![Focus](https://img.shields.io/badge/focus-blue%20team%20%2F%20detection-brightgreen)
![Telemetry](https://img.shields.io/badge/telemetry-Zeek%2FICSNPP%20%7C%20Nozomi%20%7C%20pcap-orange)
![Framework](https://img.shields.io/badge/mapped-MITRE%20ATT%26CK%20for%20ICS-red)
![License](https://img.shields.io/badge/license-MIT-green)

---

## The one idea to internalize first

Most OT protocols were designed for **trusted, isolated networks** — so they have **no authentication, no authorization, and no encryption.** A device answers whoever asks. That single fact reshapes how you defend them:

> **On an unauthenticated control protocol, a read is reconnaissance and a write is process manipulation.** There is no "unauthorized" flag in the protocol itself — the wire treats an attacker's write to a command point exactly like an engineer's. Your detection layer *is* the authorization layer the protocol never had.

So defending these protocols is less about "malformed packets" and more about answering: **who is talking to what, is that pair allowed, and is this a read (recon) or a write/command (impact)?** Almost every detection in this guide is a variation of that question.

The training range this guide is built around exposes the attacker side of exactly that model — enumerate/browse/read, then write to a "command" point (IOA, tag, node, topic, object) that manipulates the PLC. This guide is the **defender's mirror** of those actions.

## The protocols

Two families, one defensive logic.

**IT/access protocols** (how attackers reach and pivot in OT):

| Protocol | What it is here | Defender's headline |
|----------|-----------------|---------------------|
| [Nmap / scanning](protocols/nmap-scanning.md) | Host & port discovery | Active scanning in OT is itself abnormal and risky — a strong early signal |
| [HTTP](protocols/http.md) | Web UIs (e.g. OpenPLC), fingerprinting, brute force | Web login brute force + directory enum against OT web UIs |
| [VNC](protocols/vnc.md) | Remote desktop to an EWS/HMI | Hands-on-keyboard control of engineering hosts |
| [FTP](protocols/ftp.md) | File transfer, firmware/logic staging | Anonymous access + brute force + firmware/project movement |

**OT/control protocols** (read = recon, write = impact):

| Protocol | Transport | Defender's headline |
|----------|-----------|---------------------|
| [Modbus](protocols/modbus.md) | TCP/502 | Function codes split cleanly into read (recon) vs write (impact) |
| [S7comm](protocols/s7comm.md) | TCP/102 | STOP/START and program up/download against Siemens PLCs |
| [IEC 60870-5-104](protocols/iec104.md) | TCP/2404 | Command ASDUs (C_SC/C_DC/C_SE) = operate; monitor = recon |
| [DNP3](protocols/dnp3.md) | TCP/20000 | Operate/CROB to outstations; unsolicited responses |
| [MQTT](protocols/mqtt.md) | TCP/1883 | Publish to command topics; wildcard subscribe = mass recon |
| [OPC UA](protocols/opcua.md) | TCP/4840 | Anonymous sessions, Browse (recon), Write to command nodes |
| [EtherNet/IP + CIP](protocols/ethernet-ip-cip.md) | TCP+UDP/44818,2222 | CIP tag enumeration and writes; forward-open |
| [IEC 61850](protocols/iec61850.md) | TCP/102 (MMS), GOOSE/SV L2 | MMS control writes; GOOSE spoofing on the LAN |
| [BACnet/IP](protocols/bacnet.md) | UDP/47808 | Who-Is sweeps (recon); WriteProperty to command objects |

## How the guide is organized

```
ot-protocol-defense/
├── docs/
│   ├── attack-surface-model.md   ← the recon→command model + Purdue placement (read this second)
│   ├── log-sources.md            ← master telemetry guide: what sees what, per protocol
│   └── how-to-use.md             ← turning this into deployed detections
├── protocols/                    ← one file per protocol, same template
│   └── README.md                 ← index
├── detections/
│   ├── detection-catalog.csv     ← every detection, machine-readable
│   └── README.md
└── nozomi-queries/               ← the detections as Nozomi (N2QL) assertions
    ├── assertion-queries.md      ← ready-to-deploy Guardian/CMC queries
    ├── n2ql-reference.md
    └── queries-catalog.csv
```

Each protocol file follows the same template: **Snapshot · What it is · What it really means for a defender · Attacker actions (recon→impact) · Detections you can build · Log sources & telemetry · Functions/services to watch · ATT&CK mapping.**

## Where the detections live
Every detection idea across all protocols is collected in [`detections/detection-catalog.csv`](detections/detection-catalog.csv) (name, protocol, logic, log source, ATT&CK ICS) so you can turn it straight into an implementation backlog. The log-source strategy that feeds them is in [`docs/log-sources.md`](docs/log-sources.md).

## Deploy them natively in Nozomi
[`nozomi-queries/`](nozomi-queries/) translates the catalog into **N2QL assertion queries** for Nozomi Guardian/CMC — each written so that it returns rows only for the disallowed case, so the assertion rule is simply "non-empty ⇒ alert." Start with [`nozomi-queries/assertion-queries.md`](nozomi-queries/assertion-queries.md); syntax reference is in [`nozomi-queries/n2ql-reference.md`](nozomi-queries/n2ql-reference.md).

## Scope & intent
This is **defensive** documentation — detection engineering and telemetry, written from the wire-observable behaviour a defender sees. It deliberately does not include exploit payloads or attack tooling; it describes what attacker actions *look like* so you can detect them.

## Author
Mahesh Reddy — OT/ICS Security · GICSP, SANS ICS410, Nozomi Certified

## License
MIT — see [`LICENSE`](LICENSE).

> Ports, function codes, and services listed are protocol defaults; confirm against your environment. Detection thresholds are starting points to tune per site.
