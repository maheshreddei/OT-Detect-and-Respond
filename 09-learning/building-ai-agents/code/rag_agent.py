"""
rag_agent.py — retrieval exposed as a TOOL the agent can choose to call
(agentic RAG). Uses a tiny in-memory vector store stub so it runs anywhere;
swap in a real embedding model + vector DB for production.
"""
from __future__ import annotations
from dataclasses import dataclass

# ---------- tiny stub embedding + store (replace with real ones) ----------
def embed(text: str) -> list[float]:
    # toy bag-of-words hash embedding — DO NOT use in production
    v = [0.0] * 16
    for w in text.lower().split():
        v[hash(w) % 16] += 1.0
    return v

def cosine(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    na = sum(x * x for x in a) ** 0.5 or 1.0
    nb = sum(y * y for y in b) ** 0.5 or 1.0
    return dot / (na * nb)

@dataclass
class Doc:
    text: str
    source: str
    vec: list[float]

class VectorStore:
    def __init__(self):
        self.docs: list[Doc] = []
    def add(self, text: str, source: str):
        self.docs.append(Doc(text, source, embed(text)))
    def search(self, query: str, k: int = 3) -> list[dict]:
        q = embed(query)
        ranked = sorted(self.docs, key=lambda d: cosine(q, d.vec), reverse=True)
        return [{"text": d.text, "source": d.source} for d in ranked[:k]]

# ---------- build the index (offline step) ----------
store = VectorStore()
store.add("Refunds are available within 30 days of purchase with a receipt.", "policy/refunds.md")
store.add("Standard shipping takes 3-5 business days.", "policy/shipping.md")
store.add("Premium members get free next-day shipping.", "policy/membership.md")

# ---------- retrieval as a tool ----------
def search_docs(query: str) -> list[dict]:
    """Search the company knowledge base. Use when the user asks about internal
    policies, products, or documentation. Returns text chunks with sources so
    you can cite them."""
    return store.search(query, k=3)

# The agent (Chapter 08 loop) would register `search_docs` as a tool and decide
# when to call it. Grounding rule for the system prompt: answer ONLY from
# retrieved chunks and cite sources; if nothing relevant is returned, say you
# don't know.

if __name__ == "__main__":
    for hit in search_docs("can I get my money back?"):
        print(f"- {hit['text']}  [{hit['source']}]")
