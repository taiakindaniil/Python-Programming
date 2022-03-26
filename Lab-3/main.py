import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from company import *
from stock import *

# Moscow Exchange (MOEX)
# RUB currency
symbols = ["SBER", "GAZP", "TATN", "VTBR", "ALRS", "AFLT", "HYDR", "MOEX", "NLMK", "CHMF", "DSKY", "POLY", "YNDX", "AFKS", "LSRG", "LSNGP", "LKOH", "MTSS", "NVTK", "PIKK"]

# finds min values in matrix without repetition and
# returns an array of min values
def find_values(matrix, which="min", k=1):
    matrix_copy = matrix.copy()

    # return the indices for the upper-triangle of an (n, m) array
    iu1 = np.triu_indices(len(matrix_copy))

    # get rid off repetions and flat matrix
    if which == "min":
        matrix_copy[iu1] = float("inf")
        matrix_copy = matrix_copy[matrix_copy < float("inf")]
        return np.sort(matrix_copy)[:k]
    elif which == "max":
        matrix_copy[iu1] = float("-inf")
        matrix_copy = matrix_copy[matrix_copy > float("-inf")]
        return np.flip(np.sort(matrix_copy))[:k]

if __name__ == "__main__":
    total_money = 10_000_000
    total_months = 3 * 12 # years * months

    people = {
        "Anatoliy": {"money": total_money // 3, "stocks": [], "money_log": []},
        "Boris":    {"money": total_money // 3, "stocks": [], "money_log": []},
        "Evgeniy":  {"money": total_money // 3, "stocks": [], "money_log": []}
    }

    # starts from 6 - previously we analyzed stocks for 6 months (2016)
    for i in range(6, total_months+1, 6):

        sum_market_cap = 0
        all_prices = []

        # data of companies for period
        companies = []

        for symbol in symbols[0:4]:
            df = pd.read_csv(f"./data/{symbol}.csv", sep=';', names=['date', 'price', 'change', 'cap'])
            all_prices.append(df['price'][i:i+6])
            sum_market_cap += df['cap'][i]

            companies.append(
                Company(symbol, list(df['price'][i:i+6]), df['cap'][i])
            )

        for _, assets in people.items():
            for stock in assets["stocks"].copy():
                company = companies[symbols.index(stock.name)]
                assets["money"] += stock.number * company.prices[len(company.prices) - 1]
                assets["stocks"].pop()
            
            assets["money_log"].append(assets["money"])

        if i != total_months:
            # Evgeniy case
            temp_money = 0
            for company in companies:
                stock_price = company.prices[len(company.prices) - 1]
                stocks_number = people['Evgeniy']['money'] * (company.cap / sum_market_cap) // stock_price
                people['Evgeniy']['stocks'].append(Stock(company.name, stocks_number, stock_price))
                temp_money += stocks_number * stock_price
            people['Evgeniy']['money'] -= temp_money


            # finds Pearson's coefficient matrix 
            coef = np.corrcoef(all_prices)

            min_values = find_values(coef, which="min", k=3)
            max_values = find_values(coef, which="max", k=3)

            def buy_stocks(who, stocks_names):
                temp_money = 0
                for stock_name in stocks_names:
                    company = companies[symbols.index(stock_name)]
                    stock_price = company.prices[len(company.prices) - 1]
                    stocks_number = people[who]['money'] / 3 * 0.5 // stock_price
                    people[who]['stocks'].append(Stock(company.name, stocks_number, stock_price))
                    temp_money += stocks_number * stock_price
                people[who]['money'] -= temp_money

            anatoliy_stocks = []
            for min_value in min_values:
                i, j = np.where(coef == min_value)
                anatoliy_stocks.append(symbols[i[0]])
                anatoliy_stocks.append(symbols[j[0]])
            buy_stocks("Anatoliy", anatoliy_stocks)

            boris_stocks = []
            for max_value in max_values:
                i, j = np.where(coef == max_value)
                boris_stocks.append(symbols[i[0]])
                boris_stocks.append(symbols[j[0]])
            buy_stocks("Boris", boris_stocks)

    colors = {"Anatoliy": "#CE7A60", "Boris": "#00C39F", "Evgeniy": "#6DC1E6"}
    for name, assets in people.items():
        plt.plot(range(len(assets["money_log"])), assets["money_log"], color=colors[name], label=name)
    plt.legend()
    plt.show()
