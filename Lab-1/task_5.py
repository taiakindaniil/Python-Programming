import matplotlib.pyplot as plt
import random, openpyxl
from task_6 import *

n = 25

def create_excel_file(x: list, y: list):
    wb = openpyxl.Workbook()
    sheet = wb.active

    sheet.cell(1, 1, "x")
    sheet.cell(1, 2, "y")

    for i, (coord_x, coord_y) in enumerate(zip(x, y)):
        sheet.cell(2+i, 1, coord_x)
        sheet.cell(2+i, 2, coord_y)

    wb.save("coords.xlsx")

def mnk(x: list, y: list):
    sum_x = sum(x); sum_y=sum(y)
    sum_xy = sum(map(lambda x, y: x * y, x, y))
    sum_x2 = sum(map(lambda x: x ** 2, x))

    det_m = Matrix(2, 2, [sum_x2, sum_x, sum_x, n]).det()
    det_a = Matrix(2, 2, [sum_xy, sum_x, sum_y, n]).det()
    det_b = Matrix(2, 2, [sum_x2, sum_xy, sum_x, sum_y]).det()

    a = det_a / det_m
    b = det_b / det_m

    return a, b


if __name__ == "__main__":
    min_v, max_v = map(int, input().split())

    x = []; y = []
    for _ in range(n):
        x.append(random.uniform(min_v, max_v))
        y.append(random.uniform(min_v, max_v))

    create_excel_file(x, y)

    a, b = mnk(x, y)

    plt.plot([min_v, max_v], [a*min_v + b, a*max_v + b], color="#CE7A60")

    plt.scatter(x, y)
    plt.show()

    print(x, y)
