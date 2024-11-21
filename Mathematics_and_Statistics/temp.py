import yfinance as yf
import pandas as pd
import numpy as np

def get_data(tickers):
    # Download data using yfinance
    data = yf.download(tickers, start="2015-01-01", end="2023-12-31", group_by="ticker")
    return data

tickers = ["INFY.BO", "TCS.BO", "HCLTECH.BO", "WIPRO.BO"]
data = get_data(tickers)

for ticker in tickers:
    df_ticker = data[ticker]
    df_ticker['Return'] = np.log(df_ticker['Adj Close'] / df_ticker['Adj Close'].shift(1))
    print(df_ticker.head())
