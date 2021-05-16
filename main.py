import datetime as dt
import pandas_datareader as web

from data import ticker, start, days_into_future

from neural_network import run
from regression import linreg
from brownian import brownian

current = web.DataReader(ticker, "yahoo", start, dt.datetime.now())
actual_price = current['Close'].values[-1]

def do():
    lstm = run(ticker, days_into_future, current)
    regression = linreg(ticker, days_into_future, current)
    monte = brownian(ticker, start, days_into_future)

    prediction = (lstm + regression + monte) / 3

    if not ticker == "DOGE-USD":
        print(f"${round(prediction, 2)}", f"{round(((prediction - actual_price) / actual_price) * 100, 2)}%")
        return f"${round(prediction, 2)} ({round(((prediction - actual_price) / actual_price) * 100, 2)}%)"
    else:
        print(f"${round(prediction, 5)}", f"{round(((prediction - actual_price) / actual_price) * 100, 2)}%")
        return f"${round(prediction, 5)} ({round(((prediction - actual_price) / actual_price) * 100, 2)}%)"