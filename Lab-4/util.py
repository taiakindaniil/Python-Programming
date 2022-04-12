import numpy as np
import random

def rand_remove(original_data_y):
    deleted_data_y = original_data_y.copy()

    number_deleted_values = len(deleted_data_y) // 5
    values_counter = 0

    while values_counter < number_deleted_values:
        index = random.randint(0, len(deleted_data_y)-1)
        if deleted_data_y[index] is not None:
            deleted_data_y[index] = None
            values_counter += 1
    return deleted_data_y

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

def find_nearest_indexes(data, index):
    prev_elems_index = [index, None]
    next_elems_index = [index, None]

    while prev_elems_index[0] > 0 and data[prev_elems_index[0]] is None:
        prev_elems_index[0] -= 1
        prev_elems_index[1] = prev_elems_index[0]
        if prev_elems_index[0] > 0 and  data[prev_elems_index[0]] is not None:
            prev_elems_index[1] -= 1

            while prev_elems_index[1] > 0 and data[prev_elems_index[1]] is None:
                prev_elems_index[1] -= 1


    while next_elems_index[0] < len(data) and data[next_elems_index[0]] is None:
        next_elems_index[0] += 1
        next_elems_index[1] = next_elems_index[0]
        if next_elems_index[0] < len(data) and  data[next_elems_index[0]] is not None:
            next_elems_index[1] += 1
            while next_elems_index[1] < len(data) and data[next_elems_index[1]] is None:
                next_elems_index[1] += 1
    first_index = None
    second_index = None
    if prev_elems_index[0] >= 0 and next_elems_index[0] < len(data):
        if data[prev_elems_index[0]] is not None and data[next_elems_index[0]] is not None:
            first_index = prev_elems_index[0]
            second_index = next_elems_index[0]

            return first_index, second_index

    if prev_elems_index[0] >= 0 and data[prev_elems_index[0]] is None:
        first_index = next_elems_index[0]
        second_index = next_elems_index[1]

        return first_index, second_index

    return prev_elems_index[0], prev_elems_index[1]