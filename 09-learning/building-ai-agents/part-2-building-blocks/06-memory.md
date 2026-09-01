# Chapter 06 — Memory

> Part II · Building blocks. Memory is what lets an agent make progress across many steps and remember across sessions. Managing it well — especially the finite context window — is one of the central engineering challenges of agents.

## 6.1 The three horizons of memory

- **Working memory (the context window).** Everything currently visible to the model: system prompt, task, and the running transcript of thoughts, actions, and observations. It's fast and rich but **finite** — the hard limit of the model's context.
- **Task / session memory.** State for the current task that may outgrow the window — earlier steps, retrieved documents, intermediate results — kept externally and summarized or re-injected as needed.
- **Long-term memory.** Knowledge that persists across sessions: user preferences, past conversations, learned facts. Stored in a database (often a vector store) and retrieved when relevant.

The art is deciding **what to keep in the window, what to externalize, and what to retrieve** — because the window is both your most valuable and most constrained resource.

## 6.2 The context window is a budget

Every token in the window costs money and latency, and models degrade when the window is bloated with irrelevant content ("context rot"). Treat the window as a **budget to curate**, not a bucket to fill:

- Keep the **system prompt, task, and recent/relevant steps.**
- **Summarize** older turns rather than carrying them verbatim.
- **Externalize** large artifacts (documents, big tool outputs) and re-inject only what's needed.
- **Retrieve** long-term facts on demand rather than stuffing everything in up front.

## 6.3 Managing a growing transcript

As an agent runs, its transcript grows past the window. Common strategies:

- **Sliding window** — keep the last N turns; drop the oldest. Simple; risks forgetting early context.
- **Summarization** — periodically compress older turns into a running summary that stays in context. Preserves gist at some fidelity cost.
- **Scratchpad / external state** — write key facts and progress to an external store the agent reads/writes via tools, keeping the window lean.
- **Hierarchical** — combine: a short running summary + the last few turns + retrieval of specifics on demand.

Choose based on task length: short tasks need none of this; long-running agents need summarization and/or external state.

## 6.4 Long-term memory and vector stores

For memory across sessions, the standard tool is a **vector store**. The idea:

1. **Embed** each memory (a fact, a past message, a preference) into a numeric vector that captures meaning.
2. **Store** vectors in a vector database (e.g. a hosted vector DB or an embedded one).
3. At runtime, **embed the current query**, find the most **semantically similar** stored memories, and inject them into the context.

This is *semantic* recall — you retrieve by meaning, not exact match. The same machinery powers RAG (Chapter 07); memory is essentially RAG over the agent's own history and knowledge.

```python
# Conceptual: store and recall a memory
store.add(embed("User prefers metric units and terse answers"))
relevant = store.search(embed(current_user_message), k=3)   # semantic recall
context += format(relevant)
```

## 6.5 Types of long-term memory

It helps to distinguish (borrowing from cognitive science):

- **Semantic** — facts about the user/world ("the user's company is X").
- **Episodic** — specific past events/interactions ("last week the user asked about Y").
- **Procedural** — how to do things / learned strategies (sometimes stored as updated instructions).

Most agents start with simple semantic memory (key facts and preferences) and add episodic recall as needed. Don't over-engineer memory before you have a task that needs it.

## 6.6 Practical guidance

- Start with **just the context window** — many agents need nothing more.
- Add **summarization** when transcripts overflow.
- Add a **vector store** when you need cross-session recall.
- **Write memory deliberately** — decide what's worth remembering (not everything), and retrieve **selectively** (relevance beats volume).
- Watch for **stale or wrong memories** — bad long-term memory quietly poisons behavior; make it inspectable and correctable.

## Chapter summary
- Memory has three horizons: **working (context window), task/session, and long-term.**
- The **context window is a finite budget** — curate it (keep relevant, summarize old, externalize large, retrieve on demand).
- Manage growing transcripts with **sliding window, summarization, external scratchpad, or hierarchical** strategies.
- **Long-term memory** uses a **vector store** for semantic recall (semantic/episodic/procedural types).
- Start minimal; add summarization and vector memory only when the task demands it.

## Cross-references
- Chapter 07 (RAG) uses the same retrieval machinery for knowledge; Chapter 02 introduced the three horizons.
