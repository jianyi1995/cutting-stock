"""
this class using Simplex Algorithm to solve standard maximum linear problem
for the minimum problem, we multiply -1 to responding coefficient
I do not care about cycling and the whole b are negative
"""
from fractions import Fraction
import numpy as np


# t means the type of problem, 1 means max, 0 means min
# m means the number of constraints
# n means the number of variables
# a means the coefficient matrix
# b means the rhs
# c means the coefficient of objective function
# t = 1 means it is a maximum problem, t = -1 means it is a minimum problem
def read_model(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        t = int(f.readline().split()[0])
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
    return t, m, n, a, b, c


def create_tableau(m, n, a, b, c):
    tableau = [[0 for x in range(m + n + 1)] for y in range(m + 1)]
    for i in range(m):
        for j in range(n):
            tableau[i][j] = a[i][j]
        tableau[i][i + j + 1] = 1
        tableau[i][m + n] = b[i]
    for j in range(n):
        tableau[m][j] = c[j]
    return tableau


def get_pivot(tableau, m, n):
    column = tableau[m].index(min(tableau[m][:m + n]))
    if tableau[m][column] >= 0:
        # column == -1 means the current solution is optimal
        column = -1
        row = -1
    else:
        tmp = []
        for i in range(m):
            if tableau[i][column] > 0:
                tmp.append(tableau[i][m + n] / tableau[i][column])
            else:
                tmp.append(10000000000000000)
        row = tmp.index(min(tmp))
        if tmp[row] == 10000000000000000:
            # row == -1 means there is no feasible solution
            row = -1
    return row, column


def pivot(tableau, row, column, m, n):
    tmp = tableau[row][column]
    for j in range(n + m + 1):
        tableau[row][j] = Fraction(tableau[row][j], tmp)
    for i in range(m + 1):
        if i == row:
            continue
        mul = Fraction(tableau[i][column])
        for j in range(m + n + 1):
            tableau[i][j] = tableau[i][j] - tableau[row][j] * mul
    return tableau


def min_to_max(m, n, a, b, c):
    for i in range(m):
        for j in range(n):
            a[i][j] *= -1
    for i in range(m):
        b[i] *= -1
    for j in range(n):
        c[j] *= -1


def solve(tableau, m, n, solution):
    while True:
        row, column = get_pivot(tableau, m, n)
        if column == -1 or row == -1:
            result = [0] * n
            for i in solution:
                if i < n:
                    result[i] = tableau[solution.index(i)][n + m]
            break
        else:
            solution[row] = column
            pivot(tableau, row, column, m, n)
    return result, row, column


def simplex(t, m, n, a, b, c):
    # if it is a min problem, do min_to_max
    if t == -1:
        min_to_max(m, n, a, b, c)
    if min(b) >= 0:
        solution = [n + i for i in range(m)]
        tableau = create_tableau(m, n, a, b, c)
        result, row, column = solve(tableau, m, n, solution)
        if column == -1:
            print('get the optimal solution\n')
            print('optimal is %d' % tableau[m][m + n])
            optimal = tableau[m][m + n]
        else:
            print('there is no feasible solution')
            print(result)
            print(solution)
            result = None
            optimal = None
    else:
        solution = [n + i + 1 for i in range(m)]
        pre_a = a.copy()
        for i in range(m):
            pre_a[i] = [-1] + pre_a[i]
        pre_c = [0] * (n + 1)
        pre_c[0] = 1
        tableau = create_tableau(m, n + 1, pre_a, b, pre_c)
        cur_min = tableau[0][m + n + 1]
        cur_index = 0
        for i in range(1, m):
            if tableau[i][m + n + 1] < cur_min:
                cur_min = tableau[i][m + n + 1]
                cur_index = i
        row = cur_index
        column = 0
        solution[row] = column
        pivot(tableau, row, column, m, n + 1)
        result, row, column = solve(tableau, m, n + 1, solution)
        # 考虑三种情况，一是x0在基础解中且不为0，
        # 二是x0在基础解中且为0
        # 三是x0不在基础解中
        if 0 in solution:
            if result[solution.index(0)] != 0:
                print('because of x0 is greater than 0, so no infeasible solution\n')
                return None
            else:
                row = solution.index(0)
                for i in range(1, n + 1):
                    if i not in solution and tableau[row][i] > 0:
                        column = i
                        pivot(tableau, row, column, m, n + 1)
                        solution[row] = column
                        break
        for i in range(m):
            solution[i] -= 1
        for i in range(m + 1):
            tableau[i].remove(tableau[i][0])
        tmp = [0] * (m + n + 1)
        pre_c = c + [0] * (m + 1)
        for i in range(m):
            if solution[i] < n:
                for j in range(m + n + 1):
                    tmp[j] += -1 * pre_c[solution[i]] * tableau[i][j]
        for j in range(m + n + 1):
            pre_c[j] += tmp[j]
            tableau[m][j] = pre_c[j]
        optimal = tableau[m][m + n]
        tableau[m][m + n] = 0
        result, row, column = solve(tableau, m, n, solution)
        optimal += tableau[m][m + n]
    return result, optimal * t


def solve_dual(result, m, n, a, b, c):
    unsolved = [i for i in range(m)]
    for i in range(m):
        tmp = 0
        for j in range(n):
            tmp += a[i][j] * result[j]
        # 根据互补对偶理论，如果原问题约束i 不bounding，那么对应的yi为0
        # 理解为这个yi已经解决了
        if tmp != b[i]:
            unsolved.remove(i)
    # column means the number of variables
    column = len(unsolved)
    # 创建对偶的表
    tableau = []
    tmp_b = []
    for i in range(n):
        if result[i] != 0:
            tmp = []
            for dul_i in range(m):
                if dul_i in unsolved:
                    # because fraction is not the basic type in numpy
                    # so I had to change it
                    tmp.append(float(a[dul_i][i]))
            tmp_b.append([float(-1 * c[i])])
            tableau.append(tmp)
    matrix_a = np.matrix(tableau)
    matrix_b = np.matrix(tmp_b)
    matrix_y = np.dot(matrix_a.getI(), matrix_b)
    dual_result = [0] * m
    index = 0
    for i in range(m):
        if i in unsolved:
            dual_result[i] = matrix_y.A[index][0]
            index += 1
    return dual_result
