# NIST Supplements and IT/OT Standards Stack

## Primary NIST supplements

| Resource | Use |
|---|---|
| NIST CSF 2.0 Core | Outcome taxonomy for governance and communication |
| CSF Implementation Examples | Possible actions for Subcategory outcomes; not mandatory controls |
| CSF Informative References | Mappings to other standards and guidance |
| CSF Organizational Profile template | Compare Current and Target outcomes |
| CSF Tiers guide | Characterize rigor of governance and risk-management practices |
| NIST SP 800-82 Rev. 3 | Apply cybersecurity to OT while respecting safety, reliability and performance |
| NIST SP 800-53 Rev. 5 | Detailed security/privacy control catalog |
| NIST SP 800-53B | Control baselines and tailoring approach |
| NIST SP 800-37 | Risk Management Framework lifecycle |
| NIST SP 800-30 | Risk-assessment guidance |
| NIST SP 800-61 | Incident-response guidance |
| NIST SP 800-92 | Log-management guidance |
| NIST SP 800-40 | Enterprise patch-management planning |
| NIST SP 800-161 | Cybersecurity supply-chain risk management |
| NIST SP 800-207 | Zero Trust Architecture; carefully adapt to OT |
| NIST SP 800-160 | Systems-security engineering |

Verify current revision/status in the NIST catalog before a formal project.

## OT companion standards

| Standard/framework | Relationship |
|---|---|
| IEC 62443-2-1 | Asset-owner IACS security-program requirements |
| IEC 62443-2-4 | Service-provider security requirements |
| IEC 62443-3-2 | Zone/conduit risk assessment and target security levels |
| IEC 62443-3-3 | System requirements and capability security levels |
| IEC 62443-4-1 | Secure product-development lifecycle |
| IEC 62443-4-2 | Component technical security requirements |
| ISO/IEC 27001 | Organization-wide ISMS requirements |
| ISO 22301 | Business continuity management |
| IEC 61511 | Functional safety lifecycle for process industries |
| MITRE ATT&CK for ICS | Adversary-behavior knowledge for detections/hunts |
| CISA ICS guidance | Defensive practices and advisories |

Functional safety and cybersecurity interact, but security personnel must not reinterpret or modify safety requirements without competent safety engineering authority.

## Practical integration

~~~text
Business and process risk
        ↓
NIST CSF Current / Target Profile
        ↓
NIST SP 800-82 OT constraints and architecture
        ↓
IEC 62443 zones, conduits, SL-T and SR/RE selection
        ↓
SP 800-53 / vendor controls / procedures
        ↓
Implementation and safe verification
        ↓
Evidence, SL-A/current profile, metrics and improvement
~~~

## Common mistakes

- Treating CSF as a checklist or certification standard.
- Claiming a Function is “complete” from one tool.
- Applying IT controls to PLC/SIS assets without operational validation.
- Giving the whole plant one maturity or security number.
- Confusing CSF Tiers with IEC 62443 Security Levels.
- Copying a crosswalk as proof of implementation.
- Using product capability instead of configured, tested evidence.
- Ignoring safety, environmental and production consequences.
- Excluding third-party integrators and OEM support from governance.
- Failing to monitor the monitoring system itself.
