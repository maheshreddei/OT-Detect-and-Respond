# 2. System Hardening

> Control category from *Cyber Security Procurement Language for Control Systems* (DHS/ICS-CERT, Sept 2009). Each control follows the 8-part topical template. See [`../docs/topical-template.md`](../docs/topical-template.md).


## 2.1 Removal of Unnecessary Services and Programs

Unnecessary services and programs are often installed on network devices.


### Basis

Unused services in a host operating system that are left enabled are possible entry points for exploits
on the network and are generally not monitored because these services are not used. Only the services
used for control systems operation and maintenance shall be enabled to limit possible entry points.


### Language Guidance

Often, networked devices ship with a variety of services enabled and default operating system
programs/utilities pre-installed. These range from system diagnostics to chat programs, several of which
have well-known vulnerabilities. Various attacks have been crafted to exploit these services to obtain
information leading to compromise the system.

Any program that offers a network service that “listens” on specific addresses for connection
requests. On a Transmission Control Protocol (TCP)/Internet Protocol (IP) network, these addresses are a
combination of IP address and TCP or User Datagram Protocol (UDP) ports. A recommended hardening
activity is simply disabling or removing any services or programs, which are not required for normal
system operation, thus removing potential vulnerabilities.

Port scans are the normal method of ensuring existence of required services and absence of unneeded
services. A port scan shall be run before the FAT with a representative, fully functional system
configuration. All input/output (I/O) ports need to be scanned for UDP and TCP. The scan needs to be run
before the FAT and again prior to the SAT. Port scans can rarely be used on production systems. In most
cases, scanners will disrupt operations.


### Procurement Language

Post-contract award, the Vendor shall provide documentation detailing all applications, utilities,
system services, scripts, configuration files, databases, and all other software required and the appropriate
configurations, including revisions and/or patch levels for each of the computer systems associated with
the control system.

The Vendor shall provide a listing of services required for any computer system running control
system applications or required to interface the control system applications. The listing shall include all
ports and services required for normal operation as well as any other ports and services required for
emergency operation. The listing shall also include an explanation or cross reference to justify why each
service is necessary for operation.

The Vendor shall verify and provide documentation that all services are patched to current status.

The Vendor shall provide, within a pre-negotiated period, appropriate software and service updates
and/or workarounds to mitigate all vulnerabilities associated with the product and to maintain the
established level of system security.

The Vendor shall remove and/or disable all software components that are not required for the
operation and maintenance of the control system prior to the FAT. The Vendor shall provide
documentation on what is removed and/or disabled. The software to be removed and/or disabled shall
include, but not be limited to:
1. Games
2. Device drivers for network devices not delivered
3. Messaging services (e.g., MSN, h AOL IM)
4. Servers or clients for unused Internet services
5. Software compilers in all user workstations and servers except for development workstations and
servers
6. Software compilers for languages that are not used in the control system
7. Unused networking and communications protocols
8. Unused administrative utilities, diagnostics, network management, and system management functions
9. Backups of files, databases, and programs used only during system development
10. All unused data and configuration files
11. Sample programs and scripts
12. Unused document processing utilities (Microsoft Word, Excel, PowerPoint, Adobe Acrobat,

OpenOffice, etc.).


### FAT Measures

The Vendor shall verify that the Purchaser requires the results of cyber security scans (as a minimum
a vulnerability and active port scan, with the most current signature files) run on the control system as a
primary activity of the FAT. This assessment is then compared with an inventory of the required services,
patching status, and documentation, to validate this requirement. Other measures provided include:
1. The Vendor shall provide for each networked device or class of device (e.g., server, workstation, and
switch) the following configuration documentation lists:
a.   Network services required for the operation of that device. Indicate the service name, protocol

