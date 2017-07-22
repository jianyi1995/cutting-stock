from unittest import TestCase
from unittest import main
from simplex.Simplex import *
import os


class TestSimplex(TestCase):
    print(os.getcwd())

    def test_tableau(self):
        t, m, n, a, b, c = read_model('./simplex/text')
        result = [[2, 3, 1, 0, 0, 0, 6], [-3, 2, 0, 1, 0, 0, 3], [0, 2, 0, 0, 1, 0, 5],
                  [2, 1, 0, 0, 0, 1, 4], [-4, -3, 0, 0, 0, 0, 0]]
        self.assertEqual(create_tableau(m, n, a, b, c), result)

    def test_get_pivot(self):
        t, m, n, a, b, c = read_model('./simplex/text')
        tableau = create_tableau(m, n, a, b, c)
        result = (3, 0)
        self.assertEqual(get_pivot(tableau, m, n), result)

    def test_pivot(self):
        t, m, n, a, b, c = read_model('./simplex/text')
        tableau = create_tableau(m, n, a, b, c)
        row, column = get_pivot(tableau, m, n)
        result = [[0, 2, 1, 0, 0, -1, 2], [0, Fraction(7, 2), 0, 1, 0, Fraction(3, 2), 9],
                  [0, 2, 0, 0, 1, 0, 5], [1, Fraction(1, 2), 0, 0, 0, Fraction(1, 2), 2], [0, -1, 0, 0, 0, 2, 8]]
        self.assertEqual(pivot(tableau, row, column, m, n), result)

    def test_simplex(self):
        t, m, n, a, b, c = read_model('./simplex/text')
        res = simplex(t, m, n, a, b, c)
        exception = [Fraction(3, 2), 1]
        self.assertEqual(res[0], exception)

    def test_simplex_min(self):
        t, m, n, a, b, c = read_model('./simplex/test_min')
        res = simplex(t, m, n, a, b, c)
        exception = [0, 2, 1]
        self.assertEqual(res[0], exception)

    def test_simplex_max(self):
        t, m, n, a, b, c = read_model('./simplex/test_max')
        res = simplex(t, m, n, a, b, c)
        exception = [7, 0, 0, 3]
        self.assertEqual(res[0], exception)

    def test_simplex_min_without_bless0(self):
        t, m, n, a, b, c = read_model('./simplex/test_min_without_b<0')
        res = simplex(t, m, n, a, b, c)
        exception = [0, Fraction(3, 2), 0]
        self.assertEqual(res[0], exception)

    def test_max_dual(self):
        t, m, n, a, b, c = read_model('./simplex/test_max')
        res = simplex(t, m, n, a, b, c)
        dual_res = solve_dual(res[0], m, n, a, b, c)
        exception = [1, 0, 0]
        self.assertEqual(dual_res, exception)

    def test_min_dual(self):
        t, m, n, a, b, c = read_model('./simplex/test_min')
        res = simplex(t, m, n, a, b, c)
        dual_res = solve_dual(res[0], m, n, a, b, c)
        exception = [1, Fraction(1, 2), 0]
        self.assertEqual(dual_res, exception)
        self.assertEqual(res[1], 0)

    def test_hard(self):
        t, m, n, a, b, c = read_model('./simplex/test_hard')
        res = simplex(t, m, n, a, b, c)
        exception = [1, 0, 0]
        dual_res = solve_dual(res[0], m, n, a, b, c)
        dual_exception = [3, 0, 0]
        self.assertEqual(res[0], exception)
        self.assertEqual(dual_res, dual_exception)
        self.assertEqual(res[1], 3)


if __name__ == '__main__':
    main()
