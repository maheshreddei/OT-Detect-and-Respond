# 13. Wireless Technologies

> Control category from *Cyber Security Procurement Language for Control Systems* (DHS/ICS-CERT, Sept 2009). Each control follows the 8-part topical template. See [`../docs/topical-template.md`](../docs/topical-template.md).


## 13.1 Bluetooth Technology

Bluetooth technology is a short-range, wireless communications technology that can simultaneously
handle both data and voice transmissions. This allows it to be used for both hands-free voice calls and
data applications such as printing and synchronizing laptops, PDAs, or other mobile devices. Bluetooth
technology allows Bluetooth-enabled electronic devices to connect and communicate wirelessly with a
limited number of other similar devices, within proximity, as they dynamically enter and leave radio
proximity.


### Basis

Bluetooth is designed as a cable replacement and personal area networking technology that allows
freedom in placing devices without concern for running cables. Bluetooth broadcasts in the Industrial
Scientific and Medical (ISM) band at 2.4 to 2.485 GHz, similar to other devices such as microwave ovens
and cordless telephones. ISM is a license-free frequency band. Wireless technologies all have a common
security risk in that anyone in the broadcasting area can intercept the transmission. Bluetooth-enabled
devices have additional security risks, in that these provide a gateway to larger networks and other
devices not using Bluetooth. Like other wireless technologies, security is provided using encryption,
authentication, and configuration control.


### Language Guidance

Bluetooth wireless technology is a short-range communications technology intended to replace the
cables connecting portable and/or fixed devices and providing a method for connecting unrelated wireless
and wired devices. The Bluetooth specification defines a uniform structure for a wide range of devices to
connect and communicate with each other. However, the implementation of the Bluetooth specification
may vary from manufacturer to manufacturer (i.e., all Bluetooth implementations are not the same).

Bluetooth-enabled electronic devices connect and communicate wirelessly through short-range
networks. It uses a frequency hopping spread spectrum technology to minimize the possibility of
interference in the ISM band and encryption at the link or application levels to provide confidentiality and
integrity for the transmitted data. Each device can simultaneously communicate with up to seven other
devices within a single network. Line-of-sight (LoS) is not required. Most Bluetooth-enabled devices use
omni-directional antennas for the communication, eliminating orientation issues. Each device can belong
to several networks simultaneously.

A complete Bluetooth application requires a Bluetooth controller (i.e., hardware device) that typically
connects to a host computer through a USB port, and additional services and higher-level protocols,
known as the Bluetooth host, that are installed as software on the same host computer. Without proper
configuration, Bluetooth can allow any other Bluetooth device within radio proximity to access the
system.

Security for a Bluetooth network is implemented through the frequency band hops, authentication,
and encryption. The frequency hopping makes it difficult to eavesdrop. User authentication controls
access to the network. The encryption provided is implemented using custom algorithms based on the
SAFER+ block cipher and is secured at the 1, 40, and 64 bit levels.


### Procurement Language

When providing the Bluetooth-enabled device, the vendor shall meet the Bluetooth specification and
the related documentation.

Post-contract award, the Vendor shall provide specific protocols and other detailed information
required for the Bluetooth-enabled device to communicate with the control network, including other
wireless equipment that can communicate with the Vendor-supplied device.

The Vendor shall provide documentation on the range of the Bluetooth-enabled device, power
requirements, and the designated frequency of operation for each device.

The Vendor shall define interoperability limits for the Bluetooth-enabled device. This includes
specifying what equipment the Bluetooth-enabled device could replace, what additional hardware or
software is required to make the replacement, and any problems or limitations that may be introduced.
Limitations related to new functionality being introduced into the control system must also be specified.

The Vendor shall provide, within a pre-negotiated period, any test data with analysis associated with
the Bluetooth-enabled device.

The Bluetooth-enabled device shall be provided with security devices, such as passwords or security
codes, to protect the device from unauthorized access, modification or use. The Vendor shall clearly
identify these security devices and methods to change them from the Vendor-configured or manufacture
default conditions.

The Vendor shall identify the configuration control options that enable varying of the security level of
the device.
The Vendor shall remove or disable all software artifacts that are not required for the operation and
maintenance of the device prior to the FAT.

The Vendor shall provide the Purchaser SAT procedures, which include exercising all functionality
and calibration procedures.

The quality of the implementation of the Bluetooth specification may vary from manufacturer to
manufacturer (i.e., all Bluetooth implementations are not the same). The Vendor shall provide test data
showing that basic attacks, such as malformed packet injection, do not cause the receiving Bluetooth
device to crash, hang, or otherwise malfunction.


### FAT Measures

The FAT shall be performed per written procedures agreed upon by the Purchaser.

For Vendor-supplied Bluetooth-enabled device, the Vendor shall install the device and run it
continuously during the entire FAT process.

The Vendor shall ensure that FAT procedures include exercising all functionality and examining the
input or output, and validating the results. The Vendor will specify when the results are achieved at peak
performance or are environment dependent.

The Vendor shall ensure that FAT procedures include written validation and documentation of each
requirement.


### SAT Measures

The Purchaser shall perform the SAT testing in accordance with Vendor-supplied procedures.

The Purchaser shall change any Vendor-configured or manufacturer default usernames, passwords, or
other security codes at this time. The Vendor shall ensure that SAT procedures include written validation
and documentation of this requirement.


### Maintenance Guidance

The Vendor shall supply current system configuration to the Purchaser to allow traceability and to
ensure no extra services are installed.
The Vendor shall supply written maintenance guidelines for the device, including a timeline,
maintenance equipment required, and as-installed parameters and settings.

The Vendor shall provide upgrades and patches to the Bluetooth-enabled device as vulnerabilities are
identified in order to maintain the identified level of system security.


### References

Bluetooth Special Interest Group, https://www.bluetooth.org/apps/content/, Web page accessed
September 2009.
Bluetooth Specifications,
http://bluetooth.com/Bluetooth/Technology/Works/Core Specification v30.htm, Web page accessed
April 2009.
Bluetooth Host Controller Interface (HCI), http://www.palowireless.com/infotooth/tutorial/hci.asp. Web
page accessed September 2009.
Bluetooth Security, C. Gehrmann, J. Persson, B. Smeets, Artech House, 2004.
Bluetooth Profiles, D. Gratton, Prentice Hall Publishers, 2003.
Gehrmann, C., J. Persson, B. Smeets, Bluetooth Security, Artech House, 2004.
Gratton, D., Bluetooth Profiles, Prentice Hall Publishers, 2003.
Palo Wireless, “Host Controller Interface (HCI),” http://www.palowireless.com/infotooth/tutorial/hci.asp,

Web page accessed September 2009.


### Dependencies

Section 13.5, “ZigBee Technology.”


## 13.2 Wireless Closed-Circuit TV Technology

Wireless closed-circuit TV (WCCTV) is a technology that uses video cameras and wirelessly
transmits a visual signal to a specific, limited set of monitors. WCCTV is often used for surveillance in
areas that need monitoring


### Basis

Because of infrastructure, terrain, or immediate need, wired video systems are often inadequate,
making wireless video systems a viable option. Because WCCTV devices transmit wirelessly, they are

subject to interception, modification, or destruction of the signals, and care should be taken with their
configuration and use.


### Language Guidance

In industrial plants, WCCTV systems may be used to observe parts of a process that are remote from
a control room, or where the environment is not comfortable for humans. WCCTV systems are also used
for intelligence gathering, in contaminated environments, and for training purposes.
A WCCTV system is less dependent on the environment and infrastructure. It can be installed and
moved with less difficulty, giving it an advantage in temporary or short-term applications.