(e.g., TCP and UDP) and port range
b.     Dependencies on underlying operating system services
c.     Dependencies on networked services residing on other network devices
d.     All the software configuration parameters required for proper system operation
e.     Certified OS, driver, and other software versions installed on the device
f.     Results found by the vulnerability scans with mitigations affected.
2. The Vendor shall install firmware updates available for the computer or network device certified by
the system manufacturer at the time of installation and provide documentation.
3. The Vendor shall provide a summary table indicating each communication path required by the
system. Include the following information in this table:

h.   Product Disclaimer

References herein to any specific commercial product, process, or service by trade name, trademark, manufacturer, or

otherwise, does not necessarily constitute or imply its endorsement, recommendation, or favoring by the U.S. Government,

any agency thereof.

a.   Source device name and media access control (MAC) and/or IP address
b.   Destination device name and MAC and/or IP address
c.   Protocol (e.g., TCP and UDP) and port or range of ports.
4. The Vendor shall perform network-based validation and documentation steps on each device:
a.     Full TCP and UDP port scan on Ports 1–65535. This scanning needs to be completed during a

simulated “normal system operation.”


### SAT Measures

The Vendor shall compare the results of cyber security scans run on the system, as a primary activity
of the SAT, with an inventory of the required services, patching status, and required documentation. At
the conclusion of the SAT and before cutover or commissioning, the above cyber security scans (with the
most current signature files) must be run again.


### Maintenance Guidance

Document the system operating system and software patches as the system software evolves to allow
traceability and to verify no extra services are reinstalled. Anytime the system is upgraded, it is
recommended that system Vendors rerun appropriate subsets of the FAT on the baseline system before
delivery to the purchaser.


### References

North American Electric Reliability Corporation (NERC) CIP-007-1 R2, “Ports and Services,” Cyber
Security—Critical Infrastructure Protection, June 1, 2006.
ANSI/ISA-99.00.01, Security for Industrial Automation and Control Systems Part 1: Terminology,
Concepts, and Models, Section 5. i
ISA-99.00.02 (DRAFT), Security for Industrial Automation and Control Systems: Part 2: Establishing an
Industrial Automation and Control Systems Security Program, Sections 5.3, B.14, C.3.
National Institute of Standards and Technology (NIST) j —Special Publication 800-42, “Guideline on

Network Security Testing.”


### Dependencies

None. This topic is stand-alone.


## 2.2 Host Intrusion Detection System

A host intrusion detection system (HIDS) can be installed to perform a variety of integrity checks to
detect attempted unauthorized access.


### Basis

In unmonitored systems, it is difficult to detect unauthorized changes or additions to the operating
system or application programs. The vulnerability scans, suggested in the prior section, only identify what

i.   Instrumentation, Systems, and Automation Society (ISA) standards are available at

http://www.isa.org/Template.cfm?Section=Standards2&template=/Ecommerce/ProductDisplay.cfm&ProductID=8997
j.   NIST publications are located at, http://csrc nist.gov/publications/nistpubs/

is known. Continuous monitoring is necessary to detect emerging unauthorized changes or additions, or
unauthorized escalation of process privileges.


### Language Guidance

Typically, the HIDS operates by performing checks on files to detect tampering, escalations of
privileges, and unauthorized account access; by intercepting sensitive operating system functions; or by
some combination of both. Additional HIDS capabilities may include monitoring attempts to access the
system remotely (e.g., “scanning”).

The resources required to configure the HIDS is minor compared to the resources required for
ongoing log reviews, as log files generated by the HIDS can be voluminous. Log review and notification
software tools may be appropriate. Also, sending log entries in real time over a network can overwhelm
the network. Thus, it may be necessary to write logs to a local storage device such as a Universal Serial
Bus (USB) or Digital Video Disc (DVD) drive. If possible, storage devices shall be configured as
“append-only” to prevent alteration of records.


### Procurement Language

Post-contract award:
   The Vendor shall provide a configured HIDS and/or provide the information to configure a HIDS to

include, but not be limited to, static file names, dynamic file name patterns, system and user accounts,

execution of unauthorized code, host utilization, and process permissions sufficient for configuring

the HIDS.
   The Vendor shall configure the HIDS such that all system and user account connections are logged.

