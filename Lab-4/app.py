from tkinter import *
from config import *
import pandas as pd
import matplotlib.pyplot as plt
import util

symbols = ["SBER", "GAZP", "TATN", "VTBR", "ALRS", "AFLT", "HYDR", "MOEX", "NLMK", "CHMF", "DSKY", "POLY", "YNDX", "AFKS", "LSRG", "LSNGP", "LKOH", "MTSS", "NVTK", "PIKK"]

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


# print(prices)
# print(WMA(prices))

def std_deviation(orig_data: list, data: list):
    n = len(data)
    avg = sum(data) / n
    summ = 0
    for i in range(n):
        summ += (data[i] - orig_data[i])**2
    return ((1/n) * summ) ** 0.5

def App():

    root = Tk()
    root.title("Начинающий Брокер")
    root.geometry("500x200")
    root.resizable(width=False, height=False)

    frame = Frame(root, bg=bg_color)
    frame.place(relwidth=1, relheight=1)

    def option_menu(data: list, default_value) -> StringVar:
        variable = StringVar(frame)
        variable.set(default_value)
        OptionMenu(frame, variable, *data).pack()
        return variable

    symbol_variable      = option_menu(symbols, "Select Ticket")
    recovery_variable    = option_menu(["Winsoring", "Linear approximation", "Correlation"], "Select Recovery Method")
    antialising_variable = option_menu(["Moving Average", "Moving Average w/ Windowing"], "Select Anti-aliasing Method")

    title = Label(frame, text="Select second ticker if you've selected Correlation recovery method.", bg=bg_color)
    title.pack()

    symbol2_variable = option_menu(symbols, "Select Ticket")

    def build_click():
        symbol = symbol_variable.get()
        symbol2 = symbol2_variable.get()
        recovery = recovery_variable.get()
        antialising = antialising_variable.get()

        df = pd.read_csv(f"./data/{symbol}.csv", sep=';', names=['date', 'price', 'change', 'cap'])
        # prices for 18 months
        i=0
        prices = util.rand_remove(list(df['price'][i:i+18]))

        recovered_prices = []
        if recovery == "Winsoring":
            recovered_prices = winsoring(prices)
        elif recovery == "Linear approximation":
            recovered_prices = linear_approximation(prices)
        elif recovery == "Correlation":
            df = pd.read_csv(f"./data/{symbol2}.csv", sep=';', names=['date', 'price', 'change', 'cap'])
            # prices for 18 months
            i=0
            prices2 = util.rand_remove(list(df['price'][i:i+18]))
            recovered_prices = correlation(prices, prices2)[0]

        antialised_prices = []
        if antialising == "Moving Average":
            antialised_prices = MAW(recovered_prices, k=2)
        elif antialising == "Moving Average w/ Windowing":
            antialised_prices = WMA(recovered_prices)

        # show what we've done
        fig, axs = plt.subplots(3)
        axs[0].set_title("Initial data")
        axs[0].plot(range(len(prices)), prices, color="#CE7A60")
        axs[1].set_title("Recovered data")
        axs[1].plot(range(len(recovered_prices)), recovered_prices, color="#CE7A60")
        axs[2].set_title("Antialised data")
        axs[2].plot(range(len(antialised_prices)), antialised_prices, color="#FE7A60")

        plt.text(0.5, 0.5, f"σ = {std_deviation(recovered_prices, antialised_prices)}")

        fig.tight_layout()
        plt.show()

    build_btn = Button(frame, text="Build", bg=bg_color, borderwidth=0, command=build_click)
    build_btn.pack()

    root.mainloop()

if __name__ == "__main__":
    App()