The visual signal may be transmitted using wireless technology in combination with the IP, rather
than transmission over traditional analog frequencies. A typical IP video network includes both fixed and
pan-tilt-zoom (PTZ) cameras (i.e., either IP cameras or analog cameras attached to IP encoders), network
video recorders (NVR) and viewing platforms. The use of video, in combination with data and voice, has
a tremendous impact on network design and performance because of bandwidth, latency, and jitter
requirements. The bandwidth necessary for the network varies based on the resolution, frames per second
(fps) desired and codec used, as well as the motion content of the video.


### Procurement Language

The Vendor shall provide the WCCTV system and associated documentation.

Post-contract award, the Vendor shall provide specific protocols and other detailed information
required for the WCCTV to communicate with the control network, including other wireless equipment
that can communicate with the WCCTV.

The Vendor shall provide documentation on the range of the WCCTV, power requirements, and the
designated frequency of operation for each device.

The Vendor shall provide, within a pre-negotiated period, any test data with analysis associated with
the mobile radio.

The Vendor shall provide the Purchaser SAT procedures that include exercising all functionality and
calibration procedures.

The Vendor shall document the equipment configuration.

The vendor shall provide configuration specifications for implementing encryption and authentication
between the cameras and the network and specifically note all security measures associated with the
system.

The Vendor shall provide multiple levels of Quality of Service (QoS) that enable customization for
specific mission-critical applications.

The Vendor shall provide advanced video compression techniques, such as MPEG4 and H.264, which
can dramatically reduce the bandwidth requirements for video.


### FAT Measures

The FAT shall be performed per written procedures agreed upon by the Purchaser.

The Vendor shall ensure that the systems have had a minimum of a 48-hour burn-in.

The Vendor shall perform an interference rejection test and supply the results with an explanation of
the results.

The Vendor shall ensure that FAT procedures include exercising all functionality and examining the
input and output, and validating the results.

The Vendor shall verify compatibility of the WCCTV with other devices with which the device must
interface.


### SAT Measures

The Purchaser shall perform the SAT testing in accordance with Vendor-supplied procedures.

The Purchaser shall change any Vendor-configured or manufacturer default usernames, passwords, or
other security codes at this time. The Vendor shall ensure that SAT procedures include written validation
and documentation of this requirement.

The SAT shall verify that the installed system meets the specified requirements.


### Maintenance Guidance

The Vendor shall supply current system configuration to the Purchaser to allow traceability and to
ensure no extra services are installed.
The Vendor shall supply written maintenance guidelines for the device, including a timeline,
maintenance equipment required, and as-installed parameters and settings.

The Vendor shall provide upgrades and patches to the wireless device as vulnerabilities are identified
in order to maintain the identified level of system security.


### References

IEEE 802.11 n. latest draft -
http://ieeexplore.ieee.org/xpl/freeabs all.jsp?tp=&arnumber=5089380&isnumber=5089379
IEEE 802.11 n current released version -
http://ieeexplore.ieee.org/xpl/freeabs all.jsp?tp=&isnumber=14251&arnumber=654749&punumber=
5258
MPEG-4 – The Media Standard, http://www.m4if.org/public/documents/vault/m4-out-20027.pdf.


### Dependencies

Section 13.2, “802.11 Technology.”


## 13.3 Radio Frequency Identification Technology

Radio frequency identification (RFID) describes the use of radio frequency signals to provide
automatic identification and tracking of items. RFID is a method of identifying and/or tracking an item
(equipment, device, or other physical object) by remotely receiving information stored in a tag on the
object.


### Basis

RFID has some of the same type of weaknesses as other wireless technologies, though in practice
most current RFID installations are configured with the transmitting device and the reader in very close
proximity to each other. Nevertheless, vulnerabilities still exist. Besides being vulnerable to common
attacks such as eavesdropping, MitM, and DoS, RFID technology is, in particular, susceptible to spoof
and power attacks.


### Language Guidance

RFID tags are small silicon microchips attached to an antenna, which emit information using radio
waves over short distances. Miniature RFID tags can be embedded in many types of assets and scanned
from between two to three meters away, depending on several factors, revealing information about the
asset.
RFID tags consist of an integrated circuit for storing and processing information, modulating and
demodulating the signal and an antenna or coil for receiving and transmitting the signal.

RFID tags are normally classified as passive, active, or semipassive. Passive tags require no internal
power source. They receive power to transmit the stored information from the reader. Semipassive and
active tags require an internal power source, usually a small battery.

RFID systems also can be classified by frequency ranges. Low-frequency (30 kHz to 500 kHz)
systems have short reading ranges and lower system costs and high-frequency (850 MHz to 950 MHz and
2.4 GHz to 2.5 GHz) systems, offering long read ranges (greater than 90 feet), high reading speeds, and
higher system costs.

Most current RFID systems are not secure due to their primary mission (i.e., inventory of materials).
In cases where they perform a secure function, such as tracking hazardous materials being used in a
process, special care should be used in specifying and procuring these systems.


### Procurement Language

The Vendor shall provide the RFID system and associated documentation.

Post-contract award, the Vendor shall provide specific protocols and other detailed information
required for the RFID device to communicate with the control network, including other wireless
equipment that can communicate with the Vendor-supplied device.

The Vendor shall provide documentation on the range of the RFID device and power requirements.

The Vendor shall provide, within a pre-negotiated period, any test data with analysis associated with
the RFID system.

The RFID system shall provide encryption of radio signals. The Vendor shall clearly identify these
security devices and methods to change them from the Vendor-configured or manufacture default
conditions.

The Vendor shall provide the Purchaser SAT procedures that include exercising all functionality and
calibration procedures.

The Vendor shall document the equipment configuration and specifically note any security measures
associated with the system (encryption devices, password protection, etc.).

The Vendor shall identify how eavesdropping, MitM, and DoS attacks, including spoofing and power
attacks, are mitigated with their technology.


### FAT Measures

The FAT shall be performed according to written procedures agreed upon by the Purchaser.

The Vendor shall ensure that the systems have had a minimum of a 48-hour burn-in.

The Vendor shall perform an interference rejection test and supply the results with an explanation of
the results.

The Vendor shall ensure that FAT procedures include exercising all functionality and examining the
input or output, and validating the results.
The Vendor shall verify compatibility of the RFID system with other devices with which the device
must interface.


### SAT Measures

The Purchaser shall perform the SAT testing in accordance with Vendor-supplied procedures.

Any Vendor-configured or manufacturer default usernames, passwords, or other security codes shall
be changed at this time.

The SAT shall verify that the installed system meets the specified requirements.


### Maintenance Guidance

The Vendor shall supply current system configuration to the Purchaser to allow traceability and to
ensure no extra services are installed.
The Vendor shall supply written maintenance guidelines for the RFID system, including a timeline,
maintenance equipment required, and as-installed parameters and settings.

The Vendor shall provide upgrades and patches to the RFID system as vulnerabilities are identified in
order to maintain the identified level of system security.


### References

EPCGlobal, http://www.epcglobalinc.org/standards/, Web last accessed May 4, 2009.
ISO/IED 18000-2, ISO/IED 18000-3.
ISO/IEC 11784-11785.
ISO/IEC 10536.
“RFID Business Applications,” RFID Journal, http://www.rfidjournal.com/article/articleprint/1334/-1/1,
Web last accessed May 4, 2009.
L. Batina, J. Guajardo, T. Kerins, N. Mentens, P. Tuyls, and I.Verbauwhede, “Public-Key Cryptography

for RFID-Tags,” In RFID Security: Techniques,Protocols and System-On-Chip Design, P. Kitsos, and
Y. Zhang (eds.), Springer-Verlag, 34 pages, 2008.

J. Schroeter, Demystifying UHF Gen 2 RFID, HF RFID, June 02, 2008,

http://www.industrialcontroldesignline.com/howto/208802188;jsessionid=D4CZJQQUZQBDEQSN

DLQSKH0CJUNN2JVN, Web last accessed May 4, 2009.


### Dependencies

None. This topic is stand-alone.

