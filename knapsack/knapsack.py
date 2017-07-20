"""
w means the weight of each item
v means the value of each item
capacity means the total weight of the knapsack

value_table[i] means the maximum value we can get after using weight i of the knapsack
decision_table means the number of each item we choose
"""


def knapsack(w, v, capacity):
    value_table = [0] * (capacity + 1)
    choose_table = [-1]
    decision_table = [0] * len(w)
    for i in range(1, capacity + 1):
        tmp = -1
        for j in range(len(w)):
            if i - w[j] >= 0 and value_table[i - w[j]] + v[j] > value_table[i]:
                value_table[i] = value_table[i - w[j]] + v[j]
                tmp = j
        choose_table.append(tmp)
    p = choose_table[-1]
    c = capacity
    while p != -1:
        decision_table[p] += 1
        c -= w[p]
        p = choose_table[c]
    return value_table[capacity], decision_table

