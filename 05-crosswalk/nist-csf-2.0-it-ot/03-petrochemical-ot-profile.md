# Petrochemical OT Organizational Profile Guidance

## Scope

Example scope: ammonia and urea production, utilities, DCS, PLC packages, SIS/ESD, fire and gas, electrical/PMS, tank farm/loading, historians, remote access, industrial DMZ and OT security monitoring.

This is guidance for creating a Profile, not a completed risk assessment.

## Target outcomes by Function

### Govern

- Cyber risk decisions include process safety, environmental release, equipment damage and production loss.
- OT roles distinguish corporate IT, SOC, site operations, control engineering, process safety, OEMs and integrators.
- Cybersecurity changes use MOC.
- Supplier contracts cover remote access, vulnerabilities, support lifetime, backups, logging and secure development.
- Exceptions have risk owners, compensating controls and expiry.

### Identify

- Inventory includes passive and authoritative engineering sources.
- Each critical asset has process, owner, firmware, zone, criticality and recovery dependency.
- Zones/conduits and permitted industrial operations are documented.
- Risk scenarios include unauthorized logic/mode/setpoint change, SIS compromise, compressor disruption, loss of utilities and remote-vendor abuse.
- Improvement actions from incidents, audits and exercises are tracked.

### Protect

- Engineering and privileged access is named, time-bound and monitored.
- SIS/ESD and fire-and-gas access is more restrictive than ordinary DCS access.
- Portable media and laptops are controlled.
- Logic, recipes, controller configurations and network-device configurations are backed up.
- Firewall conduits deny unapproved flows.
- Patch and hardening decisions account for vendor support and process availability.

### Detect

- Monitoring covers IT/OT boundaries, Level 3, DCS controller conduits, packages, remote access and critical safety boundaries.
- Detect new assets, new links, logic downloads, controller mode changes, unexpected writes, unusual remote sessions and monitoring loss.
- Correlate Nozomi with SIEM, identity, VPN, firewall, EDR and operator/MOC records.
- Validate detections safely without manipulating production.

### Respond

- SOC validates technical evidence; operations validates process state.
- Incident command defines who can authorize isolation, trip, failover or shutdown.
- Playbooks cover controller change, SIS access, malware, remote vendor abuse, loss of view/control and ransomware.
- Communications cover control room, management, process safety, legal/regulatory and vendors.
- Evidence preserves time, capture origin, configuration and chain of custody.

### Recover

- Recovery sequences restore safety, basic control, operator visibility, utilities and business interfaces in approved order.
- Golden configurations and spare hardware are available.
- Restore tests validate logic, firmware, communications, alarms, interlocks, time and monitoring.
- RTO/RPO reflect process consequence.
- Post-incident changes return through engineering and MOC.

## Prioritization

Rate gaps using:

- Safety consequence
- Environmental consequence
- Production/quality consequence
- Cyber likelihood and exposure
- Ease of exploitation
- Existing safeguards
- Detection and recovery capability
- Regulatory/contractual requirement

A high-risk SIS or compressor-control gap should not be hidden inside an enterprise-average score.

## Profile evidence rule

A policy proves intent. A configuration proves deployment. A test proves operation at a point in time. Sustainable evidence requires all three plus ownership and monitoring.
