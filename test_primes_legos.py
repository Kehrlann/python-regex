
import unittest
from primes_legos import primes_legos
import itertools


class TestPrimesLegos(unittest.TestCase):

    def test_primes_legos_simple(self):
        result = list(itertools.islice(primes_legos(), 10))
        self.assertEqual(result, [(1, 4), (1, 9), (1, 25),
                                  (1, 49), (1, 121), (2, 169),
                                  (3, 289), (5, 361),
                                  (7, 529), (11, 841)])

    def test_primes_legos_start_stop_step(self):
        result = list(itertools.islice(primes_legos(), 50, 100, 10))
        self.assertEqual(result, [(199, 54289), (263, 80089),
                                  (317, 124609),
                                  (383, 175561),
                                  (443, 218089)])


if __name__ == '__main__':
    unittest.main()
