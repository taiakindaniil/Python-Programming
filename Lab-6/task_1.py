from statsmodels.tsa.ar_model import AutoReg
from sklearn.metrics import mean_squared_error
import gspread
import numpy as np

if __name__ == "__main__":
    gc = gspread.service_account(filename="./python-college-project-406804075937.json")
    sh = gc.open("Task 1").sheet1
    data: list = sh.col_values(2)[1:][::-1]

    train, test = np.array(data[:95]).astype("float"), np.array(data[95:]).astype("float")

    model = AutoReg(train, lags=7)
    model_fit = model.fit()

    predictions = model_fit.predict(start=len(train), end=len(train) + len(test) - 1)

    print(f"Predicted: {'{:.2f}'.format(predictions[0])}, Actual: {test[0]}")

    rmse = mean_squared_error(test, predictions) ** 0.5
    print(f"RMSE is: {rmse}")

    if test[0] > predictions[0]:
        print("The price is overvalued.")
    else:
        print("The price is undervalued.")

