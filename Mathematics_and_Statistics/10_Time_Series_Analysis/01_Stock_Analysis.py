import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from dateutil.utils import today
from statsmodels.tsa.seasonal import seasonal_decompose

# Download historical stock data from Yahoo Finance
ticker = 'ZOMATO.NS'
start_date = today() - pd.Timedelta(days=365 * 3)  # 2 years of data
end_date = today()  # Current date

data = yf.download(ticker, start=start_date, end=end_date)

# Explore and pre-process the data
print(data.head())

# Set the index to the 'Date' column
data.index = pd.to_datetime(data.index)
data = data[['Open', 'High', 'Low', 'Close', 'Volume']]

# Check for missing values
print("Null Values: \n", data.isnull().sum())

# If missing values are present, fill them with forward filling
data.fillna(method = 'ffill', inplace = True)

# Plot the closing price over time
plt.figure(figsize=(10, 6))
plt.plot(data['Close'], label='Closing Price')
plt.title(f"{ticker} Stock Closing Prices")
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.legend()
plt.show()

# Visualize the volume over time
plt.figure(figsize = (10,6))
plt.plot(data['Volume'], label='Trading Volume', color='orange')
plt.title(f"{ticker} Trading Volume")
plt.xlabel('Date')
plt.ylabel('Volume')
plt.legend()
plt.show()

# Calculate and plot moving averages
data['SMA50'] = data['Close'].rolling(window=50).mean()
data['SMA200'] = data['Close'].rolling(window=200).mean()

plt.figure(figsize=(10,6))
plt.plot(data['Close'], label='Closing Price', color='blue')
plt.plot(data['SMA50'], label = 'SMA50', color='yellow')
plt.plot(data['SMA200'], label = 'SMA200', color='red')
plt.title(f"{ticker} Stock Closing Prices with Moving Averages")
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.legend()
plt.show()

# Compute daily returns
data['Daily Returns'] = data['Close'].pct_change()

# Plot daily returns
plt.figure(figsize=(10,6))
plt.plot(data['Daily Returns'], label='Daily Returns', color='Purple')
plt.axhline(0, color='black', linewidth=1)
plt.title(f"{ticker} Daily Returns")
plt.xlabel('Date')
plt.ylabel('Daily Returns')
plt.legend()
plt.show()

# Calculate rolling valatility and plot it
data['Volatility'] = data['Daily Returns'].rolling(window=30).std()

plt.figure(figsize=(10,6))
plt.plot(data['Volatility'], label='Volatility', color='Orange')
plt.axhline(0, color='black', linewidth=1)
plt.title(f"{ticker} Volatility")
plt.xlabel('Date')
plt.ylabel('Volatility')
plt.legend()
plt.show()

# Decompose the stocks time series
decomposition = seasonal_decompose(data['Close'], model='additive', period=365)
decomposition.plot()
plt.show()

# Forecast future stock prices
data['SMA Forecast'] = data['SMA50'].shift(-9)

plt.figure(figsize=(10,6))
plt.plot(data['Close'], label='Closing Price', color='blue')
plt.plot(data['SMA50'], label = 'SMA50', color='yellow')
plt.plot(data['SMA Forecast'], label = 'SMA Forecast', color='red')
plt.title(f"{ticker} Stock Closing Prices with Moving Averages and Forecast")
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.legend()
plt.show()