# Communications & Regulatory Reporting

## Internal communications

- **Out-of-band channel first.** Assume email/AD/Teams may be compromised. Use a pre-established alternate (separate messaging, phone tree, physical control-room briefings).
- **Single source of truth.** The IC maintains the incident record; all status flows through it. Avoid parallel unofficial threads that fragment the timeline.
- **Need-to-know.** Especially for insider or safety-sensitive incidents. Broad broadcast can tip off an insider or trigger panic on the plant floor.
- **Operations briefing cadence.** The control room is briefed on any action that could touch the process, before it happens.

## External communications

Coordinated by Legal/Comms only. Responders do not talk to press, vendors' PR, or social media. Factual, minimal, approved statements.

## Regulatory reporting (verify current obligations — these change)

Reporting duties depend on sector and jurisdiction. **Confirm exact thresholds, recipients, and deadlines with Legal and your regulator** — treat the below as a prompt, not authority.

| Sector / region | Regime | Typical trigger & timing (verify) |
|-----------------|--------|-----------------------------------|
| EU essential/important entities | **NIS2** | Early warning within 24h, notification within 72h, final report within 1 month (to national CSIRT) |
| US electric (bulk power) | **NERC CIP-008** | Report Reportable Cyber Security Incidents to E-ISAC and CISA within defined hours |
| US pipeline | **TSA Security Directives** | Report to CISA within 24h |
| US public companies | **SEC cyber disclosure** | Material incident disclosed on defined timeline |
| UAE | **UAE Information Assurance (IA) Standards / sector regulator; aeCERT** | Report to relevant authority/CERT per sector critical-infrastructure rules |
| KSA | **NCA (ECC / OTCC)** | Report per National Cybersecurity Authority requirements |
| Sector ISACs | E-ISAC, WaterISAC, etc. | Voluntary/required info sharing |

**Practical rule:** start the regulatory clock assessment at declaration, not at closure. Many regimes count from *awareness*, and OT incidents with safety/availability impact frequently qualify. Get Legal engaged early so a reporting deadline isn't missed while the technical team is heads-down.

## Law enforcement & national authorities
For confirmed intrusions into critical infrastructure, engage national CERT / law enforcement per policy and jurisdiction (e.g. CISA, national CERT, aeCERT). Preserve evidence to their standards; coordinate through Legal.

## Information sharing
Share IOCs and TTPs with your ISAC and trusted community once Legal approves — it's often reciprocated and can reveal whether you're one of many targets in a campaign. Sanitize site-specific detail before sharing.
