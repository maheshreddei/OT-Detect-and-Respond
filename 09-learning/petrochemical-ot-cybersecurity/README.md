# Petrochemical OT Cybersecurity — Ammonia and Urea Plant

A role-based learning and project package for working as an OT cybersecurity/SOC analyst supporting an ammonia and urea manufacturing complex.

![Process and control context](diagrams/process-flow.svg)

## Learning modules

1. [Plant process and language](01-plant-process-and-language.md)
2. [Control systems, protocols and architecture](02-control-systems-protocols.md)
3. [IEC 62443 zones, conduits and network design](03-zones-conduits-network-design.md)
4. [OT SOC role, tools and operational workflows](04-ot-soc-role-tools-workflows.md)
5. [Competency roadmap and practical projects](05-competency-roadmap-projects.md)

## Architecture diagrams

- [Ammonia/urea process flow](diagrams/process-flow.svg)
- [IEC 62443 zones and conduits HLD](diagrams/zones-conduits-hld.svg)
- [Detailed OT network LLD](diagrams/network-lld.svg)
- [OT SOC operating model](diagrams/soc-operating-model.svg)

## Outcome

A learner completing the exercises should be able to discuss the plant process, read PFD/P&ID and network drawings at a working level, distinguish DCS/PLC/SIS/SCADA responsibilities, recognize common protocols, design zones/conduits and monitoring points, investigate Nozomi alerts with process context, and communicate safely with operators and control engineers.

## Safety boundary

This material supports cybersecurity learning. It does not authorize process operation, SIS modification, controller downloads, active scanning or containment. Plant procedures, process-safety management, MOC and authorized operations personnel always govern real actions.

## Primary references

- [US DOE: natural-gas reforming](https://www.energy.gov/cmei/fuels/hydrogen-production-natural-gas-reforming)
- [US EPA: urea manufacturing background](https://www.epa.gov/sites/default/files/2020-09/documents/final_background_document_for_urea_section_8.2.pdf)
- [ISA/IEC 62443 standards series](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards)
- [CISA ICS recommended practices](https://www.cisa.gov/resources-tools/resources/ics-recommended-practices)
- [Nozomi design package](../../01-telemetry/nozomi-design/)
