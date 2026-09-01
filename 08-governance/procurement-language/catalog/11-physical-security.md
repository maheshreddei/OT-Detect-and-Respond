# 11. Physical Security

> Control category from *Cyber Security Procurement Language for Control Systems* (DHS/ICS-CERT, Sept 2009). Each control follows the 8-part topical template. See [`../docs/topical-template.md`](../docs/topical-template.md).


## 11.1 Physical Access of Cyber Components

Control system networks and devices require protection from physical access as well as cyber access.


### Basis

Physical access to cyber equipment circumvents all cyber security controls.


### Language Guidance

Physical access to systems should have the same level of security as cyber access. Unlocked control
cabinets or operator or engineering workstations in unsecured rooms and buildings often only require
access by a computer or control system-knowledgeable person to have a significant impact on operations
by changing set points, altering code, performing manual overrides, or cycling systems with the intent of
burning up motors or disrupting the process.

Commonly, computer components such as CPUs or keyboards are locked in cabinetry while pointing
devices, limited keyboards, and monitors for operator functions are available.

Higher security facilities require two-factor authentication for cyber access. These methods can
include biometrics, passwords, and security tokens/certificates. Some authentication can be tightly
coupled with physical security (e.g., proximity monitors, keycard access to buildings) and control access
and logoff to cyber systems.


### Procurement Language

The Vendor shall provide a detailed plan for appropriate physical security mechanisms.

The Vendor shall provide lockable or locking enclosures for control system components (e.g., servers,
clients, and networking hardware).

The Vendor shall provide locking devices with a minimum of two keys per lock identifiable to each
lock, and keyed or not keyed alike depending on Purchaser requirements.

The Vendor shall recommend a room locking device(s) where the equipment and workstations are
located, if not already installed by the Purchaser.

The Vendor shall verify and provide documentation that unauthorized logging devices are not
installed (e.g., key loggers, cameras, and microphones).

The Vendor shall provide two-factor authentication for physical access control.


### FAT Measures

The Vendor shall verify and provide documentation that physical security components (e.g., hardened
devices, locks) are tested and the results provided.

The Vendor shall disable by hardware and software means all unused ports and input/output devices
(see Section 2).
The Vendor shall verify and provide documentation on the two-factor authentication requiring
physical access control.


### SAT Measures

The Vendor shall provide, as a part of the SAT procedures, validation and documentation of any
electronic or networked room or area access devices.

The Vendor shall disable by hardware and software means all unused ports and input/output devices.

The Vendor shall verify and provide documentation that physical security access schemes are tested
and the results provided.


### Maintenance Guidance

The Vendor shall maintain the same configuration and standard for all replacements of physical
security components.


### References

NERC CIP-006-1, “Physical Security of Critical Cyber Assets”.


### Dependencies

Section 2.4, “Hardware Configuration.”


## 11.2 Physical Perimeter Access

Perimeter security includes, but is not limited to fences, walls, fully enclosed buildings, entrance
gates or doors, vehicle barriers, lighting, landscaping, surveillance systems, alarm systems, and guards.
Physical security may also include site entry and exit logging as well as room or area logging possibly
through a keycard access system.


### Basis

Lack of perimeter identification can facilitate physical intrusions. Lack of notification of unauthorized
physical access (e.g., monitoring and alarms) can allow unknown breached perimeters. The ability to
detect perimeter intrusions is key to prevent physical attacks.

Individuals with access to critical components could compromise the entire system, whether due from
a skillful attack or blind luck.


### Language Guidance

A physical intrusion is defined as human-initiated bodily access or physical influence to an area
where action may negatively affect the reliability of the system in question. If risk or consequence of
physical intrusion is deemed high by the Purchaser, greater perimeter security shall be considered. A
control area’s physical perimeter is defined as the external barrier to any type of physical intrusion,
whether it be pedestrian, vehicular, or projectile. The Purchaser shall define his or her perimeter such that
all components critical to system operation are physically secured to all types of physical access.

Only personnel needing access to a location shall be given the access permission. Secured areas with
critical equipment shall not have equipment or functions associated with it that require access by many
people, including contractors.

Overly restricted access measures can hamper operations. During emergency events, previously
unauthorized individuals commonly need access to controlled areas. Highly secured physical perimeters
(e.g., access-controlled cabinets) require special environmental conditions to ensure cyber components do
not fail (e.g., overheat). Security is often bypassed if operations are hampered.
Physical security monitoring (e.g., cameras, card access) often alarm to a manned control center. For
cyber security concerns these alarms shall not be on the same network as control functions.


### Procurement Language

The Vendor shall provide a site security assessment, making special note of parameters or events that
may influence physical intrusions. The results of this assessment shall be a documented site physical
security plan.
The Vendor shall verify and provide documentation that enclosures such as walls, buildings, or fences
adequately secure the perimeter against pedestrian, vehicular, and projectile intrusion.

The Vendor shall allow access within the perimeter only to those employees, contractors, or guests
cleared by both Vendor and Purchaser.
The Vendor shall verify and provide documentation that all employed guards have completed
background checks.

The Vendor shall coordinate with local authorities when installing and using remote alarm systems.

The Vendor shall provide nonreproducible keys or keycards for all locks.

The Vendor shall verify and provide documentation that security features do not hamper operations.

The Vendor shall verify and provide documentation that monitoring and alarm of physical access can
be separated from the control network.


### FAT Measures

The Vendor shall test and provide documentation that all alarm systems pick up all instances of
intrusion with minimal false alarms.


### SAT Measures

