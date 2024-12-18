import yfinance as yf
import plotly.graph_objects as go

def ichimoku_cloud(df):
    # Calculate Ichimoku Cloud components
    df['tenkan_sen'] = (df['High'].rolling(window=9).max() + df['Low'].rolling(window=9).min()) / 2
    df['kijun_sen'] = (df['High'].rolling(window=26).max() + df['Low'].rolling(window=26).min()) / 2
    df['senkou_span_a'] = ((df['tenkan_sen'] + df['kijun_sen']) / 2).shift(26)
    df['senkou_span_b'] = ((df['High'].rolling(window=52).max() + df['Low'].rolling(window=52).min()) / 2).shift(26)
    df['chikou_span'] = df['Close'].shift(-26)

    return df

# Get stock data
ticker = 'ZOMATO.NS'
df = yf.download(ticker, period='1y', interval='1d')

# Calculate Ichimoku Cloud
df = ichimoku_cloud(df)

# Create candlestick chart with Ichimoku Cloud
fig = go.Figure(data=[go.Candlestick(x=df.index,
                    open=df['Open'],
                    high=df['High'],
                    low=df['Low'],
                    close=df['Close'])])

# Add Ichimoku Cloud
fig.add_trace(go.Scatter(x=df.index, y=df['senkou_span_a'], line=dict(color='rgba(128, 128, 128, 0.5)', width=1), name='Senkou Span A'))
fig.add_trace(go.Scatter(x=df.index, y=df['senkou_span_b'], line=dict(color='rgba(128, 128, 128, 0.5)', width=1), name='Senkou Span B'))

# Fill the area between Senkou Span A and Senkou Span B
fig.add_trace(go.Scatter(x=df.index, y=df['senkou_span_a'], fill='tonexty', fillcolor='rgba(128, 128, 128, 0.2)', line=dict(color='rgba(0,0,0,0)'), name='Ichimoku Cloud'))
fig.add_trace(go.Scatter(x=df.index, y=df['senkou_span_b'], fill='tonexty', fillcolor='rgba(255, 255, 255, 0.2)', line=dict(color='rgba(0,0,0,0)')))

# Add Tenkan-sen and Kijun-sen
fig.add_trace(go.Scatter(x=df.index, y=df['tenkan_sen'], line=dict(color='red', width=1), name='Tenkan-sen'))
fig.add_trace(go.Scatter(x=df.index, y=df['kijun_sen'], line=dict(color='blue', width=1), name='Kijun-sen'))

# Add Chikou Span
fig.add_trace(go.Scatter(x=df.index, y=df['chikou_span'], line=dict(color='green', width=1), name='Chikou Span'))

# Customize the plot
fig.update_layout(
    title=f'Ichimoku Cloud for {ticker}',
    xaxis_rangeslider_visible=False
)

fig.show()