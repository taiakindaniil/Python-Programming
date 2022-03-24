import numpy as np
import yahooapi as yapi
import json

# Moscow Exchange (MOEX)
# RUB currency
companies = ["SBER.ME", "GAZP.ME", "TATN.ME", "VTBR.ME", "ALRS.ME", "AFLT.ME", "HYDR.ME", "MOEX.ME", "NLMK.ME", "CHMF.ME", "DSKY.ME", "POLY.ME", "YNDX.ME", "AFKS.ME", "LSRG.ME", "LSNGP.ME", "LKOH.ME", "MTSS.ME", "NVTK.ME", "PIKK.ME"]

def save_charts():
    for symbol in companies:
        yapi.get_chart(symbol)

if __name__ == "__main__":

    save_charts() if input("Do you want to update stocks data? (y/n) ") == "y" else None

    for symbol in companies:
        f = open(f"./saved_api_responses/{symbol}.json", "r")
        json_data = json.load(f); f.close()

        timestamps = json_data["chart"]["result"][0]["timestamp"]
        close_arr  = json_data["chart"]["result"][0]["indicators"]["quote"][0]["close"]

        chart_data = zip(timestamps, close_arr)

        print(symbol, ":", chart_data)

