# 10. Remote Access

> Control category from *Cyber Security Procurement Language for Control Systems* (DHS/ICS-CERT, Sept 2009). Each control follows the 8-part topical template. See [`../docs/topical-template.md`](../docs/topical-template.md).


## 10.1 Dial-Up Modems

Dial-up modems allow remote access to control system equipment.


### Basis

Modems, often considered part of the telephone system and not the control network, are vulnerable
and easily overlooked. Modem lines connected to the network or control system equipment that are left
enabled are possible “back door” entry points for exploits on the network or directly on the control system
equipment.

Dial-up modems connected through the public-switched telephone network (PSTN), as opposed to
dedicated-line modems, are accessible to anyone in the world with a modem and are easy to discover via
war dialing.


### Language Guidance

Control system equipment is installed with modems enabled. Properly implementing modem security
settings (telephony firewalls and authentication, automated log monitoring, disabling power and phone
lines, dial-back modem features, caller ID authentication) mitigates modem vulnerabilities. It is common
to find little or no security protection for modem connections. Often, the only protection is provided by
the control system devices. These devices may require a password or user ID/password combination, but
even this simple protection may not be offered, especially for older legacy equipment. Throughput,
latency, and bandwidth must be investigated when considering security methods.

Modem security settings may exist on the company private branch exchange (PBX). Many security
settings can limit the time of day a phone line is active. Others may provide active logging capabilities
that can be used in an IDS for modem connections.

Telephony firewalls can provide voice-level capabilities similar to the data-level capabilities of
network firewalls in use today. The devices are normally placed between the PSTN and the modem.

Telephony authentication uses hardware keys on the PSTN side of the modem; when two modems
attempt to connect, the master key must validate the slave key before a PSTN connection is allowed.
However, if a slave key was compromised and not removed from the valid key list, an unauthorized user
could obtain access.

Automated monitoring of modem and control device connection logs can allow the system to alarm
on unexpected activities.

One simple approach to modem security is only connecting the modem power or phone line when
needed (e.g., power outlet timer). Another option to limit phone line connectivity is using PBX
time-window programming.

Configuring modems to dial back instead of auto-answer can provide another layer of authentication
security. Unfortunately, hackers have developed “dial-back spoofing” methods where a fake dial tone is
fed to the modem allowing the hacker to maintain the connection and ignore the dial-back process.

Caller ID can be combined with modems to allow or deny access based on comparison to a
preprogrammed list of valid phone numbers. Caller ID is typically used to block war dialing efforts.
Attackers have found ways to spoof a caller ID number to indicate a false number, but a correct number
on the list would first need to be discovered.

Using authentication allows both modems to confirm connection to an authorized party. Many of
these components, such as RTUs, PLCs, and IEDs may not require any authentication for connection.
Modems can be purchased with embedded keys, or hardware keys can be added to existing modems.

Man-in-the-middle (MitM) attacks use clear-text protocols to inject the attacker into the
communication stream to read user IDs and passwords and/or change the intercepted data before
forwarding it. The MitM attack could originate within the public telephone system, the internal PBX
system, or through a Voice over IP communication path. In-line encryption (bump-in-the-wire) devices
can act as an intermediary between the serial port and the modem, helping mitigate this vulnerability.
However, encryption may reduce overall throughput of the connection.


### Procurement Language

The Vendor shall verify that modems are enabled only when needed (e.g., time constraint) or limit
possible entry points (e.g., access list).

The Vendor shall change or disable configuration settings that could be used for exploitation when
not needed.

The Vendor shall provide a telephony firewall to include authorized list, automatic block, and alarm
during unauthorized access and automatic log review.

The Vendor shall not permit user credentials to be transmitted in clear text.

The Vendor shall provide physical and cyber security features including, but not limited to,
authentication, encryption, access control, event and communication logging, monitoring, and alarming to
protect the device and configuration computer from unauthorized modification or use.
The Vendor shall clearly identify the physical and cyber security features and provide the
methodologies for maintaining the features, including the methods to change settings from the
Vendor-configured or manufacturer default conditions.

The Vendor shall verify that the addition of security features does not adversely affect connectivity,
latency, bandwidth, response time, and throughput, including during the SAT when connected to existing
equipment.
The Vendor shall provide a list including all ports and services required for normal operation and
emergency operation and troubleshooting.

The Vendor shall provide, within a pre-negotiated period, appropriate software and service updates
and/or workarounds to mitigate all vulnerabilities associated with the product and to maintain the
established level of system security.

The Vendor shall remove and/or disable all software components that are not required for the
operation and maintenance of the modem and modem security system prior to the FAT. The Vendor shall
provide documentation on what is removed and/or disabled. The software to be removed and/or disabled
shall include, but is not limited to:
   Device drivers for network devices not delivered

   Unused networking and communications protocols
   Unused administrative utilities, diagnostics, network management, and system management functions
   All unused data and configuration files.

