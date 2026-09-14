# NIST Cybersecurity Framework 2.0 for IT and OT

This package explains how to use NIST CSF 2.0 across enterprise IT and operational technology, with special attention to DCS, PLC, SIS, SCADA, industrial networks and plant operations.

## Core idea

NIST CSF defines **cybersecurity outcomes**. It does not prescribe a single product or control implementation. Use it to communicate and prioritize risk; use supporting publications and standards to engineer the controls.

~~~text
                    GOVERN
          policy • risk • roles • supply chain
                       ↓
IDENTIFY → PROTECT → DETECT → RESPOND → RECOVER
 assets     controls   events    action     restoration
 context    access     analysis  comms      improvement
~~~

The Functions operate concurrently. Govern informs the other five.

## Deliverables

- [IT and OT implementation guide](01-it-ot-implementation-guide.md)
- [NIST supplements and standards stack](02-supplements-and-crosswalks.md)
- [Petrochemical OT profile guidance](03-petrochemical-ot-profile.md)
- [Category-level assessment register](csf-category-assessment.csv)

## CSF 2.0 structure

| Function | Categories | Purpose |
|---|---:|---|
| Govern (GV) | 6 | Establish context, strategy, policy, accountability, oversight and supply-chain risk |
| Identify (ID) | 3 | Understand assets, risks and improvement opportunities |
| Protect (PR) | 5 | Apply safeguards for identity, people, data, platforms and infrastructure |
| Detect (DE) | 2 | Monitor and analyze possible adverse events |
| Respond (RS) | 4 | Manage, analyze, communicate and mitigate incidents |
| Recover (RC) | 2 | Restore capabilities and communicate recovery |
| **Total** | **22** | Category-level structure |

The official Core continues below Categories into Subcategories. Implementation Examples and Informative References supplement the Core but are not themselves mandatory Core outcomes.

## How to use this package

1. Define organizational and OT operating context.
2. Select applicable CSF outcomes.
3. Build a **Current Profile** based on evidence.
4. Build a **Target Profile** based on risk and business needs.
5. Select a CSF Tier to describe the rigor of governance and risk management.
6. Prioritize gaps by safety, environmental, production, regulatory and cyber consequence.
7. Use NIST SP 800-82, SP 800-53 and IEC 62443 to design implementation.
8. Assign owners, milestones, metrics and evidence.
9. Validate controls through safe testing.
10. Update the Profile after changes, incidents and exercises.

## Important distinction

- **CSF:** what outcomes the organization wants.
- **SP 800-82:** how to adapt security for OT safety, reliability and performance.
- **SP 800-53:** detailed security/privacy control catalog.
- **IEC 62443:** lifecycle, zones/conduits, security levels and IACS-specific requirements.
- **Nozomi/SIEM/EDR/firewalls:** technologies that may support some outcomes.
- **Audit evidence:** proof that the selected outcome is implemented and effective.

## Authoritative sources

- [NIST CSF 2.0](https://doi.org/10.6028/NIST.CSWP.29)
- [NIST SP 800-82 Rev. 3](https://doi.org/10.6028/NIST.SP.800-82r3)
- [NIST CSF Profiles](https://www.nist.gov/cyberframework/profiles)
- [NIST CSF Quick-Start Guides](https://www.nist.gov/cyberframework/quick-start-guides)
- [NIST CSF Informative References](https://www.nist.gov/cyberframework/informative-references)

Use the official NIST Reference Tool for the complete current Core, Implementation Examples and machine-readable exports.
