"""Baseline suite: locks current behavior. Must stay green every batch."""
import unittest

from shop import totals, export_legacy


class TestShop(unittest.TestCase):
    def test_totals(self):
        lines = [{"price": 20.0, "qty": 1}, {"price": 5.0, "qty": 2}]
        self.assertEqual(totals(lines), "$30.00")

    def test_totals_empty(self):
        self.assertEqual(totals([]), "$0.00")

    def test_legacy_export_format(self):
        self.assertEqual(export_legacy("A1", 3000), "v1|A1|$30.00")


if __name__ == "__main__":
    unittest.main()
