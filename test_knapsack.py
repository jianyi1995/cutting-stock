from unittest import TestCase
from unittest import main
from knapsack import *


class TestSimplex(TestCase):
    def test_value(self):
        w = [3, 8, 5]
        v = [4, 6, 5]
        capacity = 8
        self.assertEqual(knapsack(w, v, capacity), 9)


if __name__ == '__main__':
    main()