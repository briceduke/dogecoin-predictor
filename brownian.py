import numpy as np  
import pandas as pd  
from pandas_datareader import data as wb  
import matplotlib.pyplot as plt  
from scipy.stats import norm

def brownian(company, start, days_into_future):
    data = pd.DataFrame()
    data[company] = wb.DataReader(company, data_source='yahoo', start=start)['Adj Close']
    print(f"Starting Monte Carlo for {company}...")
    def run():
        log_returns = np.log(1 + data.pct_change())
        # pylint: disable=E1101
        u = log_returns.mean()

        var = log_returns.var()

        drift = u - (0.5 * var)

        stdev = log_returns.std()

        np.array(drift)

        norm.ppf(0.95)

        x = np.random.rand(10, 2)

        norm.ppf(x)

        t_intervals = 1 + days_into_future
        iterations = 10

        daily_returns = np.exp(drift.values + stdev.values * norm.ppf(np.random.rand(t_intervals, iterations)))

        S0 = data.iloc[-1]

        price_list = np.zeros_like(daily_returns)
        price_list[0] = S0

        for t in range(1, t_intervals):
            price_list[t] = price_list[t - 1] * daily_returns[t]

        ans = sum(price_list[1]) / len(price_list[1])

        return ans

    vals = []
    for _ in range(10000):
        val = run()
        vals.append(val)

    final = sum(vals) / len(vals)

    return final