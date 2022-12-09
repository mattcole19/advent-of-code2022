import unittest
from day8 import *


grid = [
    [3, 0, 3, 7, 3],
    [2, 5, 5, 1, 2],
    [6, 5, 3, 3, 2],
    [3, 3, 5, 4, 9],
    [3, 5, 3, 9, 0],
]

class TestDay8(unittest.TestCase):

    def test_above(self):
        actual = above(grid, (2, 2))
        expected = [5, 3]
        self.assertEqual(actual, expected)

    def test_right(self):
        actual = right(grid, (2, 2))
        expected = [3, 2]
        self.assertEqual(actual, expected)

    def test_down(self):
        actual = down(grid, (2,2))
        expected = [5, 3]
        self.assertEqual(actual, expected)

    def test_left(self):
        actual = left(grid, (2,2))
        expected = [5, 6]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()

