# 4. Account Management

> Control category from *Cyber Security Procurement Language for Control Systems* (DHS/ICS-CERT, Sept 2009). Each control follows the 8-part topical template. See [`../docs/topical-template.md`](../docs/topical-template.md).


## 4.1 Disabling, Removing, or Modifying Well-Known or Guest

Accounts

Disabling, removing, or modifying well-known or guest accounts and changing default passwords are
necessary to reduce system vulnerabilities.


### Basis

Default accounts and passwords are available on many control systems and are often publicly
available in published materials allowing unauthorized system access.


### Language Guidance

Default, guest, or anonymous accounts are commonly used to gain limited access and potentially
useful system privileges. These can be used in turn to escalate privileges and gain unauthorized access to
additional information. Hardening activities to address these concerns include disabling, removing, or
modifying such accounts or changing default passwords.

Remote access and perimeter devices have unique account management requirements. These topics
are addressed in other sections (see Section 9, “End Devices,” and Section 10, “Remote Access”).


### Procurement Language

The Vendor shall recommend which accounts need to be active and those that can be disabled,
removed, or modified. The Purchaser shall approve in writing the Vendor’s recommendation.

The Vendor shall disable, remove, or modify all the accounts pursuant to the approved
recommendation.

Post-contract award, the Vendor shall disable or remove all default and guest accounts prior to the
FAT. Once changed, new accounts will not be published except that new account information and
passwords will be provided by the Vendor via protected media. After the SAT, the Vendor shall disable,
remove, or modify all Vendor-owned accounts or negotiate account ownership with the Purchaser.


### FAT Measures

The Vendor shall verify that FAT procedures include exercising this functionality, examining the log
files, and validating the results.

The Vendor shall verify that FAT procedures include written validation and documentation of the
requirements.


### SAT Measures

The Vendor shall verify that SAT procedures include exercising this functionality, examining the log
files, and validating the results.

The Vendor shall verify that SAT procedures include written validation and documentation of the
requirements.


### Maintenance Guidance

The Vendor shall not introduce any new accounts without explicit requirements to do so by the
Purchaser or designated authorized individual.


### References

NERC CIP-007 R5, “Account Management.”
ISA-99.00.02 (DRAFT), Security for Industrial Automation and Control Systems: Part 2: Establishing an
Industrial Automation and Control Systems Security Program,” Sections 5.3.11, B.14.2, B.14.4,
C.3.11.
NIST Special Publication 800-82, “Guide to Industrial Control Systems (ICS) Security,” Final Public
Draft.


### Dependencies

Section 4.3, “Password/Authentication Policy and Management.”
Section 9, “End Devices.”
Section 10, “Remote Access.”


## 4.2 Session Management

Weak session practices and insecure protocols exist on many systems for convenience, backwards
compatibility, and on legacy systems.


### Basis

Unauthorized access can be achieved through clear-text accounts and passwords along with weak
session security practices.


### Language Guidance

Many legacy system utilities transport user credentials in clear text, using protocols such as FTP and
TELNET—this is not acceptable. Other weak session practices include concurrent session logins,
remembered account information between login, auto-filling of fields during logins, and anonymous
services such as FTP. In many systems, you are your account, and once the account is compromised, the
system has no way of knowing who is actually using the account.

By using access protocols that encrypt or securely transmit user-login credentials (names and
passwords), such vulnerabilities can be reduced. Other hardening activities include disabling the use of
insecure protocols to access network devices, enabling secure protocols (Secure Sockets Layer [SSL] or
tunneling through Secure Shell Terminal Emulation [SSH] for instance), and setting appropriate system
parameters to enforce minimum levels of encryption. Certain applications, such as alarms and human
machine interfaces, should not time out, black out, or otherwise be blocked.


### Procurement Language

The Vendor shall not permit user credentials to be transmitted in clear text.

The Vendor shall provide the strongest encryption method commensurate with the technology
platform and response time constraints.

The Vendor shall not allow multiple concurrent logins, applications to retain login information
between sessions, provide any auto-fill functionality during login, or allow anonymous logins.

The Vendor shall provide user account-based logout and timeout settings.


### FAT Measures

The Vendor shall verify that FAT procedures include validation and documentation of the
requirements.


### SAT Measures

The Vendor shall verify that SAT procedures include validation and documentation of the
requirements.


### Maintenance Guidance

The Vendor shall not introduce any new session algorithms without explicit requirements to do so by
the Purchaser or a designated authorized individual.

The Vendor shall change encryption keys at reasonable intervals commensurate with need.


### References

