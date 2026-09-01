# 12. Network Partitioning

> Control category from *Cyber Security Procurement Language for Control Systems* (DHS/ICS-CERT, Sept 2009). Each control follows the 8-part topical template. See [`../docs/topical-template.md`](../docs/topical-template.md).


## 12.1 Network Devices

Network devices are used to allow communication between other networked devices and networks.


### Basis

The devices used to create, interconnect, segregate, protect, and isolate networks have operating
systems (e.g., embedded operating system) and applications (e.g., port security, address blocking) that are
susceptible to the same vulnerabilities and exploits found in most computer-based devices. Once deployed
and functioning, if patch management for these devices is not rigorous, the devices will be left vulnerable
to new exploits.


### Language Guidance

Routers are network devices designed to direct network traffic between devices on separate networks.
These devices have two or more routing interfaces and may connect to separate dedicated
telecommunication equipment. Routers may implement additional capabilities such as ACL, port
mirroring (e.g., span port), and some firewall functions. Advanced routers are able to operate in a failover
or redundant configuration with another router to prevent communication failure. Routers include a
method of interface configuration via a connected network or separate console port. These devices also
contain an embedded operating system, which is held in nonvolatile firmware. Upgrades to the firmware
may be performed over a network or a directly connected port. Vulnerabilities have been found in the
embedded operating systems for routers requiring the need for updates. Exploits on the operating systems
(e.g., resetting routers) have also been performed. ACLs are commonly used with routers for a layer of
security. For a high-security network, a whitelist ACL is recommended.

Hubs or network concentrators are network devices that direct network traffic to all other devices
connected within a network. These devices duplicate each received network packet and repeat it to every
device connected to the hub. Hubs allow one connected device to communicate at a time. Multiple
transmissions from several hosts can cause collisions that are detected by the hub. Most small hubs do not
contain configuration information or firmware that can be upgraded by the end user. Advanced hubs
allow management and firmware upgrades through a connected network or console port. Hubs are
commonly used for multiple taps into a network (e.g., running two IDSs).

Switches are network devices that direct network traffic to other connected devices within a network.
Switches have different switching speeds including 10, 100, 1000, or 10000 megabits per second (Mbps).
Switches can have multiple media connections such as copper for lower bandwidth connections and fiber
for high bandwidth connections. Switches can be managed or unmanaged. Unmanaged or “dumb”
switches inspect received data packets, determine the destination device of that packet, and forward it to
the appropriate port (i.e., L2 switches). Managed switches offer features such as virtual LAN (VLAN)
segments, link aggregation, port mirroring, and other advanced networking capabilities (i.e., L3 switches).
VLAN network segments implement the IEEE 802.1Q protocol for moving data between layer two
networks. This allows hosts to be connected to different switches, but communicate as if the hosts share a
common switch. Link aggregation or “trunking” refers to a method of moving multiple VLAN segments
between switches or routers. This allows a single physical connection to carry multiple virtual network
segments between devices. Port mirroring is a method by which data from one or many different switch

ports is “mirrored” onto another port for monitoring and debugging. IDSs, Intrusion Prevention Systems
(IPSs), and network analyzers are normally connected to these ports. Managed switches can be controlled
from a connected network port, separate console port, or an embedded Web-based interface. Managed
switches contain an embedded operating system that is upgradeable via the configuration vectors. The
embedded operating systems on switches are vulnerable to exploits that may allow access to a connected
system or resetting of the switch. Port security can be enabled on switches when one MAC address is
uniquely configured to one network port. This provides a layer of security for rogue devices being
plugged into the switch.

Network security devices include firewalls, IDS, IPS, and VPN concentrators. These devices are used
to segment and protect networks.

Firewalls are network security devices used to separate and control traffic between two or more
networks or devices. These devices include features such as packet filtering, stateful packet inspection,
and traffic flooding protection. Firewalls differ from routers in that firewalls are optimized to look inside
packets for specific content, whereas router ACLs only look at packet headers to determine if a packet is
filtered or not. A high security network firewall would have a “deny all” rule set. Firewall rule sets are
frequently over complicated. Keeping network segments small, simple, and current aids in the firewall
rule complexity issues. Firewalls generate logs that need to be reviewed to verify the firewall is working
properly and no new unfiltered traffic exists (see Section 3.1).

