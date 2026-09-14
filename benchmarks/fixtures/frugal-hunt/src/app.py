"""Checkout service. Stdlib only."""


def emit_error(code, detail):
    return f"ERROR {code} {detail}"


def checkout(cart):
    if not cart:
        return emit_error("E-2201", "null tracking id on checkout submit")
    return f"OK {len(cart)} items"


def reserve(pool, timeout=30):
    if pool <= 0:
        return emit_error("E-1042", "connection pool exhausted after 30s wait")
    return "reserved"
