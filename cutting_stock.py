"""
cutting stock problem: there is m orders and their widths are stored in list w
,their demand are stored in list n and the total width of the paper capacity
this problem will return two lists with the cutting patterns and number of them 
"""
from Simplex import *
from knapsack import *
import math


def copy_two_dimension_list(l):
    ll = []
    for i in l:
        tmp = []
        for j in i:
            tmp.append(j)
        ll.append(tmp)
    return ll


def cutting_stock(w, n, capacity):
    a = get_initial_solution(w, capacity)
    row = column = len(w)
    # c is -1 * the c in expression
    c = [-1] * column
    while True:
        aa = copy_two_dimension_list(a)
        nn = n.copy()
        cc = c.copy()
        result = simplex(-1, row, column, aa, nn, cc)
        dual_result = solve_dual(result, row, column, aa, nn, cc)
        value, new_column = column_generation(dual_result, capacity, w)
        if abs(value - 1) < 1e-6:
            count = 0
            for j in range(column):
                if result[j]:
                    pattern = []
                    for i in range(row):
                        pattern.append(a[i][j])
                    print('using column:')
                    print(pattern)
                    print('%d times' % math.ceil(result[j]))
                    count += math.ceil(result[j])
            print('the number of rolls is %d' % count)
            return result
        else:
            for i in range(row):
                a[i] = a[i] + [new_column[i]]
            column += 1
            c = c + [-1]


def get_initial_solution(w, capacity):
    l = len(w)
    patterns = [[0 for i in range(l)] for j in range(l)]
    for i in range(l):
        patterns[i][i] = capacity // w[i]
    return patterns


def column_generation(dual_solution, capacity, w):
    value, decision = knapsack(w, dual_solution, capacity)
    return value, decision


if __name__ == '__main__':
    capacity = 20
    w = [9, 8, 7, 6]
    n = [511, 301, 263, 383]
    result = cutting_stock(w, n, capacity)