# 3. Perimeter Protection

> Control category from *Cyber Security Procurement Language for Control Systems* (DHS/ICS-CERT, Sept 2009). Each control follows the 8-part topical template. See [`../docs/topical-template.md`](../docs/topical-template.md).


## 3.1 Firewalls

Firewalls are used to stop unauthorized connections, or to allow limited communications between two
networks or from a network to a networked device. Firewalls fall into four broad categories: packet filters,
circuit level gateways, application level gateways, and stateful multilayer inspection firewalls. Firewalls
can be implemented in software, hardware, or a combination of both.


### Basis

Overly permissive, nonexistent, or unpatched firewalls create vulnerabilities by allowing
unauthorized access.


### Language Guidance

Firewalls are network devices, which block selective (filter) traffic between network zones (subnets)
or from a network to a device. Historically, firewalls, or simple “screening routers,” blocked traffic based
on IP address and port combinations.

Although any network device that filters traffic may be referred to as a firewall; modern usage
typically assumes some advanced potentials beyond these rudimentary capabilities. These are often
described as “application aware,” “stateful inspection,” or other Vendor variations. These capabilities take
into account not only the IP addresses and ports used in a connection, but track the address that originated
a connection (allowing control of direction), state of the connection, and any number of other factors.
Advanced products also perform verification of the packet payload (which means verifying that
higher-level protocols are enforced) and provide protection to specific protocols such as simple mail
transfer protocol (SMTP), file transfer protocol (FTP), and others. Although most commercial products
provide only limited protection for industrial protocols, such as those commonly used in control system
networks, this is changing as manufacturers respond to market demand.

Firewalls produce traffic logs that are vital for network monitoring. All traffic through the firewall
needs to be logged, including outbound traffic. These logs, if effectively and efficiently designed to be
used with HIDS, NIDS, application logs, etc., are essential for forensic purposes.

Network Appliances or “all in one solutions” can combine antivirus, firewall, and NIDS functionality.
The signature file updates for such appliances are large and can rarely be sent over a control system
network. Testing signature updates on a nonproduction system can be completed to verify limitations of
signature file size. In such instances, alternative methods of updating signature files may be necessary.


### Procurement Language

The Vendor shall provide firewalls and firewall rule sets between network zones or provide firewall
rule sets if the firewalls are not provided by the Vendor.

The Vendor shall provide firewall rule sets and/or other equivalent documentation. The basis of the
rule set shall be “deny all,” with exceptions explicitly identified by the Vendor. This information is
deemed business sensitive and shall be protected as such.

Post-contract award, the Vendor shall provide detailed information on all communications (including
protocols) required through a firewall, whether inbound or outbound, and identify each network device
initiating a communication in accordance with the corresponding rule sets.


### FAT Measures

The Vendor shall install the firewall(s) or the configuration(s) and run the firewall(s) continuously
during the entire FAT process for Vendor-supplied firewall(s), or Vendor-provided firewall
configuration(s).

The Vendor shall verify that FAT procedures include exercising this functionality, examining the log
files, and validating the results.

The Vendor shall verify that FAT procedures include validation and documentation of the
requirements.


### SAT Measures

The Purchaser shall run the firewall(s) during the entire SAT process.

The Vendor shall verify that SAT procedures include exercising this functionality, examining the log
files, and validating the results.

The Vendor shall verify that SAT procedures include validation and documentation of the
requirements. Any Vendor-configured or manufacturer default usernames, passwords, or other security
codes must be changed at this time.


### Maintenance Guidance

There shall be an ongoing patch management and signature update process.


### References

NERC CIP-005-1 R1, “Electronic Security Perimeter.”
ANSI/ISA-99.00.01, “Security for Industrial Automation and Control Systems Part 1: Terminology,
Concepts, and Models,” Sections 3.5, 5.
ISA-99.00.02 (DRAFT), Security for Industrial Automation and Control Systems: Part 2: Establishing an
Industrial Automation and Control Systems Security Program,” Sections B.1, B.14, C.3, D.4.
NIST Special Publication 800-41 Rev. 1, “Guidelines on Firewalls and Firewall Policy (Draft).”
NIST Special Publication 800-82, “Guide to Industrial Control Systems (ICS) Security,” Final Public
Draft.


### Dependencies

Section 4.1, “Disabling, Removing, or Modifying Well-Known or Guest Accounts.”


## 3.2 Network Intrusion Detection System

A NIDS is used to identify unauthorized or abnormal network traffic.


### Basis

Firewalls or other vulnerabilities may allow unauthorized access, which are detectable by a NIDS.


### Language Guidance

A NIDS is not always part of a control system. It can be included as part of the higher-level IT
infrastructure, and thus outside the scope of this guide. This section assumes the NIDS is part of the
control system network.

