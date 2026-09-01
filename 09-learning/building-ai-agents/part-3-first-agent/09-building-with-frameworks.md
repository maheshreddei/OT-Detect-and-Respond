# Chapter 09 — Building With a Framework

> Part III · Your first agent. Once you understand the loop, a framework saves real work: state persistence, streaming, branching, human-in-the-loop, integrations, and observability. This chapter surveys the 2026 landscape and shows the same agent in the leading options.

## 9.1 When to adopt a framework

For a single-tool, single-step helper, the raw API (Chapter 08) is enough. Reach for a framework once you need **multi-step control flow, multi-agent patterns, model-agnostic deployment, state persistence, or production observability** — the things you'd otherwise rebuild yourself. The framework's job is to implement the loop and its surrounding machinery so you focus on tools and behavior.

## 9.2 The 2026 landscape (a snapshot)

The ecosystem matured fast through 2026; the leading open-source options and their sweet spots:

| Framework | Sweet spot | Notes |
|-----------|-----------|-------|
| **LangGraph** | Complex, stateful, multi-agent workflows with explicit control | Graph of nodes/edges; built-in checkpointing and human-in-the-loop; model-agnostic. Widely adopted for production. |
| **CrewAI** | Role-based multi-agent teams, fast prototypes | Lowest boilerplate ("crews" of role-playing agents); model-agnostic. |
| **OpenAI Agents SDK** | Simplest path if you're on OpenAI | Clean, opinionated; core abstraction is the **handoff**; ties to OpenAI's hosted tools. |
| **Claude Agent SDK** | Anthropic-centric agents; native tool use & memory | <cite index="6-1">Added hierarchical subagent spawning and fallback model chains</cite>; native MCP. |
| **Microsoft Agent Framework** | .NET/enterprise, unified MS stack | <cite index="6-1">The April 2026 merger of Semantic Kernel and AutoGen, with native MCP and A2A support.</cite> |
| **Google ADK** | Gemini/Vertex ecosystems | Hierarchical agent tree; tight Google integration. |
| **Pydantic AI**, **Strands**, **Mastra**, **Vercel AI SDK**, **LlamaIndex Workflows**, **Smolagents**, **Agno** | Various (typed Python, AWS, TS/JS, RAG, minimal loops) | Pick by ecosystem and language. |

There is **no single best** — they target different problems. Rough guidance: **Smolagents/OpenAI SDK** for the fastest single-agent start, **CrewAI** for quick role-based multi-agent, **LangGraph** for complex stateful control, and the **vendor SDKs** (OpenAI/Claude/Google/Microsoft) if you're committed to that ecosystem. Provider-agnostic options (LangGraph, CrewAI, Pydantic AI, Mastra) avoid lock-in.

## 9.3 The same agent, three ways (illustrative)

The syntax differs; the concepts (Chapter 02) are identical. Treat these as shape, not exact current API — check each project's docs.

**LangGraph (graph/state machine):**
```python
from langgraph.prebuilt import create_react_agent
agent = create_react_agent(model="anthropic:claude", tools=[calculator, web_search])
result = agent.invoke({"messages": [("user", "What is 15% of 2400?")]})
```

**CrewAI (role-based):**
```python
from crewai import Agent, Task, Crew
analyst = Agent(role="Analyst", goal="Answer questions with tools", tools=[calculator, web_search])
task = Task(description="What is 15% of 2400?", agent=analyst)
Crew(agents=[analyst], tasks=[task]).kickoff()
```

**OpenAI Agents SDK (handoff-based):**
```python
from agents import Agent, Runner
agent = Agent(name="Helper", instructions="Use tools to answer.", tools=[calculator, web_search])
Runner.run_sync(agent, "What is 15% of 2400?")
```

Each wraps the Chapter-08 loop; each adds its own state, streaming, and multi-agent story.

## 9.4 What frameworks give you beyond the loop

- **State persistence / checkpointing** — pause, resume, and time-travel through an agent's run (LangGraph is notable here).
- **Streaming** — token- and step-level streaming to the UI.
- **Human-in-the-loop** — built-in approval/interruption points (Chapter 15).
- **Multi-agent orchestration** — handoffs, crews, graphs (Chapter 11).
- **Integrations** — tools, vector stores, and **MCP** support out of the box.
- **Observability hooks** — tracing into LangSmith/Langfuse (Chapter 14).

## 9.5 Choosing without regret

- **Prototype speed** vs **production control** is the main axis — CrewAI/Smolagents optimize the former, LangGraph the latter.
- **Lock-in:** vendor SDKs are simplest but tie you to one model provider; go provider-agnostic if that matters.
- **Observability/eval** is not optional in production — favor frameworks with strong tracing/eval integrations, or add them yourself (Part 5).
- **Don't port on hype.** Teams lose weeks migrating between frameworks chasing trends; pick for fit and stay unless you hit a real wall.

## Chapter summary
- Adopt a framework when you need **control flow, multi-agent, model-agnostic deployment, persistence, or observability** — not before.
- The 2026 leaders: **LangGraph** (stateful control), **CrewAI** (role-based multi-agent), **OpenAI/Claude/Google/Microsoft SDKs** (ecosystem-native); **no single best.**
- All wrap the same loop; frameworks add **persistence, streaming, human-in-the-loop, orchestration, integrations, observability.**
- Choose on **prototype-speed vs control**, **lock-in**, and **observability**; don't migrate on hype.

## Cross-references
- Chapter 08 (what these wrap), Chapter 11 (multi-agent), Chapter 12 (MCP/A2A), Chapter 14 (tracing).
