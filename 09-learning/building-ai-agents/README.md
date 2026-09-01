# Building AI Agents — Start to End

**A complete, hands-on guide to designing, building, and shipping AI agents** — from the core concepts through working code, multi-agent systems, evaluation, and production deployment.

![Level](https://img.shields.io/badge/level-beginner%20%E2%86%92%20production-brightgreen)
![Focus](https://img.shields.io/badge/focus-LLM%20agents%20%C2%B7%20tools%20%C2%B7%20memory%20%C2%B7%20multi--agent-blue)
![Code](https://img.shields.io/badge/code-Python%20(framework--agnostic%20%2B%20frameworks)-yellow)
![License](https://img.shields.io/badge/license-MIT-green)

---

## Who this is for
Developers who can write Python and want to go from "I've called an LLM API" to "I've shipped a reliable agent." No prior agent experience assumed. Every concept is paired with runnable code, and every chapter ends with what to build next.

## The path, start to end

```
  UNDERSTAND ──▶ BUILD BLOCKS ──▶ FIRST AGENT ──▶ SCALE UP ──▶ PRODUCTION ──▶ SHIP
  what an agent   model, tools,    from scratch    patterns,     eval, tracing,   capstone
  is & when to    memory, RAG      then a          multi-agent,  guardrails,      + roadmap
  use one                          framework       protocols     deployment
     P1              P2               P3              P4             P5             P6
```

## Contents

**Part 1 — Foundations**
- [01 · What an AI agent is](part-1-foundations/01-what-is-an-agent.md) — agent vs chatbot vs workflow; when to use one
- [02 · The anatomy of an agent](part-1-foundations/02-anatomy-of-an-agent.md) — model, tools, memory, planning, the loop
- [03 · The agent loop](part-1-foundations/03-the-agent-loop.md) — ReAct, plan-and-execute, reflection

**Part 2 — Building blocks**
- [04 · The model layer](part-2-building-blocks/04-the-model-layer.md) — choosing a model, prompting, structured output
- [05 · Tools & function calling](part-2-building-blocks/05-tools-and-function-calling.md) — schemas, execution, MCP
- [06 · Memory](part-2-building-blocks/06-memory.md) — context, short-term, long-term, vector stores
- [07 · RAG for agents](part-2-building-blocks/07-rag-for-agents.md) — retrieval as a tool

**Part 3 — Your first agent**
- [08 · An agent from scratch](part-3-first-agent/08-agent-from-scratch.md) — the raw loop, no framework
- [09 · Building with a framework](part-3-first-agent/09-building-with-frameworks.md) — LangGraph, OpenAI Agents SDK, Claude Agent SDK

**Part 4 — Advanced & multi-agent**
- [10 · Agentic patterns & workflows](part-4-advanced/10-agentic-patterns-workflows.md) — chaining, routing, orchestrator-workers, evaluator-optimizer
- [11 · Multi-agent systems](part-4-advanced/11-multi-agent-systems.md) — handoffs, roles, when it helps (and hurts)
- [12 · Protocols: MCP & A2A](part-4-advanced/12-protocols-mcp-a2a.md) — standard tool and agent interop

**Part 5 — Production**
- [13 · Evaluation & testing](part-5-production/13-evaluation-and-testing.md) — eval harness, LLM-as-judge, trajectory eval
- [14 · Observability & tracing](part-5-production/14-observability-tracing.md) — spans, cost, latency, debugging
- [15 · Guardrails & safety](part-5-production/15-guardrails-and-safety.md) — validation, permissions, human-in-the-loop
- [16 · Deployment, cost & performance](part-5-production/16-deployment-cost-performance.md) — serving, caching, model routing

**Part 6 — Practice**
- [17 · Capstone & roadmap](part-6-practice/17-capstone-and-roadmap.md) — an end-to-end build + what to learn next

**Runnable code:** [`code/minimal_agent.py`](code/minimal_agent.py) · [`code/tools_example.py`](code/tools_example.py) · [`code/rag_agent.py`](code/rag_agent.py)

## How to use this guide
Read Part 1–2 for the mental model, then **build the from-scratch agent in Chapter 08** — it's the single most clarifying thing you can do. Only then reach for a framework (Chapter 09). Parts 4–5 are what separate a demo from something you can trust in production.

## The one idea to hold onto
> An agent is a **loop**: a language model that, given a goal and a set of tools, repeatedly decides an action, takes it, observes the result, and continues until the goal is met. Everything else — memory, planning, multi-agent, RAG — is a refinement of that loop. Master the loop first.

## A note on the fast-moving landscape
Agent frameworks change monthly. This guide teaches the **durable concepts** and shows current tools as examples; where a specific framework/version is named, treat it as a snapshot and check the project's docs for the latest. The fundamentals (the loop, tools, memory, evaluation) don't change.

## License
MIT — see [`LICENSE`](LICENSE).