The Vendor shall provide, within a pre-negotiated period, appropriate software and service updates
and/or workarounds to mitigate all vulnerabilities associated with the product.

The Vendor shall verify and provide documentation that the SIS is certified after incorporating the
security devices.

Post-contract award, the Vendor shall provide documentation detailing all modem configurations,
services, and all software/modem device protection configurations and keys, including revisions and/or
patch levels.


### FAT Measures

The Vendor shall verify and provide documentation of physical and cyber security features, including
but not limited to authentication, encryption, access control, event and communication logging,
monitoring, and alarming to protect the device and configuration computer from unauthorized
modification or use.

The Vendor shall verify through cyber security scans of the system and provide documentation that
the addition of security features does not adversely affect connectivity, latency, bandwidth, response time,
and throughput.

Post-FAT, the Vendor shall create a baseline of the system communications and configuration
including, but not limited to cyber security features, software, protocols, ports, and services and provide
documentation describing each item.

The Vendor shall verify and provide documentation that all validated security updates and patches are
installed and tested at the start of the FAT.
The Vendor shall verify and provide documentation that all unused software and services are
removed or disabled.

The Vendor shall provide a summary table indicating each communication path required by the
system. This table shall include:
   Source device name and MAC/IP address
   Destination device name and MAC/IP address
   Protocol (e.g., TCP and UDP) and port or range of ports.

The Vendor shall perform network-based validation and documentation steps on each device
including full TCP and UDP port scans.

The Vendor shall complete the cyber security scans during a simulated “normal system operation.”

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

The Vendor shall perform war dialing or discovery activities and provide documentation of the
results.

The Vendor shall verify through cyber security scans of the system and provide documentation that
the addition of security features does not adversely affect adequate connectivity, latency, bandwidth,
response time, and throughput when connected during the SAT.

The Vendor shall verify that SAT procedures include validation and documentation of the
requirements.


### Maintenance Guidance

The Vendor shall provide, within a pre-negotiated period, upgrades and patches as security issues are
identified to maintain the established level of system security.

The Vendor shall create a baseline of the updated system communications and configuration
including, but not limited to, cyber security features, software, protocols, ports, and services and provide
documentation describing any changes.

The Vendor shall verify and provide documentation that any Vendor-configured or manufacturer
default accounts, usernames, passwords, security settings, security codes, and other access methods are
changed, disabled, or removed.

The Vendor shall validate permissions and security settings on the baseline system before delivery of
any upgrades or replacements to maintain the established level of system security.

The Vendor shall supply maintenance capabilities for delivered system security features.
The Vendor shall document all additions and changes to the remote access equipment during the
warranty/maintenance period.


### References

NERC CIP-005-1 R1, “Electronic Security Perimeter.”
NERC CIP-005-1 R2, “Electronic Access Controls.”
NERC CIP-007-1 R5, “Account Management.”
NERC CIP-007-1 R2, “Ports and Services.”
NERC CIP-007-1 R8, “Cyber Vulnerability Assessment.”

NIST Special Publication 800-53 Revision 1, “Recommended Security Controls for Federal Information
Systems,” Appendix F: AC-2, AC-17, IA-2, IA-5.
Department of Homeland Security, Recommended Practice for Securing Control System Modems,
January 2008. p


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
Section 9, “End Devices.”
Section 10, “Remote Access.”
Section 10.2, “Dedicated Line Modems.”
Section 11, “Physical Security.”


## 10.2 Dedicated Line Modems

Modems allow remote access to control system equipment.


### Basis

Modems connected by dedicated lines, also known as nonswitched lines, are often not considered
vulnerable because the lines are permanently connected together and do not have phone numbers. While
dedicated-line modems are considered more secure than dial-up modems, the devices, like dial-up
modems, are not impervious to information discovery and hacking.


### Language Guidance

Encryption and authentication are two security methods applicable to both dial-up and dedicated-line
modems.

Using authentication allows both modems to confirm connection to an authorized party. Many of
these components, such as RTUs, PLCs, and IEDs, may not require any authentication for connection.
Password authentication can be impractical with dedicated-line modems. Modems can be purchased with
embedded keys, or hardware keys can be added to existing modems.

p.   http://csrp.inl.gov/Documents/SecuringModems.pdf

MitM attacks use clear-text protocols to inject the attacker into the communication stream to read user
IDs and passwords and/or change the intercepted data before forwarding it. The MitM attack could
originate within the public telephone system (even over leased lines), the internal PBX system, or through
a Voice over IP communication path. In-line encryption (bump-in-the-wire) devices can act as an
intermediary between the serial port and the modem, helping mitigate this vulnerability. However,
encryption may reduce overall throughput of the connection.


### Procurement Language

