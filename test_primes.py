import unittest
from primes import primes
import itertools


class TestPrimes(unittest.TestCase):

    def test_primes(self):
        cases = [
            ((20,),  [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                      31, 37, 41, 43, 47, 53, 59, 61, 67, 71]),
            ((1, 6, 2), [3, 7, 13]),
            ((10, 20, 2), [31, 41, 47, 59, 67]),
            ((98, 101), [523, 541, 547]),
        ]
        for args, expected in cases:
            result = [x for x in itertools.islice(primes(), *args)]
            self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
