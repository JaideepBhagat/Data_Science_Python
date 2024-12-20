# Create a model to predict house prices based on size and number of rooms.
# Import necessary libraries
import pandas as pd         # For data manipulation and analysis
from sklearn.model_selection import train_test_split  # To split data into training and testing sets
from sklearn.linear_model import LinearRegression    # The linear regression model
from sklearn.metrics import mean_squared_error       # To evaluate model performance

# Load the dataset
data = {
    'Size (sq ft)': [750, 800, 850, 900, 1000, 1100],    # House sizes in square feet
    'Rooms': [2, 2, 3, 3, 4, 4],                         # Number of rooms in each house
    'Price (in Lakhs)': [50, 60, 70, 80, 100, 120]       # House prices in Lakhs
}

# Create DataFrame
df = pd.DataFrame(data)

# Define Features and Labels
# Features (input) - Size and Rooms
X = df[['Size (sq ft)', 'Rooms']]

# Labels (output) - Price
y = df['Price (in Lakhs)']

# Split the data into training and testing sets
# 80% for training, 20% for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Linear Regression model
# Create the model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions
# Predict house prices for the test set
predictions = model.predict(X_test)

# Compare predictions with actual values
print("Actual Prices:", list(y_test))
print("Predicted Prices:", list(predictions))

# Evaluate the model
mse = mean_squared_error(y_test, predictions)
print("Mean Squared Error:", mse)

# Make predictions for a new house
new_house = pd.DataFrame({'Size (sq ft)': [1500], 'Rooms': [5]})
predicted_price = model.predict(new_house)
print("Predicted Price for a new house:", predicted_price[0])