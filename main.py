import datetime as dt
import pandas_datareader as web

from neural_network import run
from regression import linreg
from brownian import brownian

def do():
    ticker = input("Ticker: ")
    start = dt.datetime(1970,1,1)

    current = web.DataReader(ticker, "yahoo", start, dt.datetime.now())
    actual_price = current['Close'].values[-1]

    days_into_future = int(input("Days Into Future: "))
    iterations = int(input("Iterations: "))

    avg = 0

    list = []

    for _ in range(iterations):
        lstm = run(ticker, days_into_future, current)
        regression = linreg(ticker, days_into_future, current)
        monte = brownian(ticker, start, days_into_future)

        avg += (lstm + regression + monte) / 3

        list.append((lstm + regression + monte) / 3)

    prediction = avg / iterations

    print(list)

    if not ticker == "DOGE-USD":
        print(f"${round(prediction, 2)}", f"{round(((prediction - actual_price) / actual_price) * 100, 2)}%")
        return f"${round(prediction, 2)} ({round(((prediction - actual_price) / actual_price) * 100, 2)}%)"
    else:
        print(f"${round(prediction, 5)}", f"{round(((prediction - actual_price) / actual_price) * 100, 2)}%")
        return f"${round(prediction, 5)} ({round(((prediction - actual_price) / actual_price) * 100, 2)}%)"