# Chapter 14 — OT Threat Intelligence

> Part III. Intelligence is only useful when it changes what you look for. This chapter is a method for turning advisories, reports, and tracked-group intel into hunts your specific plant can actually run.

## 14.1 Relevance first

Before acting on any report, triage it for relevance to *your* environment, in this order:

1. **Sector and geography** — does this plausibly apply to me? If not, file it strategically and move on.
2. **Affected products and versions** — check against the **asset inventory *before* reading further**. If you don't run the targeted vendor/protocol/product, the urgency drops sharply.
3. **Access vector** — how did they get in? Map it to your boundary controls (remote access? internet exposure? supply chain?).
4. **Techniques** — map to ATT&CK for ICS and Enterprise IDs.
5. **Behavioral indicators** — what would this look like in *my* telemetry? This is the part that becomes a hunt.
6. **Atomic IOCs** — hashes/IPs/domains; search them but expect little.
7. **Detections offered** — Sigma/Snort/YARA; **test before deploying**.

This ordering saves enormous effort: most reports are "not applicable," and deciding that quickly is a legitimate, valuable outcome.

## 14.2 From report to hunt

Every consumed report should produce one of three outputs — never just be read and filed:

- **A hunt** — a concrete, testable question in your telemetry derived from the behavioral indicators.
- **A detection** — a durable rule if the behavior is worth watching continuously.
- **A documented "not applicable"** — a coverage decision with a reason, so you don't re-triage it later.

For example, a report that a group compromised water-treatment HMIs via internet-exposed remote access and altered dosing setpoints becomes concrete hunts: enumerate internet-reachable plant assets; search authentication logs for successful HMI logins from non-RFC1918 addresses; search the historian for dosing-setpoint writes outside the approved range or outside operating hours; verify default vendor accounts are disabled on every HMI.

## 14.3 Tracked activity groups

Know the ICS-relevant activity groups by their **behaviors and targeted sectors**, not just their names. Vendors and CERTs track groups with industrial capability; the useful takeaway from each is "which sectors, which access vectors, which techniques" — which feeds your relevance triage and your hunt backlog. Names change; behaviors and target patterns are what you defend against.

## 14.4 Sources worth following

- National CERTs and ICS-CERT-style advisories (vulnerabilities and campaign reporting).
- Vendor threat-intel from OT-focused firms (behavior-rich, sector-specific).
- ISACs for your sector (peer sharing).
- The vendors of your own equipment (product advisories mapped to your asset inventory).

## Chapter summary
- Triage every report for **relevance first** (sector/geography → products/versions → vector → techniques → behaviors → IOCs → offered detections).
- Turn each report into **a hunt, a detection, or a documented not-applicable** — never just read-and-file.
- Know tracked groups by **behavior and target sector**, not name.
- Check advisories against your **asset inventory** before spending effort.

## Cross-references
- Chapter 10 (ATT&CK mapping), Chapter 13 (indicators), Chapter 16 (intelligence-driven hunting).