This log will be configured such that an alarm can be displayed to the operator or security personnel

if an abnormal situation occurs.
   The Vendor shall recommend a configuration for the HIDS in a manner that does not negatively

impact the operating system functions or business objectives.
   The Vendor shall recommend log review and notification software tools.
   The Vendor shall configure devices as “append only” to prevent alteration of records on local storage

devices.


### FAT Measures

The Vendor shall verify and provide documentation that for Vendor-supplied HIDS; the Vendor shall
run the HIDS during the entire FAT process and periodically interject applicable malware.

The Vendor shall examine log files and validate the expected results. FAT procedures shall include
validation and documentation of this requirement.


### SAT Measures

The Vendor shall verify and provide documentation that for Vendor-supplied HIDS. The Vendor
shall run the HIDS during the entire SAT process and periodically interject applicable malware.

The Vendor shall examine log files and validate the expected results. SAT procedures shall include
validation and documentation of this requirement.

The Vendor shall generate a system image at the conclusion of the SAT to be used later as a control
baseline.


### Maintenance Guidance

The Vendor shall provide, within a pre-negotiated period, rule updates and patches to the HIDS as
security issues are identified to maintain the established level of system security.


### References

NERC CIP-005-1 R3, “Monitoring Electronic Access.”
NERC CIP-007-1 R6, “Security Status Monitoring.”
ANSI/ISA-99.00.01, “Security for Industrial Automation and Control Systems Part 1: Terminology,
Concepts, and Models,” Section 3.
ISA-99.00.02 (DRAFT), Security for Industrial Automation and Control Systems: Part 2: Establishing an
Industrial Automation and Control Systems Security Program, Sections C.3.”
NIST Special Publication 800-12, “An Introduction to Computer Security: The NIST Handbook.”
NIST Special Publication 800-82, “Guide to Industrial Control Systems (ICS) Security,” Final Public
Draft.
NIST Special Publication 800-94, “Guide to Intrusion Detection and Prevention Systems (IDPS).”


### Dependencies

Section 3.2, “Network Intrusion Detection Systems.”


## 2.3 Changes to File System and Operating System Permissions

Hardening file system configurations and restricting operating system permissions reduce the
vulnerabilities associated with default configurations.


### Basis

Configurations for out-of-the-box operating systems and file systems normally are more permissive
than necessary allowing exploitation.


### Language Guidance

In many cases, the operating system is shipped with the default configurations that allow unneeded
access to files, and loose configuration parameters that can be exploited to gain information for further
attacks. Common examples include operating system recovery procedures, elevated-permission user or
system accounts, diagnostic tools, remote access tools, and direct access to network device addresses.
Hardening tasks include changing or disabling access to such files and functions.


### Procurement Language

The Vendor shall configure hosts with least privilege file and account access and provide
documentation of the configuration.

The Vendor shall configure the necessary system services to execute at the least user privilege level
possible for that service and provide documentation of the configuration.
The Vendor shall document that changing or disabling access to such files and functions has been
completed.


### FAT Measures

The Vendor shall provide, as a part of the FAT procedures, validation and documentation of the
permissions assigned.


### SAT Measures

The Vendor shall provide, as a part of the SAT procedures, validation and documentation of the
permissions assigned.


### Maintenance Guidance

The Vendor shall reassess permissions and security settings on the baseline system before delivery of
any upgrades.


### References

NERC CIP-007-1 R5, “Account Management.”
ISA-99.00.02 (DRAFT), Security for Industrial Automation and Control Systems: Part 2: Establishing an
Industrial Automation and Control Systems Security Program,” Sections 5.3, B.14, C.3.


### Dependencies

Section 4.1, “Disabling, Removing, or Modifying Well-Known or Guest Accounts.”


## 2.4 Hardware Configuration

Unnecessary hardware can be physically disabled, removed, or its configuration altered through
software.


### Basis

Most control system network devices have multiple communication and data storage capabilities.
These can be used to introduce vulnerabilities such as viruses, root kits, malware, bots, key-loggers, etc.


