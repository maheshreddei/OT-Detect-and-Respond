# 9. End Devices

> Control category from *Cyber Security Procurement Language for Control Systems* (DHS/ICS-CERT, Sept 2009). Each control follows the 8-part topical template. See [`../docs/topical-template.md`](../docs/topical-template.md).


## 9.1 Intelligent Electronic Devices

An intelligent electronic device (IED) is sometimes referred to as an intelligent end device. It
incorporates microprocessors within the device, receives information from process sensors or from the
power equipment, and issues control commands to process equipment such as breakers, valves, pumps,
transformers, etc.


### Basis

Intelligent electronic devices can be used as access points to other systems that perform command and
control functions. The devices are used to provide system control at the lowest level of a process and are
vulnerable to communication interception and modification. Hardware and software (e.g., portable
configuration computers) are needed to program IEDs. IEDs and configuration computers need to be
secured by physical and cyber means (see Sections 2.4, 2.6, 4.1–4.5, and 7).


### Language Guidance

IEDs are a part of the entire system and must be able to communicate with the rest of the system
while performing specific control functions. If the communication from the network to the device or from
the device to the network is intercepted and modified, the controlled process could be adversely affected.
Therefore, it is necessary to verify that both the device itself and the communication to and from the
device are secured to achieve integrity of the communication. In addition, modifications to the control
function of the device can affect the integrity of the data transmitted and the actions taken by the control
system. To avoid this, it is necessary to secure the IED from both cyber and physical modifications.


### Procurement Language

The Vendor shall provide physical and cyber security features including, but not limited to,
authentication, encryption, access control, event and communication logging, monitoring, and alarming to
protect the device and configuration computer from unauthorized modification or use.

The Vendor shall clearly identify the physical and cyber security features and provide the
methodology(ies) for maintaining the features including the methods to change settings from the Vendor-
configured or manufacturer default conditions.

The Vendor shall verify that the addition of security features does not adversely affect connectivity,
latency, bandwidth, response time, and throughput, including during the SAT when connected to existing
equipment.

The Vendor shall remove or disable all software components that are not required for the operation
and maintenance of the device prior to the FAT. The Vendor shall provide documentation on what is
removed and/or disabled.

The Vendor shall provide, within a pre-negotiated period, appropriate software and service updates
and/or workarounds to mitigate all vulnerabilities associated with the product and to maintain the
established level of system security.

The Vendor shall verify and provide documentation that the safety instrumented system (SIS) is
certified after incorporating the security devices.


### FAT Measures

The Vendor shall verify and provide documentation of physical and cyber security features including,
but not limited to, authentication, encryption, access control, event and communication logging,
monitoring, and alarming to protect the device and configuration computer from unauthorized
modification or use.

The Vendor shall verify and provide documentation that all validated security updates and patches are
installed and tested at the start of the FAT.
The Vendor shall verify and provide documentation that all unused software and services are
removed or disabled.

Post-FAT, the Vendor shall create a baseline of the system communications and configuration
including, but not limited to, cyber security features, software, protocols, ports, and services and provide
documentation describing each item.

The Vendor shall verify through cyber security scans of the system and provide documentation that
the addition of security features does not adversely affect adequate connectivity, latency, bandwidth,
response time, and throughput for field communications.

The Vendor shall verify that FAT procedures include validation and documentation of the
requirements.


### SAT Measures

The Vendor shall verify and provide documentation of any changes to physical and cyber security
features including, but not limited to, authentication, encryption, access control, event and communication
logging, monitoring, and alarming to protect the device and configuration computer from unauthorized
modification or use.

Post-SAT, the Vendor shall create a baseline of the system communications and configuration
including, but not limited to, cyber security features, software, protocols, ports, and services and provide
documentation describing any changes.

The Vendor shall verify and provide documentation that any Vendor-configured or manufacturer
default accounts, usernames, passwords, security settings, security codes, and other access methods are
changed, disabled, or removed at the start of the SAT.