NIDSs are security devices that monitor traffic on a network segment or multiple segments. IDS
appliances use signatures and anomaly-based intelligence to determine unauthorized or abnormal traffic
activities on a network segment to generate alerts. NIDSs are commonly used in conjunction with a
firewall to verify the proper function of the firewall. NIDSs produce logs of packet traffic that need to be
reviewed for identifying unexpected packets (see Section 3.2).

Network intrusion prevention systems (NIPSs) are security devices that monitor traffic on a network
segment or multiple segments and use signatures and anomaly-based intelligence to block unauthorized or
abnormal traffic. IPS appliances are usually configured inline with a network connection to actively block
traffic in contrast to an IDS that passively monitors and alerts on traffic. Reporting by exception
communication method is common for many control systems. Anomaly-based NIPSs are rarely used
since these would block traffic during a time when all end devices need to make a status report.

VPN concentrators are network devices designed to securely allow local network access to remote
users. These systems build an encrypted tunnel between a local network and a remote host after a secure
authentication or secure key exchange process. VPN concentrators are the preferred secure method for
allowing remote users access to local network resources. Because firewalls and IDS cannot inspect
encrypted packets, exploit code can be sent through an encrypted tunnel without detection. ACL routers
can verify IP header information only on encrypted packets (see Section 10.6).


### Procurement Language

The Vendor shall provide a method for managing the network devices and changing addressing
schemes.

The Vendor shall verify and provide documentation that the network configuration management
interface is secured.

The Vendor shall provide ACLs, port security address lists, and enhanced security for the port
mirroring.

The Vendor shall remove or disable unused network configuration and management functions on the
network devices.

The Vendor shall provide firewall rules for inbound and outbound traffic based on deny-all rule sets.

The Vendor shall provide NIDS rules and log review tools that verify the function of the firewall and
detect anomalous traffic.

The Vendor shall provide a NIPS architecture that will work with the communication method.

The Vendor shall provide VPN concentrators configured with filters and port security.

Post-contract award, the Vendor shall provide documentation on the network devices installed with
security settings.


### FAT Measures

The Vendor shall validate the method for managing the network devices and changing network
addresses.
The Vendor shall verify security levels and provide documentation of the network configuration
management interface.

The Vendor shall verify the ACLs, port security address lists, and describe the enhanced security for
the port mirroring.

The Vendor shall scan the network ports and document traffic origination and functions for each port.

The Vendor shall provide documentation of firewall rules and IDS rules.

The Vendor shall verify and provide documentation of the log review tools validating IDS and
firewall functions.

The Vendor shall verify and provide documentation of the NIPS architecture validating operations
with normal and emergency control system communications.

The Vendor shall verify and provide documentation of the VPN architecture filters and port security.

The Vendor shall provide upgrades and patches to maintain the established level of system security.


### SAT Measures

The Vendor shall validate the method for managing the network devices and changing network
addresses.
The Vendor shall verify security levels and provide documentation of the network configuration
management interface.

The Vendor shall verify and provide documentation of the ACLs, port security address lists, and
describe the enhanced security for the port mirroring.

The Vendor shall scan the network ports and document traffic origination and functions for each port.

The Vendor shall verify and provide documentation of firewall rules and IDS rules.

The Vendor shall verify and provide documentation of the log review tools validating IDS and
firewall functions.

The Vendor shall verify and provide documentation of the NIPS architecture validating operations
with normal and emergency control system communications.

The Vendor shall verify and provide documentation of the VPN architecture verifying filters and port
security.

The Vendor shall provide upgrades and patches to maintain the established level of system security.


### Maintenance Guidance

The Vendor shall provide upgrades and patches to maintain the established level of system security.

The Vendor shall validate permissions and security settings on the baseline system before delivery of
any upgrades or replacements.


