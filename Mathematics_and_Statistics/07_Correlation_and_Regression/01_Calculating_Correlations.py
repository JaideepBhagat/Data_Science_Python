# Correlation heatmap of financial assets
import yfinance as yf

# Download stock data
stocks = ['INFY.NS', 'TCS.NS', 'WIPRO.NS', 'HCLTECH.NS']
data = yf.download(stocks, start='2024-01-01')['Close']
correlation_matrix = data.corr()
print(correlation_matrix)