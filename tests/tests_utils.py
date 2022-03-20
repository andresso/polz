import unittest

from polz_utils import Util


class POLZTests(unittest.TestCase):
    def setUp(self):
        self.util = Util()

    def test_projection_on_edge(self):
        word_1 = "abccabd"  # "acca"
        projections = self.util.word_projection_on_edge(word_1, "ac")
        self.assertEqual("acca", projections)

    def test_projections(self):
        # Non-commutative graph
        adj = [
            ["a", "c"],
            ["b", "c"],
            ["c", "d"],
        ]
        word_1 = "abccabd"  # ["acca", "bccb", "ccd"]
        projections = self.util.word_projections(word_1, adj)
        self.assertEqual(["acca", "bccb", "ccd"], projections)

    def test_is_congruent(self):
        adj = [
            ["a", "c"],
            ["b", "c"],
        ]
        word_1 = "abcaabc"  # ["acaac", "bcbc"]
        word_2 = "bacabac"  # ["acaac", "bcbc"]
        word_3 = "bacabca"  # ["acaca", "bcbc"]

        congruent_1 = self.util.is_congruent(word_1, word_2, adj)
        congruent_2 = self.util.is_congruent(word_1, word_3, adj)

        self.assertEqual(True, congruent_1)
        self.assertEqual(False, congruent_2)