13.4     802.11 Technology


### Basis

The reference, 802.11, refers to a family of specifications developed by IEEE for wireless local area
network (WLAN) technology. It specifies a wireless interface between a wireless device and a base
station (access point) or between two wireless devices (peer to peer). 802.11 devices operate in the 5 GHz
and 2.4 GHz public spectrum bands. Because these transmissions are through the air, these can be
intercepted or interfered with by those having the proper equipment.


### Language Guidance

There is only one current 802.11 standard. It is denoted by IEEE 802.11 followed by the date that it
was published. The standard is updated by means of amendments. When a wireless device is referred to
as 802.11x, x is an amendment to the original 802.11 standard. As of this date, IEEE 802.11-2007 is the
most current 802.11 document available and contains cumulative changes (802.11a,b,d,e,g,h,i,j) from
multiple subletter task groups. Care must be exercised when defining the 802.11 standard in procurement
documents to be sure of the latest version.

The 802.11 standard, hereafter referred to as 802.11, defines the MAC and physical layers for a LAN
with wireless connectivity where the connected devices are within close proximity to each other.

The Basic Service Set is the basic component of an 802.11 wireless LAN. The Basic Service Set
consists of a group of stations. The station is the basic component of the WLAN. It is any device that
provides the 802.11 protocol (MAC, physical layers, and a connection to the wireless device). The station
might be a personal computer, handheld device, or an access point and may be mobile or stationary.

Security is provided by encryption, authentication, and configuration control. The encryption methods
used are Wired Equivalent Privacy (WEP), WiFi Protected Access (WPA), or WPA2. WEP can be easily
intercepted and decoded. Numerous free software tools exist to aid in such endeavors. Due to these
weaknesses, enhanced security was introduced for Wireless Fidelity (WiFi) networks through the WPA
protocol. The security of connections using this protocol depends largely on the strength of the user-
supplied pass-phrase. Free software and descriptions of how to attack these connections also are available
online. Improving upon previous security implementations, the WiFi Alliance released the WPA2
standard, which uses a stronger encryption algorithm.

Despite the availability of strong encryption for user communication, the management frames of
IEEE 802.11 messages are not encrypted, leaving the door open for DoS attacks. Several tools are
available that can cause users to drop off the network or send messages to hamper the functionality of
wireless end points. Such tools include WiFi jammers, designed to block IEEE 802.11 transmissions, and
rogue access points, that are set up in hopes of attracting connections then stealing sensitive information
or altering communications. Adding to and enabling attacks is the fact that WiFi access points are often
set up quickly and without security foresight. This results in the use of weak or no encryption, allowing
attackers to impersonate wireless end points in hopes of providing false data. It also may result in users

not changing default passwords for device management, allowing attackers to gain full control of the
access point as default passwords are common knowledge. Recently, researchers have considered the
possibility of worms that use the aforementioned security weaknesses to propagate on the local network.
Such malicious code would rely on two assumptions to propagate. First, in urban settings, numerous WiFi
networks exist within close proximity of one another. Second, that victim machines are configured to
connect to multiple networks.


### Procurement Language

The Vendor shall provide the WiFi device, meeting the requirements of the required sections of IEEE
802.11, and associated documentation.

Post-contract award, the Vendor shall provide specific protocols and other detailed information
required for the WiFi device to communicate with the control network, including other wireless
equipment that can communicate with the Vendor-supplied device.

The Vendor shall provide documentation on the range of the WiFi device, power requirements, and
the designated frequencies of operation for each device.

The Vendor shall allow and recommend alarm settings in accordance to the needs of the system.

The Vendor shall define interoperability limits for the WiFi device specifically stating the devices
that could be replaced and any associated problems that might be associated with the replacement.

The Vendor shall provide, within a pre-negotiated period, any test data with analysis associated with
the WiFi device.

The WiFi device shall be provided with security devices, such as passwords or security codes, to
protect the device from unauthorized modification or use. The Vendor shall clearly identify these security
devices and methods to change them from the Vendor-configured or manufacture default conditions.

The Vendor shall provide the WiFi device with the standard security measures as specified in the
802.11 standard and support the required level of encryption.
The Vendor shall remove or disable all software artifacts that are not required for the operation and
maintenance of the device prior to the FAT.

The Vendor shall provide the Purchaser SAT procedures, which include exercising all functionality
and calibration procedures.

The Vendor shall document the equipment configuration and specifically note any security measures
associated with the system (encryption devices, password protection, etc.).

The Vendor shall identify the configuration control options that enable varying of the security level of
the device.

The Vendor shall demonstrate that cooperative WiFi nodes can distinguish jamming from channel
saturation and provide operational alerts.

The Vendor shall provide test data with analysis showing that basic attacks such as malformed packet
injection, do not cause the WiFi device to crash, hang, or otherwise malfunction.


### FAT Measures

The FAT shall be performed per written procedures agreed upon by the Purchaser and in agreement
with the requirements of the specified sections of 802.11.

For Vendor-supplied WiFi device, the Vendor shall install the device and run it continuously during
the entire FAT process.

The Vendor shall ensure that the systems have had a minimum of a 48-hour burn-in.

The Vendor shall perform an interference rejection test and supply the results with an explanation of
the results.

The Vendor shall ensure that FAT procedures include exercising all functionality examining the input
or output, and validating the results.

The Vendor shall verify compatibility of the WiFi device with other interfaced devices.


### SAT Measures

The Purchaser shall run the 802.11 system during the entire SAT process. SAT procedures shall
include exercising this functionality, examining the log files, and validating the results.

Any Vendor-configured or manufacturer default usernames, passwords, or other security codes must
be changed at this time. The Vendor shall ensure that SAT procedures include written validation and
documentation of this requirement.

The Purchaser shall perform the SAT testing in accordance with Vendor-supplied procedures.

The SAT shall verify that the installed system meets the specified requirements.

The Purchaser shall perform testing to: analyze the potential for radio frequency interference,
determine adequate wireless LAN coverage, and set configuration parameters properly.


### Maintenance Guidance

The Vendor shall supply current system configuration to the Purchaser to allow traceability and to
ensure no extra services are installed.
The Vendor shall supply written maintenance guidelines for the device, including a timeline,
maintenance equipment required, and as-installed parameters and settings.

The Vendor shall provide upgrades and patches to the WiFi device as vulnerabilities are identified in
order to maintain the identified level of system security.


### References

Aime, M., G. Calandriello, A. Lioy, Dependability in Wireless Networks, IEEE Security and Privacy,
January/February 2007.
Akriditis, P, et al., Proximity Breeds Danger: Emerging Threats in Metro-area Wireless Networks, 2007,
http://www.usenix.org/events/sec07/tech/full papers/akritidis/akritidis html/metrowifi.html, Web
page accessed September 2009.

Bellardo, J. and S. Savage, “802.11 Denial-of-Service Attacks: Real Vulnerabilities and Practical

Solutions,” 2003, www.cs.ucsd.edu/~savage/papers/UsenixSec03.pdf, Web page accessed

September 2009.
Gizmodo.com, Gadgets: Wireless Jammer, July 28, 2005, http://gizmodo.com/gadgets/gadgets/wireless­
jammer-114698.php, Web page last accessed September 2009.
IEEE 802.11, “The Working Group for WLAN Standards,” Institute of Electrical and Electronics
Engineers, 2007.
IEEE Std 802.11i-2004, “Part 11: Wireless LAN Medium Access Control (MAC) and Physical Layer
(PHY) specifications Amendment 6: Medium Access Control (MAC) Security Enhancements,”
Institute of Electrical and Electronics Engineers, 2007.
Infrostream Technologies, Cellphone Jammers, WIFI/Bluetooth Jammers, Wireless Camera Hunter,

http://www.infostream.biz/ Web page last accessed September 2009.
Kirk, J. 'Evil twin' Wi-Fi access points proliferate, April 2007,