The Vendor shall verify through cyber security scans of the system and provide documentation that
the addition of security features does not adversely affect adequate connectivity, latency, bandwidth,
response time, and throughput when connected during the SAT.

The Vendor shall verify that SAT procedures include validation and documentation of the
requirements.


### Maintenance Guidance

The Vendor shall provide, within a pre-negotiated period, upgrades and patches to the IED as security
issues are identified to maintain the established level of system security.

The Vendor shall create a baseline of the updated system communications and configuration
including, but not limited to, cyber security features, software, protocols, ports, and services and provide
documentation describing any changes.

The Vendor shall verify and provide documentation that any Vendor-configured or manufacturer
default accounts, usernames, passwords, security settings, security codes, and other access methods are
changed, disabled, or removed.

The Vendor shall validate permissions and security settings on the baseline system before delivery of
any upgrades or replacements to maintain the established level of system security.

The Vendor shall supply maintenance capabilities for delivered system security features.
The Vendor shall document all additions and changes to the control system during the
warranty/maintenance period.


### References

IEC61850, “International Standard for Substation Automation Systems.”
EIA-485, “OSI Model Physical Layer Electrical Specification of a Two-wire, Half-duplex, Multipoint
Serial Connection.”
ANSI/ISA-99.00.01, “Security for Industrial Automation and Control Systems Part 1: Terminology,
Concepts, and Models,” Sections 6.3.2.2, 6.3.6.
ANSI/ISA-TR99.00.01-2007 Security Technologies for Industrial Automation and Control Systems,”
Section 5.1.
NERC CIP-005-1 R1, “Electronic Security Perimeter.”
NERC CIP-005-1 R2, “Electronic Access Controls.”
NERC CIP-006-1, “Physical Security of Critical Cyber Assets.”
NERC CIP-007-1 R2, “Ports and Services.”
NERC CIP-007-1 R3, “Security Patch Management.”
NERC CIP-007-1 R5, “Account Management.”
NERC CIP-007-1 R8, “Cyber Vulnerability Assessment.”
NIST Special Publication 800-53 Revision 1, “Recommended Security Controls for Federal Information
Systems,” Appendix F: AC-2, AC-3, IA-2, IA-5.


### Dependencies

Section 2.1, “Removal of Unnecessary Services and Programs.”
Section 2.4, “Hardware Configuration.”
Section 2.6, “Installing Operating Systems, Applications, and Third-Party Software Updates.”
Section 4.1, “Disabling, Removing, or Modifying Well-Known or Guest Accounts.”
Section 4.3, “Password/Authentication Policy and Management.”
Section 5.1, “Coding for Security.”
Section 6, “Flaw Remediation.”
Section 7.1 “Malware Detection and Protection.”
Section 8.1, “Network Addressing and Name Resolution.”
Section 10, “Remote Access.”
Section 11, “Physical Security.”


## 9.2 Remote Terminal Units

A remote terminal unit (RTU) is a microprocessor-controlled device that is used to provide system
control of industrial processes.


### Basis

RTUs can be used as access points to other systems that perform command and control functions. The
devices are used to provide system control at the lowest level of a process and are vulnerable to
communication interception and modification. Hardware and software (e.g., portable configuration
computers) are needed to program RTUs. RTUs and configuration computers need to be secured by
physical and cyber means (see Sections 2.4, 2.6, 4.1–4.5, and 7).


### Language Guidance

The RTU accepts inputs from multiple sources, outputs control signals to control devices, and
interfaces with a distributed control system or SCADA network by transmitting data to the system and/or
altering the state of connected objects based on control messages received from the system. The RTU is a
first-level decision-making device that is a part of the entire system and must be able to communicate
with the rest of the system while performing its specific control function. If the communication from the
input device (e.g., sensor) to the RTU or from the RTU to the output device (e.g., controller) or the
network is intercepted and modified, the controlled process could be adversely affected. In addition, the
processing unit within the RTU is susceptible to modification thus affecting the control functions.
Therefore, it is necessary to verify that both the RTU itself and the communication to and from the device
are secured to achieve integrity of the communication and the processing unit. It is also necessary to
secure the RTU from both cyber and physical modifications.


