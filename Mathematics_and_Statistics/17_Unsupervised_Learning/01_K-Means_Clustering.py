import yfinance as yf  # Imports the yfinance library, which is used to download financial data, such as stock prices.
import pandas as pd  # Imports pandas, a powerful library for data manipulation and analysis.
import matplotlib.pyplot as plt  # Imports matplotlib.pyplot, a library used for creating static, animated, and interactive visualizations.
from dateutil.utils import today  # Imports the today() function from the dateutil library, which is used to get the current date.
from sklearn.cluster import KMeans  # Imports the KMeans clustering algorithm from scikit-learn, used for partitioning data into clusters.
from sklearn.metrics import silhouette_score  # Imports the silhouette_score, a metric to evaluate the quality of clustering.

# Download stock data
ticker = input("Enter the stock ticker symbol: ") + ".NS"  # Prompts the user to input a stock ticker symbol and appends .NS (indicating a stock from the National Stock Exchange of India).
start_date = today()-pd.Timedelta(days=365)  # Sets the start date to 1 year ago from the current date.
end_date = today()  # Sets the end date to the current date.
data = yf.download(ticker, start=start_date, end=end_date)  #  Downloads stock data for the specified ticker and date range using yfinance.

# Preprocess the data
data = data[['Close']]  # Extracts only the Close price column from the downloaded stock data.
data = data.dropna()  # Removes any rows with missing values to ensure clean data for clustering.

# Perform K-Means clustering
n_clusters = int(input("Enter the number of clusters: "))  # Prompts the user to input the desired number of clusters.
kmeans = KMeans(n_clusters=n_clusters, random_state=0)  # Initializes the K-Means clustering model with the specified number of clusters and a fixed random seed for reproducibility.
kmeans.fit(data)  # Fits the K-Means model to the Close price data, assigning data points to clusters.

# Calculate the silhouette score
labels = kmeans.labels_  # Extracts the labels assigned to each data point by the K-Means model
silhouette_avg = silhouette_score(data, labels)  # Calculates the silhouette score, which measures how well each data point is clustered. A higher score indicates better-defined clusters.

# Visualize the clusters
plt.scatter(data.index, data['Close'], c=labels, cmap='viridis')  # Creates a scatter plot of the closing prices (Close) over time, colored by their cluster labels.
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.title('K-Means Clustering')
plt.show()

# Print the silhouette score
print("Silhouette Score:", silhouette_avg)

# Print the cluster centers
print("Cluster Centers:", kmeans.cluster_centers_)

# Print the minimum and maximum closing price in each cluster
print("Minimum and Maximum Closing Price in Each Cluster:", data.groupby(labels)['Close'].agg(['min', 'max']))