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
prices = util.rand_remove(prices)

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
# i is index for all_data
def correlation(i, all_data: list):
    # finds Pearson's coefficient matrix 
    coef = np.corrcoef(all_data)
    pass

print(prices)
print(linear_approximation(prices))

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