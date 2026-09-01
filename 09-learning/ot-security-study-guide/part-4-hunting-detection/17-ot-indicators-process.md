# Chapter 17 — OT Indicators: the Process Layer

> Part IV. The indicators unique to OT — the physical ones — are the highest-confidence evidence you have, because an attacker who wants a physical effect cannot avoid producing them. This chapter develops that layer in depth.

## 17.1 Three layers, one that matters most

Recall the three evidence layers (Chapter 13): atomic **IOCs** (weak in OT), behavioral **IOAs** (durable), and **process indicators** (strongest). Process indicators are the ones visible only in historian/process data — the physical reality of the plant — and they are the hardest for an attacker to fake and the most consequential when true.

## 17.2 The core process indicators

**Approach-to-limit.** A critical value being driven toward a trip point or safe limit, especially while the operator view looks normal, is the signature of a developing manipulation. You detect it by watching the *margin* to the trip and its *rate of change* — a value inside the pre-alarm band and still closing is high-signal.

**Setpoint anomaly.** A setpoint written **outside the approved engineering range**, or **outside operating hours**, or **by an unexpected source**. Oldsmar was exactly this. The three legitimacy questions for any write are: is the source an authorized HMI/EWS? is that register/tag one operators legitimately write? is the value inside the safe range?

**Command-versus-feedback mismatch.** The controller/SIS commanded a state, but the field feedback disagrees — the valve was told to close but position feedback says open. This means either a fault or a **manipulated view/actuator**, and it is one of the highest-confidence indicators because it exposes a lie between the digital command and the physical world.

**Frozen or replayed value.** A live process value that holds *perfectly* constant beyond its normal micro-variation, or repeats a prior pattern, suggests a **replay or spoof** feeding the operators old/false data (the Stuxnet technique).

**Voting/redundancy anomaly.** Redundant safety transmitters that disagree beyond tolerance, or a voting group that has silently degraded — protection eroding while the process still runs (Chapter 04).

## 17.3 Why the physical layer is decisive

An attacker can change tools, infrastructure, and even techniques, but to achieve a *physical* goal they must move the physical process — and that movement, or the lie required to hide it, appears in the process data. The historian is therefore not just an operational system; it is the sensor that watches the attacker's ultimate objective. Anchor your highest-confidence detections here, and pair every network-layer write detection with a historian check to separate a probe from a real impact.

## 17.4 Building process-indicator detections

Practically, this means:
- Curate the safety/process tags (Chapter 09): setpoints, trip points, critical values, bypass/mode states, redundant transmitters.
- Baseline each tag's normal range, variability, and update cadence.
- Alert on: margin-to-trip breaches with negative rate; setpoint writes outside range/hours/source; command-vs-feedback divergence; frozen values; voting degradation.
- Correlate with the network layer (who wrote it) and the identity layer (who was logged in) for a complete, high-confidence incident.

## Chapter summary
- **Process indicators** are the strongest OT evidence — visible only in the physical/historian data and unavoidable for an attacker seeking physical effect.
- Core indicators: **approach-to-limit, setpoint anomaly, command-vs-feedback mismatch, frozen/replayed value, voting degradation.**
- Apply the three **legitimacy questions** to every write (authorized source? legitimate register? safe value?).
- Anchor high-confidence detections in the historian; **pair network writes with a historian check** to separate probe from impact.

## Cross-references
- Chapter 03 (historian), Chapter 04 (SIS/voting), Chapter 09 (curated tags), Chapter 20 (building the rules).
- Companion: `ot-historian-detection`, `sis-safety-detection`.
