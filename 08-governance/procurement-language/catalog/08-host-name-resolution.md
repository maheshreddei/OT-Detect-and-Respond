# 8. Host Name Resolution

> Control category from *Cyber Security Procurement Language for Control Systems* (DHS/ICS-CERT, Sept 2009). Each control follows the 8-part topical template. See [`../docs/topical-template.md`](../docs/topical-template.md).


## 8.1 Network Addressing and Name Resolution

Each computer in a network has a unique IP address. Remembering each address for each computer
in a network is difficult, so addresses are often mapped to host names, which are easier to remember.
DNS servers translate the host name used by people to the IP address used by computers. IP addresses can
be assigned statically or can be allocated dynamically from a pool of addresses using DHCP. The most
widely used DNS software is Berkeley Internet Name Domain (BIND) produced by Internet Software
Consortium (ISC), although other packages exist, including Microsoft DNS.


### Basis

DNS servers are susceptible to many types of cyber exploits including spoofing, cache poisoning, and
denial of service (DoS) attacks. In a spoofing attack, an attacker, who has obtained DNS zone data (the
name to IP address mapping), creates packets that appear to come from a valid address. The attacker can
then redirect clients by appearing as the legitimate name server. Cache poisoning involves polluting the
cache on the DNS server with erroneous data to redirect traffic to a server under the control of the
attacker. In a DoS attack, the attacker floods the DNS server with recursive queries. Eventually, the DNS
service is no longer available. m


### Language Guidance

To protect against DNS exploits, DNS servers for the internal control system network should reside
inside the firewall and should be separate from the DNS servers on the corporate network. DNS servers
for the control system network should be authoritative for the address space of the control system network
only. That is, the DNS servers should contain the complete zone information (name to IP address
mappings) only for hosts on the control system network. Ideally, the control system network is isolated
and hosts will not need to resolve external names. However, if hosts need to resolve names for hosts
outside the trusted control system network, queries should go to the control system DNS server, which
will forward the queries through the firewall to a DNS server on the corporate network.

DNS servers are typically set up as a minimum configuration in pairs for failover and reliability. A
master server and a slave server make up the pair. The master server contains the original zone data, and
zone transfers are made to the slave server when changes occur. As mentioned above, IP addresses can be
assigned statically or dynamically. If possible, static addressing schemes should be used in control system
networks. Dynamic addressing results in frequent IP address changes, and thus, frequent zone updates and
transfers. Zone updates and transfers can provide a potential avenue for an attacker to modify DNS
records or to gain information about the network. With dynamic addressing, the zone data on the master
server are updated automatically with DHCP. With static addressing, zone data changes can be made
manually by a system administrator, eliminating potential vulnerabilities associated with automatic
updates. Also, the stable IP addresses associated with static addressing results in fewer zone transfers.
Regardless of whether static or dynamic addressing is used, restrictions should be placed on both master

m. Microsoft, “Securing DNS for Windows 2003,”
<http://technet2 microsoft.com/WindowsServer/en/Library/fea46d0d-2de7-4da0-9c6f-2bb0ae9ca7e91033 mspx?mfr=true>.

and slave servers to only allow zone transfers to trusted hosts. In addition, transaction signatures should
be used to authenticate zone transfers by adding cryptographic signatures. n

Considerations for securely configuring DNS are summarized by o :
    Using dedicated servers for DNS and related services and disable all unneeded services.
    Using the latest software builds with current patches.
    Backing up and reviewing DNS configuration files periodically and running integrity checks to verify

the integrity of configuration files, zone data, and other DNS files.
    Running DNS servers as a user other than a root. Enabling access controls to allow only specific

individuals to create, delete, or modify DNS data.
    Enabling cache pollution prevention.
    Restricting addresses that can query control system DNS servers to control system hosts.
    Restricting zone transfers to only trusted hosts and authenticating zone transfers.
    Using a static addressing scheme. If dynamic addressing is used, allow dynamic updates from only

trusted hosts.
    Configuring the firewall to allow communication between the control system and corporate DNS

servers only on UDP and TCP Port 53.
    Allowing special considerations for hosts with multiple IP addresses for redundancy.


### Procurement Language

Pre-contract award, the Vendor shall provide recommended network addressing and name resolution
methodology.
The Vendor shall provide a means to verify the integrity of configuration files, zone data, and other
DNS files (e.g., such integrity checking may be done with a HIDS).

Post-contract award, the Vendor shall provide a configured DNS server(s) or the information to
configure a DNS server(s) that meets a pre-negotiated standard of security.

The Vendor shall consider addressing information as business sensitive and protect it as such.


### FAT Measures

The Vendor shall install and run Vendor-supplied DNS servers continuously during the entire FAT
process.

The Vendor shall verify all domain servers, and hosts within the domain involved in testing are
resolvable by all client and server systems connected to the network.

The Vendor shall document both forward (hostname to IP address) resolution and reverse (IP address
to hostname) resolution.

n.   RFC 2845: Secret Key Transaction Authentication for DNS (TSIG).
o.   Allen Householder et al., “Securing an Internet name server,” August 2002, http://www.cert.org/archive/pdf/dns.pdf; Cheng
C. Teoh, “Defense in Depth for DNS,” 2003, http://www.sans.org/reading room/whitepapers/dns/.


### SAT Measures

The Vendor shall run the DNS server during the entire SAT process.

The Vendor shall verify all domain servers and hosts within the domain involved in testing are
resolvable by all client and server systems connected to the network.

The Vendor shall document both forward (hostname to IP address) resolution and reverse (IP address
to hostname) resolution.


### Maintenance Guidance

The Vendor shall provide an ongoing patch management process for DNS and related services such
as DHCP.


### References

NIST Special Publication 800-53 Revision 2, “Recommended Security Controls for Federal Information
Systems.”
NIST Special Publication 800-81, “Secure Domain Name System (DNS) Deployment Guide.”


### Dependencies

Section 2.1, “Removal of Unnecessary Services and Programs.”
Section 2.2, “Host Intrusion Detection System.”
Section 2.6, “Installing Operating Systems, Applications, and Third-Party Software Updates.”
