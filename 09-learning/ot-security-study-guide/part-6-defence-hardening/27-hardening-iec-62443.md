# Chapter 27 — Security Hardening, Best Practices and IEC 62443

> Part VI · Defence & Hardening. Detection tells you when something is wrong; hardening reduces how often it can go wrong. This chapter is the defensive foundation, organized around the OT security standard, IEC 62443.

## 27.1 IEC 62443 in brief

**IEC 62443** is the family of standards for industrial automation and control system security. You don't need to memorize it, but you should know its key constructs:

- **Zones and conduits** — group assets of like trust into zones; control and monitor the conduits between them (Chapter 05). The organizing principle of OT network security.
- **Security Levels (SL 1–4)** — graduated protection targets, from casual/coincidental (SL1) up to a determined, well-resourced adversary (SL4). You assign a target SL to each zone based on consequence.
- **Foundational Requirements (7)** — identification/authentication, use control, system integrity, data confidentiality, restricted data flow, timely response to events, resource availability. A checklist of what "secure" means for a zone.
- **Roles** — the standard separates the **asset owner**, the **integrator**, and the **product supplier**, each with responsibilities. This is why procurement language (specifying security requirements to suppliers and integrators) is a real control.

## 27.2 Segmentation first

If you do one thing, **segment**. Zones and conduits with a real IT/OT boundary (DMZ) are the highest-value control in OT because they compensate for the insecure-by-design protocols (Chapter 06). Concretely:

- A genuine **IT/OT DMZ** — no direct IT-to-OT paths; all exchange through controlled brokers (jump host, replicated historian, data diode).
- **Internal segmentation** between control zones/cells so a foothold in one doesn't reach all.
- **Deny-by-default conduits** carrying only the specific, documented flows from the communication matrix.

## 27.3 Access hardening

Because access (not exploits) is the dominant attack path (Chapter 11), access controls pay off most:

- **MFA on all remote access**; no standing vendor VPNs without it.
- A controlled **jump host** as the single sanctioned path into OT; alert on anything that bypasses it.
- **Least privilege** and removal of **default vendor accounts** and shared credentials.
- Disciplined **vendor/contractor access** — time-bound, monitored, revoked promptly.

## 27.4 Device and host hardening

- **Disable unused services and ports** on devices and OT hosts.
- **Application allow-listing** on EWS/HMI/historian — these change rarely, so allow-listing is highly effective.
- **Control removable media** — a real vector even in isolated plants.
- **Key-switches in RUN** on controllers; PROGRAM mode only during authorized changes.

## 27.5 Process and program controls

Security is also process:

- **Management of Change (MOC)** — every change to logic, config, or network is authorized and recorded, which also makes deviations detectable.
- **Backups** of controller logic/config and their integrity protection (the forensic baseline of Chapter 26).
- **Patch/vulnerability management** within outage windows, prioritized by consequence (Chapter 13).
- An **OT-specific security policy** and periodic assessment against 62443.

## 27.6 Defense in depth

The unifying idea, shared with functional safety (Chapter 04): **layer independent controls so no single failure is catastrophic.** Segmentation, access control, hardening, monitoring, and response each catch what the others miss. You rarely patch your way to OT security; you **segment, control access, harden, and monitor** — 62443 gives the structure, and the boundary plus allow-lists do the heavy lifting.

## Chapter summary
- **IEC 62443** provides zones/conduits, **Security Levels (SL1–4)**, seven foundational requirements, and asset-owner/integrator/supplier roles.
- **Segment first** — a real IT/OT DMZ, internal segmentation, deny-by-default conduits.
- **Harden access** (MFA, jump host, least privilege, no default accounts) because access is the dominant vector.
- Harden **devices/hosts** (disable services, app allow-listing, media control, key-switch in RUN) and enforce **process controls** (MOC, backups, consequence-based patching).
- **Defense in depth** — layered independent controls; you segment/control/harden/monitor rather than patch your way to security.

## Cross-references
- Chapter 05 (zones/conduits), Chapter 11 (why access controls matter), Chapter 13 (consequence-based patching), Chapter 28 (operationalizing all this).
- Companion: `ics-procurement-language` (62443-aligned supplier/integrator requirements).
