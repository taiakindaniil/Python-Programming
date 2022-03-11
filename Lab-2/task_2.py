import matplotlib.pyplot as plt
import numpy as np
import random

from custom_module import Matrix
from task_3 import *

def remove_items(table):
    for _ in range(10):
        i = random.randint(0, len(table) - 1)
        j = random.randint(0, len(table) - 1)
        table[i][j] = None
    return table

# util function for debug
def show_plot(X: list, Y: list):
    plt.plot(X, Y, color="#CE7A60")
    plt.scatter(X, Y)
    plt.show()

def linear_approximation(table):
    # Using MNK method for approximation
    def mnk(x: list, y: list):
        n = len(x)

        sum_x = sum(x); sum_y=sum(y)
        sum_xy = sum(map(lambda x, y: x * y, x, y))
        sum_x2 = sum(map(lambda x: x ** 2, x))

        det_m = Matrix(2, 2, [sum_x2, sum_x, sum_x, n]).det()
        det_a = Matrix(2, 2, [sum_xy, sum_x, sum_y, n]).det()
        det_b = Matrix(2, 2, [sum_x2, sum_xy, sum_x, sum_y]).det()

        a = det_a / det_m
        b = det_b / det_m

        return a, b
    
    def find_nearest_elements(Y: list, index):
        prv = index; nxt = index
        while True:
            if nxt == len(Y) - 1:
                nxt = 0

            prv -= 1 if Y[prv] == None else 0
            nxt += 1 if Y[nxt] == None else 0
            
            if Y[prv] != None and Y[nxt] != None:
                break
        
        return prv, nxt
    
    for i_Y, Y in enumerate(table):
        X = [x for x in range(len(Y))]

        indices = [i for i, y in enumerate(Y) if y == None]
        for i in indices:
            prv, nxt = find_nearest_elements(Y, i)

            a, b = mnk([X[prv], X[nxt]], [Y[prv], Y[nxt]])
            table[i_Y][i] = a*X[i] + b

    return table


if __name__ == "__main__":
    table = remove_items(rand_table())

    print(
"""
1. Linear approximation
2. Correlation    
""")

    opt = int(input("Select option: "))

    if opt == 1:
        print("Before:", table, "\n")
        linear_table = linear_approximation(table)
        print("After:", linear_table)
    elif opt == 2:
        r_table = table.copy()
        while True:
            print(
"""
Select two columns that you want correlate:
(Enter two numbers with a space between)
""")

            for i, x in enumerate(r_table):
                print(i, x)

            a, b = map(int, input("Columns: ").split())

            items1 = [0 if x == None else x for x in r_table[a]]
            items2 = [0 if x == None else x for x in r_table[b]]

            indices1 = [i for i, y in enumerate(r_table[a]) if y == None]
            indices2 = [i for i, y in enumerate(r_table[b]) if y == None]

            coef = np.corrcoef(items1, items2)[0][1]

            for i in indices1:
                if r_table[a][i] is None and r_table[b][i] is not None:
                    r_table[a][i] = r_table[b][i] * coef
                elif r_table[b][i] is None and r_table[a][i] is not None:
                    r_table[b][i] = r_table[a][i] * coef

            for i in indices2:
                if r_table[a][i] is None and r_table[b][i] is not None:
                    r_table[a][i] = r_table[b][i] * coef
                elif r_table[b][i] is None and r_table[a][i] is not None:
                    r_table[b][i] = r_table[a][i] * coef

            print(r_table)

    else:
        exit(1)

    # show_plot(range(len(table)), table[0])
    # show_plot(range(len(table)), linear_table[0])