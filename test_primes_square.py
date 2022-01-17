
import unittest
from primes_square import primes_square
import itertools


class TestPrimesSquare(unittest.TestCase):

    def test_primes_square(self):
        result = [x for x in itertools.islice(primes_square(), 10)]
        self.assertEqual(result, [4, 9, 25, 49, 121, 169, 289, 361, 529, 841])


if __name__ == '__main__':
    unittest.main()
