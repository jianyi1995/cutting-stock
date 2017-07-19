'''
w means the weight of each item
v means the value of each item
capcity means the total weight of the knapsack
'''


def knapsack(w, v, capacity):
    value_table = [0] * (capacity + 1)
    choose_table = []
    for i in range(1, capacity + 1):
        for j in range(len(w)):
            if i - w[j] >= 0:
                value_table[i] = max(value_table[i], value_table[i - w[j]] + v[j])
    return value_table[capacity]

