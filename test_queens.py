import unittest
from queens import queens
from functools import reduce


class TestQueens(unittest.TestCase):

    @classmethod
    def _size(_, gen):
        return reduce(lambda current, _: current + 1, gen, 0)

    def test_size(self):
        self.assertEqual(0, TestQueens._size([]))
        self.assertEqual(5, TestQueens._size(range(5)))

    def test_queens_no_solution(self):
        self.assertEqual(0, TestQueens._size(queens(2)))
        self.assertEqual(0, TestQueens._size(queens(3)))

    def test_queens_four(self):
        self.assertEqual(
            set(
                (
                    (1, 3, 0, 2),
                    (2, 0, 3, 1)
                )
            ),
            set([tuple(x) for x in queens(4)])
        )

    def test_queens_many(self):
        n_size = [
            (5, 10),
            (6, 4),
            (7, 40),
            (8, 92),
            (9, 352),
            (10, 724)
        ]

        for n, size in n_size:
            self.assertEqual(size, TestQueens._size(queens(n)))


if __name__ == '__main__':
    unittest.main()