http://www.networkworld.com/news/2007/042507-infosec-evil-twin-wi-fi-access.html, Web page last

accessed September 2009.
Teska, T., How To Crack WPA / WPA, January 2008,
http://www.smallnetbuilder.com/content/view/30278/98/, Web page last accessed September 2009.
Vladimirov, A., K. Gavrilenko, and A. Mikhailovsky, 2004, WiFoo: The Secrets of Wireless Hacking,
Person/Addison Wesley, http://www.wi-foo.com, Web page accessed March 2009.
WiFi Alliance, WPA2 (WiFi Protected Access 2), 2007, http://www.wi-fi.org/knowledge center/wpa2,
Web page last accessed September 2009.


### Dependencies

None. This topic is stand-alone.
IEEE 802.15/Bluetooth, IEEE 802.11/WLAN and IEEE 802.16/WiMAX technologies are complementary
to each other and each play a unique role in today's wireless communications.


## 13.5 ZigBee Technology


### Basis

ZigBee is a specification for a communication protocol using small, low-power digital radios based
on IEEE 802.15.4 standard. It is more specifically known as Low-Rate Wireless Personal Area Networks
(LR-WPAN) the name for a short-range, low-power, low-cost, low data-rate wireless multi-hop
networking technology standard. Because these transmissions are through the air, these can be intercepted
or interfered with by those having the proper equipment.


### Language Guidance

The ZigBee Alliance is an association of companies involved with building specifications based on
IEEE 802.15.4. This includes network, security, and application protocols. IEEE 802.15.4 specifies the
physical layer and some of the data link layer. The higher layer protocols, in this case ZigBee, were
developed by the ZigBee Alliance.

The ZigBee specification defines the higher-layer network and application services that build upon
the IEEE 802.15.4 LR-WLAN standard. The networks can range from simple single-hop star topologies
to more complex multi-hop mesh networks. ZigBee operates in the ISM radio bands.

ZigBee network features include: self-organization, support for multi-hop routed networking
topologies, interoperable application profiles, and security based on the Advanced Encryption Standard
(AES).


### Procurement Language

The Vendor shall design and provide a configured ZigBee wireless network, meeting the
requirements of the ZigBee specification, and associated documentation and running on a licensed
frequency. The Vendor shall configure the ZigBee network such that the following conditions are met:
1. The ZigBee network infrastructure shall be protected with a Network Key
2. Address filtering shall be employed at the MAC layer
3. The ZigBee encryption security service shall be utilized
4. Source node authentication shall be implemented
5. A personal area network (PAN) Identifier shall be preassigned and node connectivity shall be
restricted
6. Out-of-band key loading method shall be used
7. Layer-2 security mechanisms supported in the IEEE 802.15.4 lower layer MAC shall be enabled
8. Secure network admission control shall be implemented
9. Nodes with the Trust Center address shall be preconfigured.

Post-contract award, the Vendor shall provide specific protocols and other detailed information
required for the LR-WPAN device to communicate with the control network, including other wireless
equipment that can communicate with the vendor-supplied device.

The Vendor shall provide documentation on the range of the LR-WPAN device, power requirements,
and the designated frequency of operation for each device.

The Vendor shall allow and recommend alarm settings in accordance to the needs of the system.

The Vendor shall define interoperability limits for the LR-WPAN device specifically stating the
devices the LR-WPAN device could replace and any associated problems that might be associated with
the replacement.

The Vendor shall provide, within a pre-negotiated period, any test data h with analysis associated
with the LR-WPAN device.

LR-WPAN device shall be provided with security devices, such as passwords or security codes, to
protect the device from unauthorized modification or use. The Vendor shall clearly identify these security
devices and methods to change them from the Vendor-configured or manufacture default conditions.

The Vendor shall provide the LR-WPAN device with the standard security measures as specified in
the ZigBee standard.
The Vendor shall remove or disable all software artifacts that are not required for the operation and
maintenance of the device prior to the FAT.

The Vendor shall provide the Purchaser SAT procedures that include exercising all functionality and
calibration procedures.

The Vendor shall document the equipment configuration and specifically note any security measures
associated with the system (encryption devices, password protection, etc.).

The Vendor shall identify the configuration control options that enable varying of the security level of
the device.


### FAT Measures

The FAT shall be performed according to written procedures agreed upon by the Purchaser and in
agreement with the requirements of the ZigBee specification.

For Vendor-supplied ZigBee Network or Vendor-provided ZigBee Network configuration(s), the
Vendor shall install the ZigBee Network or the configuration(s) and run the ZigBee Network
continuously during the entire FAT process.

The Vendor shall ensure that FAT procedures include exercising this functionality, examining the log
files, and validating the results.

The Vendor shall ensure that the systems have had a minimum of a 48-hour burn-in.

The Vendor shall perform an interference rejection test and supply the results with an explanation of
the results.

The Vendor shall verify compatibility of the LR-WPAN device with other devices with which the
device must interface.


### SAT Measures

The Purchaser shall run the ZigBee Network during the entire SAT process. SAT procedures shall
include exercising this functionality, examining the log files, and validating the results.

The Purchaser shall change any Vendor-configured or manufacturer default usernames, passwords, or
other security codes at this time. The Vendor shall ensure that SAT procedures include written validation
and documentation of this requirement.


### Maintenance Guidance

Changes may require an update to the ZigBee Network configuration and/or documentation.

The Vendor shall supply current system configuration to the Purchaser to allow traceability and to
ensure no extra services are installed.
The Vendor shall supply written maintenance guidelines for the device, including a timeline,
maintenance equipment required, and as-installed parameters and settings.

The Vendor shall provide upgrades and patches to the LR-WPAN device as vulnerabilities are
identified in order to maintain the identified level of system security.


### References

Daintree Networks, Inc., “Understanding 802.15.4 and ZigBee Networking,”
http://www.daintree.net/resources/index.php#primer, Web page accessed September 2009.

Gutierrez, J., E. Callaway, and R. Barrett, “Low-Rate Wireless Personal Area Networks: Enabling
Wireless Sensors with IEEE 802.15.4™,” IEEE Press, ISN 0-7381-3557-7, 2004.
IEEE 802.15.4-2003 standard: http://grouper.ieee.org/groups/802/15/pub/TG4.html, Web page accessed
September 2009.
IEEE 802.15-2006 revised standard: http://grouper.ieee.org/groups/802/15/pub/TG4b.html, Web page
accessed September 2009.
The ISA Working Group SP100 is developing standards for LR-WPAN industrial wireless technology
and has created a set of application classes based on criticality/consequence for in-plant wireless
systems ISA, http://www.isa.org/wsummit/presentations/SextonVancouverTalk.ppt, Web page
accessed September 2009.
Werb, J., et al., “Improved Quality of Service in IEEE 802.15.4 Mesh Networks,” Sensicast Systems and
GE Global Research, http://www.cs.utexas.edu/~cdj/wia files/submissions/008Final.pdf, Web page
accessed September 2009.
ZigBee Alliance, http://www.ZigBee.org, Web page accessed September 2009.


### Dependencies

Section 13.1, “Bluetooth.”


## 13.6 WirelessHART Technology


### Basis

Wireless Highway Addressable Remote Transducer (HART) is a Wireless Mesh Network
Communications Protocol designed to meet the needs of process automation applications. WirelessHART
is a key part of the HART Field Communications Protocol Revision 7 and is backward compatible with
existing HART devices and applications. The WirelessHART standard was approved on June 2007 and
was released in September 2007.

WirelessHART is in the early stages of development and deployment; hence, there is not much
publicly available information regarding its security. It shall be noted that because the IEEE 802.15.4
protocol is the basis for this technology, the previous IEEE 802.15.4 security analysis is applicable.
WirelessHART like all wireless technologies is subject to the same security issues because of over the air
transmission of data.


