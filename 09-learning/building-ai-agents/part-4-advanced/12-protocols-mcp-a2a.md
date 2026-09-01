# Chapter 12 — Protocols: MCP & A2A

> Part IV · Advanced. As agents proliferate, two open standards are becoming the connective tissue: **MCP** for connecting agents to tools/data, and **A2A** for agents to talk to each other. Understanding them future-proofs what you build.

## 12.1 Why protocols matter

Without standards, every tool integration is bespoke — you rewrite the same Slack/GitHub/database connector for each framework, and agents from different vendors can't collaborate. Protocols solve the **N×M problem**: instead of building every tool for every agent, you build a tool once against a standard and any compliant agent can use it. This is the same shift that USB or HTTP brought — a common interface that decouples the pieces.

## 12.2 MCP — Model Context Protocol (agent ↔ tools/data)

**MCP** is an open standard for connecting agents to **tools and data sources** through a uniform interface. The model:

- An **MCP server** exposes capabilities — **tools** (functions the agent can call), **resources** (data the agent can read), and **prompts** (reusable templates).
- An **MCP client** (inside your agent/framework) connects to servers and makes their capabilities available to the model.

Build a tool as an MCP server once, and **any MCP-aware agent** (Claude Agent SDK, Microsoft Agent Framework, and a growing list) can use it — no per-framework rewrite. <cite index="6-1">The MCP 2026-07-28 spec is in release-candidate status</cite>, and an ecosystem of ready-made MCP servers (for popular apps and databases) means you often **consume** existing servers rather than build your own.

```
  ┌────────────┐   MCP    ┌──────────────┐
  │  your      │◀────────▶│ MCP server:  │  (tools + resources + prompts)
  │  agent     │          │ GitHub / DB /│
  │ (MCP client)│         │ Slack / files│
  └────────────┘          └──────────────┘
```

**Practical guidance:** prefer standard MCP tools over bespoke integrations where a server exists; if you're building a reusable tool, consider shipping it as an MCP server so it works everywhere.

## 12.3 A2A — Agent-to-Agent (agent ↔ agent)

Where MCP connects an agent to tools, **A2A** connects **agents to each other** — a standard for agents (potentially built by different teams, on different frameworks/vendors) to discover each other's capabilities and collaborate. <cite index="6-1">A2A adoption crossed 150 organizations</cite>, and it's supported natively by frameworks like the Microsoft Agent Framework. The idea: an agent advertises what it can do (a capability description), and other agents can delegate tasks to it over a common protocol — cross-vendor multi-agent systems without custom glue.

## 12.4 MCP vs A2A — complementary, not competing

| | MCP | A2A |
|---|-----|-----|
| Connects | Agent → tools & data | Agent → agent |
| Analogy | Giving the agent hands and eyes | Letting agents talk to colleagues |
| Use when | You need the agent to *do*/read something | You need agents to *collaborate* across boundaries |

A realistic system uses **both**: your agents use **MCP** to reach tools and data, and **A2A** to delegate to specialized agents elsewhere.

## 12.5 Should you adopt them now?

- **MCP: yes, increasingly the default** — the tool ecosystem and native framework support make it the path of least resistance for integrations. Prefer it for new tool work.
- **A2A: adopt when you have real cross-boundary multi-agent needs** — it shines when agents span teams/vendors; for a single in-house multi-agent system, your framework's native orchestration (Chapter 11) may be simpler. Watch the space, as it's moving fast.

Because these standards are evolving quickly, treat version specifics as snapshots and check the current specs — but the *direction* (standard tool and agent interop) is durable and worth building toward.

## Chapter summary
- Protocols solve the **N×M integration problem** — build once against a standard, work everywhere.
- **MCP** connects agents to **tools/data** (servers expose tools/resources/prompts); increasingly the default for integrations, with a rich server ecosystem.
- **A2A** connects **agents to each other** for cross-boundary collaboration; adopt for real multi-team/vendor needs.
- They're **complementary** — MCP for hands/eyes, A2A for colleagues; a mature system uses both.

## Cross-references
- Chapter 05 (tools) and Chapter 09 (frameworks) for how MCP plugs in; Chapter 11 (multi-agent) for what A2A standardizes.
