from unittest import TestCase
from unittest import main
from Simplex import Simplex
from fractions import Fraction


class TestSimplex(TestCase):

    def test_tableau(self):
        with open('text', 'r', encoding='utf-8') as f:
            m = int(f.readline().split()[0])
            n = int(f.readline().split()[0])
            a = [[0 for x in range(n)] for y in range(m)]
            for i in range(m):
                tmp = f.readline().split()
                for j in range(n):
                    a[i][j] = Fraction(tmp[j])
            b = []
            for i in range(m):
                b.append(Fraction(f.readline().split()[0]))
            c = []
            for j in range(n):
                c.append(Fraction(f.readline().split()[0]))
        s = Simplex(m, n, a, b, c)
        result = [[2, 3, 1, 0, 0, 0, 6], [-3, 2, 0, 1, 0, 0, 3], [0, 2, 0, 0, 1, 0, 5],
                  [2, 1, 0, 0, 0, 1, 4], [-4, -3, 0, 0, 0, 0, 0]]
        self.assertEqual(s.create_tableau(), result)

    def test_get_pivot(self):
        with open('text', 'r', encoding='utf-8') as f:
            m = int(f.readline().split()[0])
            n = int(f.readline().split()[0])
            a = [[0 for x in range(n)] for y in range(m)]
            for i in range(m):
                tmp = f.readline().split()
                for j in range(n):
                    a[i][j] = Fraction(tmp[j])
            b = []
            for i in range(m):
                b.append(Fraction(f.readline().split()[0]))
            c = []
            for j in range(n):
                c.append(Fraction(f.readline().split()[0]))
        s = Simplex(m, n, a, b, c)
        tableau = s.create_tableau()
        result = (3, 0)
        self.assertEqual(s.get_pivot(tableau), result)

    def test_pivot(self):
        with open('text', 'r', encoding='utf-8') as f:
            m = int(f.readline().split()[0])
            n = int(f.readline().split()[0])
            a = [[0 for x in range(n)] for y in range(m)]
            for i in range(m):
                tmp = f.readline().split()
                for j in range(n):
                    a[i][j] = Fraction(tmp[j])
            b = []
            for i in range(m):
                b.append(Fraction(f.readline().split()[0]))
            c = []
            for j in range(n):
                c.append(Fraction(f.readline().split()[0]))
        s = Simplex(m, n, a, b, c)
        tableau = s.create_tableau()
        row, column = s.get_pivot(tableau)
        result = [[0, 2, 1, 0, 0, -1, 2], [0, Fraction(7, 2), 0, 1, 0, Fraction(3, 2), 9],
                  [0, 2, 0, 0, 1, 0, 5], [1, Fraction(1, 2), 0, 0, 0, Fraction(1, 2), 2], [0, -1, 0, 0, 0, 2, 8]]
        self.assertEqual(s.pivot(tableau, row, column), result)

    def test_simplex(self):
        with open('text', 'r', encoding='utf-8') as f:
            m = int(f.readline().split()[0])
            n = int(f.readline().split()[0])
            a = [[0 for x in range(n)] for y in range(m)]
            for i in range(m):
                tmp = f.readline().split()
                for j in range(n):
                    a[i][j] = Fraction(tmp[j])
            b = []
            for i in range(m):
                b.append(Fraction(f.readline().split()[0]))
            c = []
            for j in range(n):
                c.append(Fraction(f.readline().split()[0]))
        s = Simplex(m, n, a, b, c)
        res = s.simplex()
        exception = [Fraction(3, 2), 1]
        self.assertEqual(res, exception)
if __name__ == '__main__':
    main()