### Language Guidance

The architecture of WirelessHART also supports field devices, gateways, and a network manager.
There is a considerable similarity between this standard and the Zigbee standard. Since the creation of the
WirelessHart convergence committee in Industrial Standards Automation (ISA)100, WirelessHART will
likely merge into ISA100. WirelessHART operates in the 2.4 GHz ISM band.

WirelessHART uses IEEE 802.15.4-2006 compatible physical and MAC Layer. Additionally, it
supports hybrid Frequency Hopping SS and Direct Sequence SS. Securing communications is done with
AES-128 block ciphers with individual Join and Session Keys and Data-Link Level Network Key. A
primary objective of the WirelessHART standard is to be directly compatible with existing HART-
enabled equipment, applications, and tools.


### Procurement Language

The Vendor shall provide, within a pre-negotiated period, any test data with analysis associated with
the WirelessHART devices.

The WirelessHART device shall be provided with security devices, such as passwords or security
codes, to protect the device from unauthorized modification or use. The Vendor shall clearly identify
these security devices and methods to change them from the Vendor-configured or manufacture default
conditions.

The Vendor shall provide the WirelessHART device with the standard security measures as specified
in the WirelessHART standard.
The Vendor shall remove or disable all software artifacts that are not required for the operation and
maintenance of the device prior to the FAT.

The Vendor shall provide the Purchaser SAT procedures that include exercising all functionality and
calibration procedures.

The Vendor shall document the equipment configuration and specifically note any security measures
associated with the system (encryption devices, password protection, etc.).


### FAT Measures

The FAT shall be performed per written procedures agreed upon by the Purchaser and in agreement
with the requirements of the WirelessHART specification.

For Vendor-supplied WirelessHART Network or Vendor-provided WirelessHART Network
configuration(s), the Vendor shall install the WirelessHART Network or the configuration(s) and run the
WirelessHART Network continuously during the entire FAT process.

The Vendor shall ensure that FAT procedures include exercising this functionality, examining the log
files, and validating the results.

The Vendor shall ensure that the systems have had a minimum of a 48-hour burn-in.

The Vendor shall perform an interference rejection test and supply the results with an explanation of
the results.

The Vendor shall verify compatibility of the WirelessHART device with other devices with which the
device must interface.


### SAT Measures

The Purchaser shall run the WirelessHART Network during the entire SAT process. SAT procedures
shall include exercising this functionality, examining the log files, and validating the results.

The Purchaser shall change any Vendor-configured or manufacturer default usernames, passwords, or
other security codes at this time. The Vendor shall ensure that SAT procedures include written validation
and documentation of this requirement.


### Maintenance Guidance

Changes may require an update to the WirelessHART Network configuration and/or documentation.

The Vendor shall supply current system configuration to the Purchaser to allow traceability and to
ensure no extra services are installed.
The Vendor shall supply written maintenance guidelines for the device, including a timeline,
maintenance equipment required, and as-installed parameters and settings.

The Vendor shall provide upgrades and patches to the WirelessHART device as vulnerabilities are
identified in order to maintain the identified level of system security.


### References

Hale, G., WirelessHART products out and on the way, InTech Online Magazine, April 24, 2008,
http://www.isa.org/InTechTemplate.cfm?Section=InTech Home1&template=/ContentManagement/C
ontentDisplay.cfm&ContentID=68959, Web page last accessed March 2009.
HART Communication Foundation http://www.hartcomm2.org/index.html.
HART Communication Foundation, WirelessHART Technical Data Sheet, May 15, 2007 HCF_LIT-89,
Revision 1.0B, May 15, 2007.
ISA100, Wireless Compliance Institute, http://www.isa.org/asci/ISA100-Wireless-Compliance-Institute­
Prospectus.pdf Web page last accessed April 2009.


### Dependencies

Section 13.8, “Wireless Mesh Network Technology.”


## 13.7 Mobile Radios


### Basis

Mobile radios refer to wireless communications systems and devices that transmit and receive
information, primarily voice, on radio frequencies. The transmitter and/or the receiver are mobile.
Because these devices transmit wirelessly, these are subject to interception and modification of the
signals.


### Language Guidance

Mobile radios include walkie-talkies, Citizen Band (CB) radios, two-way radios, hand-held two-way
radios, radio telephones, and mobile data transmittal devices. A modern mobile radio consists of a radio
transceiver, housed in a single box, and a microphone with a push-to-talk release-to-listen button. A
mobile radio must have an associated antenna. Other features of mobile radio systems may include: point­
to-multipoint communications, large coverage areas, closed user groups, and use of Very High Frequency
(VHF) or Ultra High Frequency (UHF) bands.

Because these mobile radios are used primarily for voice communication, for this document mobile
data transmittal devices or devices used to transmit sensitive voice communication are of primary
concern. Those devices used for day-to-day voice communication are normally off-the-shelf and include
no security devices such as walkie-talkies and CB radios.

Different types of radio service for mobile radios include Land Mobile Radio and General Mobile
Radio Service (GMRS). Land Mobile Radio is a field radio communications system that uses portable,
mobile, base station, and dispatch console radios typically used by police forces and fire brigades. Land
Mobile Radio devices may be based on such standards as Mobile Professional Mobile Radio (PMR)

Trunk (MPT)-1327, TETRA and APCO 25. GMRS is a licensed land-mobile FM UHF radio service
available for short-distance two-way communication, similar to Family Radio Service radios. GMRS is an
improved walkie-talkie system that shares some frequencies (Channels 1–7) with Family Radio Service.
GMRS radios may be portable, mobile, and base station-style.

Mobile radio Vendors are now offering IP-based mobile radio products. As mobile radios move into
the IP-based digital domain, these products become susceptible to the same communications
vulnerabilities as IP-based computer communications. This evolution, however, given the open network
environment, introduces new security threats.

The following sections pertain only to those systems that transmit/receive sensitive information of
control data. These shall not be used for the procurement or testing of off-the-shelf devices.


### Procurement Language

The Vendor shall provide the wireless mobile radio device and associated documentation.

Post-contract award, the Vendor shall provide specific protocols and other detailed information
required for the mobile radio to communicate with the control network, including other wireless
equipment that can communicate with the Vendor-supplied device.

The Vendor shall provide documentation on the range of the mobile radio, power requirements, and
the designated frequency of operation for each device.

The Vendor shall provide, within a pre-negotiated period, any test data with analysis associated with
the mobile radio.

The mobile radio shall be provided with security devices, such as passwords or security codes, to
protect the device from unauthorized modification or use. The Vendor shall clearly identify these security
devices and methods to change them from the Vendor-configured or manufacture default conditions.
The Vendor shall remove or disable all software artifacts that are not required for the operation and
maintenance of the device prior to the FAT.

The Vendor shall provide the Purchaser SAT procedures, that include exercising all functionality and
calibration procedures.

The Vendor shall document the equipment configuration and specifically note any security measures
associated with the system (encryption devices, password protection, etc.).


### FAT Measures

The FAT shall be performed per written procedures agreed upon by the Purchaser.

The Vendor shall ensure that the systems have had a minimum of a 48-hour burn-in.

The Vendor shall perform an interference rejection test and supply the results with an explanation of
the results.

The Vendor shall ensure that FAT procedures include exercising all functionality and examining the
input or output, and validating the results.

The Vendor shall verify compatibility of the mobile radio with other wireless devices with which the
device must interface.

The Vendor shall ensure that FAT procedures include written validation and documentation of this
requirement.


### SAT Measures

The Purchaser shall perform the SAT testing in accordance with Vendor-supplied procedures.

The Purchaser shall change any Vendor-configured or manufacturer default usernames, passwords, or
other security codes at this time. The Vendor shall ensure that SAT procedures include written validation
and documentation of this requirement.

The SAT shall verify that the installed system meets the specified requirements.


