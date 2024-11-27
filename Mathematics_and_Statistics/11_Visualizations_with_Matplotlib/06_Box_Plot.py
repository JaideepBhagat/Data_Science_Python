import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf
from dateutil.utils import today
# Box Plots: Ideal for comparing distributions.
# Download data from Yahoo Finance
ticker = 'ZOMATO.NS'
start_date = today() - pd.Timedelta(days=365)
end_date = today()  # Current date

data = yf.download(ticker, start=start_date, end=end_date)

# Plot the box plot
plt.boxplot(data['Close'])
# Add Title
plt.title('Box Plot Example')
# Add Labels
plt.xlabel('Closing Price')
# Change background color
plt.gca().set_facecolor('#f2f2f2')
# Show the plot
plt.show()