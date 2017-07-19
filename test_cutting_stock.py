from unittest import TestCase
from unittest import main
from cutting_stock import *


class TestSimplex(TestCase):
    def test_initial(self):
        capacity = 20
        w = [9, 8, 7, 6]
        n = [511, 301, 263, 383]
        exception = [[2, 0, 0, 0],
                     [0, 2, 0, 0],
                     [0, 0, 2, 0],
                     [0, 0, 0, 3]]
        self.assertEqual(get_initial_solution(w, capacity), exception)


if __name__ == '__main__':
    main()