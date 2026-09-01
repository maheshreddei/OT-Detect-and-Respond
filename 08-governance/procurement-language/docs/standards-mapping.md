# Standards Mapping

The source document (2009) predates most of the current OT-security standards landscape. This mapping bridges its 12 control categories to the frameworks a modern program actually works in, so procurement requirements trace cleanly to your control catalog. **Mappings are for orientation — they're approximate and category-level, not a certified crosswalk.**

Frameworks referenced:
- **NIST SP 800-82 Rev 3** — Guide to OT Security
- **IEC 62443-3-3** — System security requirements (SR families) · **-4-2** — component requirements · **-4-1** — secure product development · **-2-3** — patch management
- **NIST CSF 2.0** — Functions/Categories (GV, ID, PR, DE, RS, RC)

| # | Procurement category | IEC 62443 (primary) | NIST CSF 2.0 | Notes / 800-82r3 area |
|---|----------------------|---------------------|--------------|------------------------|
| 2 | System Hardening | 3-3 SR 7.6 (network & security config), SR 2.4; 4-2 CR 7.6 | PR.PS (Platform Security) | Least functionality; secure baseline config |
| 3 | Perimeter Protection | 3-3 SR 5.1/5.2 (segmentation), SR 6.2 | PR.IR, DE.CM | Boundary protection; IDS at the perimeter |
| 4 | Account Management | 3-3 SR 1.1–1.9 (Identification & Authentication Control), SR 2.1 (authorization enforcement) | PR.AA (Identity, Authentication & Access Control) | RBAC, session mgmt, password/auth policy, auditing |
| 5 | Coding Practices | **4-1** (Secure Development Lifecycle) | PR.PS | Secure coding is a product-development requirement |
| 6 | Flaw Remediation | **2-3** (patch management), 4-1 DM/SUM (defect & update mgmt) | ID.RA, PR.PS, RS.MA | Vendor vuln notification & problem reporting |
| 7 | Malware Detection & Protection | 3-3 SR 3.2 (malicious code protection) | DE.CM, PR.PS | Anti-malware suited to OT constraints |
| 8 | Host Name Resolution | 3-3 SR 5.x (network integrity/segmentation) | PR.IR | Addressing & name-resolution security |
| 9 | End Devices | **4-2** component requirements (embedded/host/network device CRs) | PR.PS, PR.AA | IEDs, RTUs, PLCs, sensors/actuators/meters |
| 10 | Remote Access | 3-3 SR 1.13 (access via untrusted networks), SR 2.6 (remote session termination) | PR.AA, PR.IR | Modems, TCP/IP, web UIs, VPNs, serial |
| 11 | Physical Security | 2-1 (program); 800-53 PE family | PR.AA, ID.AM, PR.IR | Physical access to cyber components, manual override |
| 12 | Network Partitioning | 3-3 SR 5.1/5.2 (**zones & conduits** — core concept) | PR.IR | The zone/conduit model at the heart of 62443 |
| 13 | Wireless Technologies | 3-3 SR 1.6 (wireless access mgmt), SR 2.2 (wireless use control) | PR.AA, PR.IR | Bluetooth, Wi-Fi, ZigBee, WirelessHART, cellular, etc. |

## How to use this mapping

- **Traceability:** when you pull a control's *Procurement Language* into an RFP, tag it with the mapped 62443 SR / CSF category so procurement requirements roll up to your master control catalog and audit scope.
- **Modernization:** where the 2009 wording has dated (wireless specifics especially), treat the mapped 62443/800-82r3 clause as the authoritative current requirement and use the procurement text as the contract-language starting point.
- **Gap-check:** the 62443 SR families (SR 1–7: identification/authentication, use control, system integrity, data confidentiality, restricted data flow, timely response to events, resource availability) are a good completeness lens — if a procurement omits a whole SR family, that's a gap the 2009 catalog may not surface on its own.

## The one concept to carry forward
**Network Partitioning (category 12) is the seed of IEC 62443's zones-and-conduits model** — the single most important architectural idea in OT security. If you adopt only one thing from this document at the architecture level, make it rigorous segmentation into security zones connected by controlled conduits, specified in the procurement so the delivered system is segmentable by design rather than flat.