NERC CIP-007 R5, “Account Management.”
NIST Special Publication 800-12, “An Introduction to Computer Security: The NIST Handbook.”
NIST Special Publication 800-15, “Minimum Interoperability Specification for PKI Components
(MISPC), Version 1.”
NIST Special Publication 800-32, “Introduction to Public Key Technology and the Federal PKI
Infrastructure.”

NIST Special Publication 800-67, “Recommendation for the Triple Data Encryption Algorithm (TDEA)
Block Cipher.”


### Dependencies

Section 4.3, “Password/Authentication Policy and Management.”


## 4.3 Password/Authentication Policy and Management

Instant availability requirements in control systems often result in a weak password policy.


### Basis

Weak passwords introduce vulnerabilities to the control systems network. In addition, sometimes
passwords are hard-coded into software to facilitate control system internal communications allowing
anyone with access to the code/configuration files knowledge of the password(s).


### Language Guidance

This requirement can apply to any of several authentication methods. Users often select poor or
easily-guessed passwords even with the best of intentions. Commonly, an automated “brute force” attack
can be used to guess user passwords by using common dictionary terms, sequential password patterns,
and other means, often revealing the correct password within minutes. By enforcing password complexity
limits, restricting user-login attempts, and locking out accounts after repeated failed attempts, such attacks
can be thwarted.


### Procurement Language

The Vendor shall provide a configurable account password management system that allows for
selection of password length, frequency of change, setting of required password complexity, number of
login attempts, inactive session logout, screen lock by application, and denial of repeated or recycled use
of the same password.

The Vendor shall not store passwords electronically or in Vendor-supplied hardcopy documentation
in clear text unless the media is physically protected.

The Vendor shall control configuration interface access to the account management system.
The Vendor shall provide a mechanism for rollback of security authentication policies during
emergency system recovery or other abnormal operations, where system availability would be negatively
impacted by normal security procedures.


### FAT Measures

The Vendor shall verify that FAT procedures include validation and documentation of the password
and authentication policy and management.


### SAT Measures

The Vendor shall verify that SAT procedures include validation and documentation of the password
and authentication policy and management.


### Maintenance Guidance

The Vendor shall not introduce changes to password or authentication policy and management
without explicit requirements to do so by the Purchaser or other designated authorized individual.


### References

NERC CIP-007 R5, “Account Management.”
FIPS PUB 112, “Password Usage Standard.”
ANSI/ISA-99.00.01, “Security for Industrial Automation and Control Systems Part 1: Terminology,
Concepts, and Models,” Sections 5.7.4, 6.5.3.
ISA-99.00.02 (DRAFT), Security for Industrial Automation and Control Systems: Part 2: Establishing an
Industrial Automation and Control Systems Security Program,” Sections 5.3.11, B.14.1, B.14.2,
B.14.4, C.2, C.3.11.
NIST Special Publication 800-12, “An Introduction to Computer Security: The NIST Handbook.”
NIST Special Publication 800-53 Revision 2, “Recommended Security Controls for Federal Information
Systems.”
NIST Special Publication 800-63 Version 1.0.2, “Electronic Authentication Guideline: Recommendations
of the National Institute of Standards and Technology.”
NIST Special Publication 800-82, “Guide to Industrial Control Systems (ICS) Security,” Final Public
Draft.


### Dependencies

Section 5, “Coding Practices.”


## 4.4 Account Auditing and Logging

Account auditing and logging allow the Purchaser/Operator to verify that authorized operations have
been maintained. Logging is also necessary for forensic analysis and anomaly detection.


### Basis

Logging and auditing of both active and disabled accounts are useful for anomaly and unauthorized
access detection. However, cyber attackers commonly modify audit logs to cover activities.


### Language Guidance

Account logging must provide an audit trail of user activity that allows specific actions to be traced to
a single user/process, location, and time in a verifiable manner.

Advanced cyber security attackers will modify log files to make forensics activities difficult.
Monitoring of log access will detect malicious modifications. Writing log files to read-only media also
prevents malicious modification.


### Procurement Language

The Vendor shall provide a system whereby account activity is logged and is auditable both from a
management (policy) and operational (account use activity) perspective.

The Vendor shall time stamp, encrypt, and control access to audit trails and log files.

The Vendor shall ensure audit logging does not adversely impact system performance requirements.

The Vendor shall provide read-only media for log creation.


### FAT Measures

The Vendor shall verify that FAT procedures include validation and documentation of the
requirements.

The Vendor shall record system performance measurements that include the system with and without
logging activities.


### SAT Measures

The Vendor shall verify that SAT procedures include validation and documentation of the
requirements.
The Vendor shall record system performance measurements to verify that logging activities do not
adversely impact system performance.


