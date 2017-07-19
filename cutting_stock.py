"""
cutting stock problem: there is m orders and their widths are stored in list w
,their demand are stored in list n and the total width of the paper capacity
this problem will return two lists with the cutting patterns and number of them 
"""


def cutting_stock(w, n, capacity):
    initial_solution = get_initial_solution(w, capacity)


def get_initial_solution(w, capacity):
    l = len(w)
    patterns = [[0 for i in range(l)] for j in range(l)]
    for i in range(l):
        patterns[i][i] = capacity // w[i]
    return patterns
