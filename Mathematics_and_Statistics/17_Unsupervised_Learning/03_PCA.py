# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split  # For train-test split
from sklearn.decomposition import PCA  # For PCA
from sklearn.preprocessing import StandardScaler  # For standardization
from sklearn.linear_model import LinearRegression  # For linear regression
from sklearn.metrics import mean_squared_error, r2_score  # For evaluation

# Generate a sample dataset
data = {
    'Area': [2000, 1500, 1800, 2400, 3000, 1200, 1600, 1900, 2200, 2500],
    'Bedrooms': [3, 2, 3, 4, 5, 2, 3, 3, 4, 4],
    'Bathrooms': [2, 1, 2, 3, 3, 1, 2, 2, 3, 3],
    'Garage Size': [2, 1, 2, 2, 3, 1, 2, 2, 2, 3],
    'Year Built': [2000, 1995, 2005, 2010, 2020, 1990, 2000, 2005, 2015, 2018],
    'Lot Size': [5000, 4000, 4500, 6000, 8000, 3500, 4000, 4500, 7000, 7500],
    'Price': [400000, 300000, 350000, 500000, 700000, 250000, 320000, 360000, 600000, 650000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Split features and target variable
X = df.drop('Price', axis=1)  # Features
y = df['Price']               # Target variable

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply PCA to reduce dimensions
pca = PCA(n_components=2)  # Reduce to 2 principal components
X_pca = pca.fit_transform(X_scaled)

# Print explained variance ratio
print("Explained Variance Ratios:", pca.explained_variance_ratio_)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_pca, y, test_size=0.2, random_state=42)

# Train a Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on test data
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("R-Squared:", r2)

# Visualize PCA results
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 6))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='viridis', s=100)
plt.colorbar(label='House Prices')
plt.title('PCA Applied to House Data')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.show()

# New House Prediction
# Define the new house features
new_house = {
    'Area': 2000,
    'Bedrooms': 3,
    'Bathrooms': 2,
    'Garage Size': 2,
    'Year Built': 2010,
    'Lot Size': 5000
}

# Convert to DataFrame
new_house_df = pd.DataFrame([new_house])

# Standardize the features
new_house_scaled = scaler.transform(new_house_df)

# Apply PCA transformation
new_house_pca = pca.transform(new_house_scaled)

# Predict the price
predicted_price = model.predict(new_house_pca)
print(f"Predicted Price: ${predicted_price[0]:,.2f}")