The Vendor shall provide physical and cyber security features including, but not limited to,
authentication, encryption, access control, event and communication logging, monitoring, and alarming to
protect the device and configuration computer from unauthorized modification or use.
The Vendor shall clearly identify the physical and cyber security features and provide the
methodologies for maintaining the features including the methods to change settings from the
Vendor-configured or manufacturer default conditions.

The Vendor shall not permit user credentials to be transmitted in clear text.

The Vendor shall verify that the addition of security features does not adversely affect connectivity,
latency, bandwidth, response time, and throughput, including during the SAT when connected to existing
equipment.
The Vendor shall provide a list including all ports and services required for normal operation and
emergency operation and troubleshooting.

The Vendor shall provide, within a pre-negotiated period, appropriate software and service updates
and/or workarounds to mitigate all vulnerabilities associated with the product and to maintain the
established level of system security.

The Vendor shall verify and provide documentation that the SIS is certified after incorporating the
security devices.

The Vendor shall remove and/or disable all software components that are not required for the
operation and maintenance of the modem and modem security system prior to the FAT. The Vendor shall
provide documentation on what is removed and/or disabled. The software to be removed and/or disabled
shall include, but not be limited to:
   Device drivers for network devices not delivered
   Unused networking and communications protocols
   Unused administrative utilities, diagnostics, network management, and system management functions
   All unused data and configuration files.

Post-contract award, the Vendor shall provide documentation detailing all modem configurations,
services, and all software/modem device protection configurations and keys, including revisions and/or
patch levels.


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

The Vendor shall provide a summary table indicating each communication path required by the
system. This table shall include:
   Source device name and MAC/IP address
   Destination device name and MAC/IP address
   Protocol (e.g., TCP and UDP) and port or range of ports.

The Vendor shall perform network-based validation and documentation steps on each device,
including full TCP and UDP port scans.

The Vendor shall complete the cyber security scans during a simulated “normal system operation.”

The Vendor shall verify that FAT procedures include validation and documentation of the
requirements.


### SAT Measures

The Vendor shall verify and provide documentation of and changes to physical and cyber security
features, including but not limited to authentication, encryption, access control, event and communication
logging, monitoring, and alarming to protect the device and configuration computer from unauthorized
modification or use.

Post-SAT, the Vendor shall create a baseline of the system communications and configuration
including, but not limited to cyber security features, software, protocols, ports and services and provide
documentation describing any changes.

The Vendor shall perform discovery activities and provide documentation of the results.

The Vendor shall verify and provide documentation that any Vendor-configured or manufacturer
default accounts, usernames, passwords, security settings, security codes, and other access methods are
changed, disabled, or removed at the start of the SAT.

The Vendor shall verify through cyber security scans of the system and provide documentation that
the addition of security features does not adversely affect adequate connectivity, latency, bandwidth,
response time, and throughput when connected during the SAT.

The Vendor shall verify that SAT procedures include validation and documentation of the
requirements.


### Maintenance Guidance

The Vendor shall provide, within a pre-negotiated period, upgrades and patches as security issues are
identified to maintain the established level of system security.

The Vendor shall create a baseline of the updated system communications and configuration
including, but not limited to cyber security features, software, protocols, ports, and services and provide
documentation describing any changes.

The Vendor shall verify and provide documentation that any Vendor-configured or manufacturer
default accounts, usernames, passwords, security settings, security codes, and other access methods are
changed, disabled, or removed.

The Vendor shall validate permissions and security settings on the baseline system before delivery of
any upgrades or replacements to maintain the established level of system security.

The Vendor shall supply maintenance capabilities for delivered system security features.
The Vendor shall document all additions and changes to the remote access equipment during the
warranty/maintenance period.


### References

NERC CIP-005-1 R1, “Electronic Security Perimeter.”
NERC CIP-005-1 R2, “Electronic Access Controls.”
NERC CIP-006-1 R1, “Physical Security of Critical Cyber Assets.”
NERC CIP-007-1 R2, “Ports and Services.”
NERC CIP-007-1 R3, “Security Patch Management.”
NERC CIP-007-1 R8, “Cyber Vulnerability Assessment.”
NIST Special Publication 800-53 Revision 1, “Recommended Security Controls for Federal Information
Systems,” Appendix F: AC-2, AC-3, IA-2, IA-5.
Department of Homeland Security, Recommended Practice for Securing Control System Modems,
January 2008. q


### Dependencies

Section 2.1, “Removal of Unnecessary Services and Programs.”
Section 2.4, “Hardware Configuration.”
Section 2.6, “Installing Operating Systems, Applications, and Third-Party Software Updates.”
Section 4.1, “Disabling, Removing, or Modifying Well-Known or Guest Accounts.”
Section 4.3, “Password/Authentication Policy and Management.”
Section 5.1, “Coding for Security.”
Section 6, “Flaw Remediation.”

q.   http://csrp.inl.gov/Documents/SecuringModems.pdf