### Language Guidance

Hardware configuration activities may include configuring the network devices to limit access from
only specific locations (e.g., IP filtering) or requiring additional verification of user credentials
(e.g., password, personal identification number [PIN], crypto key, or token). Local hardening can require
similar verification for protecting system Basic Input/Output System (BIOS) configuration parameters,
and limiting system access through local media (e.g., disabling/removing USB ports, CD/DVD drives,
and other removable media devices). It may be desirable to physically lock devices with accessible drives
or ports, such that only the human-machine interface is accessible.

System administrators shall be able to re-enable devices if the devices are disabled by software.


### Procurement Language

The Vendor shall disable, through software or physical disconnection, all unneeded communication
ports and removable media drives, or provide engineered barriers, and provide documentation of the
results.

The Vendor shall password protect the BIOS from unauthorized changes unless it is not technically
feasible, in which case the Vendor shall document this case and provide mitigation measures.

The Vendor shall provide a written list of all disabled or removed USB ports, CD/DVD drives, and
other removable media devices.

The Vendor shall configure the network devices to limit access to/from specific locations, where
appropriate, and provide documentation of the configuration.

The Vendor shall configure the system to allow the system administrators the ability to re-enable
devices if the devices are disabled by software and provide documentation of the configuration.


### FAT Measures

The Vendor shall provide, as a part of the FAT procedures, validation and documentation of the
disabled or locked physical access and the removed drivers.


### SAT Measures

The Vendor shall provide, as a part of the SAT procedures, validation and documentation of the
disabled or locked physical access and the removed drivers.


### Maintenance Guidance

The Vendor shall verify and provide documentation that any replacement device is configured the
same and exhibits the same behaviors as the original.


### References

NERC CIP-005-1, “Electronic Security Perimeter(s).”
NERC CIP-006-1, “Physical Security of Critical Cyber Assets.”


### Dependencies

None. This topic is stand-alone.


## 2.5 Heartbeat Signals

Heartbeat signals indicate the communication health of the system.


### Basis

Heartbeat signals or protocols can be corrupted, spoofed, or possibly used as an entry point for
unauthorized access.


### Language Guidance

Heartbeat status signals can be sent over serial connections or routed protocols. These are often used
in reporting-by-exception schemes and may be used by third-party add-on applications. Heartbeat signals
can be configured in the hardware, software, or firmware.


### Procurement Language

The Vendor shall identify heartbeat signals or protocols and recommend whether any should be
included in network monitoring.
Post-contract award, the Vendor shall provide packet definitions of the heartbeat signals and
examples of the heartbeat traffic if the signals are included in the network monitoring.


### FAT Measures

The Vendor shall provide, as a part of the FAT procedures, documentation of the requirements.
The Vendor shall create a baseline of the heartbeat communications traffic, to include frequency,
packet sizes, and expected packet configurations.


### SAT Measures

The Vendor shall provide, as a part of the SAT procedures, documentation of the requirements.

The Vendor shall create a baseline of the heartbeat communications traffic and validate the results
against FAT documentation.


### Maintenance Guidance

The periodicity of the heartbeat communications is normally configurable. The Vendor shall provide
a recommended frequency for monitoring. If changed, the network monitoring shall be modified and
documented by the appropriate party


### References

NERC CIP-007-1 R6, “Security Status Monitoring.”


### Dependencies

Section 2.2, “Host Intrusion Detection System.”
Section 3.2, “Network Intrusion Detection System.”


## 2.6 Installing Operating Systems, Applications,

and Third-Party Software Updates

Patches and software updates, including those for anti-virus scanners, are required to reduce attack
surface.


### Basis

Most successful cyber attacks occur in nonpatched systems or applications.


### Language Guidance

As control system applications come under increased scrutiny by the hacker community, it can be
expected that any vulnerabilities and exploits will become common knowledge among that community
quickly, as has been shown within the IT community. Responsible system and product Vendors regularly

