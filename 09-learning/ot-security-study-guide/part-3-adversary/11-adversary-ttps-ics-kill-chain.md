# Chapter 11 — Adversary TTPs and the ICS Kill Chain

> Part III. This chapter shows how an industrial intrusion actually unfolds, stage by stage, and where your best detection opportunities sit within it.

## 11.1 The two-stage ICS kill chain

Industrial attacks that reach physical impact almost always happen in **two stages**:

**Stage 1 — the IT-style intrusion.** Reconnaissance → initial access → foothold → privilege escalation → internal movement toward the OT boundary. This stage looks like a normal enterprise intrusion and is detectable with enterprise telemetry and techniques.

**Stage 2 — the ICS attack.** Develop an ICS capability → test it → deliver it into the control network → execute the physical effect. This stage requires the attacker to understand the specific process and speak its protocols.

The crucial insight for a defender is the **gap between the stages**. Building and testing an ICS capability, learning the process, and staging tools takes time — often weeks or months. That dwell time is your best window: catch Stage 1 in IT/boundary telemetry and you usually never have to catch Stage 2 at the controller. But instrument both, because you will not always be early.

## 11.2 The common initial-access vectors

Across real incidents, OT is entered through a small, repeating set of doors:

1. **Remote access / vendor connections.** VPNs without MFA, remote-access appliances with weak or shared credentials — the single most common vector.
2. **IT-to-OT pivot.** Phishing → corporate foothold → credential theft → the jump host into OT. The enterprise breach is the on-ramp.
3. **Internet-exposed OT.** HMIs, PLCs, and gateways directly reachable from the internet, often at small, unmanned remote sites.
4. **Supply chain.** Trojanized installers or updates from an ICS vendor's own distribution (the Havex pattern).
5. **Removable media.** USB carried across the air gap — still effective in isolated plants.
6. **Insider / contractor misuse.** Legitimate access used improperly.
7. **Wireless and physical.** A rogue AP, an unmonitored network jack in an unlocked cabinet, or a radio link.

Notice that the top vectors are about **access, not exploits** — which is why remote-access monitoring, boundary logging, and internet-exposure hunts pay off more than chasing CVEs.

## 11.3 Living off the land in OT

Once inside — especially on an EWS — sophisticated attackers use the **legitimate engineering software** to act on controllers. There is no malware to find; the "tool" is the vendor's own programming environment, and the malicious download looks like an engineering download. Detection therefore shifts from *what* (there's no unusual binary) to **who, when, and from where**: an engineering action from an unexpected host, outside a change window, from an unusual account or source. This is why the command/account/software allow-lists (Chapter 09) matter so much.

## 11.4 Mapping TTPs to your telemetry

For each stage and vector, know what it would look like in your data:

| Stage / vector | Telemetry that catches it |
|----------------|---------------------------|
| IT pivot / credential theft | Enterprise EDR, identity/auth logs, boundary firewall |
| Remote-access abuse | VPN/jump-host auth, new source into OT |
| Internet-exposed OT | Perimeter NetFlow, inbound to HMI/PLC from non-RFC1918 |
| ICS capability delivery | Passive protocol monitoring (program transfer, new writer) |
| Physical execution | Historian (process/setpoint/trip), command-vs-feedback |

## Chapter summary
- Industrial attacks unfold in **two stages** (IT intrusion → ICS attack); the **gap between them** is your best detection window.
- Initial access is dominated by **remote access, the IT pivot, and internet exposure** — access, not exploits.
- Advanced attackers **live off the land** with legitimate engineering tools; detect on **who/when/from where**, not on malware.
- Map every stage and vector to the telemetry that catches it.

## Cross-references
- Chapter 10 (ATT&CK) supplies the technique vocabulary; Chapter 12 (malware) is these TTPs realized in code; Chapter 15 (case studies) shows them end to end.
- Companion: `perimeter-to-endpoint-detections` (Stage-1 coverage), `ot-protocol-defense` (Stage-2).
