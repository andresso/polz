import unittest

from lempel_ziv_complexity import lempel_ziv_decomposition, lempel_ziv_complexity

from polz import POLZ
from polz_utils import Util


class POLZTests(unittest.TestCase):
    def setUp(self):
        self.polz = POLZ()
        self.util = Util()

    def test_decomposition_1(self):
        adj = [
            ["n", "s"],
            ["e", "w"],
        ]
        seq = "nnssenw"  # n, ns, s, e, nw
        complexity, encoded_dict = self.polz.encode(seq, adj)

        self.assertEqual(complexity, 5)
        self.assertEqual(encoded_dict, [(0, "n"), (1, "s"), (0, "s"), (0, "e"), (1, "w")])

    def test_decomposition_2(self):
        adj = [
            ["n", "s"],
            ["e", "w"],
        ]
        seq = "nnnnnn"  # n, nn, nnn
        complexity, encoded_dict = self.polz.encode(seq, adj)

        self.assertEqual(complexity, 3)
        self.assertEqual([(0, 'n'), (1, 'n'), (2, 'n')], encoded_dict)

    def test_decomposition_3(self):
        adj = [
            ["a", "c"],
            ["b", "c"],
        ]
        seq = "abaacbaabc"  # a, b, aa, c, ba, abc
        complexity, encoded_dict = self.polz.encode(seq, adj)

        self.assertEqual(complexity, 6)
        self.assertEqual([(0, "a"), (0, "b"), (1, "a"), (0, "c"), (2, "a"), (5, "c")], encoded_dict)

    def test_decomposition_4(self):
        # Complete non-commutative graph
        adj = [
            ["a", "b"],
            ["a", "c"],
            ["b", "c"],
        ]
        seq = "abaacbaabc"  # a, b, aa, c, ba, ab, c
        complexity, encoded_dict = self.polz.encode(seq, adj)

        self.assertEqual(complexity, 6)
        self.assertEqual(encoded_dict, [(0, "a"), (0, "b"), (1, "a"), (0, "c"), (2, "a"), (1, "b")])

    def test_decomposition_lz78(self):
        # Complete non-commutative graph
        adj = [
            ["a", "b"],
            ["a", "c"],
            ["b", "c"]
        ]

        seq = "abaacbaabc"  # a, b, aa, c, ba, ab, c
        complexity, encoded_dict = self.polz.encode(seq, adj)
        seq_eq, decoding_list = self.polz.decode(encoded_dict)

        self.assertEqual(lempel_ziv_complexity(seq), complexity)
        self.assertEqual(lempel_ziv_decomposition(seq), decoding_list)

    def test_decode_1(self):
        # Complete non-commutative graph
        adj = [
            ["a", "b"],
            ["a", "c"],
            ["b", "c"]
        ]

        seq = "abaacbaab"  # a, b, aa, c, ba, ab
        complexity, encoded_dict = self.polz.encode(seq, adj)

        seq_eq, l = self.polz.decode(encoded_dict)
        self.assertEqual(seq, seq_eq)

    def test_decode_2(self):
        # Complete non-commutative graph
        adj = [
            ["a", "c"],
            ["b", "c"]
        ]

        seq = "abaacbaabc"  # a, b, aa, c, ba, abc
        complexity, encoded_dict = self.polz.encode(seq, adj)

        seq_eq, l = self.polz.decode(encoded_dict)
        is_congruent = self.util.is_congruent(seq, seq_eq, adj)
        self.assertEqual(True, is_congruent)
