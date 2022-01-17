import unittest
from queens import queens
import types


class TestQueensGenerator(unittest.TestCase):

    def test_generator(self):
        print(type(queens(4)))
        self.assertTrue(
            isinstance(queens(4), types.GeneratorType)
            or
            isinstance(queens(4), filter)
        )


if __name__ == '__main__':
    unittest.main()