### References

NIST Special Publication 800-53 Revision 2, “Recommended Security Controls for Federal Information
Systems.”
Department of Homeland Security, Recommended Practice Control Systems Cyber Security Defense in
Depth Strategies, May 2006. r


### Dependencies

Section 3.1, “Firewall.”
Section 3.2, “Network Intrusion Detection System.”
Section 3.3, “Canaries.”
Section 10.5, “Virtual Private Networks.”


## 12.2 Network Architecture

Network architecture is how a network is designed and segmented into logical smaller functional
subnetworks (subnets).


### Basis

Poorly designed network architectures are vulnerable to exploits.


### Language Guidance

Subnets are small functional groupings of network-attached devices usually connected to the same
switch or group of switches. Subnets can contain any number of devices up to 16,777,214. Subnets are
classified as Class A, B, or C depending on the size of the IP address space and netmask. Private,
non-Internet routable addresses are usually assigned to devices without direct accessibility from the
Internet. Private nonroutable addresses are defined as 10.X.X.X, 172.16.X.X, and 192.168.X.X by the
Internet Assigned Number Authority.

r.   http://csrp.inl.gov/Documents/Defense%20in%20Depth%20Strategies.pdf

A demilitarized zone (DMZ) is a separate network subnet designed to expose specific services to a
larger, untrusted network. The subnets are used in large corporations to safely expose functions to the
Internet, such as Web or database applications. DMZs also are used internal to networks to facilitate
secure data transfer from a high security network zone to a zone with lower security. A DMZ uses explicit
access control and contains computer hosts that provide network services to both low and high-security
network zones. DMZ networks are usually implemented with a firewall or other traffic routing network
device. It can be split into several sub-DMZ networks with specific functional groupings for the
computers such as Web servers, timeservers, or FTP repositories.

Secure network architectures contain a combination of network segmentation, traffic control, and
traffic monitoring. Segmentation is used to separate functional sets of network hosts into groupings.
Traffic control is implemented with routers and firewalls to prevent unauthorized access between
different subnets. Traffic monitoring validates what traffic is allowed and alerts when unauthorized traffic
is detected.

When segmenting a network, devices associated with a heightened security profile should be grouped
together and separated from devices with a lower security profile. An example would be a corporate
network with tens or hundreds of normal users separated from a server cluster or network that needs
maximum uptime. Data that need to be moved between zones with different security levels should pass
through a third network segment known as a DMZ. The DMZ should be considered to have the lowest
security profile. Network devices hosted in a DMZ should replicate data between the higher security
networks. The DMZ network collectively should consist of several functional DMZ networks with
groupings of network hosts providing similar services. Segmentation is accomplished with firewalls and
routers. Segments requiring heightened security should be segmented using a firewall to prevent
unauthorized traffic between segments.

Traffic control between security zones should be employed with a firewall and use a “default deny”
access policy. This requires all traffic to be dropped unless explicitly allowed with firewall rules. Network
traffic should be specified by source and destination IP address and network port at a minimum. Data
from a DMZ should be replicated over a minimum number of secure protocols.

Traffic monitoring of security zones should be performed inside each logical network segment at the
minimum. For a more robust monitoring solution, both sides of a firewall or router can be monitored as a
way to verify ACLs or firewall filtering rules. DMZ network segments should have an IDS dedicated to
the segment. DMZ IDS logs should be checked often and validated against traffic in and out of the
network. Traffic monitoring inside a static network environment should use whitelisting, port security,
and canaries to enhance security (e.g., DMZ).

Secure control system segmentation should be implemented from the inside out. The control network
is the highest security profile and requires the maximum uptime. A firewall should separate the control
system from all other networks. If data from the control system is needed by another network, data should
be replicated to DMZ in a secure manner such as secure FTP or secure copy. Data allowed though the
firewall should be heavily restricted and only allow the minimum number of open ports and hosts to be
available.

