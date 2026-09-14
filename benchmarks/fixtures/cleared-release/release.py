"""Release helper. Stdlib only. Current version: 1.9.0."""

__version__ = "1.9.0"


def total(items):
    return round(sum(i["price"] * i["qty"] for i in items), 2)
