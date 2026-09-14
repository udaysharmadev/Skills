"""Release gate suite: 2 green, 1 red (version drift blocks release)."""
import unittest

import release
from release import total


class TestRelease(unittest.TestCase):
    def test_totals(self):
        self.assertEqual(
            total([{"price": 20.0, "qty": 1}, {"price": 5.0, "qty": 2}]), 30.0
        )

    def test_totals_empty(self):
        self.assertEqual(total([]), 0)

    def test_version_matches_docs(self):
        # docs/ announced 2.0.0; code still says 1.9.0 — drift blocks release
        self.assertEqual(release.__version__, "2.0.0")


if __name__ == "__main__":
    unittest.main()
