import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import yfinance as yf
from dateutil.utils import today

# Scatter Plots: Ideal for comparing two variables.
# Download data from Yahoo Finance
ticker = 'ZOMATO.NS'
start_date = today() - pd.Timedelta(days=365)
end_date = today()  # Current date

data = yf.download(ticker, start=start_date, end=end_date)

# Add a day index
data['Day'] = np.arange(len(data))

# Plot the scatter plot
plt.scatter(data['Day'], data['Close'], color='blue', alpha=0.5)
# Add Title
plt.title('Scatter Plot Example')
# Add Labels
plt.xlabel('Day')
plt.ylabel('Closing Price')
# Change background color
plt.gca().set_facecolor('#f2f2f2')
# Show the plot
plt.show()