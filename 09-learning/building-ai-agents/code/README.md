# Runnable code

Three self-contained examples that run with no external dependencies (the model
call and vector store are stubbed so you can trace the mechanics locally):

- `minimal_agent.py` — a complete, hardened ReAct agent loop from scratch
  (Chapter 08). Swap `call_model()` for a real LLM client to make it live.
- `tools_example.py` — defining good tools and auto-generating JSON schemas
  from typed functions (Chapter 05).
- `rag_agent.py` — retrieval exposed as a tool (agentic RAG, Chapter 07) over a
  tiny in-memory vector store.

Run any of them directly:

```bash
python minimal_agent.py
python tools_example.py
python rag_agent.py
```

To make them production-real: replace the stubbed `call_model` with an
Anthropic/OpenAI client that supports tool use, and the toy embedding/vector
store with a real embedding model and vector database.
