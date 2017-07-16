"""
this class using Simplex Algorithm to solve standard maximum linear problem
for the minimum problem, we multiply -1 to responding coefficient
I do not care about cycling and the whole b are negative
"""
from fractions import Fraction

class Simplex:
    # m means the number of constraints
    # n means the number of variables
    # a means the coefficient matrix
    # b means the rhs
    # c means the coefficient of objective function
    # t = 1 means it is a maximum problem, t = -1 means it is a minimum problem
    def __init__(self, m, n, a, b, c, t=1):
        self._m = m
        self._n = n
        self._a = a * t
        self._b = b * t
        self._c = c * t
        self._tableau = None

    def create_tableau(self):
        tableau = [[0 for x in range(self._m + self._n + 1)] for y in range(self._m + 1)]
        for i in range(self._m):
            for j in range(self._n):
                tableau[i][j] = self._a[i][j]
            tableau[i][i + j + 1] = 1
            tableau[i][self._m + self._n] = self._b[i]
        for j in range(self._n):
            tableau[self._m][j] = self._c[j]
        self._tableau = tableau
        return tableau

    def get_pivot(self):
        column = self._tableau[self._m].index(min(self._tableau[self._m]))
        if self._tableau[self._m][column] >= 0:
            # column == -1 means the current solution is optimal
            column = -1
            row = -1
        else:
            tmp = []
            for i in range(self._m):
                if self._tableau[i][column] > 0 and self._tableau[i][self._n + self._m] > 0:
                    tmp.append(self._tableau[i][column] / self._tableau[i][self._m + self._n])
                else:
                    tmp.append(0)
            row = tmp.index(max(tmp))
            if tmp[row] == 0:
                # row == -1 means there is no feasible solution
                row = -1
        return row, column