### Maintenance Guidance

The Vendor shall supply current system configuration to the Purchaser to allow traceability and to
ensure no extra services are installed.
The Vendor shall supply written maintenance guidelines for the device, including a timeline,
maintenance equipment required, and as-installed parameters and settings.

The Vendor shall provide upgrades and patches to the wireless device as vulnerabilities are identified
in order to maintain the identified level of system security.


### References

GSM http://en.wikipedia.org/wiki/GSM Web page last accessed April 2009.
MPT 1327, A Signalling Standard for Trunked Private Land Mobile Radio Systems,
http://wiki.radioreference.com/index.php/MPT-1327, Web page last accessed May 2009.
Project 25, “APCO Project 25 and its Project 25 (P25) Standards for Public Safety Digital Radio,”

http://www.apco911.org/frequency/project25/information.html, Web page last accessed March 2009.
TETRA RELEASE 1.3, ETSI 300 392-1 General Design
http://portal.etsi.org/action/pu/20080603/tr 1003921704v010101p.pdf Web page last accessed
April 2009.


### Dependencies

None. This topic is stand-alone.


## 13.8 Wireless Mesh Network Technology


### Basis

A Wireless Mesh Network (WMN) is a communications network made up of radio nodes organized
in a mesh topology. In WMNs, nodes are composed of mesh routers and mesh clients. Each node operates
not only as a host but also as a router, forwarding packets on behalf of other nodes that may not be within
direct wireless transmission range of their destinations.

Potential vulnerabilities exist with route management protocols, remote centralized management
system, and over-the-air firmware upgrades via IP Internet traffic, WMN operating system, and
applications running on any node of the wireless mesh network such as SSH (Secure Shell) daemons or

lightweight Hypertext Transfer Protocol (HTTP) servers. Because the transmissions between WMN nodes
are through the air, they can be intercepted or interfered with by those having the proper equipment.


### Language Guidance

Most, if not all IEEE 802.15.4-based technologies are WMNs. In addition to these networks, there are
also other proprietary mesh network technologies. Regardless of technology, WMNs consist of the end
devices or end nodes that could be a sensor or other asset. These assets are connected to the mesh network
via a wireless router or repeater unit that is used to forward its data to the central host. Typically, these
networks will have a special node called a gateway, which will connect the wireless network to the wire-
line network. WMN integration with the Internet, cellular, IEEE 802.11, IEEE 802.15, IEEE 802.16,
sensor networks, etc., can be accomplished through gateway and bridging functions in the mesh routers.
WMNs provide a method for transport of data by routing the data through adjacent routers/nodes. This
provides wide coverage by multiple smaller cells using wireless nodes to route data.


### Procurement Language

The Vendor shall provide the WMN, meeting the requirements of the required sections of
IEEE 802.11, and associated documentation.

Post-contract award, the Vendor shall provide specific protocols and other detailed information
required for the WMN to communicate with the control network, including any other equipment that can
communicate with the WMN.

The Vendor shall provide documentation on the range of the WMN device, power requirements, and
the designated frequencies of operation for each device.

The Vendor shall allow and recommend alarm settings in accordance to the needs of the system.

The Vendor shall define interoperability limits for the WMN device specifically stating the devices
that could be replaced and any related problems that might be associated with the replacement.

The Vendor shall provide, within a pre-negotiated period, any test data with analysis associated with
the WMN device.

Each WMN device shall be provided with security mechanisms, such as passwords or security codes,
to protect the device from unauthorized modification or use. The Vendor shall clearly identify these
mechanisms and methods to change them from the Vendor-configured or manufacture default conditions.

The Vendor shall provide the WMN device with the standard security measures as specified in the
802.11 standard and support the required level of encryption.
The Vendor shall remove or disable all software artifacts that are not required for the operation and
maintenance of the device prior to the FAT.

The Vendor shall provide the Purchaser SAT procedures which include exercising all functionality
and calibration procedures.

The Vendor shall identify the configuration control options that enable varying of the security level of
the device.

The Vendor shall demonstrate that cooperative WMN nodes can distinguish jamming from channel
saturation and provide operational alerts.

The Vendor shall provide test data showing that basic attacks, such as malformed packet injection, do
not cause the WMN device to crash, hang, or otherwise malfunction.


### FAT Measures

The FAT shall be performed per written procedures agreed upon by the Purchaser and in agreement
with the requirements of the specified sections of 802.11.

For Vendor-supplied WiFi device, the Vendor shall install the device and run it continuously during
the entire FAT process.

The Vendor shall ensure that the systems have had a minimum of a 48-hour burn-in.

The Vendor shall perform an interference rejection test and supply the results with an explanation of
the results.

The Vendor shall ensure that FAT procedures include exercising all functionality and examining the
input or output, and validating the results.

The Vendor shall verify compatibility of the WiFi device with other interfaced devices.


### SAT Measures

The Purchaser shall run the 802.11 system during the entire SAT process. SAT procedures shall
include exercising this functionality, examining the log files, and validating the results.

Any Vendor-configured or manufacturer default usernames, passwords, or other security codes must
be changed at this time. The Vendor shall ensure that SAT procedures include written validation and
documentation of this requirement.

The Purchaser shall perform the SAT testing in accordance with Vendor-supplied procedures.

The SAT shall verify that the installed system meets the specified requirements.

The Purchaser shall perform testing to: analyze the potential for radio frequency interference,
determine adequate wireless WMN coverage, and set configuration parameters properly.


### Maintenance Guidance

The Vendor shall supply current system configuration to the Purchaser to allow traceability and to
ensure no extra services are installed.
The Vendor shall supply written maintenance guidelines for the device, including a timeline,
maintenance equipment required, and as-installed parameters and settings.

The Vendor shall provide upgrades and patches to the WMN device as vulnerabilities are identified in
order to maintain the identified level of system security.


### References

Akyildiz, I., X. Wang, W. Wang, “Wireless Mesh Networks: A Survey,” Elsevier, 2004.
Bahr, M., “Proposed Routing for IEEE 802.11s WLAN Mesh Networks,” WICON’06, The 2nd Annual
International Wireless Internet Conference, Boston, Massachusetts, August 25, 2006.
Edler, J., M. Oskowsky, W. Wang, “Wireless Mesh Network for Building Automation,”

http://wireless.industrial-networking.com/articles/articleprint.asp?id=1264, Web page last accessed

March 2009.
Mogre, P., M. Hollick, R. Steinmetz, “QoS in Wireless Mesh Networks: Challenges, Pitfalls, and
Roadmap to its Realization,” 17th International workshop on Network and Operating Systems
Support for Digital Audio & Video, Urbana-Champaign, Illinois, June 4-5, 2007.


### Dependencies

Section 13.1, “Bluetooth Technology.”
Section 13.2, “802.11 Technology.”
Section 13.5, “ZigBee Technology.”


## 13.9 Cellular Technology


### Basis

Monitoring and controlling equipment occurs at various points within an enterprise. In many cases,
traditional cabled solutions or private radio networks are not a cost-effective option to cover all assets.
Cellular technology may be used to manage and control industrial processes where cabling is not an
option. Although the law provides penalties for the interception of cellular telephone calls, it is easily
accomplished and impossible to detect.


### Language Guidance

A cellular network is a radio network that is composed of radio cells. Cellular technology is being
used in SCADA environments when wide area coverage is required and the cost of alternative
technologies (private radio systems, satellite, etc.) is uneconomical. Cellular is not available in some areas
due to remoteness and lack of customer base.

Cellular modems are available that support both CDMA (Code Division Multiple Access) EVDO
(Evolution Data Only) and GSM (Global System for Mobile Communications) protocols. Cellular routers
may incorporate a cellular modem, or allow one to connect the cellular modem to the router, and support
shared Internet access with multiple Ethernet ports. Packet data may be sent over cellular networks. The
“always on” nature of packet networks makes these cellular packet data networks highly suitable for
monitoring and control applications.

