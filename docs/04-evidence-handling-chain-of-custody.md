# Evidence Handling & Chain of Custody

Evidence is only as good as its integrity and its provenance. If the incident may lead to legal action, insurance claims, regulatory findings, or internal HR action, every artifact must be defensibly collected, integrity-verified, and custody-tracked. This applies even when you *think* it won't — you rarely know at collection time.

## Order of volatility (RFC 3227, OT-adapted)

Collect most-volatile first — **but never let volatility override safety.** In OT, the safest sources (historian, network capture) are also durable, so lead with them while volatile host/controller state is captured only when safe.

| Rank | Evidence | Volatility | OT note |
|------|----------|-----------|---------|
| 1 | CPU registers/cache, live memory (RAM) | Seconds–minutes | Capture from Windows OT hosts only if the host tolerates it; **do not** run intrusive tooling on a fragile HMI mid-process |
| 2 | Network state: live connections, ARP/MAC tables, session tables | Seconds–minutes | Capture from network devices/taps — non-disruptive, do early |
| 3 | Running processes, logged-on users, open handles | Minutes | Prefer EDR/agent telemetry over live poking |
| 4 | Controller volatile state: live logic, force tables, diagnostic buffer | Minutes–hours | **High value, high risk** — read-only upload, engineer-led, capture-or-lose |
| 5 | Temp/pagefile/swap | Hours | |
| 6 | Disk artifacts: event logs, prefetch, registry, $MFT | Hours–days | Bread-and-butter host forensics |
| 7 | **Historian values & alarm journal** | Days–months | **Durable, safe, decisive** — the physics record; pull early and often |
| 8 | Remote/archived logs, SIEM, backups, physical config | Months+ | |

**The OT inversion:** because #7 (historian) is both safe to collect and decisive for proving physical impact, treat it as an early-priority source even though it's low on the volatility scale. Volatility ordering tells you what's *decaying*; the historian tells you what actually *happened to the process*.

## Collection principles

- **Copy, don't work on the original.** Image/export to a working copy; analyze the copy.
- **Hash everything at collection.** SHA-256 the artifact the moment you collect it; record the hash in the evidence log. Re-hash before analysis to prove integrity.
- **Use write-blockers** for disk imaging. Use tested, dedicated collection media that has never touched a production OT network.
- **Timestamp and record source.** Every artifact: what, where (exact host/path/device), when (collection time + source timezone), who collected it, tool + version used.
- **Preserve source timestamps.** Note the source system's clock and any skew vs. a trusted reference — OT clocks drift and matter for timeline reconstruction.
- **Prefer least-intrusive method.** Passive tap over active scan; agent telemetry over live login; read-only upload over anything that writes.
- **Two-person integrity** for high-stakes OT acquisition (one acts, one records) — protects both the evidence and the responder.

## Chain of custody

Every artifact carries an unbroken record of who held it, from collection to disposition. Any gap can invalidate it. Use [`../templates/chain-of-custody-form.md`](../04-response/templates/chain-of-custody-form.md) and [`../templates/evidence-collection-log.md`](../04-response/templates/evidence-collection-log.md).

Each transfer records: artifact ID, date/time, from-whom, to-whom, purpose, and storage location/state. Store evidence with access control; log every access.

## Integrity verification

```bash
# At collection
sha256sum artifact.evtx | tee -a evidence-hashes.txt
# Before each analysis session, re-verify
sha256sum -c evidence-hashes.txt
```

For network captures, hash the pcap immediately after the capture stops. For historian exports, export to an immutable format (CSV/PI export) and hash it; note the query and time range used so the extraction is reproducible.

## Legal hold & retention
On any incident with potential legal/regulatory weight, Legal issues a **legal hold** — suspend routine deletion/rotation of relevant logs and backups. Confirm SIEM and historian retention windows cover the incident timeline before rotation erases them. This is time-critical: OT logs and historian data can roll off faster than the investigation runs.
