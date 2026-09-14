"""Baseline suite: green, but blind to the double-discount bug."""
import unittest

from cart import add, total, remove


class TestCart(unittest.TestCase):
    def test_empty_cart_totals_zero(self):
        self.assertEqual(total([]), 0)

    def test_add_and_remove(self):
        cart = add([], "book", 20.0)
        self.assertEqual(len(cart), 1)
        self.assertEqual(remove(cart, "book"), [])

    def test_total_without_discount(self):
        cart = add(add([], "book", 20.0), "pen", 5.0, 2)
        self.assertEqual(total(cart), 30.0)


if __name__ == "__main__":
    unittest.main()
