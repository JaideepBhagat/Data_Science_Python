import pandas as pd
import yfinance as yf
import plotly.graph_objects as go
from dateutil.utils import today
from fontTools.misc.plistlib import end_date

# Fetch stock data
stock_ticker = 'ZOMATO.NS'  # Replace with your preferred stock symbol
start_date = today() - pd.DateOffset(days=365*3)
end_date = today()
data = yf.download(stock_ticker, start=start_date, end=end_date, interval='1d')

# Flatten column names
data.columns = [col[0] for col in data.columns]

# Calculate moving averages
data['MA50'] = data['Close'].rolling(window=50).mean()
data['MA200'] = data['Close'].rolling(window=200).mean()

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

# Customize layout
fig.update_layout(
    title=f'{stock_ticker} Stock Price Analysis',
    xaxis_title='Date',
    yaxis_title='Price',
    xaxis_rangeslider_visible=False,
    template='plotly_dark',
    legend=dict(x=0.01, y=0.99)
)

# Show the figure
fig.show()
