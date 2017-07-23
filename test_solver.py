from unittest import TestCase
from unittest import main
from Solver import solver


class TestSolver(TestCase):
    def test_1(self):
        a = [[1, -1, -2, -1],
             [2, 0, 1, -4],
             [-2, 1, 0, 1]]
        b = [4, 2, 1]
        c = [1, -2, -3, -1]
        t = 1
        exception = [7, 0, 0, 3]
        optimal = 4
        s = solver(a, b, c, t)
        dual_exception = [1, 0, 0]
        self.assertEqual(exception, s[0])
        self.assertEqual(optimal, s[1])
        self.assertEqual(dual_exception, s[2])

    def test_2(self):
        a = [[2, -1, 1],
             [1, 0, 2],
             [-7, 4, -6]]
        b = [-1, 2, 1]
        c = [3, -1, 2]
        t = -1
        exception = [0, 2, 1]
        optimal = 0
        s = solver(a, b, c, t)
        dual_exception = [1, 0.5, 0]
        self.assertEqual(exception, s[0])
        self.assertEqual(optimal, s[1])
        self.assertEqual(dual_exception, s[2])

    def test_3(self):
        a = [[-3, 3, 1],
             [2, -1, -2],
             [-1, 0, 1]]
        c = [-1, -1, 2]
        b = [3, 1, 1]
        t = 1
        s = solver(a, b, c, t)
        self.assertEqual('unbounded', s)

    def test_4(self):
        a = [[-2, 0, 3],
             [2, -1, 1],
             [3, 2, -1]]
        b = [-1, 1, 0]
        c = [5, -2, -1]
        t = -1
        s = solver(a, b, c, t)
        self.assertEqual('infeasible' in s, True)

    def test_5(self):
        a = [[-1, -2, 0],
             [4, 1, 7],
             [2, -3, 1]]
        b = [-3, -1, -5]
        c = [0, -2, 1]
        t = -1
        exception = [0, 1.5, 0]
        s = solver(a, b, c, t)
        dual_exception = [1, 0, 0]
        self.assertEqual(exception, s[0])
        self.assertEqual(dual_exception, s[2])

    def test_6(self):
        a = [[1, 2, 2],
             [-3, 0, 1],
             [-2, -1, 0]]
        b = [1, -1, -1]
        c = [3, 4, 5]
        t = 1
        exception = [1, 0, 0]
        s = solver(a, b, c, t)
        dual_exception = [3, 0, 0]
        self.assertEqual(exception, s[0])
        self.assertEqual(dual_exception, s[2])


if __name__ == '__main__':
    main()
