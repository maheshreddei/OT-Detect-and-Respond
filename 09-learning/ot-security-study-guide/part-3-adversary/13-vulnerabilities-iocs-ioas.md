# Chapter 13 — Vulnerabilities, IOCs and IOAs

> Part III. How to think about OT weakness and evidence: prioritize vulnerabilities by consequence, and understand why behavioral and process indicators beat atomic ones in industrial environments.

## 13.1 Consequence-based vulnerability prioritization

A CVSS score alone is a poor guide in OT. Triage each vulnerability with three questions:

1. **Is the vulnerable device reachable from outside its zone?** If not, deprioritize — segmentation is a compensating control.
2. **Does exploitation cause a safety-relevant effect** (crash, halt, logic change, loss of protection)? If yes, escalate regardless of CVSS.
3. **Is there a compensating detection?** If not, write one now — a detection ships in hours; a patch may wait months for an outage.

This produces a ranking driven by **reachability × consequence**, not by base score. A medium-CVSS bug on a breaker-controlling device outranks a critical-CVSS bug on an isolated reporting server.

## 13.2 Insecure-by-design is not a CVE

Many of the most important OT weaknesses are not vulnerabilities in the CVE sense — they are **design features**: unauthenticated writes, plaintext protocols, no integrity on commands. No patch fixes them because they are how the protocol works. You address these by **segmentation and detection**, not remediation. Treat "insecure by design" as a permanent condition to monitor, not a bug to wait on.

## 13.3 Three layers of evidence

Evidence in OT comes in three layers, of increasing value:

- **Atomic IOCs** — hashes, IPs, domains. **Weak in OT:** they age out fast and rarely match, because industrial attacks are often bespoke and human-operated. Search them as a quick check; expect little.
- **Behavioral IOAs (Indicators of Attack)** — *actions and patterns*: a write from a non-master, a program download, a mode change, a new east–west conversation. **Durable and high-value** — they describe what the attacker *does*, which is hard to change.
- **Process indicators** — the *physical* evidence (Chapter 17): a value driven toward a trip while the view looks normal; a setpoint outside the safe range; a command whose feedback disagrees. **The strongest layer**, because the attacker cannot achieve the physical goal without producing them.

## 13.4 Why IOAs and process indicators win in OT

In IT, atomic IOCs still have real value (large-scale commodity malware reuses infrastructure). In OT, attacks are targeted, human-operated, and often use legitimate tools, so atomic indicators seldom fire. The **actions** (IOAs) and the **physical effects** (process indicators), by contrast, are unavoidable — an attacker who wants to change the process *must* issue a write and *must* move the process. Anchor your highest-confidence detections there and use atomic IOCs only as a supplementary check.

## Chapter summary
- Prioritize vulnerabilities by **reachability × consequence**, not CVSS: is it reachable across a zone, does it cause a safety effect, is there a compensating detection?
- **Insecure-by-design** weaknesses have no patch — segment and monitor.
- Three evidence layers: atomic **IOCs** (weak in OT), behavioral **IOAs** (durable), and **process indicators** (strongest).
- Spend your effort on **IOAs and process indicators**; treat atomic IOCs as a quick supplementary check.

## Cross-references
- Chapter 14 (threat intel) supplies indicators; Chapter 17 develops process indicators; Chapter 20 turns IOAs into rules.
- Companion: `ics-procurement-language` (designing weakness out via requirements).
