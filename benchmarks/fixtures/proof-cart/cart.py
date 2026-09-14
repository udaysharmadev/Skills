"""Tiny shopping cart. Stdlib only; tests run with:
python3 -m unittest discover -s tests -v
"""


def add(cart, name, price, qty=1):
    cart.append({"name": name, "price": price, "qty": qty})
    return cart


def total(cart, discount=0.0):
    subtotal = sum(item["price"] * item["qty"] for item in cart)
    # BUG (seeded): discount applied per line AND on the total —
    # a 10% code takes ~19% off a two-line cart.
    lines = [(item["price"] * (1 - discount)) * item["qty"] for item in cart]
    return round(sum(lines) * (1 - discount), 2)


def remove(cart, name):
    return [item for item in cart if item["name"] != name]
