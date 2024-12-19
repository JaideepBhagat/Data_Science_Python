import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf
from dateutil.utils import today

# Histograms: Ideal for comparing distributions.
# Download data from Yahoo Finance
ticker = 'ZOMATO.NS'
start_date = today() - pd.Timedelta(days=365)
end_date = today()  # Current date

data = yf.download(ticker, start=start_date, end=end_date)

# Plot the histogram
plt.hist(data['Close'], bins=20, color='blue', alpha=0.7)
# Add Title
plt.title('Histogram Example')
# Add Labels
plt.xlabel('Closing Price')
plt.ylabel('Frequency')
# Change background color
plt.gca().set_facecolor('#f2f2f2')
# Show the plot
plt.show()