Section 7.1, “Malware Detection and Protection.”
Section 8.1, “Network Addressing and Name Resolution.”
Section 9, “End Devices.”
Section 10, “Remote Access.”
Section 10.1, “Dial-up Modems.”
Section 11, “Physical Security.”


## 10.3 TCP/IP

The TCP/IP stack is the foundation of communication on the Internet and most commercial networks.
It is named after its two most important protocols: the IP and the TCP. Other important IPs include UDP,
Address Resolution Protocol (ARP), and Internet Control Message Protocol (ICMP). IP operates at the
network layer of a network and provides connectionless unreliable communication. IP is responsible for
sending and routing packets, but is connectionless and does not guarantee transmission. TCP runs on top
of the IP and provides connection-oriented reliable communication.


### Basis

Poor TCP/IP implementations and/or implementations that do not fully comply with TCP/IP Requests
for Comments (RFCs) can result in protocol stacks that contain vulnerabilities. Buffer overflows, the
inability to handle packet fragmentation, or malformed network traffic are common problems. Intentional
or accidental exploitation of vulnerabilities can lead to a device/function being compromised/targeted or
can produce a DoS.


### Language Guidance

The TCP/IP specifications lack basic security mechanisms resulting in fully compliant
implementations remaining vulnerable to attacks (e.g., DoS, IP spoofing, session hijacking, and syn
flooding). At this time, within the TCP/IP framework external mitigations are required (e.g., encryption,
authentication, proper network partitioning, and correct firewall configuration). A good software security
solution is IP Security (IPsec), which provides the ability to authenticate and encrypt IP traffic within the
protocol stack.

Intrusion Detection Systems (IDS) will not work with encrypted data. In order to use encryption and
IDSs in a control system, it is necessary to place an IDS on a device that can decrypt the traffic, analyze
it, and then re-encrypt it before forwarding it.

There are currently two IP standards: IPv4 and IPv6. Most network devices comply with IPv4
specifications; however, many newer devices are compatible with both IPv4 and IPv6. When IPv6 is the
main standard, new network devices may not be backwards compatible with IPv4. Control system devices
are often operational in excess of 20 years; therefore, it is advisable that the devices be IPv6 compatible.


### Procurement Language

The Vendor shall provide physical and cyber security features including, but not limited to,
authentication, encryption, access control, event and communication logging, monitoring, and alarming to
protect the device and configuration computer from unauthorized modification or use.

The Vendor shall clearly identify the physical and cyber security features and provide the
methodologies for maintaining the features including the methods to change settings from the
Vendor-configured or manufacturer default conditions.

The Vendor shall verify that the addition of security features does not adversely affect connectivity,
latency, bandwidth, response time, and throughput, including during the SAT when connected to existing
equipment.

The Vendor shall remove or disable all software components that are not required for the operation
and maintenance of the device prior to the FAT. The Vendor shall provide documentation on what is
removed and/or disabled.

The Vendor shall provide, within a pre-negotiated period, appropriate protocol stack updates and/or
workarounds to mitigate all vulnerabilities associated with the product and to maintain the established
level of system security.

The Vendor shall verify and provide documentation that the SIS is certified after incorporating the
security devices.

The Vendor shall use a TCP/IP implementation that fully complies with the current TCP/IP RFCs.

The Vendor shall deliver a product that is IPv6 compatible.

The Vendor shall provide the ability to monitor traffic in an encryption scheme.

The Vendor shall provide, within a pre-negotiated period, upgrades and patches to the protocol stack
as vulnerabilities are identified to maintain the established level of system security.
Post-contract award, the Vendor shall provide an independent third-party security validation of the
IPv6 implementations (e.g., using fuzzing techniques).
Post-contract award, the Vendor shall mitigate all vulnerabilities discovered during the testing of the
IPv6 implementations and provide documentation of the results.


### FAT Measures

The Vendor shall verify and provide documentation of physical and cyber security features including,
but not limited to, authentication, encryption, access control, event and communication logging,
monitoring, and alarming to protect the system from unauthorized modification or use.

The Vendor shall verify and provide documentation that all validated security updates and patches are
installed and tested at the start of the FAT.
The Vendor shall verify and provide documentation that all unused software and services are
removed or disabled.

Post-FAT, the Vendor shall create a baseline of the system communications and configuration
including, but not limited to cyber security features, software, protocols, ports and services and provide
documentation describing each item.

The Vendor shall verify through cyber security scans of the system and provide documentation that
the addition of security features does not adversely affect adequate connectivity, latency, bandwidth,
response time, and throughput.

The Vendor shall provide documentation of the results of the independent third-party security
validation of the IPv6 implementations.

The Vendor shall verify that FAT procedures include validation and documentation of the
requirements.


### SAT Measures

The Vendor shall verify and provide documentation of and changes to physical and cyber security
features, including but not limited to, authentication, encryption, access control, event and communication
logging, monitoring, and alarming to protect the system computer from unauthorized modification or use.

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

