import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import pandas as pd
import pandas_datareader as web
import operator

from sklearn.linear_model import LinearRegression
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split

def linreg(company, days_into_future, current):
    dict = {}
    
    print(f"Starting Linear Regression for {company}...")
    def run():
        forecast_out = days_into_future # predicting days into future

        data = current

        df = pd.DataFrame(data, columns=['Close'])
        df = df[['Close']]

        df['Prediction'] = df[['Close']].shift(-forecast_out)

        X = np.array(df.drop(['Prediction'], 1))
        X = preprocessing.scale(X)
        X_forecast = X[-forecast_out:]
        X = X[:-forecast_out]
        y = np.array(df['Prediction'])
        y = y[:-forecast_out]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
        # Training
        clf = LinearRegression()
        clf.fit(X_train,y_train)
        # Testing
        confidence = clf.score(X_test, y_test)
        prediction = clf.predict(X_forecast)
        # print(prediction)

        # Multiday Outlook
        prediction = prediction[-1]
        prediction = str(prediction)
        prediction = prediction.replace('[', '')
        prediction = prediction.replace(']', '')
        prediction = float(prediction)
        dict[prediction] = confidence

    for _ in range(80):
        run()

    ans = max(dict, key=dict.get)

    return ans