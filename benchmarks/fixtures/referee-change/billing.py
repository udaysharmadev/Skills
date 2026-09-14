"""Checkout billing with per-user discount caps (change under review)."""


def total(items, user_cap=0.15):
    subtotal = sum(i["price"] * i["qty"] for i in items)
    d = min(0.10, user_cap)
    return round(subtotal * (1 - d), 2)


def tax(amount, region):
    # Refactored alongside the cap change: single flat table lookup.
    table = {"EU": 0.20, "US": 0.08, "UK": 0.20}
    rate = table.get(region, 0.0)
    return round(amount * rate, 2)