Cellular systems have had prolific growth in the last 10 years. Cellular systems have advanced three
generations and standards are complete for fourth-generation technologies providing ultra high-speed
wireless data. Standards primarily originate from two different technology families, CDMA and GSM.
Despite the differences in the cellular families, both have very similar architectures. The main
characteristic of fourth generation technologies is that the technologies are IP based. Examples include
LTE (Long Term Evolution) and Worldwide Interoperability for Microwave Access (WiMax).

Cellular technologies are categorized by using the term “generation” or G. Some earlier cellular
technologies have had problems with security; however, 3G technologies have improved their security
mechanisms significantly.

3G CDMA (EVDO) technologies include the use of 128-bit privacy and authentication keys. The
Secure Hashing Algorithm-1 (SHA-1) is used for hashing and integrity with CDMA2000 networks (a
hybrid 2.5G/3G network). While the AES algorithm is used for message encryption. GSM uses a similar
encryption and authentication scheme known as the A5/A8 algorithm (a.k.a. A5/1, A5/2).

Some applications of cellular technology are as a cellular bridge or as a cellular gateway. A cellular
bridge is a wireless bridge that uses a public cellular network to connect a remote device to a central host.
These bridges use a cellular modem to provide connectivity. The cellular bridges can connect devices to
an IP network by way of the Internet, or can use e-mail alarms or short message service to transmit and

receive process control information. For instance, a BlackBerry device could be used to view process
variables or control valves in a location that is remote from the user.

The cellular gateway is very similar to the cellular bridge. Cellular gateways use the cellular network
to bring network information to a centralized control system or host, but also provide a separate wireless
network, such as an access point, to support additional wireless devices. Vendor offerings use GPRS,
EDGE or EVDO for the cellular backhaul and WiFi for the WLAN.

The following sections pertain only to those systems that transmit/receive sensitive information of
security or control data. This shall not be used for the procurement or testing of off-the-shelf devices for
routine operations.


### Procurement Language

The Vendor shall provide the cellular system equipment and associated documentation.

Post-contract award, the Vendor shall provide specific protocols and other detailed information
required for the cellular system to communicate with the control network, including other equipment that
can communicate with the cellular system.

The Vendor shall provide documentation on the range of the cellular system, power requirements, and
the designated frequency of operation for each device.

The Vendor shall provide, within a pre-negotiated period, any test data with analysis associated with
the cellular system.

The Vendor shall provide the Purchaser SAT procedures, which include exercising all functionality
and calibration procedures.

The Vendor shall document the equipment configuration and specifically note any security measures
associated with the system (encryption devices, password protection,).


### FAT Measures

The FAT shall be performed per written procedures agreed upon by the Purchaser.

The Vendor shall ensure that the systems have had a minimum of a 48-hour burn-in.

The Vendor shall perform an interference rejection test and supply the results with an explanation of
the results.

The Vendor shall ensure that FAT procedures include exercising all functionality and examining the
input or output, and validating the results.
The Vendor shall verify compatibility of the cellular system with other devices with which the system
must interface.


### SAT Measures

The Purchaser shall perform the SAT testing in accordance with Vendor-supplied procedures.

The Purchaser shall change any Vendor-configured or manufacturer default usernames, passwords, or
other security codes at this time. The Vendor shall ensure that SAT procedures include written validation
and documentation of this requirement.

The SAT shall verify that the installed system meets the specified requirements.


### Maintenance Guidance

The Vendor shall supply current system configuration to the Purchaser to allow traceability and to
ensure no extra services are installed.
The Vendor shall supply written maintenance guidelines for the device, including a timeline,
maintenance equipment required, and as-installed parameters and settings.

The Vendor shall provide upgrades and patches to the wireless device as vulnerabilities are identified
in order to maintain the identified level of system security.


### References

IEEE 802.11n, “Standard for Enhancements for Higher Throughput,”
http://www.ieee802.org/11/Reports/tgn update.htm Web accessed September 2009.
Mouly, M. and M. Pautet, The GSM System for Mobile Communications Cell and Sys Publishers, 1992,
pp 168170.
NASA, “Cellular Phones,” http://www.hq.nasa.gov/office/ospp/securityguide/V2comint/Cellular.htm,
Web page accessed March 2009.
Pesonen, L. GSM Interception, November 1999, http://www.dia.unisa.it/professori/ads/corso­
security/www/CORSO-9900/a5/Netsec/netsec.html, Web page accessed September 2009.
Wingert, C., M. Naidu, CDMA 1x Security Overview, August 2002.


### Dependencies

Section 13.7, “Mobile Radio.”
Section 13.10, “WiMAX.”


## 13.10 WiMAX Technology

WiMAX is the name given to the IEEE 802.16 standards. While similar to WiFi, WiMAX is very
different. WiMAX is a long-range system. WiFi is a short-range system. WiMAX has a QoS
implementation that is different from WI-Fi and its MAC layer uses a scheduling algorithm, while WiFi is
based on a contentions access system (i.e., Carrier Sense Multiple Access). But, because these
transmissions are through the air like WiFi, they can be intercepted or interfered with by those having the
proper equipment.

WiMAX is a wireless broadband technology made for longer distances based on the IEEE 802.16
standard. WiMAX is a relatively new technology that can be configured for point-to-point links, point-to­
multipoint links or mobile cellular type access. WiMAX uses both licensed and unlicensed frequencies:
2.3–2.7, 3.4–3.6, and 5.8 GHz bands. Like other wireless technologies, WiMAX security is dependent on
vendor and owner/operator implementation. The optional nature of dual authentication techniques, per the
standard, could allow for operation of a rogue station. Additionally, the lack of encryption of management
frames could permit DoS attacks.


### Language Guidance

While there are variations on the WiMAX standard, there are two versions of interest for industrial
wireless systems: fixed WiMAX and mobile WiMAX. Fixed WiMAX is intended for point-to-point or
multi-point links. This could be deployed in either the 5.8 GHz in the ISM band, or other licensed
frequencies. Point-to-Point WiMAX is very similar to how microwave is currently being used in industry
today. Mobile WiMAX is being deployed in the commercial 2.5 GHz similar to having a wireless cable
modem or DSL connection. It is deployed very similar to microwaves and can be considered a “last mile”
solution Mobile WiMAX is expected to meet the demands for mobile data and deliver high-speed access
to applications.

WiMAX security supports two quality encryptions standards: Data Encryption Standard and AES.
The standard defines a dedicated security processor on board the base station. There are also minimum
encryption requirements for the traffic and for end-to-end authentication. For end-to-end authentication,
the public key management (PKM)-Extensible Authentication Protocol (EAP) methodology is used which
relies on the Transport Layer Security standard of public key encryption. The key management protocol
uses either EAP [IETF RFC 3748] or X.509 digital certificates [IETF RFC 3280] together with Rivest
Shamir Adleman (RSA) public-key encryption algorithm (PKCS 1) or a sequence starting with RSA
authentication and followed by EAP authentication.


### Procurement Language

The Vendor shall provide the WiMAX subscriber station equipment and associated documentation.

Post-contract award, the Vendor shall provide specific protocols and other detailed information
required for the WiMAX subscriber station to communicate with the base station, including other
equipment that can communicate with the WiMAX subscriber station.

The Vendor shall provide documentation on the range of the WiMAX subscriber station, power
requirements, and the designated frequency of operation for each device.

The Vendor shall provide, within a pre-negotiated period, any test data with analysis associated with
the WiMAX subscriber station to base station communications.
The Vendor shall clearly identify these security devices and methods to change them from the
Vendor-configured or manufacture default conditions.
The Vendor shall remove or disable all software artifacts that are not required for the operation and
maintenance of the device prior to the FAT.