The Vendor shall provide access control mechanisms to the Purchaser.

The Vendor shall provide a walk-through of expected physical security functionality to the Purchaser.

The Vendor shall provide adequate onsite training to operators and guards prior to site startup.

The Vendor shall verify and provide documentation on all remote alarm, surveillance, and locking
functionality prior to startup.


### Maintenance Guidance

The Vendor shall maintain access control mechanisms in a secure configuration.

The Vendor shall validate perimeter security performance on a pre-negotiated basis.
The Vendor shall change all locks, locking codes, keycards, and any other keyed entrances on a pre­
negotiated basis.

The Vendor shall coordinate access control changes with the Purchaser to include, but not be limited
to, an update of the site physical security.


### References

IEEE Standard 1402-2000, “IEEE Guide for Electric Power Substation Physical and Electronic Security,”
IEEE, New York, New York, April 4, 2000.
NERC, CIP-002-1—CIP-009-1, Critical Infrastructure Protection Reliability Standards.


### Dependencies

None. This topic is stand-alone.


## 11.3 Manual Override Control

Manual override controls include mechanisms such as circuit breaker hand switches, valve levers, and
end-device panels.


### Basis

Physical security of manual override controls are commonly overlooked with the potential for exploit
and system damage.


### Language Guidance

Physical access to manual override controls should be heavily restricted to authorized personnel only.
Unauthorized access to manual override controls poses the risk for system damage or intrusion, and
therefore must be secured.

Detrimental system effects due to physical control or damage to one remote manual control
mechanism (MCM) have been demonstrated in interconnected nodal systems. Therefore, although the
local node may be unimportant, manual override control of a device within the local node may provide
access or influence to other, more critical nodes.

The system importance of a particular MCM is a function of the type and amount of control it
performs. In the power system for example, manual control of a transmission circuit breaker may affect
operation of a large area of the system, and could result in massive blackouts, whereas control of
distribution switchgear may affect a much smaller region, with fewer consequences. If the mal-operation
of a MCM results in the loss of the node, plant, substation, or of a significant area outside that which it
controls, it should be subject to increased security measures. If it is apparent that control of one MCM

may result in the control of an entire system, as may be the case with local SCADA or cyber-related
control mechanisms, then security of all such mechanisms shall be deemed of utmost importance.

The Purchaser shall be aware of the system importance of the MCM he or she wishes to protect. For
MCMs requiring a locking device, the device shall be appropriate for the environment in which it is
deployed.


### Procurement Language

The Vendor shall provide the means to physically secure the MCM, whether through a lockable
enclosure or locking functionality built into the MCM itself.

The Vendor shall provide two nonreproducible keys to all locking MCMs, as requested by the
Purchaser.

The Vendor shall change all locks, locking codes, keycards, and any other keyed entrances according
to a pre-negotiated period.


### FAT Measures

The Vendor shall verify and provide documentation that the MCM meets the requirements
appropriate for the environment in which it is deployed.


### SAT Measures

The Vendor shall verify and provide documentation that the implemented security does not
compromise the required functionality of the MCM.

The Vendor shall provide results of security measure assessments identifying any potential bypass
vulnerabilities.


### Maintenance Guidance

The Vendor shall verify the implemented security and the functionality of the MCM according to a
pre-negotiated interval.


### References

IEEE Standard 1402-2000, “IEEE Guide for Electric Power Substation Physical and Electronic Security,”
IEEE, New York, New York, April 4, 2000.
NERC, CIP-002-1—CIP-009-1, Critical Infrastructure Protection Reliability Standards.


### Dependencies

Section 11.4, “Intra-perimeter Communications.”


## 11.4 Intraperimeter Communications

Mechanisms within the perimeter may rely on intraperimeter communication to ensure secure
operation. The communication medium may consist of a physical, electrical (fly-by-wire), or wireless
connection.


### Basis

Intraperimeter communications are commonly overlooked for security concerns. Access to the
intraperimeter communication medium constitutes access to the function or device itself with the potential
for exploit and damage. The communication path must be physically secured to the same level as the
components.


### Language Guidance

The length and complexity of the communication channel to be protected should be minimized. The
communication channel and access ports should also be hidden from view, out of reach, and/or behind
layers of perimeter security if possible. A conduit may be placed around the communication medium to
provide additional resistance to tampering. Wireless communication should not be detectable or
accessible outside the perimeter.


### Procurement Language

The Vendor shall verify and provide documentation that physical communication channels are
secured from physical intrusion.

The Vendor shall verify and provide documentation that the range of the wireless communications is
limited to within the perimeter.

The Vendor shall verify and provide documentation that communication channels are as direct as
possible.


### FAT Measures

The Vendor shall verify and provide documentation that the range of the wireless communications is
limited to the required area.
The Vendor shall verify and provide documentation that the physical intrusion of communication
channels is detectable.


### SAT Measures

The Vendor shall verify and provide documentation that the range of the wireless communications is
limited to within the perimeter.
The Vendor shall verify and provide documentation that the physical intrusion of communication
channels is detectable.

The Vendor shall document the communication channels’ locations and access points.


### Maintenance Guidance

The Vendor shall provide documentation that the implemented security measures are verified
according to a pre-negotiated interval.


### References

IEEE Standard 1402-2000, “IEEE Guide for Electric Power Substation Physical and Electronic Security,”
IEEE, New York, New York, April 4, 2000.
NERC, CIP-002-1—CIP-009-1, Critical Infrastructure Protection Reliability Standards.


### Dependencies

Section 12, “Network Partitioning.”