### Procurement Language

The Vendor shall provide physical and cyber security features including, but not limited to,
authentication, encryption, access control, event and communication logging, monitoring, and alarming to
protect the device and configuration computer from unauthorized modification or use.
The Vendor shall clearly identify the physical and cyber security features and provide the
methodologies for maintaining the features, including the methods to change settings from the
Vendor-configured or manufacturer default conditions.

The Vendor shall verify that the addition of security features does not adversely affect connectivity,
latency, bandwidth, response time, and throughput, including during the SAT when connected to existing
equipment.

The Vendor shall remove or disable all software components that are not required for the operation
and maintenance of the device prior to the FAT. The Vendor shall provide documentation on what is
removed and/or disabled.

The Vendor shall provide, within a pre-negotiated period, appropriate software and service updates
and/or workarounds to mitigate all vulnerabilities associated with the product and to maintain the
established level of system security.

The Vendor shall verify and provide documentation that the SIS is certified after incorporating the
security devices.


### FAT Measures

The Vendor shall verify and provide documentation of physical and cyber security features including,
but not limited to, authentication, encryption, access control, event and communication logging,
monitoring, and alarming to protect the device and configuration computer from unauthorized
modification or use.

The Vendor shall verify and provide documentation that all validated security updates and patches are
installed and tested at the start of the FAT.
The Vendor shall verify and provide documentation that all unused software and services are
removed or disabled.

Post-FAT, the Vendor shall create a baseline of the system communications and configuration
including, but not limited to, cyber security features, software, protocols, ports, and services and provide
documentation describing each item.

The Vendor shall verify through cyber security scans of the system and provide documentation that
the addition of security features does not adversely affect adequate connectivity, latency, bandwidth,
response time, and throughput.

The Vendor shall verify that FAT procedures include validation and documentation of the
requirements.


### SAT Measures

The Vendor shall verify and provide documentation of changes to physical and cyber security
features including, but not limited to, authentication, encryption, access control, event and communication

logging, monitoring, and alarming to protect the device and configuration computer from unauthorized
modification or use.

Post-SAT, the Vendor shall create a baseline of the system communications and configuration
including, but not limited to, cyber security features, software, protocols, ports, and services and provide
documentation describing any changes.

The Vendor shall verify and provide documentation that any Vendor-configured or manufacturer
default accounts, usernames, passwords, security settings, security codes, and other access methods are
changed, disabled, or removed at the start of the SAT.

The Vendor shall verify through cyber security scans of the system and provide documentation that
the addition of security features does not adversely affect adequate connectivity, latency, bandwidth,
response time, and throughput when connected during the SAT.

The Vendor shall verify that SAT procedures include validation and documentation of the
requirements.


### Maintenance Guidance

The Vendor shall provide, within a pre-negotiated period, upgrades and patches to the RTU as
security issues are identified to maintain the established level of system security.

The Vendor shall create a baseline of the updated system communications and configuration
including, but not limited to, cyber security features, software, protocols, ports, and services and provide
documentation describing any changes.

The Vendor shall verify and provide documentation that any Vendor-configured or manufacturer
default accounts, usernames, passwords, security settings, security codes, and other access methods are
changed, disabled, or removed.

The Vendor shall validate permissions and security settings on the baseline system before delivery of
any upgrades or replacements to maintain the established level of system security.

The Vendor shall supply maintenance capabilities for delivered system security features.
The Vendor shall document all additions and changes to the control system during the
warranty/maintenance period.


### References

