# 6. Flaw Remediation

> Control category from *Cyber Security Procurement Language for Control Systems* (DHS/ICS-CERT, Sept 2009). Each control follows the 8-part topical template. See [`../docs/topical-template.md`](../docs/topical-template.md).


## 6.1 Notification and Documentation from Vendor

Flaw remediation is a process by which flaws are documented and tracked for completion of
corrective actions.


### Basis

Vulnerabilities exist in control systems when flaws in software and/or hardware configurations are
not patched. Many times intended patches are not applied in a timely manner due to operational issues. In
many instances, workarounds and temporary fixes may become permanent solutions; however, the
vulnerabilities may be reintroduced with future updates, upgrades, patches, and fixes.


### Language Guidance

Awareness of application vulnerabilities, particularly security-related flaws, is needed in a timely
fashion. Guidance about corrective actions, fixes, or monitoring is needed to mitigate all vulnerabilities
associated with the flaw. Auditable history of flaws and remediation steps are required to roll back
patches. Vulnerabilities and flaws are normally closely held until remediation becomes available.
However, some vulnerabilities are made public before a fix has been developed and then it becomes
urgent to mitigate these vulnerabilities.


### Procurement Language

The Vendor shall have and provide documentation of a written flaw remediation process.

The Vendor shall provide appropriate software updates and/or workarounds to mitigate all
vulnerabilities associated with the flaw within a pre-negotiated period.

Post-contract award, after the Vendor is made aware of or discovers any flaws, the Vendor shall
provide notification of such flaws affecting security of Vendor-supplied software within a pre-negotiated
period. Notification shall include, but is not limited to, detailed documentation describing the flaw with
security impact, root cause, corrective actions, etc. (This language is typically found in a quality
assurance document, but is included here for completeness.)


### FAT Measures

The Vendor shall verify that for flaws known by the Vendor, the Vendor’s corrective actions follow
their process and the process is effective.

The Vendor shall verify that FAT documentation of the flaws validation and remediation are
provided.

The Vendor shall verify that any changes to the core system code, logic, or configuration are analyzed
to verify new vulnerabilities are not introduced into the system as a result of the change.


### SAT Measures

The Vendor shall verify that for flaws known by the Vendor, the Vendor’s corrective actions follow
their process and the process is effective.

The Vendor shall verify that SAT documentation of the flaws validation and repair are provided.

The Vendor shall verify that any changes to the core system code, logic, or configuration are analyzed
to verify new vulnerabilities are not introduced into the system as a result of the change.


### Maintenance Guidance

The Vendor shall maintain for a pre-negotiated period a master list of all flaws and corrective actions
for auditing purposes.


### References

NIST Special Publication 800-40 Version 2.0, “Creating a Patch and Vulnerability Management
Program.”


### Dependencies

Section 2.6, “Installing Operating Systems, Applications, and Third-Party Software Updates.”


## 6.2 Problem Reporting

Vulnerabilities exist in core logic and configuration of control systems. When flaws in software
and/or hardware configuration are discovered by users, the Vendor shall have a process in place by which
the user can report such flaws. A flaw remediation process shall be used to track progress of patches,
fixes, and workarounds until completion.


### Basis

Zero-day exploits are not defendable and are a primary attack vector.


### Language Guidance

Timely notification of flaws is essential to create defenses for zero-day exploits. The Vendor and the
Purchaser must communicate flaw information in a secure manner during the mitigations development
process.
Public release of problem reports could lead to nondefendable exploits. Consequently, knowledge of
open flaws shall be closely protected.


### Procurement Language

The Vendor shall provide a process for users to submit problem reports and remediation requests to
be included in the system security. The process shall include tracking history and corrective action status
reporting.

The Vendor shall review and report their initial action plan within 24 hours of submitting the problem
reports.

The Vendor shall protect problem reports regarding security vulnerabilities from public discloser and
notify Purchaser of all problems and remediation steps, regardless of origin of discovery of the problem.

The Vendor shall inform the Purchaser in writing of flaws within applications and operating systems
in a timely fashion and provide corrective actions, fixes, or monitoring guidance for vulnerability exploits
associated with the flaw.

The Vendor shall provide an auditable history of flaws including the remediation steps taken for each.


### FAT Measures

None.


### SAT Measures

None.


### Maintenance Guidance

The Vendor shall provide pre-negotiated updates to the Purchaser.


### References

NIST Special Publication 800-40 Version 2.0, “Creating a Patch and Vulnerability Management
Program.”


### Dependencies

None. This topic is stand-alone.
