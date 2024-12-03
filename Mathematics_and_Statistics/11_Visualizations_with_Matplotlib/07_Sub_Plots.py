import matplotlib.pyplot as plt
from dateutil.utils import today
import pandas as pd
import yfinance as yf
import numpy as np
# Create multi-panel figures using plt.subplot().
# Subplots are used to create a grid of plots within a single figure.

# Downlaod data from Yahoo Finance
ticker = 'MARICO.NS'
start_date = today() - pd.Timedelta(days=365)
end_date = today()  # Current date

data = yf.download(ticker, start=start_date, end=end_date)

# Set the index to the 'Date' column
data['Day'] = np.arange(len(data))

# Create subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# Plot the data in the first subplot
axes[0, 0].plot(data['Volume'], label='Volume', color='orange')
axes[0, 0].set_title('Volume')

# Plot the data in the second subplot
axes[0, 1].hist(data['Close'], bins=50, color='green', alpha=0.7)
axes[0, 1].set_title('Stock Price Histogram')

# Plot the data in the third subplot
data['SMA50'] = data['Close'].rolling(window=50).mean()
data['SMA200'] = data['Close'].rolling(window=200).mean()
axes[1, 0].plot(data['Close'], label='Closing Price', color='blue')
axes[1, 0].plot(data['SMA50'], label='SMA50', color='green')
axes[1, 0].plot(data['SMA200'], label='SMA200', color='red')
axes[1, 0].set_title("Closing Prices with Moving Averages")

# Plot the data in the fourth subplot
data['Daily Returns'] = data['Close'].pct_change()
axes[1, 1].plot(data['Daily Returns'], label='Daily Returns', color='Purple')
axes[1, 1].axhline(0, color='black', linewidth=1)
axes[1, 1].set_title('Daily Returns')

# Adjust spacing between subplots
plt.tight_layout()

# Show the plot
fig.suptitle("Stock Analysis")
plt.show()