ISO 11898-3:2006, Road vehicles -- Controller area network (CAN) -- Part 3: Low-speed, fault-tolerant,
medium-dependent interface.
ANSI/ISA-99.00.01, “Security for Industrial Automation and Control Systems Part 1: Terminology,
Concepts, and Models,” Sections 3.2.57, 6.2.1.4, 6.3.2.2, 6.3.6.
ANSI/ISA-TR99.00.01-2007 Security Technologies for Industrial Automation and Control Systems,”
Sections 5.1.1, 6.2.6, 7.3.4, 8.6.2, 9.2.4.
ISA-99.00.02 (DRAFT), Security for Industrial Automation and Control Systems: Part 2: Establishing an
Industrial Automation and Control Systems Security Program,” Sections 5.3, B.14, C.3.
NERC CIP-005-1 R1, “Electronic Security Perimeter.”
NERC CIP-005-1 R2, “Electronic Access Controls.”

NERC CIP-006-1 R1, “Physical Security of Critical Cyber Assets.”
NERC CIP-007-1 R2, “Ports and Services.”
NERC CIP-007-1 R3, “Security Patch Management.”
NERC CIP-007-1 R5, “Account Management.”
NERC CIP-007-1 R8, “Cyber Vulnerability Assessment.”
NIST Special Publication 800-53 Revision 1, “Recommended Security Controls for Federal Information
Systems,” Appendix F: AC-2, AC-3, IA-2, IA-5.


### Dependencies

Section 2.1, “Removal of Unnecessary Services and Programs.”
Section 2.3, “Changes to File System and Operating System Permissions.”
Section 2.4, “Hardware Configuration.”
Section 2.6, “Installing Operating Systems, Applications, and Third-Party Software Updates.”
Section 4.1, “Disabling, Removing, or Modifying Well-Known or Guest Accounts.”
Section 4.3, “Password/Authentication Policy and Management.”
Section 5.1, “Coding for Security.”
Section 6, “Flaw Remediation.”
Section 7.1 “Malware Detection and Protection.”
Section 8.1, “Network Addressing and Name Resolution.”
Section 10, “Remote Access.”
Section 11, “Physical Security.”


## 9.3 Programmable Logic Controllers

A PLC is a digital computer used to provide system control of industrial processes. PLCs are
designed for multiple inputs and outputs along with a processing unit used to monitor inputs, make
decisions, and control outputs.


### Basis

Programmable logic controllers can be used as access points to other systems that perform command
and control functions. PLCs communicate over open networks that are vulnerable to communication
interception and modification. Hardware and software (e.g., portable configuration computers) are needed
to program PLCs. PLCs and configuration computers need to be secured by physical and cyber means
(see Sections 2.4, 2.6, 4.1–4.5, and 7).


### Language Guidance

The PLC is a first-level decision-making device that is a part of the entire system and must be able to
communicate with the rest of the system while performing its specific control function. If the

communication from the input device (e.g., sensor) to the PLC or from the PLC to the output device
(e.g., controller) or the network is intercepted and modified, the controlled process could be adversely
affected. In addition, the processing unit within the PLC is susceptible to modification thus affecting the
control functions. Therefore, it is necessary to verify that both the PLC itself and the communication to
and from the device are secured to achieve integrity of the communication and the processing unit. It is
also necessary to secure the PLC from both cyber and physical modifications.

Some newer PLCs are including embedded operating systems that have many common operating
system components (e.g., Linux). These embedded operating systems need to be hardened (see Section 2).

SISs frequently run on PLC architectures. These systems are the last line of automated protection for
critical processes that could result in severe damage or fatalities if compromised. Industry certifications
are common for SIS. Legacy SIS/PLCs run on separate architectures from control functions. There is a
new trend for SIS to be integrated with traditional control functions (e.g., one PLC runs control and safety
functions). The cyber security concerns for integrated SIS are paramount.


### Procurement Language

The Vendor shall provide physical and cyber security features including, but not limited to,
authentication, encryption, access control, event and communication logging, monitoring, and alarming to
protect the device and configuration computer from unauthorized modification or use.
The Vendor shall clearly identify the physical and cyber security features and provide the
methodologies for maintaining the features, including the methods to change settings from the
Vendor-configured or manufacturer default conditions.

