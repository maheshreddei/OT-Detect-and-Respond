# Chapter 16 — Deployment, Cost & Performance

> Part V · Production. The final step: running the agent as a reliable service and keeping it fast and affordable. Agents have a unique cost/latency profile — many model calls per task — so optimization here has outsized impact.

## 16.1 Serving an agent

An agent in production is a service with some specific needs:

- **Long-running requests** — a task may take many steps and seconds to minutes. Use async processing and, for long tasks, a **job queue** with status polling or streaming rather than a blocking request.
- **Streaming** — stream steps/tokens to the UI so users see progress; agents feel slow otherwise.
- **State management** — persist conversation/task state (Chapter 06) in a store, not in memory, so runs survive restarts and scale across workers.
- **Concurrency** — model-call latency dominates, so agents are I/O-bound; scale with async workers.
- **Resilience** — retries with backoff for transient model/tool errors, timeouts, and graceful degradation (fall back to a simpler path or a human).

## 16.2 The cost problem

Agents can be expensive because **each step is a model call**, and a task may take many steps — cost multiplies by trajectory length. A careless agent can cost 10–50× a single LLM call. Control it deliberately.

## 16.3 Cost and latency levers

- **Model routing** — use a strong (costly) model only for hard reasoning/planning steps; use a cheaper/faster model for routine steps (formatting, simple extraction, easy tool selection). This is often the biggest single lever.
- **Prompt caching** — cache stable prefixes (system prompt, tool schemas, long context) so repeated calls don't re-pay for them; major savings on agents that reuse a large fixed context.
- **Limit steps and context** — enforce step budgets (Chapter 03) and curate the context window (Chapter 06); shorter trajectories and leaner context cost less and often work better.
- **Parallelize** independent steps (Chapter 10) to cut latency.
- **Reduce tool round-trips** — a well-designed tool that returns everything needed beats three chatty tools.
- **Batch and pre-compute** — do expensive work (embeddings, retrieval indexing) offline, not per request.
- **Right-size retrieval** — retrieve fewer, better chunks (Chapter 07) rather than stuffing context.

## 16.4 Reliability in production

- **Handle model/tool failures** — treat them as expected; retry transient errors, and have a fallback (a simpler model, a cached answer, or human escalation). Some SDKs support **fallback model chains** natively.
- **Idempotency** — design write actions so a retry doesn't double-charge or double-send.
- **Graceful degradation** — if the agent can't complete, return partial progress and escalate rather than failing silently.
- **Versioning** — version prompts, tools, and models; you need to know exactly what ran when debugging (ties to observability, Chapter 14).

## 16.5 The pre-launch checklist

Before an agent handles real traffic:

- [ ] **Evaluation** passes on your task set, including edge and safety cases (Ch 13).
- [ ] **Observability/tracing** is live — every run is traceable (Ch 14).
- [ ] **Guardrails** are in place — input/output/action, budgets, human-in-the-loop for high-stakes (Ch 15).
- [ ] **Cost controls** — step/budget limits, model routing, prompt caching (this chapter).
- [ ] **State** persists durably; runs survive restarts.
- [ ] **Failure handling** — retries, fallbacks, graceful degradation, escalation.
- [ ] **Monitoring & alerts** — success rate, cost, latency, tool errors, drift.
- [ ] **Rollback** — you can revert a prompt/model/tool change quickly.

## 16.6 Iterate in production

Launch is the start, not the end. Run the improvement loop (Chapter 14): trace real usage, evaluate against it, find failures, fix them, re-evaluate, ship. Start with **tighter guardrails and more oversight**, and loosen them as evaluation earns trust. Agents that are measured and iterated get better; agents that are shipped and forgotten degrade.

## Chapter summary
- Serve agents as **async, streaming, stateful** services with **job queues** for long tasks and **resilience** (retries, timeouts, degradation).
- Agents are costly because **cost scales with trajectory length**; the biggest levers are **model routing, prompt caching, step/context limits, parallelization, and fewer tool round-trips.**
- Build for reliability: **failure handling with fallbacks, idempotent writes, graceful degradation, and versioning.**
- Ship against a **pre-launch checklist** (eval, observability, guardrails, cost controls, durable state, failure handling, monitoring, rollback).
- **Iterate in production** via the trace→eval→fix loop; loosen guardrails as trust is earned.

## Cross-references
- Chapter 04 (model routing), Chapter 06 (context/state), Chapter 13–15 (eval/observability/guardrails), Chapter 03 (budgets).
