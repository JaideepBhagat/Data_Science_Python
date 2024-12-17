import yfinance as yf
import plotly.graph_objects as go

# Fetch stock data
stock_ticker = 'ZOMATO.NS'  # Replace with your preferred stock symbol
data = yf.download(stock_ticker, start='2022-01-01', end='2024-12-01', interval='1d')

# Flatten column names
data.columns = [col[0] for col in data.columns]

# Debugging data
print(data.head())  # Check the first few rows
print(data.info())  # Check for missing data

# Drop rows with missing values in key columns
data.dropna(subset=['Open', 'High', 'Low', 'Close', 'Volume'], inplace=True)

# Calculate moving averages
data['MA50'] = data['Close'].rolling(window=50).mean()
data['MA200'] = data['Close'].rolling(window=200).mean()

# Identify the highest and lowest price points
highest_price = data['High'].max()
lowest_price = data['Low'].min()

# Calculate Fibonacci retracement levels
diff = highest_price - lowest_price
fib_levels = {
    "0%": highest_price,
    "22.6%": highest_price - 0.226 * diff,
    "38.2%": highest_price - 0.382 * diff,
    "50%": highest_price - 0.5 * diff,
    "61.8%": highest_price - 0.618 * diff,
    "100%": lowest_price,
}

# Create the figure
fig = go.Figure()

# Add candlestick chart
fig.add_trace(go.Candlestick(
    x=data.index,
    open=data['Open'],
    high=data['High'],
    low=data['Low'],
    close=data['Close'],
    name='Candlesticks',
    increasing_line_color='green',
    decreasing_line_color='red'
))

# Add moving averages
fig.add_trace(go.Scatter(
    x=data.index, y=data['MA50'],
    mode='lines', name='50-Day MA',
    line=dict(color='blue', width=2)
))

fig.add_trace(go.Scatter(
    x=data.index, y=data['MA200'],
    mode='lines', name='200-Day MA',
    line=dict(color='orange', width=2)
))

# Add Fibonacci retracement levels
for level_name, level_value in fib_levels.items():
    fig.add_hline(
        y=level_value,
        line=dict(color='gold', dash='dash'),
        annotation_text=level_name,
        annotation_position="right",
        name=f'Fibonacci {level_name}'
    )

# # Add volume if available
# if 'Volume' in data.columns:
#     fig.add_trace(go.Bar(
#         x=data.index, y=data['Volume'],
#         name='Volume', marker_color='purple', opacity=0.4
#     ))
# else:
#     print("Volume data is not available for this stock.")

# Customize layout
fig.update_layout(
    title=f'{stock_ticker} Stock Price Analysis with Fibonacci Retracement',
    xaxis_title='Date',
    yaxis_title='Price',
    xaxis_rangeslider_visible=False,
    template='plotly_dark',
    legend=dict(x=0.01, y=0.99)
)

# Show the figure
fig.show()
