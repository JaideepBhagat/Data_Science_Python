# Import required libraries
import numpy as np
import pandas as pd
import yfinance as yf
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# 1. Fetch stock data using yfinance
ticker = str(input("Enter the stock ticker symbol: "))
start_date = "2023-12-22"
end_date = "2024-12-23"

# Download stock data
data = yf.download(ticker, start=start_date, end=end_date)

# Reset index to get the Date as a column
data.reset_index(inplace=True)

# Extract 'Date' and 'Close' columns for simplicity
data = data[['Date', 'Close']]

# Convert 'Date' to numerical value (days since start date)
data['Days'] = (data['Date'] - data['Date'].min()).dt.days

# Features and target
X = data[['Days']]  # Independent variable (numerical date representation)
y = data['Close']   # Dependent variable (closing stock price)

# 2. Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# 4. Make predictions
y_pred = model.predict(X_test)

# 5. Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

# Predict future stock price
future_date = datetime.strptime(end_date, "%Y-%m-%d") + timedelta(days=1)  # 30 days after end date
future_days = (future_date - data['Date'].min()).days
future_price = model.predict([[future_days]])  # Predict returns a NumPy array

# Extract the scalar value (first element of the array) using .item()
predicted_price = future_price.item()  # This will give us the scalar value

# Print the predicted stock price, ensuring it's formatted correctly
print(f"Predicted Stock Price on {future_date.strftime('%Y-%m-%d')}: {predicted_price:.2f}")

# Visualize the predicted stock price
plt.figure(figsize=(12, 6))
plt.scatter(X, y, color='blue', label='Actual Prices')
plt.plot(X, model.predict(X), color='red', label='Regression Line')
plt.scatter(future_days, predicted_price, color='green', label='Predicted Price')
plt.xlabel('Days Since Start Date')
plt.ylabel('Stock Price')
plt.title(f'Stock Price Prediction for {ticker}')
plt.legend()
plt.show()
