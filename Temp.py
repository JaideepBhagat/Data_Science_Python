# Expart data for a stock from yfinance and export it to csv
import yfinance as yf
import pandas as pd
from dateutil.utils import today

ticker = input("Enter the stock ticker symbol: ") + ".NS"
start_date = today()-pd.Timedelta(days=365)
end_date = today()
data = yf.download(ticker, start=start_date, end=end_date)
df = pd.DataFrame(data)
df.to_csv('stock_data.csv')