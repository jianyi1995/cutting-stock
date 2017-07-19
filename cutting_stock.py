"""
cutting stock problem: there is m orders and their widths are stored in list w
,their demand are stored in list n and the total width of the paper capacity
this problem will return two lists with the cutting patterns and number of them 
"""
from Simplex import *
from knapsack import *


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
    c = [1] * column
    while True:
        aa = copy_two_dimension_list(a)
        nn = n.copy()
        cc = c.copy()
        result = simplex(-1, row, column, aa, nn, cc)
        dual_result = solve_dual(result, row, column, aa, nn, cc)
        value, new_column = column_generation(dual_result, capacity, w)
        if value < 1:
            return result
        else:
            for i in range(row):
                a[i] += new_column[i]
            column += 1


def get_initial_solution(w, capacity):
    l = len(w)
    patterns = [[0 for i in range(l)] for j in range(l)]
    for i in range(l):
        patterns[i][i] = capacity // w[i]
    return patterns




def column_generation(dual_solution, capacity, w):
    value, decision = knapsack(w, dual_solution, capacity)
    return value, decision