There are two basic types of NIDSs: signature and anomaly-based. Signature-based NIDSs are similar
to antivirus and vulnerability scanners in that only known signatures are detected. The signatures are
essentially strings of code known to be indicative of malicious traffic. Anomaly-based NIDSs function on
historically based network traffic and alarm when traffic is outside of the expectations. Anomaly-based
NIDSs require running a network to record known, good traffic to which to compare future traffic. The
challenge for anomaly-based detection is defining what is normal. This makes it very difficult to establish
a baseline if normal network behavior constantly changes. However, anomaly-based NIDSs work well for
deterministic networks with few report-by-exception events.

As with any appliance that can generate voluminous logs, the configuration of the NIDS is a minor
effort as compared to the degree of effort required for ongoing log reviews. Log review and notification
software tools may be appropriate to semi-automate the review of voluminous data.


### Procurement Language

Pre-contract award, the Vendor shall provide a recommended placement of the NIDS within the
control system network.
The Vendor shall provide traffic profiles with expected communication paths, network traffic, and
expected utilization boundaries, for anomaly-based NIDSs.

The Vendor shall provide appropriate signatures, for signature-based NIDSs.

Post-contract award, the Vendor shall provide a configured NIDS and/or provide the information to
configure a NIDS.


### FAT Measures

The Vendor shall install the NIDS or the configuration(s) and run the NIDS continuously during the
entire FAT process for Vendor-supplied NIDSs, or Vendor-provided NIDS configuration(s).

The Vendor shall verify that FAT procedures include exercising this functionality, examining the log
files, and validating the results.

The Vendor shall verify that FAT procedures include validation and documentation of the
requirements.


### SAT Measures

The Vendor shall run the NIDS(s) during the entire SAT process to include exercising this
functionality, examining the log files, and validating the results.

The Vendor shall document the results of tuning signatures and adjusting thresholds to reduce false
positives and minimize false negatives.

The Vendor shall verify that SAT procedures include validation and documentation of the
requirements. Any Vendor-configured or manufacturer default usernames, passwords, or other security
codes must be changed at this time.


### Maintenance Guidance

The Vendor shall tune signatures and adjust thresholds to reduce false positives and minimize false
negatives.
The Vendor shall update the NIDS configuration and/or documentation as needed when changes are
made.


### References

NERC CIP-005-1 R1, “Electronic Security Perimeter.”
ANSI/ISA-99.00.01, “Security for Industrial Automation and Control Systems Part 1: Terminology,
Concepts, and Models,” Sections B.10, C.3.
NIST Special Publication 800-12, “An Introduction to Computer Security: The NIST Handbook.”
NIST Special Publication 800-82, “Guide to Industrial Control Systems (ISC) Security,” Final Public
Draft.
NIST Special Publication 800-94, “Guide to Intrusion Detection and Prevention Systems (IDPS).”


### Dependencies

Section 4.1, “Disabling, Removing, or Modifying Well-Known or Guest Accounts.”


## 3.3 Canaries

Honey pots (which analyze unauthorized connections) and/or Canary(ies) (which flag that a
connection attempt has taken place) have been implemented in certain network configurations to provide
passive network monitoring.


### Basis

Canaries enhance network traffic screening since most signatures created for a NIDS are immature
and only detect proper protocol versions limiting network-monitoring capabilities.


### Language Guidance

Canaries only work in a static address topology or where dynamic host configuration protocol
(DHCP) is not used. It is not recommended that retaliatory devices or actions (poison boxes) be used.
Canary(ies) can be a stand-alone computer or an unused network interface card (NIC) in existing
hardware.


### Procurement Language

Pre-contract award, the Vendor shall provide a recommended placement of the canary(ies) within the
control system network.

The canary(ies) shall be configured with alerting software to indicate unauthorized connection
attempts.

Post-contract award, the Vendor shall provide a configured canary(ies) or information to configure a
canary(ies).


### FAT Measures

The Vendor shall install the canary(ies) or the configuration(s) and run the canary(ies) continuously
during the entire FAT process for Vendor-supplied canary(ies) or Vendor-provided canary
configuration(s).

The Vendor shall verify that FAT procedures include exercising this functionality, examining the log
files, and validating the results.

The Vendor shall verify that FAT procedures include written validation and documentation of the
requirements.


### SAT Measures

The Vendor shall run the canary(ies) during the entire SAT process.

The Vendor shall verify that SAT procedures include exercising this functionality, examining the log
files, and validating the results.

The Vendor shall verify that SAT procedures include written validation and documentation of the
requirements. Any Vendor-configured or manufacturer default usernames, passwords, or other security
codes must be changed at this time.


### Maintenance Guidance

The Vendor shall reconfigure canary(ies) as needed when network address topologies change.


### References

NERC CIP-005-1 R2, “Electronic Access Controls.”


### Dependencies

Section 2.2, “Host Intrusion Detection Systems.”
Section 3.2, “Network Intrusion Detection System.”
