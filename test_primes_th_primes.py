
import unittest
from primes_th_primes import primes_th_primes
import itertools


class TestPrimesThPrimes(unittest.TestCase):

    def test_primes_th_primes_simple(self):
        result = list(itertools.islice(primes_th_primes(), 10))
        self.assertEqual(result, [5, 7, 13, 19, 37, 43, 61, 71, 89, 113])

    def test_primes_th_primes_start_stop_step(self):
        result = list(itertools.islice(primes_th_primes(), 1, 20, 2))
        self.assertEqual(result, [7, 19, 43, 71, 113, 163, 193, 251, 293, 359])


if __name__ == '__main__':
    unittest.main()
