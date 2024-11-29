import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from dateutil.utils import today
import seaborn as sns

# Download Zomato stock data
start_date = today() - pd.Timedelta(days=365)
end_date = today()

data = yf.download('ZOMATO.NS', start=start_date, end=end_date)
prices = data['Close']  # Extract closing prices
prices.columns = ['Close']  # Rename columns

plt.figure(figsize=(10, 6))
sns.lineplot(prices['Close'], label='Closing Price')
plt.xlabel('Day')
plt.ylabel('Price')
plt.title('Zomato Stock Price')
plt.legend()
plt.show()