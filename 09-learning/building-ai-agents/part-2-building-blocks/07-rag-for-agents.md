# Chapter 07 — RAG for Agents

> Part II · Building blocks. Retrieval-Augmented Generation gives an agent access to knowledge it wasn't trained on — your documents, your data — by retrieving relevant pieces and putting them in context. For agents, RAG is best understood as **retrieval offered as a tool.**

## 7.1 Why RAG

An LLM only knows what it was trained on, up to a cutoff, and nothing about *your* private data. RAG bridges that gap without retraining: at query time, **find the relevant information and give it to the model in context.** It's how agents answer questions over company docs, code bases, product catalogs, or any corpus you control — grounded in real sources rather than the model's memory (which reduces hallucination).

## 7.2 The RAG pipeline

```
  INDEXING (offline)                      RETRIEVAL (at query time)
  documents → chunk → embed → store        query → embed → search → top-k chunks
                                                            │
                                                            ▼
                                        model answers using the retrieved chunks
```

**Indexing (build once, update as data changes):**
1. **Load** your documents.
2. **Chunk** them into passages (size matters — too big dilutes relevance, too small loses context).
3. **Embed** each chunk into a vector.
4. **Store** vectors + text in a vector database.

**Retrieval (every query):**
1. **Embed** the query.
2. **Search** for the most similar chunks (semantic search).
3. **Assemble** the top-k chunks into the context.
4. **Generate** an answer grounded in them, ideally with citations.

## 7.3 RAG as a tool for the agent

In a plain RAG app, retrieval happens once before generation. In an **agentic** RAG setup, retrieval is a **tool the agent chooses to call** — which is more powerful:

- The agent decides **whether** it needs to retrieve (skip it for questions it can answer directly).
- It can **reformulate** the query, retrieve **multiple times**, and **refine** based on what it finds.
- It can combine retrieval with other tools (search the docs, then call an API).

```python
def search_docs(query: str) -> list[dict]:
    """Search the company knowledge base. Use when the user asks about
    internal policies, products, or documentation."""
    hits = vector_store.search(embed(query), k=5)
    return [{"text": h.text, "source": h.source} for h in hits]
# register search_docs as a tool; the agent calls it when it decides it needs to.
```

This turns RAG from a fixed pre-step into a **capability the agent wields judiciously** — the agentic version of "look it up."

## 7.4 Making retrieval good

Retrieval quality caps answer quality — garbage retrieved, garbage answered. Levers that matter:

- **Chunking** — respect document structure (sections, paragraphs); avoid splitting mid-idea; consider overlap.
- **Embedding model** — better embeddings → better semantic matches; match the model to your domain/language.
- **Hybrid search** — combine semantic (vector) with keyword (BM25) search; keywords catch exact terms (names, codes) that embeddings miss.
- **Re-ranking** — retrieve a broad set, then re-rank with a stronger model to put the best chunks first.
- **Metadata filtering** — filter by source, date, or type before/after semantic search to scope results.

## 7.5 Grounding and citations

A major benefit of RAG is **traceability**: because the answer is built from retrieved chunks, you can **cite sources**. Design the agent to attribute claims to the chunks it used, and to say "I don't know" when retrieval returns nothing relevant rather than hallucinating. Grounded, cited answers are both more trustworthy and more debuggable.

## 7.6 When RAG isn't the answer

RAG isn't always right. If the data is small enough, just put it in the prompt. If the task needs *fresh* data, a live API tool beats a stale index. If it needs *computation over structured data*, a database query tool beats semantic search. Choose retrieval for **large, unstructured, semi-static knowledge**; choose other tools for small, fresh, or structured needs.

## Chapter summary
- **RAG** grounds the agent in your data by **retrieving relevant chunks into context** at query time — no retraining, less hallucination.
- Pipeline: **chunk → embed → store** (offline), then **embed query → search → assemble → generate** (per query).
- In agents, expose retrieval as a **tool** the agent calls judiciously (agentic RAG) — whether to retrieve, reformulate, and re-retrieve.
- Retrieval quality is the ceiling: tune **chunking, embeddings, hybrid search, re-ranking, metadata**; ground answers with **citations.**
- Use RAG for large unstructured knowledge; prefer live APIs or DB queries for fresh or structured data.

## Cross-references
- Chapter 06 (memory) uses the same vector-store machinery; Chapter 05 (tools) — retrieval is a tool.
- Code: [`../code/rag_agent.py`](../code/rag_agent.py).
