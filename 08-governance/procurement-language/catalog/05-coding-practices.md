# 5. Coding Practices

> Control category from *Cyber Security Procurement Language for Control Systems* (DHS/ICS-CERT, Sept 2009). Each control follows the 8-part topical template. See [`../docs/topical-template.md`](../docs/topical-template.md).


## 5.1 Coding for Security

Standard programming texts generally address data processing, but not security ramifications; this
may mislead programmers into writing insecure code.


### Basis

Software flaws are a primary avenue for gaining system access. Many control system security
vulnerabilities are the direct result of writing software with inadequate attention to defense against
deliberate and persistent malicious attack. These attacks include, but are not limited to:
   Buffer overflows, in which input fields are populated with long data sequences that overflow program

buffers, often yielding program controls to the remote user (providing a useful command prompt in

some cases).
   Data insertion and injection, in which input fields are populated with control or command sequences

embedded in various ways that are nevertheless accepted by the application, or possibly passed to the

OS, and that allow privileged malicious and unauthorized programs to be run on the remote system.

These vulnerabilities are particularly threatening because the control system can be compromised by
bypassing normal access control checks, such as firewalls—control system traffic will appear normal as
far as the network is concerned. Network protections such as proxies, which provide some defense against
these vulnerabilities, are available for well-known protocols, such as Web-based (HTTP) or e-mail
(SMTP), but not for some lesser-known protocols.


### Language Guidance

Software development process standards have been historically used as an indirect measure of the
quality, safety, and security of computer source code written according to those process standards. One
software process element, the code review, is widely recognized as an effective mechanism for assessing
security, among other attributes. Code reviews can be accomplished through numerous means with
varying degrees of automation. The Vendor shall provide documentation of code reviews and other
software development process steps used to assess software security. Software subject to these reviews
shall include both Vendor-developed applications and any other source code the Vendor has control over
that forms a necessary part of the control system.

Many critical systems have software reviewed by the Purchaser or third party prior to acceptance of
the system. Third-party software integrated into Vendor products shall be assessed for security
vulnerabilities. Experience has shown that system integration often contributes to the overall vulnerability
of the system.

Because control system software, with regard to security, is very similar to other real-time distributed
software systems, many existing security references apply. Most software security references include the
following imperatives:
   Check inputs for reasonable values
   Encrypt data files

   Understand security impacts of OSs and other third-party libraries
   Make sure OSs and other third-party libraries have an update policy
   Forbid buffer overflow
   Verify log files are unalterable
   Use end-to-end authentication and integrity checks on process-to-process data communications
   Verify no clear-text passwords or encryption keys are embedded in the code or communicated
   Use design and code reviews.


### Procurement Language

Pre-contract award, the Vendor shall provide documentation of development practices and standards
applied to Vendor-written control system software, including firmware, used to ensure a high level of
defense against unauthorized access.

The Vendor shall provide the results of Code Reviews.

Post-contract award, the Vendor shall provide documentation of coding practices used in developing
the delivered software.


### FAT Measures

The Vendor shall verify that FAT procedures include validation and documentation of the software
development process and/or code review.


### SAT Measures

The Vendor shall verify that SAT procedures include validation and documentation of the software
development process and/or code review.


### Maintenance Guidance

The Vendor shall verify that software upgrades and patches are validated according to the same
software development process or review plan.


### References

ISA-99.00.02 (DRAFT), Security for Industrial Automation and Control Systems: Part 2: Establishing an
Industrial Automation and Control Systems Security Program,” Section B.17.4.
NIST Special Publication 800-12, “An Introduction to Computer Security: The NIST Handbook.”
NIST Special Publication 800-42, “Guideline on Network Security Testing.”


### Dependencies

Section 4.3, “Password/Authentication Policy and Management.”