The Vendor shall supply maintenance capabilities for delivered system security features.
The Vendor shall document all additions and changes to the remote access equipment during the
warranty/maintenance period.

The Vendor shall provide, within a pre-negotiated period, upgrades and patches to the protocol stack
as security issues are identified to maintain the established level of system security.

The Vendor shall create a baseline of the updated system communications and configuration
including, but not limited to, cyber security features, software, protocols, ports, and services and provide
documentation describing any changes.

The Vendor shall verify and provide documentation that any Vendor-configured or manufacturer
default accounts, usernames, passwords, security settings, security codes, and other access methods are
changed, disabled, or removed.

The Vendor shall validate permissions and security settings on the baseline system before delivery of
any upgrades or replacements to maintain the established level of system security.
The Vendor shall document all additions and changes to the remote access equipment during the
warranty/maintenance period.


### References

NERC CIP-005-1 R1, “Electronic Security Perimeter.”

NERC CIP-005-1 R2, “Electronic Access Controls.”
NERC CIP-006-1 R1, “Physical Security of Critical Cyber Assets.”
NERC CIP-007-1 R2, “Ports and Services.”
NERC CIP-007-1 R3, “Security Patch Management.”
NERC CIP-007-1 R5, “Account Management.”
NERC CIP-007-1 R8, “Cyber Vulnerability Assessment.”
NIST Special Publication 800-53 Revision 1, “Recommended Security Controls for Federal Information
Systems,” Appendix F: AC-2, AC-3, IA-2, IA-5.
RFC 793, Transmission Control Protocol.
RFC 791, Internet Protocol.
RFC 793, Transmission Control Protocol.
RFC 4301, Security Architecture for the Internet Protocol.


### Dependencies

Section 2.2, “Host Intrusion Detection Systems.”
Section 3.1, “Firewalls.”
Section 3.2, “Network Intrusion Detection System.”
Section 4.3, “Password/Authentication Policy and Management.”
Section 12, “Network Partitioning.”


## 10.4 Web-based Interfaces

Many control systems have Web-based interfaces for performing some tasks.


### Basis

Web-based interfaces to control systems are gaining popularity and are often poorly designed and
configured, making these interfaces vulnerable to exploits.


### Language Guidance

Web applications are often vulnerable to injection attacks of several varieties including command
injection, Remote File Include (RFI) and Cross-Site Scripting (XSS). Web applications with a database
back-end commonly mishandle Structured Query Language (SQL) statements as well, allowing SQL
injection. In addition, the HTTP servers on which these applications are hosted can be vulnerable to
buffer overflows or other memory corruption attacks. Another common mistake in Web applications is
directory traversal, which allows attackers access to more files than the programmer intended. Web
applications in embedded devices are often written in a low-level language like C and are potentially
vulnerable to buffer overflows.
Other non-HTTP services also are commonly included (e.g., FTP, TELNET) on devices, and the
combination of these services can lead to greater information disclosure or other attacks.

Authentication. Web interfaces typically contain a large amount of configuration and site-specific
information. Therefore, authentication is essential to prevent an attacker from gaining more knowledge
about the system. Poorly implemented interfaces using default passwords can completely undermine the
security provided by authentication. Authentication can also be circumvented by SQL injection and XSS
flaws, allowing an attacker to gain database access that can lead to database corruption or a full
compromise of the host or device.

RFI. Remote File Include (RFI) vulnerabilities are only present, except in rare circumstances, in
applications written in the PHP (hypertext preprocessor) scripting language. When an RFI attack is
successful, it results in the attacker running arbitrary PHP scripts on the Web server; this is usually
equivalent to full-host compromise.

