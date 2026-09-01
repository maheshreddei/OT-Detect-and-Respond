# Chapter 14 — Observability & Tracing

> Part V · Production. You cannot fix what you cannot see. Because an agent's behavior is a dynamic, multi-step trajectory, observability — capturing every step of every run — is what makes agents debuggable, improvable, and trustworthy in production.

## 14.1 Why agents need tracing especially

A single agent run may involve a dozen model calls and tool executions, branching decisions, and retries. When it does something wrong — loops, picks the wrong tool, gives a bad answer — "it broke" is useless. You need the **full trajectory**: every prompt, every model output, every tool call and result, with timing and cost. Tracing turns an opaque black box into a readable story you can diagnose.

## 14.2 What to capture

For every run, capture a **trace** made of **spans** (one per step):

- **Inputs/outputs** of each model call (the actual prompts and completions).
- **Tool calls** — name, arguments, result, success/failure.
- **Decisions** — which path/tool the model chose and (if ReAct) its reasoning.
- **Timing** — latency per step and end to end.
- **Cost** — tokens and dollars per step and per run.
- **Metadata** — model/version, prompt version, user/session, outcome.

A trace is a tree: the run at the root, spans for each step, nested spans for sub-steps or sub-agents.

## 14.3 Tooling

Dedicated LLM-observability platforms make this turnkey — **LangSmith**, **Langfuse**, and others — with framework integrations that auto-instrument the loop, plus dashboards for latency, cost, and error rates, and the ability to save interesting traces into eval datasets. Most agent frameworks (Chapter 09) have first-class hooks into these. If you build from scratch (Chapter 08), emit structured logs per span and ship them to your tracing backend. Either way, **instrument from day one** — retrofitting observability after a production incident is painful.

## 14.4 Using traces

Observability pays off in four ways:

- **Debugging** — replay a failed run step by step to see exactly where it went wrong.
- **Cost/latency optimization** — find the expensive or slow steps and fix them (Chapter 16).
- **Quality improvement** — spot patterns of failure across runs (a tool that's often misused, a prompt that's often misread) and fix the root cause.
- **Eval dataset growth** — promote real production failures into your eval set (Chapter 13), closing the loop between observability and evaluation.

## 14.5 Production monitoring

Beyond per-run tracing, monitor in aggregate:

- **Success/failure rate** and common failure modes.
- **Cost and latency** trends (per run, per user, per day).
- **Tool error rates** — a spiking tool failure often precedes agent failures.
- **Drift** — quality changes after a model/prompt update or a change in input mix.
- **Alerts** on anomalies (cost spike, error surge, latency regression).

This is the same operational discipline as any production system, applied to the agent's unique step-level behavior.

## 14.6 The loop that ties Part V together

Observability, evaluation, and improvement form one loop: **trace production → find failures → add them to evals → fix and re-evaluate → ship → trace again.** This is how an agent gets *better* in production instead of silently degrading. Teams that run this loop ship reliable agents; teams that don't ship demos that erode.

## Chapter summary
- Agents are multi-step and dynamic, so **tracing the full trajectory** is essential to debug and improve them.
- Capture per-step **spans**: model inputs/outputs, tool calls/results, decisions, timing, cost, metadata.
- Use **LLM-observability tools** (LangSmith, Langfuse) with framework integrations; instrument from day one.
- Use traces to **debug, optimize cost/latency, improve quality, and grow eval sets**; monitor **success rate, cost, tool errors, and drift** in aggregate.
- Observability + evaluation + fixing form the **improvement loop** that keeps agents reliable in production.

## Cross-references
- Chapter 13 (evaluation) consumes traces; Chapter 16 (cost/performance) acts on them; Chapter 08/09 for where to instrument.
