# TDA-IT-003 — DNS tunnelling

| Field | Value |
|-------|-------|
| Use case | C2 / exfil over DNS |
| Detection tested | OUT-01 |
| ATT&CK | T1071.004 App Layer: DNS · T1048 Exfil over Alt Protocol |
| TDA goals | Log validation · Logic · FP reduction · Speed |
| Layer / severity | IT / egress · High |
| Environment | Lab / authorized |

## Objective
Prove that high-volume, long-label DNS to a single domain is detected as tunnelling without flooding on normal chatty domains.

## Preconditions (log validation)
- DNS query logs (`DnsEvents` / CIM `Network_Resolution` / MDE `DeviceNetworkEvents`) feeding the SIEM.
- OUT-01 rule deployed; baseline of normal DNS built.

## Attack simulation
Lab resolver + lab-controlled domain. Record start time.
```
# Generate many long-label queries to one lab domain (benign payload)
for i in $(seq 1 600); do
  nslookup "$(head -c 40 /dev/urandom | base32 | tr -d = ).tunnel.lab-domain.test" >/dev/null 2>&1
done
```
(Or use a DNS-tunnelling test tool against a **lab** domain you control.) Capture start time.

## Expected detection
OUT-01: high query volume + long average sub-label length / high distinct subdomains for one domain → alert. Fields: **client IP, domain, query count, avg label length**.

## Validation criteria
- [ ] Data present — DNS query logs for the client arrived.
- [ ] Rule fired — OUT-01 alert on the lab domain.
- [ ] Fidelity — client, domain, volume, label-length present.
- [ ] Speed — MTTD ≤ target.
- [ ] **FP** — chatty-but-benign domains (CDNs, telemetry) do **not** trigger.

## Result (fill in)
State: ☐ Pass ☐ Partial ☐ Fail-no-rule ☐ Fail-no-data · MTTD: ____ · Evidence: · Notes:

## Remediation (if failed)
- No data → enable DNS query logging / MDE network events.
- Miss → tune volume & label-length thresholds against the baseline.
- FP-prone → allow-list known high-volume legitimate domains; then retest.
