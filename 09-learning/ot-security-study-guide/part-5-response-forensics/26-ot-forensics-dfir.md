# Chapter 26 — OT Forensics / DFIR

> Part V. Digital forensics in OT is shaped by one hard constraint: you usually cannot turn the systems off. This chapter is how you preserve and analyze evidence from a plant that must keep running.

## 26.1 The constraint that defines OT DFIR

Standard DFIR often begins with "image the disk, capture memory, take it offline." In OT, taking a controller or HMI offline may stop production or defeat protection. So OT forensics leans on the evidence you can gather **without stopping the process**: network artifacts, host artifacts from the Windows OT machines, the historian, and carefully authorized device acquisition during planned windows.

## 26.2 The evidence sources, in order of accessibility

- **Network (PCAP + Zeek logs)** — the wire truth, captured passively; often your richest and safest source. What was written, downloaded, or commanded is on the network.
- **Windows OT hosts (EWS/HMI/historian)** — Windows Security logs, Sysmon, memory and disk artifacts from the engineering and operator stations, where hands-on-keyboard activity leaves traces.
- **Historian** — the physical record around the event: what the process actually did, when setpoints changed, when trips fired.
- **Controller state** — diagnostic buffers, the running program, force tables, online-edit history, communication/security config — acquired carefully and with engineering support.

## 26.3 Controller triage without stopping the device

Three questions reveal most controller tampering and can often be answered without a shutdown:

1. **Does the running logic match the known-good baseline?** Upload the running program and diff it against the version captured under change control. Any difference is proof of modification (this is why baselining matters — see 26.5).
2. **What's in the force table and online-edit history?** Forces disconnect logic from reality; edit history shows what changed and when.
3. **Which sources are allowed to write, and which actually did?** Compare the controller's communication/security config and observed writers against the command allow-list.

These are read-oriented checks that expose the classic manipulations (logic change, forcing, unauthorized writes) without taking the controller down.

## 26.4 Chain of custody

OT incidents can become safety, insurance, or regulatory investigations, so treat evidence formally from the first moment: **hash on collection, work only from copies, and document everything** — who collected what, when, from where, and how. This discipline costs little during collection and is irreplaceable later.

## 26.5 Forensics is set before the incident

The uncomfortable truth: your forensic capability is largely determined *before* anything happens, by two things you either did or didn't do earlier:

- **Did you capture known-good baselines** — controller logic/config, asset inventory, conversation and command allow-lists? Without them, you cannot tell "changed" from "normal."
- **Did you retain the telemetry** — enough PCAP/Zeek/host/historian history to reconstruct the event? Without retention, the evidence expired before you looked.

Network, historian, and host artifacts carry most OT cases — but only if you prepared to have them.

## Chapter summary
- OT DFIR is defined by the **can't-power-off constraint**; it relies on **network, host, historian, and careful controller acquisition.**
- **Controller triage** = running-logic-vs-baseline, force table/edit history, and allowed-vs-actual writers — mostly without a shutdown.
- Maintain **chain of custody** (hash, copies, documentation) — OT incidents become formal investigations.
- Forensic capability is **set before the incident** by baselines and telemetry retention.

## Cross-references
- Chapter 07/09 (artifacts and telemetry), Chapter 18 (PCAP), Chapter 25 (IR), Chapter 02 (controller internals).
- Companion: `it-ot-incident-response` (evidence-source matrix, safe acquisition guides).
