# Monitoring Architecture (How to Watch an SIS Safely)

The overriding constraint: **monitoring the SIS must never affect its safety function.** A safety controller taking a demand while a monitoring tool perturbs it is unacceptable. Everything here is passive and read-only.

## Hard rules
- **Passive only.** Instrument the safety network with a **tap/SPAN**, not an inline device. Never active-scan, port-scan, or probe safety controllers. Never run a query that writes.
- **No new load on the SIS.** Don't poll the safety controller for data; consume its **diagnostic/event logs** and the **historian** instead. If a value is needed, take it from the historian or a passive capture, not a live read of the SIS.
- **Read-only accounts** for any log/historian collection, least privilege.
- **Change nothing on the safety network** during monitoring setup without following the plant's functional-safety management-of-change.

## Sensor placement
- Place the NDR/tap on the **safety network segment** so it sees SIS engineering and controller traffic. A sensor north of the SIS↔BPCS boundary will miss intra-SIS traffic.
- Tap the **SIS↔BPCS interface/gateway** to see the boundary exchange (category A).
- Where the SIS engineering station is on a separate segment, ensure the tap covers the path between it and the safety controllers (category B).
- For final-element / line-monitoring status, take it from the SIS diagnostics or historised I/O — not by probing the circuit.

## Collection pattern
```
  Safety sensors → SIS logic solver → final elements        (the SIF - do not touch)
        │                │  │                                 
        │        (passive tap on safety network)  ─────────────► NDR (Nozomi/Dragos) ──┐
        │                │  └─ diagnostic/event log  ───────────────────────────────────┤
        │                └─ status/trip/bypass/voting → Historian ──────────────────────┤
  SIS engineering station ─ EDR/host logs ────────────────────────────────────────────┤
  SIS↔BPCS gateway ─ interface logs ──────────────────────────────────────────────────┤
                                                                                        ▼
                                                                     SIEM (correlate, alert, IR)
                                                                     — read-only, no path back to SIS
```

## Conduit rules
- The path from SIS telemetry to the SIEM is **outbound only** — no inbound path from the SIEM or IT into the safety network.
- Prefer a **data-diode / unidirectional** feed off the safety segment where available.
- Treat the SIS engineering station as a crown-jewel host: it's the TRITON entry point — EDR it, restrict it, and monitor its sessions closely.

## Response note
Because any confirmed SIS detection is minimum **SEV-1**, wire these detections to a path that engages the **plant safety authority**, not just the cyber on-call. And keep the detections themselves passive — the response may involve the SIS, but the monitoring never does.
