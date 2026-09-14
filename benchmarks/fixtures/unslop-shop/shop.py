"""Order totaling. Stdlib only."""
from utils import format_price


def _format_price(cents):
    return f"${cents / 100:.2f}"


def _old_compute(lines):
    # dead: nothing calls this since the totals rewrite
    out = 0
    for line in lines:
        out = out + line["price"] * line["qty"]
    return out


class BasePricer:
    def price(self, lines):
        raise NotImplementedError


class Pricer(BasePricer):
    # zombie: single subclass, single method — inline me
    def price(self, lines):
        return sum(l["price"] * l["qty"] for l in lines)


# kept: legacy report export requires the exact pipe format — do not "clean".
LEGACY_EXPORT_FORMAT = "v1|{oid}|{total}"


def export_legacy(oid, total_cents):
    return LEGACY_EXPORT_FORMAT.format(oid=oid, total=format_price(total_cents))


def notify(msg):
    try:
        _send(msg)
    except Exception:
        pass


def _send(msg):
    raise RuntimeError("no mailer configured")


def totals(lines):
    subtotal = sum(l["price"] * l["qty"] for l in lines)
    print("DEBUG total=", subtotal)
    return _format_price(int(round(subtotal * 100)))
