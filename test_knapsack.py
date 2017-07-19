from unittest import TestCase
from unittest import main
from knapsack import *


class TestSimplex(TestCase):
    def test_value(self):
        w = [3, 8, 5]
        v = [4, 6, 5]
        capacity = 8
        self.assertEqual(knapsack(w, v, capacity)[0], 9)

    def test_decision(self):
        w = [3, 8, 5]
        v = [4, 6, 5]
        capacity = 8
        self.assertEqual(knapsack(w, v, capacity)[1], [1, 0, 1])

    def test_1(self):
        v = [10, 40, 30, 50]
        w = [5, 4, 6, 3]
        capacity = 10
        self.assertEqual(knapsack(w, v, capacity)[0], 150)
        self.assertEqual(knapsack(w, v, capacity)[1], [0, 0, 0, 3])


if __name__ == '__main__':
    main()