The Vendor shall verify that the addition of security features does not adversely affect connectivity,
latency, bandwidth, response time, and throughput, including during the SAT when connected to existing
equipment.

The Vendor shall remove or disable all software components that are not required for the operation
and maintenance of the device prior to the FAT. The Vendor shall provide documentation on what is
removed and/or disabled.

The Vendor shall provide, within a pre-negotiated period, appropriate software and service updates
and/or workarounds to mitigate all vulnerabilities associated with the product and to maintain the
established level of system security.

The Vendor shall verify and provide documentation that the SIS is certified after incorporating the
security devices.


### FAT Measures

The Vendor shall verify and provide documentation of physical and cyber security features including,
but not limited to, authentication, encryption, access control, event and communication logging,
monitoring, and alarming to protect the device and configuration computer from unauthorized
modification or use.

The Vendor shall verify and provide documentation that all validated security updates and patches are
installed and tested at the start of the FAT.
The Vendor shall verify and provide documentation that all unused software and services are
removed or disabled.

Post-FAT, the Vendor shall create a baseline of the system communications and configuration
including, but not limited to, cyber security features, software, protocols, ports, and services and provide
documentation describing each item.

The Vendor shall verify through cyber security scans of the system and provide documentation that
the addition of security features does not adversely affect adequate connectivity, latency, bandwidth,
response time, and throughput.

The Vendor shall verify that FAT procedures include validation and documentation of the
requirements.


### SAT Measures

The Vendor shall verify and provide documentation of and changes to physical and cyber security
features including, but not limited to, authentication, encryption, access control, event and communication
logging, monitoring, and alarming to protect the device and configuration computer from unauthorized
modification or use.

Post-SAT, the Vendor shall create a baseline of the system communications and configuration
including, but not limited to, cyber security features, software, protocols, ports, and services and provide
documentation describing any changes.

The Vendor shall verify and provide documentation that any Vendor-configured or manufacturer
default accounts, usernames, passwords, security settings, security codes, and other access methods are
changed, disabled, or removed at the start of the SAT.

The Vendor shall verify through cyber security scans of the system and provide documentation that
the addition of security features does not adversely affect adequate connectivity, latency, bandwidth,
response time, and throughput when connected during the SAT.

The Vendor shall verify that SAT procedures include validation and documentation of the
requirements.


### Maintenance Guidance

The Vendor shall provide, within a pre-negotiated period, upgrades and patches to the PLC as
security issues are identified to maintain the established level of system security.

The Vendor shall create a baseline of the updated system communications and configuration
including, but not limited to, cyber security features, software, protocols, ports, and services and provide
documentation describing any changes.

The Vendor shall verify and provide documentation that any Vendor-configured or manufacturer
default accounts, usernames, passwords, security settings, security codes, and other access methods are
changed, disabled, or removed.

The Vendor shall validate permissions and security settings on the baseline system before delivery of
any upgrades or replacements to maintain the established level of system security.

The Vendor shall supply maintenance capabilities for delivered system security features.
The Vendor shall document all additions and changes to the control system during the
warranty/maintenance period.


### References

IEC 61131-3, “Programmable Controllers – Part 3: Programming Languages.”
ANSI/ISA-99.00.01, “Security for Industrial Automation and Control Systems Part 1: Terminology,
Concepts, and Models,” Sections 3.2.57, 6.2.1.4, 6.3.2.2, 6.3.6.
ANSI/ISA-TR99.00.01-2007 Security Technologies for Industrial Automation and Control Systems,”
Sections 5.1.1, 6.2.6, 7.3.4, 8.6.2, 9.2.4.
NERC CIP-005-1 R1, “Electronic Security Perimeter.”
NERC CIP-005-1 R2, “Electronic Access Controls.”
NERC CIP-006-1 R1, “Physical Security of Critical Cyber Assets.”
NERC CIP-007-1 R2, “Ports and Services.”
NERC CIP-007-1 R3, “Security Patch Management.”
NERC CIP-007-1 R5, “Account Management.”
NERC CIP-007-1 R8, “Cyber Vulnerability Assessment.”
NIST Special Publication 800-53 Revision 1, “Recommended Security Controls for Federal Information
Systems,” Appendix F: AC-2, AC-3, IA-2, IA-5.