### Maintenance Guidance

The Vendor shall archive auditing and logging records.

The Vendor shall configure audit policies and review audit data on a regular basis.


### References

NERC CIP-007 R5, “Account Management.”
ANSI/ISA-99.00.01, “Security for Industrial Automation and Control Systems Part 1: Terminology,
Concepts, and Models,” Section 5.7.
ISA-99.00.02 (DRAFT), Security for Industrial Automation and Control Systems: Part 2: Establishing an
Industrial Automation and Control Systems Security Program, ” Sections 4.15, 4.19, 5.3.12, 5.3.15,
B.3, B.5, B.15.4, B.19, C.3.3, C.3.8, C.3.13, C.3.15, C.3.17.
NIST Special Publication 800-12, “An Introduction to Computer Security: The NIST Handbook.”
NIST Special Publication 800-14, “Generally Accepted Principles and Practices for Securing Information
Technology Systems.”
NIST Special Publication 800-61, “Computer Security Incident Handling Guide.”
NIST Special Publication 800-82, “Guide to Industrial Control Systems (ICS) Security,” Final Public
Draft.
NIST Special Publication 800-92, “Guide to Computer Security Log Management.”


### Dependencies

None. This topic is stand-alone.


## 4.5 Role-Based Access Control for Control System Applications

Role-based access control (RBAC) refers to the system’s ability to make access decisions based on
the role(s) of individual users/processes in the control system environment. Using RBAC results in
significant improvements in security. The use of roles to control access can be an effective means for
developing and enforcing systemwide security policies and for streamlining security management
processes. RBAC limits the exposure to risk associated with unauthorized actions by assigning the least
privileges corresponding to the assigned duty or function. The use of RBAC for administrative functions
is not common on legacy systems.


### Basis

Legacy control systems typically do not have RBAC, which allows any user full access, control, and
administrative privileges. Thus if an unauthorized user achieves login, that user would have full access to
the system.


### Language Guidance

User credentials consist of account names, passwords/pass phrases and other factors used to
authenticate a user to the network or to a network device. Credentials are the most basic form of security
control used to protect systems. User accounts and identification required by control system applications,
system operator access, database maintenance, display maintenance, and overall system operation and
maintenance with access to resources and functionality must be appropriate for the user’s role (i.e., areas
of responsibility and authority). Thus, each role may need unique access and permission levels. Logging
must nevertheless resolve individual users and applications as resources are accessed.

Once the RBAC scheme is established, it shall be protected (e.g., encrypted). Only approved
administrators, who are aware of how roles and permissions can affect the security of the control system,
shall be allowed to change the RBAC scheme.


### Procurement Language

The Vendor shall provide for user accounts with configurable access and permissions associated with
the defined user role.

The Vendor shall adhere to least privileged permission schemes for all user accounts, and
application-to-application communications.

The Vendor shall configure the system so that initiated communications start with the most privileged
application controlling the communication. Upon failed communication, the most privileged side will
restart communications.

The Vendor shall verify that the master network device initiates communications. The Vendor shall
inform the Purchaser if this condition cannot be met.

The Vendor shall verify that a user cannot escalate privileges, under any circumstances, without
logging into a higher-privileged role first.

The Vendor shall provide a mechanism for changing user(s) role (e.g., group) associations.
Post-contract award, the Vendor shall provide documentation defining access and security
permissions, user accounts, applications, and communication paths with associated roles.


### FAT Measures

The Vendor shall compare the control system assessment during this period with required
documentation to validate the requirements.

The Vendor shall baseline user roles and permissions and negotiate agreements on modifications with
the system Purchaser/Operators.


### SAT Measures

The Vendor shall verify that all additions to the control system, after the completion of the FAT, have
the same rigor of documentation that was necessary pre-FAT and appropriate comparisons are required
post-SAT to validate the requirement.


### Maintenance Guidance

The Vendor shall verify that all additions to the control system during the warranty/maintenance
period have the same rigor of documentation, as stated in this requirement.


### References

NERC CIP-007 R5, “Account Management.”
ISA-99.00.02 (DRAFT), Security for Industrial Automation and Control Systems: Part 2: Establishing an
Industrial Automation and Control Systems Security Program,” Sections 5.3.11, B.14.2, B.14.4,
C.3.117.
NIST Special Publication 800-12, “An Introduction to Computer Security: The NIST Handbook.”
NIST Special Publication 800-14, “Generally Accepted Principles and Practices for Securing Information
Technology Systems.”
NIST Special Publication 800-27 Rev A, “Engineering Principles for Information Technology Security
(A Baseline for Achieving Security), Revision A.”
NSIT Special Publication 800-82, “Guide to Industrial Control Systems (ICS) Security,” Final Public
Draft.


