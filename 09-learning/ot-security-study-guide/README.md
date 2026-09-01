# OT / ICS Security — Study Guide

**A single, deduplicated learning path across OT/ICS security — from foundations to threat hunting, detection, DFIR, and career.** Synthesized from two overlapping OT security training works into one clean chapter set with no repeated material.

![Chapters](https://img.shields.io/badge/chapters-31-blue)
![Parts](https://img.shields.io/badge/parts-7-brightgreen)
![Scope](https://img.shields.io/badge/scope-foundations%20%E2%86%92%20hunting%20%E2%86%92%20DFIR%20%E2%86%92%20career-lightgrey)
![Framework](https://img.shields.io/badge/aligned-Purdue%20%7C%20ATT%26CK%20for%20ICS%20%7C%20IEC%2062443-red)

---

## What this is (and how it was built)

Two source works were merged: an **OT & ICS Security learning book** (18 chapters, 7 parts) and an **OT Threat Hunting manual** (27 chapters, 6 parts), both by Ganesha T. They cover much of the same ground — Purdue model, protocols, ATT&CK for ICS, hunting methodology, detection engineering, DFIR — so a straight concatenation would repeat ~40% of the material.

This guide **deduplicates** them into **31 unique chapters across 7 parts**: where both sources cover a topic, the two treatments are merged into one chapter (foundations from the learning book, the hunter's practical angle from the manual). Each chapter here is written as an **original orientation/synthesis in this compiler's own words** — learning objectives, the key concepts, practitioner takeaways, and cross-references — not a reproduction of the source texts.

> **Attribution:** scope and structure are based on two OT security training works by *Ganesha T* (an OT/ICS learning book and an OT threat-hunting manual). This repository is an original study framework covering those topics; read the source works for their full treatment.

## How the two sources were merged (dedup map)

| Merged chapter (this guide) | From learning book | From hunting manual |
|-----------------------------|:------------------:|:-------------------:|
| 01 Why OT security is different | Ch 1 | Ch 1 |
| 02 ICS components: field devices, PLC, RTU | Ch 2, 3 | Ch 3 |
| 03 HMI, SCADA, DCS, historian, EWS, MES | Ch 4 | Ch 3 |
| 04 Safety systems (SIS) & the safety lifecycle | Ch 5 | Ch 3 |
| 05 Purdue model & OT networking | Ch 6 | Ch 2 |
| 06 Industrial protocols in depth | Ch 7 | Ch 4 |
| 07 Data flow, config, auth & logging | Ch 8 | — |
| 08 Passive visibility: TAP/SPAN/sensor placement | — | Ch 5 |
| 09 Telemetry, logs & data sources | Ch 8 | Ch 6 |
| 10 MITRE ATT&CK for ICS | Ch 10 | Ch 7 |
| 11 Adversary TTPs & the ICS kill chain | — | Ch 8 |
| 12 ICS malware deep dive | Ch 9 | Ch 9 |
| 13 Vulnerabilities, IOCs & IOAs | Ch 11 | Ch 10, 13 |
| 14 OT threat intelligence | — | Ch 11 |
| 15 Real-world case studies | Ch 9 | Ch 26 |
| 16 Threat-hunting methodology for OT | Ch 12 | Ch 12 |
| 17 OT indicators — process layer | Ch 11 | Ch 13 |
| 18 PCAP analysis with Wireshark | Ch 15 | Ch 14 |
| 19 Zeek for ICS | Ch 14 | Ch 15 |
| 20 Detection engineering (Sigma/YARA/KQL) | Ch 13 | Ch 16 |
| 21 Network & host detections (Suricata/Snort/Sysmon) | Ch 14 | Ch 16 |
| 22 Hunting on SIEM/XDR (Sentinel/Splunk/Elastic) | Ch 13 | Ch 17, 18 |
| 23 OT-native platforms (Nozomi/Claroty) | — | Ch 19 |
| 24 Hunting playbooks library | Ch 12 | Ch 20 |
| 25 OT incident response | Ch 15 | Ch 21 |
| 26 OT forensics / DFIR | Ch 15 | Ch 22 |
| 27 Hardening & IEC 62443 | Ch 16 | — |
| 28 Building & running an OT SOC | Ch 17 | Ch 6, 20 |
| 29 Home lab setup | Ch 18 | Ch 23 |
| 30 Hands-on labs & purple team | — | Ch 24, 25 |
| 31 Interview questions, career & glossary | Ch 18 | Ch 27 |

Overlapping chapters (marked in both columns) are where the dedup happened.

## The seven parts
1. **[Foundations](part-1-foundations/)** — what OT is, its components, safety systems, and the Purdue model (ch 01–05).
2. **[Protocols, visibility & telemetry](part-2-protocols-visibility/)** — industrial protocols and how to see them (ch 06–09).
3. **[The adversary](part-3-adversary/)** — ATT&CK for ICS, TTPs, malware, vulns, intel, case studies (ch 10–15).
4. **[Hunting & detection](part-4-hunting-detection/)** — methodology, indicators, PCAP, Zeek, detection engineering, platforms, playbooks (ch 16–24).
5. **[Response & forensics](part-5-response-forensics/)** — OT IR and DFIR (ch 25–26).
6. **[Defence & hardening](part-6-defence-hardening/)** — IEC 62443 and building an OT SOC (ch 27–28).
7. **[Practice & career](part-7-practice-career/)** — home lab, labs, purple team, interview & glossary (ch 29–31).

## Chapter format
Each chapter is a concise brief: **learning objectives · key concepts · practitioner takeaways · cross-references** (to related chapters and, where relevant, to companion detection repos). It's a study/reference scaffold — original, deduplicated, and skimmable — not a textbook reproduction.

## License
MIT for the original synthesis text in this repo (see [`LICENSE`](LICENSE)). The underlying source works remain the property of their author.
