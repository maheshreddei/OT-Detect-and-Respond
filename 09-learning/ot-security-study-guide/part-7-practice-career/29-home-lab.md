# Chapter 29 — Home Lab Setup

> Part VII · Practice & Career. Skill in OT security is built by doing, and doing safely means a lab. This chapter is how to build an isolated environment where you can practice every technique in this guide — and validate detections — without risking any real plant.

## 29.1 Rule one: isolation

The first and non-negotiable rule of an OT lab is **isolation**. Use host-only or internal virtual networks with **no bridge to production, the corporate network, or the internet** — especially for any attacker tooling. An OT lab generates real protocol traffic and runs offensive tools; it must never be able to touch anything real. Build the isolation before you build anything else.

## 29.2 The process and control side

Recreate a small slice of a plant:

- **Soft PLC** — **OpenPLC** runs real control logic and speaks Modbus, DNP3, and EtherNet/IP; it's the workhorse of an OT lab.
- **ICS honeypot / device simulator** — **Conpot** simulates devices across several protocols (Modbus, S7comm, BACnet, IEC-104) and is great for generating varied traffic.
- **HMI/SCADA** — **ScadaBR**, **FUXA**, or **Rapid SCADA** give you an operator interface and a supervisory layer.
- **Protocol simulators** — `pymodbus`, `python-snap7` (S7), and similar libraries let you script masters, slaves, reads, and writes.
- **Process/physics simulation** — **GRFICS** provides a full virtual chemical plant with simulated physics, PLCs, and an HMI; **Node-RED** can build lighter custom processes.

## 29.3 The monitoring side

Stand up the defensive stack against a mirror of the lab network:

- **Passive sensor** — **Zeek + ICSNPP** on a mirror/SPAN, producing the per-protocol logs you learned in Chapter 19.
- **SIEM** — **Wazuh**, **OpenSearch**, or **Security Onion** to receive logs, run detections, and hunt.
- Optionally an **OT-native platform trial** (Nozomi/Claroty/Dragos where available) to compare with the open-source pipeline.

This gives you the full chain — traffic → Zeek → SIEM → detection — to develop and test rules against.

## 29.4 The attacker side

- A **Kali Linux** VM with OT tooling — Nmap NSE ICS scripts, Metasploit modules, protocol clients, and the Industrial Exploitation Framework — **isolated, for authorized lab use only.**

With attacker, process, and monitoring in one isolated environment you can run an entire scenario: scan → find a controller → issue an unauthorized write or program download → and watch your Zeek/SIEM detections fire (or discover they don't, and fix them).

## 29.5 Docker-first, reproducible

Build the lab with **Docker/compose** so it is reproducible and disposable — you can tear down and rebuild a clean environment in minutes, snapshot known-good states, and share the setup. A reproducible lab lowers the friction of practice, which is the whole point.

## 29.6 What the lab is for

The lab is where you: learn to read industrial traffic, practice hunts safely, **validate detections** before they go near production, and rehearse incident scenarios. It is also the **lighthouse/pilot** environment for demonstrating capability (Chapter 28) and the safe venue for the purple-team exercises of Chapter 30 and the Threat Detection Assurance cases.

## Chapter summary
- **Isolation first** — host-only/internal networks, no bridge to anything real, especially for attacker tooling.
- Process side: **OpenPLC, Conpot, ScadaBR/FUXA, protocol sims, GRFICS.**
- Monitoring side: **Zeek+ICSNPP → Wazuh/OpenSearch/Security Onion.**
- Attacker side: **isolated Kali** with OT tooling.
- Build **Docker-first** for reproducibility; use the lab to learn, validate detections, and rehearse.

## Cross-references
- Chapter 08/19 (capture and Zeek), Chapter 30 (labs and purple team run here), Chapter 20 (validate detections).
- Companion: an open-source OT lab pairs with `threat-detection-assurance` for safe validation.