### Dependencies

Section 2.1, “Removal of Unnecessary Services and Programs.”
Section 2.3, “Changes to File System and Operating System Permissions.”
Section 2.4, “Hardware Configuration.”
Section 2.6, “Installing Operating Systems, Applications, and Third-Party Software Updates.”
Section 4.1, “Disabling, Removing, or Modifying Well-Known or Guest Accounts.”
Section 4.3, “Password/Authentication Policy and Management.”
Section 5.1, “Coding for Security.”
Section 6, “Flaw Remediation.”
Section 7.1 “Malware Detection and Protection.”
Section 8.1, “Network Addressing and Name Resolution.”
Section 10, “Remote Access.”
Section 11, “Physical Security.”


## 9.4 Sensors, Actuators, and Meters

Sensors, actuators, and meters are traditionally dumb devices that produce outputs or accept inputs
from a control system. The trend is toward sensors, actuators, and meters that incorporate
microprocessors, also known as “smart devices.” “Smart” sensors are also referred to as “smart
transducers.”


### Basis

Sensors, actuators, and meters can be used as access points to other systems (e.g., PLCs and IEDs)
that perform command and control functions. These devices communicate over networks that are
vulnerable to communication interception and modification. Hardware and software (e.g., portable
configuration computers) are needed to program smart devices. Smart devices and configuration
computers need to be secured by physical and cyber means (see Sections 2.4, 2.6, 4.1–4.5, and 7).


### Language Guidance

These devices are a part of the entire system and must be able to communicate with the rest of the
system while performing specific control functions. Since the devices do not possess processing
capabilities, the only vulnerability is the communication link with the control system. If the
communication from the input device (e.g., sensor or meter) to the control system or from the control
system to the output device (e.g., actuator) is intercepted and modified, the controlled process could be
adversely affected. These communication paths, Ethernet or serial, can be compromised. Security
measures such as port security (e.g., one MAC/port) or inline encryption are options. Sensors, actuators,
and meters and the communication to and from these devices need to be secured from both cyber and
physical modifications.

Sensors and meters are now often network-enabled and contain resident logic. These devices have
network and computer components that require security (e.g., updates).

Wireless communications are central in many sensor and meter networks complicating the security
profile (e.g., WPA).


### Procurement Language

The Vendor shall provide physical and cyber security features including, but not limited to,
authentication, encryption, access control, event and communication logging, monitoring, and alarming to
protect the device and configuration computer from unauthorized modification or use.

The Vendor shall clearly identify the physical and cyber security features and provide the
methodologies for maintaining the features, including the methods to change settings from the Vendor-
configured or manufacturer default conditions.

The Vendor shall provide secure (serial, Ethernet, and wireless) communication paths, including the
ability to filter and monitor communications.

The Vendor shall verify that the addition of security features does not adversely affect connectivity,
latency, bandwidth, response time, and throughput, including during the SAT when connected to existing
equipment.

For smart devices:
   The Vendor shall remove or disable all software components that are not required for the operation

and maintenance of the device prior to the FAT. The Vendor shall provide documentation on what is

removed and/or disabled.
   The Vendor shall provide, within a pre-negotiated period, appropriate software and service updates

and/or workarounds to mitigate all vulnerabilities associated with the product and to maintain the

established level of system security.
   The Vendor shall verify and provide documentation that the SIS is certified after incorporating the

security devices.


### FAT Measures

