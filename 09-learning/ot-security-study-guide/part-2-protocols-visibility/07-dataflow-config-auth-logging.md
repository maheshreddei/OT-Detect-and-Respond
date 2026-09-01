# Chapter 07 — Data Flow, Configuration Files, Authentication and Logging

> Part II. Before you can hunt, you must know where data and commands flow, where the evidence lives, and the hard limits of authentication and logging in OT. This chapter maps the terrain your later investigations depend on.

## 7.1 How data and commands flow

Data flows **up**; commands flow **down**.

```
   Field I/O ─▶ Controller ─▶ SCADA/HMI ─▶ Historian ─▶ MES ─▶ Enterprise/ERP
   (measure)    (control)     (supervise)   (record)    (manage)  (business)
   commands ◀────────────────────────────────────────────  (setpoints, recipes)
```

Two observation points dominate because so much flows through them: the **historian** (every value and event, the physical record) and the **IT/OT boundary/DMZ** (everything crossing between OT and IT). If you can only instrument a few places, these two plus the engineering/operator hosts give disproportionate coverage.

## 7.2 Configuration artifacts — the plant's DNA

OT runs on configuration, and that configuration is both your reference baseline and an attacker's target:

- **Controller projects / logic** — the ladder/FBD/ST programs; the "known-good" you compare against in forensics.
- **Firmware** — the layer below logic; a stealthy persistence target.
- **HMI/SCADA projects** — screens, tags, scripts.
- **Network configs** — firewall rules, switch/router configs, VLANs.
- **Engineering documents** — P&IDs, network diagrams, the communication matrix, the PLC I/O list, the cause-and-effect matrix.

These are exactly the documents you gather before a monitoring deployment (they define what "normal" is) and the artifacts you diff during an incident (running logic vs known-good). Store and integrity-protect them; their absence or staleness is itself a finding.

## 7.3 Authentication reality

Authentication in OT is weak or absent at the device layer by design:

- Controllers and many HMIs have **no real user identity** on the wire — the protocol doesn't authenticate.
- Where credentials exist, they are often **shared, default, or never rotated**.
- **Real identity control lives at the boundary**: the jump host, the VPN/remote-access gateway, and the OT domain (AD). This is precisely why those are Tier-1 log sources — they are where you *can* attribute actions to people.

The practical consequence: attribution in OT usually comes from correlating a boundary/identity event (who logged into the jump host) with an OT action (what write then occurred), not from the OT device itself.

## 7.4 Logging reality

Controllers log little natively. Visibility therefore comes from three places, in order of value:

1. **Passive network monitoring** — the wire is the ground truth for OT protocol actions.
2. **Host logs on Windows OT machines** — EWS, HMI, historian, jump host (Windows Security + Sysmon).
3. **The historian** — for the physical/process record.

Plan for the device-logging gap rather than being surprised by it. When a controller "won't tell you" what happened, the network capture and the historian will.

## 7.5 What this means for the hunter

Map, in advance, **where each kind of evidence lives**:

| Question | Where the evidence is |
|----------|-----------------------|
| Did a controller's logic change? | Network (program transfer) + the running logic vs baseline |
| Who made a change? | Boundary/identity logs (jump host, VPN, AD) correlated to the OT action |
| Did the process actually move? | Historian trends and alarms |
| What did an engineering host do? | Windows Security + Sysmon on the EWS/HMI |
| Was a config altered? | Config file diff vs the stored known-good |

Doing this mapping before an incident is the difference between a fast investigation and a scramble.

## Chapter summary
- Data flows up (to historian/MES/ERP), commands flow down (setpoints/recipes); the **historian and DMZ** are the richest observation points.
- Configuration artifacts (logic, firmware, HMI projects, network configs, engineering docs) are both your **baseline** and the attacker's target — store and integrity-protect them.
- Device authentication is weak; **attribution comes from the boundary/identity layer** correlated with OT actions.
- Device logging is sparse; visibility is **network + host + historian.**
- Pre-map where every kind of evidence lives.

## Cross-references
- Chapter 09 develops the telemetry/data-source picture; Chapter 26 uses these artifacts forensically.
- Companion repository: `ot-monitoring-deployment` (the pre-deployment document package and log-source matrix).