release updates, patches, service packs, or other fixes to their products to address known and potential
vulnerabilities. Of course, to be effective, these must be installed in a timely fashion.

Most common operating systems ship with a number of well-known vulnerabilities; even a new
system is likely to be vulnerable based on the services that are active and because patches are not likely to
be current. Therefore, an essential system hardening activity is simply installing the latest versions or
updates of any necessary software loaded on a system. Of course, testing and validation of the patches
and upgrades are necessary prior to performing the updates on a production system.

In many cases, Vendor support is limited to the installation of specific software releases. Therefore,
updates can only be reliably applied based on the requirements of that particular software product.
Patches have been known to introduce security vulnerabilities or reverse security features making it
important to understand all processes (services, ports, permissions, etc.) affected by the patch. k

Scanning is an effective tool to identify vulnerabilities. Use caution, however, because active
scanning of live control system networks has been known to disable the networks during operations. FAT
and SAT provide critical opportunities for active scanning tests without an impact to production. Even
passive scanning is not recommended on production systems until the impact to operations is fully
understood.


### Procurement Language

The Vendor shall have a patch management and update process.
Pre-contract award, the Vendor shall provide details on their patch management and update process.
Responsibility for installation and update of patches shall be identified.
Post-contract award, the Vendor shall provide notification of known vulnerabilities affecting
Vendor-supplied or required OS, application, and third-party software within a pre-negotiated period after
public disclosure.

Post-contract award, the Vendor shall provide notification of patches affecting security within a pre­
negotiated period as identified in the patch management process. The Vendor shall apply, test, and
validate the appropriate updates and/or workarounds on a baseline reference system before distribution.
Mitigation of these vulnerabilities shall occur within a pre-negotiated period.


### FAT Measures

The Vendor shall install and update all tested and validated security patches prior to the start of the
FAT.

The Vendor shall verify and provide documentation that all updates have been tested and installed.

The Vendor shall perform contractually agreed upon security scans (with the most current signature
files) to verify that the system has not been compromised during the testing phase.

The Vendor shall provide documentation of the results of the scans.
The Vendor shall document the system after the FAT to support future validation of patches. (In
many instances, this is referred to as the system baseline.)

k.   http://www.theregister.co.uk/2004/09/02/winxpsp2_security_review/


### SAT Measures

The Vendor shall install and update all tested and validated security patches at the start of the SAT.

The Vendor shall provide documentation that all the updates have been tested and installed.

The Vendor shall verify system functionality, based on pre-negotiated procedures, at the conclusion
of patch updates, and provide documentation of the results.

The Vendor shall perform security scans (with the most current signature files) to verify that the
system has not been compromised during the testing phase of the results.
The Vendor shall document the system after the SAT to support future validation of patches. (In
many instances, this is referred to as delivered system configuration.)


### Maintenance Guidance

The Vendor shall provide a patch management process to include policies and procedures for the
system after installation. These policies and procedures shall include the patch management process and
mitigation strategies for instances when the Vendor informs the user not to apply released patches.

The Vendor shall provide a level of support for testing patch releases. This shall include the level of
revision on a documented system configuration (i.e., Vendor platform, FAT system, SAT system, current
production).

Users are encouraged to install received security updates on a nonproduction system for testing and
validation prior to installation on production systems.


### References

NERC CIP-007-1 R3, “Security Patch Management.”
ANSI/ISA-99.00.01, “Security for Industrial Automation and Control Systems Part 1: Terminology,
Concepts, and Models,” Section 6.5.
ISA-99.00.02 (DRAFT), Security for Industrial Automation and Control Systems: Part 2: Establishing an
Industrial Automation and Control Systems Security Program,” Sections 3.29, 3.43, 5.3, B.14, B.17,
B.19, C.3.


### Dependencies

Section 4.5, “Role-Based Access Control for Control System Applications.”
Section 5.1, “Coding for Security.”
Section 6.1, “Notification and Documentation from Vendor.”
