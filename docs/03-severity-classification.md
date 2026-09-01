# Severity Classification

OT severity is **consequence-driven**, not data-driven. A ransomware note on an IT laptop and a one-bit change to a safety controller are not the same class of event even if both are "malware." Severity is the *higher* of the IT-impact and OT-consequence assessments, and it accounts for **potential** consequence, not just realized.

## Severity levels

| Level | Name | OT/process consequence | IT consequence | Response |
|-------|------|------------------------|----------------|----------|
| **SEV-1** | Critical | Safety system affected/defeated; imminent risk to people/environment; loss of control or view of a critical process; production down | Enterprise-wide compromise; critical data/system loss | Full IR team, executive + safety engaged, 24/7, regulator likely |
| **SEV-2** | High | Confirmed unauthorized activity on OT assets (L2-L3); single-loop/process integrity at risk; degraded control | Confirmed compromise of key IT systems; sensitive data at risk | IR team activated, operations engaged, IC assigned |
| **SEV-3** | Medium | Suspicious activity in OT/DMZ zones; recon; policy violation; no confirmed process impact | Contained malware; limited unauthorized access | SOC-led, operations informed, standard hours + on-call |
| **SEV-4** | Low | Anomaly needing review; near-miss; single benign-looking indicator | Minor policy violation; blocked attempt | SOC triage, monitor, document |

## Consequence dimensions (score the incident on each)

- **Safety** — could this harm people or environment? *Any credible yes forces SEV-1/2.*
- **Process control** — is control or view of the process lost or degraded?
- **Scope** — one asset, one zone, or spreading across zones?
- **Confidence** — confirmed malicious, suspicious, or unconfirmed?
- **Potential** — worst credible outcome if it progresses uncontained?

## The OT escalators (auto-raise severity)

Raise severity immediately if **any** are true:
- A **safety-instrumented system (SIS)** or safety-related tag is involved → minimum SEV-1.
- **Controller logic or firmware** shows unauthorized modification → minimum SEV-1.
- **Loss of view or loss of control** reported by operators → minimum SEV-1.
- Activity confirmed **at or below Purdue Level 2** with control-affecting capability → minimum SEV-2.
- **Cross-zone movement** from IT into OT confirmed → minimum SEV-2.

## Potential vs realized

An adversary with confirmed access to an engineering workstation that *can* program a controller is SEV-1/2 on **potential**, even if no malicious logic change has been observed yet. In OT you respond to capability and position, not only to executed harm — because executed harm can be a physical event you cannot undo.
