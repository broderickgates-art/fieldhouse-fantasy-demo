import unittest
from fantasy import ppr_points, rank_players, recommend_starter


class FantasyTests(unittest.TestCase):
    def test_ppr_example(self):
        self.assertEqual(ppr_points(7, 85, 2), 27.5)

    def test_ppr_zeros(self):
        self.assertEqual(ppr_points(0, 0, 0), 0)

    def test_invalid_stats(self):
        with self.assertRaises(ValueError):
            ppr_points(-1, 80, 1)

    def test_ranking_and_unchanged_input(self):
        original = [{"name": "B", "projection": 12}, {"name": "A", "projection": 19}]
        result = rank_players(original)
        self.assertEqual([p["name"] for p in result], ["A", "B"])
        self.assertEqual(original[0]["name"], "B")

    def test_starter_and_tie(self):
        self.assertEqual(recommend_starter("A", 19, "B", 22), "B")
        self.assertEqual(recommend_starter("A", 20, "B", 20), "TIE")


if __name__ == "__main__":
    unittest.main()