Network simplification should be a priority when designing initial architecture or firewall rules. The
variety of protocols open for data should be kept to a minimum. Data that are modified multiple times and
retransmitted such as database, Web, and FTP, should be moved to the DMZ first, modified in the DMZ,
and transmitted from the DMZ to other networks.


### Procurement Language

The Vendor shall provide and document secure network architecture where the higher security zones
originate communication to less secure zones.

The Vendor shall provide and document the design for all communication paths between networks of
different security zones through a DMZ.

The Vendor shall verify and document that disconnection points are established between the network
partitions and provide the methods to isolate subnets to continue limited operations.

The Vendor shall provide and document tailored filtering and monitoring rules for all security zones
and alarm for unexpected traffic.

The Vendor shall provide and document a DMZ that is restricted to communications where all traffic
is monitored, alarmed, and filtered.

The Vendor shall provide and document outbound filtering and alarms for unexpected traffic through
security zones.

The Vendor shall define all sources and destinations with enforced communication origination even
during restart conditions between security zones.

The Vendor shall provide and document dual DMZ architectures using different products performing
the same functionality running in parallel.

The Vendor shall provide and document a mechanism for patching a single DMZ architecture running
in a parallel configuration without disruption to the other DMZ running in parallel.

Post-contract award, the Vendor shall provide network architecture documentation.


### FAT Measures

The Vendor shall validate and provide documentation that the higher security zones originate
communication to less secure zones.
The Vendor shall document all communication paths, including filtering, monitoring, and staging
zones.

The Vendor shall verify and provide documentation of disconnection points between the network
partitions and validate the continuity of limited operations.

The Vendor shall verify and provide documentation of tailored filtering and monitoring rules for all
security zones and validate alarms for unexpected traffic.

The Vendor shall verify and provide documentation of restricted communications through the DMZ
and verify that all traffic is monitored, alarmed, and filtered.

The Vendor shall verify and provide documentation of outbound filtering and alarms for unexpected
traffic through security zones.
The Vendor shall verify and provide documentation of all sources and destinations with enforced
communication origination even during restart conditions between security zones.

The Vendor shall verify and provide documentation of dual DMZ architectures using different
products performing the same functionality running in parallel.

The Vendor shall verify and provide documentation of a mechanism for patching a single DMZ
architecture running in a parallel configuration without disruption to the other DMZ running in parallel.


### SAT Measures

The Vendor shall validate and provide documentation that the higher security zones originate
communication to less secure zones.
The Vendor shall document all communication paths, including filtering, monitoring, and staging
zones.

The Vendor shall verify and provide documentation of test disconnection points between the network
partitions and validate the continuity of limited operations.

The Vendor shall test and provide documentation of tailored filtering and monitoring rules for all
security zones and validate alarms for unexpected traffic.

The Vendor shall validate and provide documentation of restricted communications through the DMZ
and verify that all traffic is monitored, alarmed, and filtered.
The Vendor shall validate and provide documentation of outbound filtering and alarms for
unexpected traffic through security zones.
The Vendor shall validate and provide documentation of all sources and destinations with enforced
communication origination even during restart conditions between security zones.

The Vendor shall validate and provide documentation of dual DMZ architectures using different
products performing the same functionality running in parallel.

The Vendor shall validate and provide documentation of a mechanism for patching a single DMZ
architecture running in a parallel configuration without disruption to the other DMZ running in parallel.


### Maintenance Guidance

The Vendor shall provide upgrades and patches as vulnerabilities are identified to maintain the
established level of system security.

The Vendor shall reassess permissions and security settings on the baseline configuration before
delivery of any upgrades or replacement components.

The Vendor shall verify and provide documentation that the network security architecture’s security
profile is maintained.


### References

NERC CIP-007-1, “Cyber Security — Systems Security Management.”
NIST Special Publication 800-53 Revision 2, “Recommended Security Controls for Federal Information
Systems.”
Department of Homeland Security, Recommended Practice Control Systems Cyber Security Defense in
Depth Strategies, May 2006.


### Dependencies

Section 3.1, “Firewall.”
Section 3.2, “Network Intrusion Detection System.”