### Dependencies

None. This topic is stand-alone.


## 4.6 Single Sign-On

Single sign-on (SSO) refers to a means of user authentication such that a single login allows a user to
have authorized role-based access across a network or between programs and systems, without requiring
re-authentication to each application.


### Basis

Single sign-on authentication has been commonly designed for convenience, sometimes at the
expense of security, and potentially provides an avenue for the introduction of vulnerabilities. However,
careful attention to system design can lead to single sign-on schemes that enhance security.


### Language Guidance

To enhance security, single sign-on shall be used with RBAC and a two-factor authentication. For
configured users of the system, permissions shall be validated and show equivalent results in running
validation tests against a direct login and a single sign-on login, on each terminal and for each application.
Single sign-on may not prohibit the weak session practice of concurrent logins. SSO can also be between
enterprise systems using federated authentication not currently applicable in control systems.


### Procurement Language

The Vendor shall provide an SSO such that RBAC enforcement is equivalent to that enforced as a
result of direct login.

The Vendor shall provide a means of allowing SSO to a suite of applications via SSH, terminal
services, or other authenticated means. This system shall be RBAC capable.

The Vendor shall provide documentation on configuring such a system, and documentation showing
equivalent results in running validation tests against the direct login and the SSO.

The Vendor shall protect key files and access control lists (ACLs) used by the SSO system from
nonadministrative user read, write, and delete access. The SSO must resolve individual user’s logins to
each application.


### FAT Measures

The Vendor shall verify that FAT procedures include validation and documentation that the SSO
permissions and session management are handled properly.


### SAT Measures

The Vendor shall verify that SAT procedures include validation and documentation that the SSO
permissions and session management are handled properly.


### Maintenance Guidance

The Vendor shall not introduce changes to the SSO process without explicit requirements to do so by
a Purchaser’s system administrator or other designated authorized individual.


### References

NERC CIP-007 R5, “Account Management.”


### Dependencies

Section 4.1, “Disabling, Removing, or Modifying Well-Known or Guest Accounts.”
Section 4.2, “Session Management.”
Section 4.5, “Role-Based Access Control for Control System Applications.”


## 4.7 Separation Agreement

The Purchaser needs to have agreements with Vendors to protect their control systems security
posture.


### Basis

Integrators and companies that support control systems are very dynamic and competitive, resulting
in frequent turnover of key support personnel potentially exposing sensitive information.


### Language Guidance

Many stakeholders including Purchasers/Operators, Vendors, and contractors hold control
systems-related sensitive information. Sensitivity needs to be maintained as individuals move to new
positions or leave the organization. In addition, should a Vendor become unable to maintain control of its
products (e.g., go out-of-business), the Vendor products used to construct the Purchaser’s control system
would need to be accessible.


### Procurement Language

Pre-contract award, the Vendor shall provide a separation agreement to delineate how Vendor
employees who have sensitive knowledge of the Purchaser’s control systems and who leave their
positions or have responsibilities changed will be prohibited from disclosing that knowledge, where
disclosure could lead to a reduction in security.
The Vendor shall notify the Purchaser within a pre-negotiated period when key personnel leave or
change positions, should it possibly impact control system security.

The Vendor shall provide detailed documentation on how the control system security can be
maintained and supported in the event the Vendor leaves the business (e.g., security-related procedures
and products placed in escrow).
The Vendor shall return to the Purchaser any sensitive data in the Vendor’s possession when the
Vendor is no longer able to maintain control of the Purchaser’s products.


### FAT Measures

The Vendor shall verify that FAT procedures include validation and documentation of the ability to
change key employee/support personnel access and permissions.


### SAT Measures

The Vendor shall verify that SAT procedures include validation and documentation of the ability to
change key employee/support personnel access and permissions.


### Maintenance Guidance

The Vendor shall notify the Purchaser within a pre-negotiated period when key personnel leave or
change positions, should it possibly impact control system security.


### References

NERC CIP-007-1 R4, “Malicious Software Prevention.”
ISA-99.00.02 (DRAFT), Security for Industrial Automation and Control Systems: Part 2: Establishing an
Industrial Automation and Control Systems Security Program,” Sections C.2, C.3.5, C.3.13.
NIST Special Publication 800-12, “An Introduction to Computer Security: The NIST Handbook.”


### Dependencies

Section 4.1, “Disabling, Removing, or Modifying Well-Known or Guest Accounts.”
Section 4.3, “Password/Authentication Policy and Management.”
