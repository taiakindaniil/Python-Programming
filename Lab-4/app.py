from tkinter import *
from config import *
import numpy as np
import pandas as pd
import util

symbols = ["SBER", "GAZP", "TATN", "VTBR", "ALRS", "AFLT", "HYDR", "MOEX", "NLMK", "CHMF", "DSKY", "POLY", "YNDX", "AFKS", "LSRG", "LSNGP", "LKOH", "MTSS", "NVTK", "PIKK"]


symbol = "SBER"
df = pd.read_csv(f"./data/{symbol}.csv", sep=';', names=['date', 'price', 'change', 'cap'])
i=0

# prices for 10 months
prices = list(df['price'][i:i+10])
# prices = util.rand_remove(prices)

# gets all prices for 10 months (hardcoded)
def get_all_prices() -> list:
    all_prices = []
    for symbol in symbols:
        df = pd.read_csv(f"./data/{symbol}.csv", sep=';', names=['date', 'price', 'change', 'cap'])
        all_prices.append(list(df['price'][i:i+10]))
    return all_prices



# recovery methods
# - winsoring method
def winsoring(data: list):
    data_copy = data.copy()
    prev_val = None; next_val = None
    for (i, x) in enumerate(data_copy):
        if x == None:
            j = i+1
            while j < len(data_copy):
                if data_copy[j] != None:
                    next_val = data_copy[j]; break
                j += 1
        else:
            prev_val = x
        
        data_copy[i] = prev_val or next_val

    return data_copy

# - linear approximation
def linear_approximation(data: list):
    data_copy = data.copy()

    indices = [i for i, x in enumerate(data_copy) if x == None]
    for i in indices:
        # find nearest indexes to get an approximation
        prv, nxt = util.find_nearest_indexes(data_copy, i)

        a, b = util.mnk([prv, nxt], [data_copy[prv], data_copy[nxt]])

        r_y = a*i + b
        data_copy[i] = r_y

    return data_copy

# - correlation
def correlation(values1, values2):
    for i, _ in enumerate(values1):
        if values1[i] == None:
            if i == len(values1) - 1:
                p1 = values1[i - 1]
                v1 = values2[i - 1]
                v2 = values2[i]
                values1[i] = p1 * v1 / v2
            else:
                p2 = values1[i + 1]
                v1 = values2[i]
                v2 = values2[i + 1]
                values1[i] = p2 * v2 / v1
        elif values2[i] == None:
            if i == len(values2) - 1:
                p1 = values1[i - 1]
                p2 = values1[i]
                v1 = values2[i - 1]
                values2[i] = p1 * v1 / p2
            else:
                p1 = values1[i]
                p2 = values1[i + 1]
                v2 = values2[i + 1]
                values2[i] = p2 * v2 / p1
    return values1, values2

# print(prices)
# print(correlation(util.rand_remove(prices), prices))


# smoothing methods
# - moving average with windowing
# https://wiki.loginom.ru/articles/windowing-method.html
def MAW(Y, k=2):
    n = len(Y)
    temp_Y = Y[0:k]
    for t in range(k, n):
        slice_Y = Y[t-k:t]
        temp_Y.append(sum(slice_Y) / len(slice_Y))
    return temp_Y

def WMA(data):
    data_copy = data.copy()

    # количество значений исходной функции для расчёта скользящего среднего
    n = 2

    for t in range(n, len(data)):
        sum_data = 0
        for i in range(n):
            sum_data += (n-i)*data[t-i]
        
        for i in range(n):
            data_copy[t] = (2 / (n * (n+1))) * sum_data

    return data_copy


print(prices)
print(WMA(prices))


def App():

    root = Tk()
    root.title("Начинающий Брокер")
    root.geometry("500x500")
    root.resizable(width=False, height=False)

    def build_click():
        print("logging")

    frame = Frame(root, bg=bg_color)
    frame.place(relwidth=1, relheight=1)

    title = Label(frame, text="Пример", bg=bg_color)
    title.pack()

    build_btn = Button(frame, text="Build", bg=bg_color, borderwidth=0, command=build_click)
    build_btn.pack()

    root.mainloop()

if __name__ == "__main__":
    # App()
    pass