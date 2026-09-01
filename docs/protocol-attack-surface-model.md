# The Attack-Surface Model

Read this once and the per-protocol pages become variations on a theme. Defending OT protocols comes down to three properties they mostly share and three questions those properties force you to ask.

## Three properties of (most) OT protocols

1. **No authentication.** The protocol doesn't verify who's talking. A PLC answers a read or executes a write regardless of source. (Exceptions and partial mitigations exist — OPC UA can authenticate; DNP3-SA and IEC 62351 add security — but in the field they're often unused.)
2. **No authorization.** Even where a session exists, there's usually no notion of "this client may read but not write." Any client that can reach the device can, in principle, command it.
3. **No encryption / integrity.** Traffic is cleartext and often un-integrity-protected, so it can be read, replayed, or (on a shared segment) spoofed.

The consequence: **the protocol provides none of the access control you'd assume from IT.** The security has to come from the *network* (segmentation, allow-lists) and from *your detection layer*. Detection isn't a nice-to-have here; it's compensating for a control the protocol structurally lacks.

## The recon → command spectrum

Every one of these protocols exposes operations that fall on a spectrum from harmless-looking to process-affecting:

```
  DISCOVER            READ / BROWSE            WRITE / COMMAND            DISRUPT
  ────────            ─────────────            ──────────────            ───────
  find devices,       enumerate points,        write a value, operate    stop CPU,
  ports, banners      tags, registers,         a point, publish to a     download logic,
  (Nmap, Who-Is,      address space            command topic/IOA/node    force outputs
  device id)          (recon in depth)         ("ShockPLC command")      (max impact)
       │                     │                        │                       │
   abnormal in           the intel an              THE event that          rare, severe,
   a steady-state        attacker needs to         changes the             unambiguous
   OT segment            target the process        physical process
```

- **Discover / Read** operations are how an attacker *learns* the process. In a steady-state OT network these are often abnormal in themselves — engineering tools poll known devices in known patterns; broad discovery or enumeration from an unexpected host is a signal.
- **Write / Command** operations are the events that *change* the process. The range's "ShockPLC command" points are the archetype: a write to a specific IOA / tag / node / topic / object that drives a malicious action. **These are your highest-severity detections** — a write to a command point from a non-engineering source is close to a true positive by construction.

This is why the per-protocol pages split observed operations into **read/recon** vs **write/command** — the split *is* the severity model.

## The three questions every detection answers

1. **Who ↔ what?** Which source talked to which OT asset? Baseline the legitimate client↔server pairs (engineering stations, HMIs, SCADA masters) so anything outside the baseline stands out. This alone catches most attacks, because attackers speak from the wrong place.
2. **Allowed pair?** Is that source *permitted* to speak this protocol to this device? A workstation that has never spoken Modbus suddenly issuing function codes is the whole detection.
3. **Read or write?** Is this recon (read/browse/discover) or impact (write/command/operate)? Weight severity accordingly; alert hard on writes to control/command points.

Answer these three and you've reconstructed the authorization the protocol never had.

## Purdue placement — where you'll see each protocol

| Purdue level | Typical protocols | Who legitimately speaks them |
|--------------|-------------------|------------------------------|
| L0–L1 (process / control) | Modbus, S7comm, EtherNet/IP, IEC 61850 GOOSE/SV, PROFINET | PLCs, IEDs, I/O, controllers |
| L2 (supervisory) | Modbus, DNP3, IEC-104, OPC UA, S7comm, BACnet | HMIs, SCADA masters, engineering workstations |
| L2–L3 (site / DMZ) | OPC UA, MQTT, HTTP, historian feeds | Historians, gateways, MES, brokers |
| IT / access into OT | HTTP, VNC, FTP, RDP, SSH | Jump hosts, vendor access, EWS remote sessions |

Two placement rules drive detection:
- **Control protocols crossing a zone boundary** (e.g. Modbus originating from IT, or an IEC-104 command arriving from outside the SCADA zone) is high-signal — these should be intra-zone.
- **IT/access protocols reaching control assets** (VNC/FTP/HTTP straight to a PLC or EWS from an unexpected source) is the pivot you most want to catch.

## What this means for the detection library
Because the model is shared, your detections are largely **reusable patterns instantiated per protocol**:
- *Unauthorized client* — new source speaking the protocol to an OT asset.
- *Recon* — discovery/enumeration/broad reads from an unexpected source.
- *Write/command* — any write/operate to a control or command point, especially cross-zone or off-hours.
- *Disruptive function* — protocol-specific "stop/download/force" operations.
- *Baseline deviation* — new asset, new pair, new function code, off-schedule polling.

The per-protocol pages fill in the specific function codes, services, and log fields that make each pattern concrete.
