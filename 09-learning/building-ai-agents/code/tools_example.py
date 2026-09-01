"""
tools_example.py — defining good tools and auto-generating their schemas.

Shows the pattern most frameworks use: write a typed Python function with a
docstring, and derive the JSON schema the model sees from its signature.
"""
from __future__ import annotations
import inspect, typing

def tool_schema(fn) -> dict:
    """Build a JSON-schema tool definition from a typed function + docstring."""
    hints = typing.get_type_hints(fn)
    sig = inspect.signature(fn)
    props, required = {}, []
    type_map = {str: "string", int: "integer", float: "number", bool: "boolean"}
    for name, param in sig.parameters.items():
        if name == "return":
            continue
        props[name] = {"type": type_map.get(hints.get(name, str), "string")}
        if param.default is inspect.Parameter.empty:
            required.append(name)
    return {
        "name": fn.__name__,
        "description": (fn.__doc__ or "").strip(),
        "input_schema": {"type": "object", "properties": props, "required": required},
    }

# --- Example tools: focused, well-described, clean results, useful errors ---

def get_order_status(order_id: str) -> dict:
    """Look up the status of a customer order. Use when the user asks where
    their order is or about delivery. `order_id` looks like 'ORD-12345'."""
    orders = {"ORD-12345": {"status": "shipped", "eta": "2 days"}}
    if order_id not in orders:
        return {"error": f"no order found with id {order_id}"}   # error as data
    return {"order_id": order_id, **orders[order_id]}

def issue_refund(order_id: str, amount: float) -> dict:
    """Issue a refund for an order. WRITE/side-effecting tool — gate behind
    human approval in production (see Chapter 15)."""
    return {"order_id": order_id, "refunded": amount, "status": "ok"}

if __name__ == "__main__":
    import json
    for fn in (get_order_status, issue_refund):
        print(json.dumps(tool_schema(fn), indent=2))