The Vendor shall verify and provide documentation of physical and cyber security features including,
but not limited to, authentication, encryption, access control, event and communication logging,
monitoring, and alarming to protect the device and configuration computer from unauthorized
modification or use.

Post-FAT, the Vendor shall create a baseline of the system communications and configuration
including, but not limited to, cyber security features, software, protocols, ports and services and provide
documentation describing each item.

The Vendor shall verify through cyber security scans of the system and provide documentation that
the addition of security features does not adversely affect adequate connectivity, latency, bandwidth,
response time, and throughput.

The Vendor shall verify that FAT procedures include validation and documentation of the
requirements.

For smart devices:
   The Vendor shall verify and provide documentation that all validated security updates and patches are

installed and tested at the start of the FAT.
   The Vendor shall verify and provide documentation that all unused software and services are

removed or disabled.


### SAT Measures

The Vendor shall verify and provide documentation of and changes to physical and cyber security
features including, but not limited to, authentication, encryption, access control, event and communication
logging, monitoring, and alarming to protect the device and configuration computer from unauthorized
modification or use.

Post-SAT, the Vendor shall create a baseline of the system communications and configuration
including, but not limited to cyber security features, software, protocols, ports and services and provide
documentation describing any changes.

The Vendor shall verify through cyber security scans of the system and provide documentation that
the addition of security features does not adversely affect adequate connectivity, latency, bandwidth,
response time, and throughput when connected during the SAT.

The Vendor shall verify that SAT procedures include validation and documentation of the
requirements.

For smart devices:
   The Vendor shall verify and provide documentation that any Vendor-configured or manufacturer

default accounts, usernames, passwords, security settings, security codes, and other access methods

are changed, disabled, or removed at the start of the SAT.
   The Vendor shall verify and provide documentation that any Vendor-configured or manufacturer

default usernames, passwords, or other access methods are changed at the start of the SAT.


### Maintenance Guidance

The Vendor shall provide, within a pre-negotiated period, upgrades and patches to the devices as
security issues are identified to maintain the established level of system security.

The Vendor shall create a baseline of the updated system communications and configuration
including, but not limited to, cyber security features, software, protocols, ports, and services and provide
documentation describing any changes.

The Vendor shall verify and provide documentation that any Vendor-configured or manufacturer
default accounts, usernames, passwords, security settings, security codes, and other access methods are
changed, disabled, or removed.

The Vendor shall validate permissions and security settings on the baseline system before delivery of
any upgrades or replacements to maintain the established level of system security.

The Vendor shall supply maintenance capabilities for delivered system security features.
The Vendor shall document all additions and changes to the control system during the
warranty/maintenance period.


### References

ANSI/ISA-99.00.01, “Security for Industrial Automation and Control Systems Part 1: Terminology,”
Sections 6.2.1.4, 6.3.8.
ANSI/ISA-TR99.00.01-2007 Security Technologies for Industrial Automation and Control Systems,”
Section 9.2.24.
NERC CIP-005-1 R1, “Electronic Security Perimeter.”
NERC CIP-005-1 R2, “Electronic Access Controls.”
NERC CIP-006-1 R1, “Physical Security of Critical Cyber Assets.”
NERC CIP-007-1 R2, “Ports and Services.”
NERC CIP-007-1 R3, “Security Patch Management.”
NERC CIP-007-1 R5, “Account Management.”
NERC CIP-007-1 R8, “Cyber Vulnerability Assessment.”
NIST Special Publication 800-53 Revision 1, “Recommended Security Controls for Federal Information
Systems,” Appendix F: AC-2, AC-3, IA-2, IA-5.


### Dependencies

Section 2.1, “Removal of Unnecessary Services and Programs.”
Section 2.4, “Hardware Configuration.”
Section 6, “Flaw Remediation.”
Section 7.1 “Malware Detection and Protection.”
Section 8.1, “Network Addressing and Name Resolution.”
Section 10, “Remote Access.”
Section 11, “Physical Security.”
