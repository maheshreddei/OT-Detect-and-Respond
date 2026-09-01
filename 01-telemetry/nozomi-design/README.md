# Nozomi Networks OT Monitoring Design Package

> Reference architecture and implementation workbook. Validate appliance model, N2OS release, license, throughput, retention and port labels against the approved Nozomi bill of materials and current vendor documentation before implementation.

## Documents

1. [High-level design](01-hld.md)
2. [Low-level design](02-lld.md)
3. [SPAN and TAP implementation](03-span-tap-change-plan.md)
4. [Interface and connectivity design](04-interface-connectivity.md)
5. [Commissioning and acceptance](05-commissioning-runbook.md)
6. [Experienced-practitioner interview guide](06-interview-guide.md)

## Design intent

Nozomi Guardian passively receives copies of OT traffic from network TAPs, packet brokers, or switch SPAN/mirror sessions. It analyzes the copies; it is not inserted into the control path. A separate management network carries administration, updates, integrations, synchronization, and alert forwarding. A Central Management Console (CMC) provides enterprise visibility across Guardians. Remote Collectors extend capture into small or isolated locations and forward encrypted traffic to a Guardian.

## Non-negotiable principles

- Preserve safety and availability: no active scanning or control-system change without asset-owner approval.
- Keep management and monitoring planes separate.
- Prefer physical TAPs or packet brokers for critical, high-load, redundant, or evidentiary links.
- Treat SPAN as a capacity-limited copy, not guaranteed packet capture.
- Monitor choke points and control conversations, not every switch port.
- Avoid duplicate packet feeds; document every observed VLAN and traffic direction.
- Size from measured packets per second, throughput, burst rate, nodes, network elements, protocols, retention, and growth—not link speed alone.
- Use a formal Management of Change (MOC) process for production switch, firewall, hypervisor, rack, power, or cabling work.

## Product terminology

- **Guardian:** network sensor that analyzes mirrored/TAP traffic.
- **CMC:** central manager for multiple Guardians.
- **Remote Collector:** low-resource sensor that captures at distributed locations and forwards to Guardian; analysis occurs at Guardian.
- **Vantage:** cloud-delivered management/analytics option where approved.
- **Arc:** endpoint sensor for supported hosts; it complements rather than replaces network visibility.
- **Management interface:** addressed/routable interface for administration and integrations.
- **Monitoring interface:** passive packet-ingest interface; normally no production IP, default gateway, or user traffic.
- **Expansion ports:** additional appliance NICs/slots; their role depends on the installed module and approved configuration.

## Authoritative references

- [Nozomi technical specifications](https://www.nozominetworks.com/platform/technical-specifications)
- [Guardian installation documentation](https://technicaldocs.nozominetworks.com/products/n2os/topics/installation/virtual/t_vm_monitor-interface_add_guardian.html)
- [Remote Collector overview](https://technicaldocs.nozominetworks.com/products/remote-collector/topics/intro/c_rc-1.html)
- [Nozomi network sensors](https://technicaldocs.nozominetworks.com/products/nozomi/c_nozomi_platform_sensors_network.html)

This package is deliberately model-neutral. Exact connector numbers, maximum traffic rates, supported optics, node counts, collector limits and features vary by hardware and release.