The Vendor shall provide the Purchaser SAT procedures that include exercising all functionality and
calibration procedures.

The Vendor shall document the equipment configuration and specifically note any security measures
associated with the system (encryption devices, password protection, etc.).


### FAT Measures

The FAT shall be performed per written procedures agreed upon by the Purchaser.

The Vendor shall ensure that the systems have had a minimum of a 48-hour burn-in.

The Vendor shall perform an interference rejection test and supply the results with an explanation of
the results.

The Vendor shall ensure that FAT procedures include exercising all functionality and examining the
input or output, and validating the results.

The Vendor shall verify compatibility of the WiMAX equipment and communications with other
devices with which the device must interface.


### SAT Measures

The Purchaser shall perform the SAT testing in accordance with Vendor-supplied procedures.

The Purchaser shall change any Vendor-configured or manufacturer default usernames, passwords, or
other security codes at this time. The Vendor shall ensure that SAT procedures include written validation
and documentation of this requirement.

The SAT shall verify that the installed system meets the specified requirements.


### Maintenance Guidance

The Vendor shall supply current system configuration to the Purchaser to allow traceability and to
ensure no extra services are installed.
The Vendor shall supply written maintenance guidelines for the device, including a timeline,
maintenance equipment required, and as-installed parameters and settings.

The Vendor shall provide upgrades and patches to the wireless device as vulnerabilities are identified
in order to maintain the identified level of system security.


### References

IEEE Standard 802.16e, Part 16: Air Interface for Fixed and Mobile Broadband Wireless Access Systems,
2005, pp 269313.
Petäjäsoja, S., et al., Wireless Security: Past, Present and Future, February 2008,

http://www.codenomicon.com/resources/whitepapers/Codenomicon Wireless WP v1 0.pdf, Web

page accessed September 2009.
WiMAX Forum Mobile System Profile, Release 1.0 Approved Specification, Release 1.0 Approved
Specification, (Revision 1.4.0: 2007-05-02), 2007.
WiMAX Technology, “http://www.WiMAXforum.org/resources/frequently-asked-questions/, Web page
accessed September 2009.


### Dependencies

Section 13.2, “802.11 Technology.”


## 13.11 Microwave and Satellite Technology


### Basis

Both microwave and satellite communications use microwaves for transmitting information from
point to point, both fixed and mobile. Point-to-point communication is directly between two points on the
earth and requires unobstructed LoS. This is typical in a microwave communication link between two
cellular network towers. Point-to-multipoint communication provides coverage from a single tower,
which may include both LoS and non-LoS paths. Satellite communications transmit from a point on the

earth to a satellite and then back to other points on the earth. Satellites introduce some potential latency
but can transmit over longer distances and provide connectivity in very remote areas. Microwave
communications are preferable because satellite technology is the more expensive technology. Both
microwave and satellite transmissions are susceptible to eavesdropping and intrusion techniques by those
having the proper knowledge and equipment.


### Language Guidance

Microwaves are electromagnetic waves in the radio frequencies between about 300 MHz and about
30 GHz with corresponding wavelengths of 1 cm to 1 m. Higher frequency waves have shorter
wavelengths. Shorter wavelength transmissions have the advantage of being easier to control. They can be
directed by small antennas, which helps keep the energy confined to a tight beam. This beam can be
focused on another antenna many miles away. Since the beam is physically narrow, it is more difficult to
intercept the signal. Another advantage to microwaves is that greater amounts of information (bandwidth)
can be sent because of the high frequency.

LoS paths are limited in distance by the curvature of the earth, obstacles along the path, and
free-space loss. They have a conservative range of 25 to 30 miles but have been effective up to 100 miles.
Non-LoS paths are generally used in the lower frequencies (<2 GHz) where refraction, diffraction, and
reflection may extend communications coverage beyond LoS distances. The performance of both LoS and
non-LoS is affected by free-space path loss, terrain, atmosphere, and precipitation.

Microwave/satellite communication systems also use oscillators, amplifiers, and antennas as part of
the communication system. The oscillator produces the transmission frequency; the amplifiers increase
either the transmitted or the received signal, while the antenna, which is normally only 1 foot or a few feet
across, provides the means to focus the signal.

Microwave links are very vulnerable to interception during transmission as the signal is sent across
free-space line of sight links. Commercial equipment to tap into the signal for this kind of interception is
readily and cheaply available. Fixed microwave facilities, such as office buildings, are common targets
for this kind of interception as a very small rooftop antenna and decoder near the microwave link are all
that is required. Antenna radiation patterns also present the opportunity for monitoring links outside direct
LoS due to the presence of signal “sidelobes,” which can be picked up by sensitive receivers in the area.
These systems can intercept microwave beams from satellites placed in appropriate positions.


### Procurement Language

The Vendor shall provide the microwave device, meeting the requirements of GR-63 NEBS and
GR-1089, with associated documentation, and running on a licensed frequency.

Post-contract award, the Vendor shall provide specific protocols and other detailed information
required for the microwave device to communicate with the control network, including other equipment
that can communicate with the microwave device.

The Vendor shall provide documentation on the range of the microwave device, power requirements,
and the designated frequency of operation for each device.

The Vendor shall allow and recommend alarm settings in accordance to the needs of the system.

The Vendor shall define interoperability limits for the microwave device specifically stating the
devices that could be replaced and any problems that might be associated with the replacement.

The Vendor shall provide, within a pre-negotiated period, any test data with analysis associated with
the microwave device.

The microwave device shall be provided with security features, such as passwords or security codes,
to protect the device from unauthorized modification or use. The Vendor shall clearly identify these
security measures and the necessary methods to change them from the Vendor-configured or manufacture
default conditions.
The Vendor shall remove or disable all software artifacts that are not required for the operation and
maintenance of the device prior to the FAT.

The Vendor shall provide the Purchaser SAT procedures, which include exercising all functionality
and calibration procedures.

The Vendor shall document the equipment configuration and specifically note any security measures
associated with the system (encryption devices, password protection, etc.). All information carried across
the microwave links shall be secured through digital encryption.


### FAT Measures

The FAT shall be performed per written procedures agreed upon by the Purchaser and in agreement
with the requirements of GR-63 NEBS and GR-1089.

For Vendor-supplied microwave device, the Vendor shall install the device and run it continuously
during the entire FAT process.

The Vendor shall ensure that the systems have had a minimum of a 48-hour radio/gear burn-in.

The Vendor shall also apply a bit error test for a minimum of 24 hours and verify that it has the
agreed upon level of accuracy.

The Vendor shall perform an interference rejection test and supply the results with an explanation of
the results.

The Vendor shall ensure that FAT procedures include exercising all functionality and examining the
input or output, and validating the results.

The Vendor shall ensure that FAT procedures include written validation and documentation of this
requirement.


### SAT Measures

The Purchaser shall perform the SAT testing in accordance with Vendor-supplied procedures.

Any Vendor-configured or manufacturer default usernames, passwords, or other security codes must
be changed at this time. The Vendor shall ensure that SAT procedures include written validation and
documentation of this requirement.

The SAT shall verify that the installed system meets the specified requirements.


### Maintenance Guidance

The Vendor shall supply current system configuration to the Purchaser to allow traceability and to
ensure no extra services are installed.
The Vendor shall supply written maintenance guidelines for the device, including a timeline,
maintenance equipment required, and as-installed parameters and settings.

The Vendor shall provide upgrades and patches to the microwave device as vulnerabilities are
identified in order to maintain the identified level of system security.


### References

GR-63-CORE, “NEBS Requirements: Physical Protection,” April 2002.
GR-1089-CORE, “Electromagnetic Compatibility and Electrical Safety - Generic Criteria for Network
Telecommunications Equipment,” October 2002.
Senetas Security, “Whitepaper – Microwave Link Encryption,” June 2006.


### Dependencies

None. This topic is stand-alone.
