# Chapter 21 — Network and Host Detections: Suricata, Snort, Sysmon

> Part IV. Complementing log-based rules with signature IDS on the wire and rich host telemetry on the Windows OT machines. Network catches the wire; the host catches the keyboard — OT intrusions usually touch both.

## 21.1 Suricata and Snort — signature IDS on the wire

**Suricata** and **Snort** are signature-based intrusion detection engines you run on the OT capture. They match known-bad patterns in traffic and have some ICS coverage (Modbus, DNP3, EtherNet/IP rulesets exist). Their strengths and limits:

- **Strength:** fast, precise detection of well-defined patterns — a specific exploit, a known-bad command, a protocol violation.
- **Limit:** signature-bound — blind to novel activity, and noisy if rules aren't tuned to the environment.
- **In OT:** useful for known malware/exploit patterns and some protocol misuse, but tune hard against the baseline, and pair with behavioral logic (Zeek scripts, allow-list deviations) for the unknown.

Where a detection is behavioral rather than a fixed pattern (a *new* conversation, a rate anomaly), express it in **Zeek scripting** rather than forcing it into a signature.

## 21.2 Sysmon — the host view on Windows OT machines

You cannot put an agent on a PLC, but you can — and should — instrument the Windows **EWS, HMI, historian, and jump host** with **Sysmon** (plus native Windows Security logs). The high-value Sysmon events for OT:

| Event | What it catches |
|-------|-----------------|
| 1 — Process creation (with command line) | LOLBins, encoded PowerShell, engineering-tool launches — needs command line enabled |
| 3 — Network connection | A host reaching a controller it shouldn't; C2 |
| 7 — Image load | Malicious DLLs loaded into engineering software |
| 8 / 10 — Remote thread / process access | Credential access (LSASS), injection |
| 11/13 — File / registry | Persistence (run keys), dropped tools |

This is the coverage for the **IT/engineering path** — the encoded PowerShell, the LOLBin, the persistence, the credential access that precede an OT action. It's the same host detection discipline as enterprise, applied to the OT-adjacent Windows estate.

## 21.3 Placement and correlation

- **Network detections** on the sensor (Suricata/Zeek), seeing the OT segments.
- **Host detections** on the Windows OT hosts (Sysmon + Windows Security).
- **Correlate the two.** The high-confidence OT incident is usually a *combination*: a VNC/RDP session into the EWS (network + auth) **and** an engineering-tool launch or program transfer (host + network) **and** a process move (historian). Any one alone may be benign; together they're an incident. Build correlation rules that join network, host, and process on the same asset and time window.

## Chapter summary
- **Suricata/Snort** give fast signature IDS on the wire (some ICS rulesets); tune hard, and use **Zeek scripting** for behavioral logic.
- **Sysmon + Windows Security** on EWS/HMI/historian/jump host cover the **IT/engineering path** (process, network, injection, persistence) — the part you *can* agent.
- **Correlate network + host + process** on the same asset — that combination is the high-confidence OT incident.

## Cross-references
- Chapter 19 (Zeek) and Chapter 20 (rules); Chapter 22 (correlate in the SIEM); Chapter 11 (the IT path these catch).
- Companion: `perimeter-to-endpoint-detections` (host and network detection library).