Input Validation. String input validation is needed to prevent command injection, which can lead to
complete host compromise. Like SQL injection, command injection can be accomplished by inputting
characters that the application treats specially. The specific characters used will depend on the target
system, but commonly include those in the following (nonexhaustive) list: $ % ! ` ; ' " \. Flaws of this
nature are usually easy to find, are relatively simple, and provide access to an attacker as the user running
the HTTP server. When combined, these factors make command injection a dangerous vulnerability that
must be addressed.

Cross-Site Scripting (XSS). There are two basic types of XSS: reflected and persistent. In a reflected
XSS vulnerability, the attacker must convince a user to visit a malicious Web site or click on a malicious
link. The persistent variety, in which the exploit is stored on the target server itself, is less common but
more likely to succeed in a control system environment because using the Web application is sufficient to
trigger the exploit. Regardless of how XSS is launched, it works by running JavaScript on the user’s
browser in the context of the target Web page. This allows an attacker to steal the user’s cookies, thereby
gaining access as that user.
Like other types of software, Web applications need to be designed and developed with security in
mind.


### Procurement Language

The Vendor shall provide physical and cyber security features including, but not limited to,
authentication, encryption, access control, event and communication logging, monitoring, and alarming to
protect the system from unauthorized modification or use.
The Vendor shall clearly identify the physical and cyber security features and provide the
methodologies for maintaining the features including the methods to change settings from the
Vendor-configured or manufacturer default conditions.

The Vendor shall verify that the addition of security features does not adversely affect connectivity,
latency, bandwidth, response time, and throughput, including during the SAT when connected to existing
equipment.

The Vendor shall remove or disable all software components and services that are not required for the
operation and maintenance of the devices that run an HTTP server prior to the FAT. The Vendor shall
provide documentation on what is removed and/or disabled.

The Vendor shall provide, within a pre-negotiated period, appropriate software and service updates
and/or workarounds to mitigate all vulnerabilities associated with the product and to maintain the
established level of system security.

The Vendor shall verify and provide documentation that the SIS is certified after incorporating the
security devices.

The Vendor shall provide documentation of input sanitization for all Web-form inputs including, but
not limited to, measures for prevention of command injection, SQL injection, directory traversal, RFI,
XSS, and buffer overflow.

The Vendor shall follow secure coding practices and reporting for all Web-based interface software
(see Section 5.1). This requirement includes both Web applications and Web servers.

The Vendor shall provide user configurable and managed passwords (see Section 4.3).

The Vendor shall provide an independent third-party security code validation of all Web-based
interface software (see Section 5.1).


### FAT Measures

The Vendor shall verify and provide documentation of physical and cyber security features including,
but not limited to, authentication, encryption, access control, event and communication logging,
monitoring, and alarming to protect the system from unauthorized modification or use.

The Vendor shall verify and provide documentation that all validated security updates and patches are
installed and tested at the start of the FAT.
The Vendor shall verify and provide documentation that all unused software and services are
removed or disabled.

Post-FAT, the Vendor shall create a baseline of all communications to and from any device running
an HTTP server and configuration including, but not limited to cyber security features, Web-based
interfaces, software, protocols, ports, and services and provide documentation describing the functionality
of each item.

The Vendor shall verify through cyber security scans of the system and provide documentation that
the addition of security features does not adversely affect adequate connectivity, latency, bandwidth,
response time, and throughput.

The Vendor shall provide documentation of the results of the independent third-party security code
validation for all Web application and Web server software.

The Vendor shall verify that FAT procedures include validation and documentation of the
requirements.


### SAT Measures

The Vendor shall verify and provide documentation of and changes to physical and cyber security
features including, but not limited to, authentication, encryption, access control, event and communication
logging, monitoring, and alarming to protect the system from unauthorized modification or use.

Post-SAT, the Vendor shall create a baseline of all communications to and from any device running
an HTTP server and configuration including, but not limited to, cyber security features, Web-based
interfaces, software, protocols, ports, and services and provide documentation describing any changes.

The Vendor shall verify through cyber security scans of the system and provide documentation that
the addition of security features does not adversely affect adequate connectivity, latency, bandwidth,
response time, and throughput when connected during the SAT.

The Vendor shall verify and provide documentation that any Vendor-configured or manufacturer
default accounts, usernames, passwords, security settings, security codes, and other access methods are
changed, disabled, or removed at the start of the SAT.
The Vendor shall verify and provide documentation that all unused software and services are
removed or disabled.

The Vendor shall verify that SAT procedures include validation and documentation of the
requirements.


### Maintenance Guidance

The Vendor shall create a new baseline of all Web-based interfaces and provide documentation
explaining any changes to the functionality of each interface.

The Vendor shall create a new baseline of all communications to and from any device running an
HTTP server and provide documentation explaining any changes to the functionality of each service and
protocol.

The Vendor shall create a baseline of the updated system communications and configuration
including, but not limited to, cyber security features, software, protocols, ports, and services and provide
documentation describing any changes.

The Vendor shall verify and provide documentation that any Vendor-configured or manufacturer
default accounts, usernames, passwords, security settings, security codes, and other access methods are
changed, disabled, or removed.

The Vendor shall provide, within a pre-negotiated period, upgrades and patches to the Web
applications as security issues are identified to maintain the established level of system security.

The Vendor shall validate permissions and security settings on the baseline system before delivery of
any upgrades or replacements to maintain the established level of system security.

The Vendor shall supply maintenance capabilities for delivered system security features.
The Vendor shall document all additions and changes to the remote access equipment during the
warranty/maintenance period.


### References

None. This topic is stand-alone.


### Dependencies

Section 4.1, “Disabling, Removing, or Modifying Well-Known or Guest Accounts.”
Section 4.3, “Password/Authentication Policy and Management.”
Section 5.1, “Coding for Security.”


## 10.5 Virtual Private Networks

Virtual private networks (VPNs) allow for secure or trusted communications over an unsecured or
untrusted infrastructure such as the Internet. The advantages of such systems are confidentiality, integrity,
and availability. A poorly configured VPN creates easily exploitable vulnerabilities. The term VPN is a

very large category that includes any mechanism that creates a logical division where there is not a
physical division of a network. This situation creates a subnetwork that is not accessible by members of
the network who are not part of the subnetwork. This large category encroaches on the category of
network partitioning. This section will concentrate on the subcategory of VPN limited to the encrypted
tunneling of traffic through untrusted networks. Examples of where this type of VPN is useful are:
   Site-to-site control system communication over an unsecured communication line (i.e., Internet).
   Nonlocal Vendor support of a deployed control system.


### Basis

The primary vulnerability of any VPNs is the end-points. If one end-point is compromised, then the
entire VPN is potentially compromised.


### Language Guidance

The main components that make a VPN secure are encrypted traffic and protected authentication
mechanism. The authentication method used can be security token, known key, securely distributed
certificate, password, or combination of any of these methods. Once the authentication is complete, the
VPN should encrypt all traffic between end-points to ensure no data are leaked and prevent MitM attacks.
Multifactor identification and authentication is strongly advised to neutralize the effectiveness of
brute-force attacks. A common multifactor identification is a combination of a security token, known key,
or certificate and a password, PIN, or biometrics.

When using any statically assigned authentication value such as password, PIN, certificate, etc., the
value must never be communicated in plain text through an untrusted network.

With the addition of encryption comes the reduction in ability to monitor communications. Some
installations need to be able to monitor all communications to and from the installation site. When
encrypting the VPN communication, the standard firewall and IDS may not be able to inspect the contents
of the VPN communication. Most VPNs can have monitoring software installed on the server or an end­
point to record the pre-encrypted traffic.

Additional security measures may be necessary when partitioning a network that contains a VPN
server. As such, VPN server placement and ownership should be agreed upon for each VPN that is being
deployed. A good solution is to place the VPN server in a DMZ separate from the control network and
allow a user on it to connect onto the control network using the authentication process required for a user
who is accessing the network locally.

VPNs are strongly affected by firewall rules and as such should be considered when requesting
firewall solutions. The form of VPN affects the ability to filter traffic on the firewall. VPNs that are
created on Layer 3, like IPSec, can only be filter-based on IP addresses, protocol number, and entropy.
VPNs that are created on Layer 4, like those based on SSL, can be filter on the aforementioned properties
plus port numbers and additional TCP/UDP properties. The actual filtering effectiveness may not improve
with additional properties; however, the ability to route traffic through Network Address Table (NAT)
firewalls usually improves with additional properties.


### Procurement Language

The Vendor shall provide physical and cyber security features including, but not limited to,
multifactor authentication (e.g., security token, known key, and/or certificate), encryption, access control,
event and communication logging, monitoring, and alarming to protect the system and configuration
computer from unauthorized modification or use.

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

The Vendor shall provide a DMZ outside the control network for the VPN server to reside.
The Vendor shall use different authentication methods for establishing control network access and
VPN connection.


### FAT Measures

The Vendor shall verify and provide documentation of physical and cyber security features including,
but not limited to, multifactor authentication (e.g., security token, known key, and/or certificate),
encryption, access control, event and communication logging, monitoring, and alarming to protect the
system and configuration computer from unauthorized modification or use.

The Vendor shall verify and provide documentation that all validated security updates and patches are
installed and tested at the start of the FAT.

The Vendor shall create a baseline of the delivered system communications and configuration
including, but not limited to, cyber security features, software, protocols, ports, and services and provide
documentation describing each item.

Post-FAT, the Vendor shall create a baseline of the delivered system communications and
configuration including, but not limited to, cyber security features, Web-based interfaces, software,
protocols, ports, and services and provide documentation describing the functionality of each item.
The Vendor shall verify and provide documentation that all unused software and services are
removed or disabled.

The Vendor shall verify that FAT procedures include validation and documentation of the
requirements.


### SAT Measures

The Vendor shall verify and provide documentation of and changes to physical and cyber security
features, including but not limited to, authentication, encryption, access control, event and communication
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

The Vendor shall provide, within a pre-negotiated period, upgrades and patches as security issues are
identified to maintain the established level of system security.

The Vendor shall create a baseline of the updated system communications and configuration
including, but not limited to, cyber security features, software, protocols, ports, and services and provide
documentation describing any changes.

The Vendor shall verify and provide documentation that any Vendor-configured or manufacturer
default accounts, usernames, passwords, security settings, security codes, and other access methods are
changed, disabled, or removed.

The Vendor shall validate permissions and security settings on the baseline system before delivery of
any upgrades or replacements to maintain the established level of system security.

The Vendor shall supply maintenance capabilities for delivered system security features.
The Vendor shall document all additions and changes to the remote access equipment during the
warranty/maintenance period.


### References

RFC 2341, “Cisco Layer Two Forwarding (Protocol) ‘L2F.’”
RFC 2637, “Point-to-Point Tunneling Protocol.”
RFC 2661, “Layer Two Tunneling Protocol ‘L2TP.’”
RFC 2764, “A Framework for IP Based Virtual Private Networks.”
RFC 4026, “Provider Provisioned Virtual Private Network (VPN) Terminology.”


### Dependencies

Section 2.6, “Installing Operating Systems, Applications, and Third-Party Software Updates.”
Section 3.1, “Firewalls.”
Section 4.3, “Password/Authentication Policy and Management.”
Section 12, “Network Partitioning.”


## 10.6 Serial Communications Security

Many protocols are used for both serial and Ethernet communications.


### Basis

Researchers have demonstrated that the protocols used in serial communications can be exploited to
gain control of network devices. These devices can then be leveraged by an attacker to gain further
control of the network.


### Language Guidance

When a vulnerability is found in one of these protocols (usually over Ethernet) it is often overlooked
in the serial realm. Mitigation strategies must be employed to prevent exploitations from occurring within
the serial domain. These mitigation strategies often involve patching applications supporting the protocol
or the protocol itself. Field communication devices (e.g., front-end processor [FEP], data acquisition
processor, protocol converter, or data concentrator) are often interconnected, which can provide an
attacker with greater access to the control system after a compromise has occurred.

Because of the legacy issues with serial protocols, the protocols are commonly excluded in cyber
security standards. Vulnerable end-point protocols create a larger attack surface due to the distribution of
serial devices over a large geographic area.

Link encryptors are used to protect field communications (e.g., bump-in-the-wire devices).


### Procurement Language

The Vendor shall provide physical and cyber security features including, but not limited to,
authentication, encryption, access control, event and communication logging, monitoring, and alarming to
protect the serial communications and communication devices from unauthorized modification or use.
The Vendor shall provide an independent third-party validation of all software running on field
communication devices (see Section 5.1).
The Vendor shall clearly identify the physical and cyber security features and provide the
methodologies for maintaining the features, including the methods to change settings from the
Vendor-configured or manufacturer default conditions.

The Vendor shall verify through security scans of the field communications that the addition of
security features does not adversely affect connectivity, latency, bandwidth, response time, and
throughput specified for serial communications, including during the SAT when connected to existing
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

The Vendor shall verify and provide documentation of physical and cyber security features, including
but not limited to authentication, encryption, access control, event and communication logging,
monitoring, and alarming to protect the serial communications and communication devices from
unauthorized modification or use.

The Vendor shall provide documentation of the independent third-party validation of all software
running on field communication devices (see Section 5.1).

The Vendor shall verify and provide documentation that all validated security updates and patches are
installed and tested at the start of the FAT.
The Vendor shall verify and provide documentation that all unused software and services are
removed or disabled.

Post-FAT, the Vendor shall create a baseline of the system communications and configuration
including, but not limited to, cyber security features, software, protocols, ports and services and provide
documentation describing each item.

The Vendor shall verify through cyber security scans of the system and provide documentation that
the addition of security features does not adversely affect adequate connectivity, latency, bandwidth,
response time, and throughput.

The Vendor shall verify that FAT procedures include validation and documentation of the
requirements.


### SAT Measures

The Vendor shall verify and provide documentation of any changes to physical and cyber security
features including, but not limited to authentication, encryption, access control, event and communication
logging, monitoring, and alarming to protect the device and configuration computer from unauthorized
modification or use.

Post-SAT, the Vendor shall create a baseline of all serial communications and configuration
including, but not limited to, cyber security features, software, protocols, ports, and services and provide
documentation describing any changes.

The Vendor shall verify and provide documentation that any Vendor-configured or manufacturer
default accounts, usernames, passwords, security settings, security codes, and other access methods are
changed, disabled, or removed.

The Vendor shall verify through cyber security scans of the system and provide documentation that
the addition of security features does not adversely affect adequate connectivity, latency, bandwidth,
response time, and throughput for field communications when connected during the SAT.

The Vendor shall verify that SAT procedures include validation and documentation of the
requirements.

The Vendor shall test and install all validated security updates and patches at the start of the SAT.


### Maintenance Guidance

The Vendor shall provide, within a pre-negotiated period, upgrades and patches as security issues are
identified to maintain the established level of system security.

The Vendor shall create a baseline of the updated system communications and configuration
including, but not limited to, cyber security features, software, protocols, ports, and services and provide
documentation describing any changes.

The Vendor shall verify and provide documentation that any Vendor-configured or manufacturer
default accounts, usernames, passwords, security settings, security codes, and other access methods are
changed, disabled, or removed.

The Vendor shall validate permissions and security settings on the baseline system before delivery of
any upgrades or replacements to maintain the established level of system security.

The Vendor shall supply maintenance capabilities for delivered system security features.
The Vendor shall document all additions and changes to the remote access equipment during the
warranty/maintenance period.


### References

None. This topic is stand-alone.


### Dependencies

Section 4.3, “Password/Authentication Policy and Management.”
Section 5.1, “Coding for Security.”
