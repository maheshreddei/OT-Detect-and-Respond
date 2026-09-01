# OT Security Portfolio

**Building, running, and defending an OT/ICS Security Operations Centre — end to end.** This is the index to a body of work spanning strategy, deployment, detection engineering (protocol, physics, safety, and IT), incident response, and procurement.

![Repos](https://img.shields.io/badge/repositories-9-blue)
![Framework](https://img.shields.io/badge/mapped-MITRE%20ATT%26CK%20for%20ICS-red)
![Standards](https://img.shields.io/badge/aligned-IEC%2062443%20%7C%20NIST%20800--82r3%20%7C%20NIST%20CSF%202.0-lightgrey)
![License](https://img.shields.io/badge/license-MIT-green)

---

## The journey, start to end

The repositories aren't standalone — each is a **deliverable in a phase** of an OT SOC program. This is the map from content to real delivery.

```mermaid
flowchart TD
    S["1 · Strategy &amp; plan<br/><i>ot-soc-delivery-playbook</i><br/>business case · prerequisites · proposal"]
    A["2 · Assess &amp; design<br/><i>ot-monitoring-deployment · ics-procurement-language</i><br/>docs · risk · architecture · log plan"]
    D["3 · Deploy<br/><i>ot-monitoring-deployment</i><br/>passive sensors · SIEM · tiered log onboarding"]
    DET["4 · Detect<br/><i>ot-protocol-defense · ot-historian-detection ·<br/>ot-detection-engineering · sis-safety-detection ·<br/>perimeter-to-endpoint-detections</i><br/>protocol · physics · safety · IT"]
    R["5 · Respond<br/><i>it-ot-incident-response</i><br/>IR plan · SOPs · evidence · playbooks"]
    RUN["6 · Run &amp; improve<br/>monitor · KPIs/SLAs · threat hunting · detection lifecycle"]

    S --> A --> D --> DET --> R --> RUN
    RUN -. continuous improvement .-> DET

    classDef plan fill:#F1EFE8,stroke:#5F5E5A,color:#2C2C2A;
    classDef build fill:#E6F1FB,stroke:#185FA5,color:#042C53;
    classDef detect fill:#E1F5EE,stroke:#0F6E56,color:#04342C;
    classDef respond fill:#FAECE7,stroke:#993C1D,color:#4A1B0C;
    class S,RUN plan;
    class A,D build;
    class DET detect;
    class R respond;
```

*Legend: gray = plan · blue = build · teal = detect · coral = respond.*

> If the diagram above doesn't render, see [`assets/journey-map.svg`](assets/journey-map.svg).

## The repositories

| # | Repository | Phase | One-line pitch |
|---|-----------|-------|----------------|
| 1 | **ot-soc-delivery-playbook** | Strategy | Where to start, the business case, prerequisites, and how to build & price an OT SOC proposal — the delivery method that ties it all together. |
| 2 | **ot-monitoring-deployment** | Assess / Design / Deploy | The documents to gather before deploying OT monitoring, and the tiered order to onboard log sources after. |
| 3 | **ics-procurement-language** | Assess | The DHS OT procurement-language reference, made browsable — 47 controls to put security into RFPs and contracts. |
| 4 | **ot-protocol-defense** | Detect | What 13 industrial protocols mean for a defender, 54 detections, and Nozomi (N2QL) assertion queries. |
| 5 | **ot-historian-detection** | Detect | Baseline-and-deviation detection on the process historian — the physics layer that catches Stuxnet/TRITON-class manipulation. |
| 6 | **ot-detection-engineering** | Detect | 87 Sigma rules across protocol, IT→OT cross-zone, and threat-actor detection. |
| 7 | **sis-safety-detection** | Detect | Safety-system (SIS) monitoring grounded in IEC 61511 — the TRITON/TRISIS-class coverage most SOCs lack. |
| 8 | **perimeter-to-endpoint-detections** | Detect | 62 enterprise detections across the external-facing kill chain (network, identity, endpoint, east-west, DNS, scanning, prohibited traffic). |
| 9 | **it-ot-incident-response** | Respond | An OT-adapted IR plan, investigation SOPs, and an evidence layer that maps *what you need to prove* to *where the artifact lives*. |

## How they compose into a service

| Tier | Includes |
|------|----------|
| **Essential** | Visibility + boundary/remote-access detection + IR readiness |
| **Advanced** | + full protocol & Sigma detection + physics layer |
| **Safety-critical** | + SIS monitoring + IT perimeter + threat hunting |

Full mapping: `ot-soc-delivery-playbook/06-portfolio-map.md`.

## Through-line
Everything here is **defensive, read-only, and safety-first** — mapped to MITRE ATT&CK for ICS and aligned to IEC 62443, NIST SP 800-82r3, and NIST CSF 2.0. The consistent idea: detection in OT has to see the *process*, not just the packets.

## Author
Mahesh Reddy — OT/ICS Security · GICSP, SANS ICS410, Nozomi Certified

## License
MIT — see [`LICENSE`](LICENSE).
