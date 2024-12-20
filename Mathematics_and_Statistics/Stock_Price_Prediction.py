import numpy as np
import pandas as pd
import yfinance as yf
from dateutil.utils import today
from pandas import to_datetime
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Fetch stock data for INFY.NS
def fetch_stock_data(ticker, start_date, end_date):
    """
    Fetch historical stock prices using yfinance.
    """
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    stock_data = stock_data[['Close']].dropna()  # Use 'Close' prices and drop NaN values
    stock_data.reset_index(inplace=True)
    stock_data['Day'] = np.arange(len(stock_data))  # Add a day index
    return stock_data

# Prepare data for regression
def prepare_data(stock_data):
    """
    Prepare data for training a regression model.
    """
    X = stock_data['Day'].values.reshape(-1, 1)  # Day index as features
    y = stock_data['Close'].values  # Closing prices as labels
    return X, y

# Predict next trading day's price
def predict_next_day(model, last_day_index):
    """
    Predict stock price for the next trading day.
    """
    next_day_index = np.array([[last_day_index + 1]])
    next_price = model.predict(next_day_index)  # Predict returns an array
    return next_price[0]  # Extract the scalar value


# Main function
def main():
    # Parameters
    ticker = str(input("Enter the stock ticker symbol: ")) or "IDEA.NS"
    # one year ago as start date
    start_date = today() - pd.Timedelta(days=365)
    # today's date as end date
    end_date = today()

    # Fetch and preprocess data
    stock_data = fetch_stock_data(ticker, start_date, end_date)
    X, y = prepare_data(stock_data)

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train Linear Regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Evaluate model
    score = model.score(X_test, y_test)
    print(f"Model Score: {score:.2f}")

    # Predict next trading day's price
    last_day_index = stock_data['Day'].iloc[-1]
    next_price = predict_next_day(model, last_day_index)

    # Display results
    print(f"Previous day index: {last_day_index} and closing price: {stock_data['Close'].iloc[-1]}")
    print(f"Predicted stock price for the next trading day: {next_price.item():.2f}")

    # Visualization
    plt.figure(figsize=(10, 6))
    plt.scatter(X, y, label="Actual Prices", color="blue", alpha=0.6)
    plt.plot(X, model.predict(X), label="Fitted Line", color="red")
    plt.scatter(last_day_index + 1, next_price, label="Next Day Prediction", color="green", zorder=5)
    plt.title(f"Stock Price Prediction for {ticker}")
    plt.xlabel("Day Index")
    plt.ylabel("Stock Price")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.show()


# Run the program
if __name__ == "__main__":
    main()
