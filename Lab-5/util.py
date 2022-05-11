import numpy as np

def MAW(Y, k=2):
    n = len(Y)
    temp_Y = Y[0:k]
    for t in range(k, n):
        slice_Y = Y[t-k:t]
        temp_Y.append(sum(slice_Y) / len(slice_Y))
    return temp_Y

def mnk(x: list, y: list):
    n = len(x)

    sum_x = sum(x); sum_y=sum(y)
    sum_xy = sum(map(lambda x, y: x * y, x, y))
    sum_x2 = sum(map(lambda x: x ** 2, x))

    det_m = np.linalg.det(np.matrix([[sum_x2, sum_x], [sum_x, n]]))
    det_a = np.linalg.det(np.matrix([[sum_xy, sum_x], [sum_y, n]]))
    det_b = np.linalg.det(np.matrix([[sum_x2, sum_xy], [sum_x, sum_y]]))

    a = det_a / det_m
    b = det_b / det_m

    return a, b