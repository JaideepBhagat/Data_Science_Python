import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from dateutil.utils import today
from sklearn.cluster import KMeans  #  Imports the KMeans clustering algorithm from scikit-learn, used for partitioning data into clusters.

# Download stock data (assuming user input remains the same)
ticker = input("Enter the stock ticker symbol: ") + ".NS"
start_date = today()-pd.Timedelta(days=365)
end_date = today()
data = yf.download(ticker, start=start_date, end=end_date)

# Preprocess the data
data = data[['Close']]
data = data.dropna()

# Define a function to calculate WCSS (Within-Cluster Sum of Squares)
def calculate_wcss(data, k):
    kmeans = KMeans(n_clusters=k, random_state=0)  # Initializes a K-Means clustering model with k clusters and a fixed random state for reproducibility.
    kmeans.fit(data)  # Fits the K-Means model to the Close price data.
    return kmeans.inertia_  #  Returns the WCSS, which measures the sum of squared distances between data points and their cluster centroids. Lower WCSS indicates better clustering.

# Apply elbow method to find optimal k
wcss_list = []  # Initializes an empty list to store WCSS values for different numbers of clusters.
k_range = range(1, 10)  # Sets the range of cluster counts (k) to test. Here, k ranges from 1 to 9.

for k in k_range:  # Iterates over each value of k in the specified range and:
    wcss_list.append(calculate_wcss(data, k))  # Calculates WCSS for the current value of k and appends it to the wcss_list.
    # Also Appends the WCSS value to the wcss_list.

# Plots the number of clusters (k) on the x-axis and the corresponding WCSS on the y-axis.
plt.plot(k_range, wcss_list, marker='o', linestyle='-') # marker='o': Marks each data point with a circle., linestyle='-': Connects the points with a line.
plt.xlabel('Number of clusters (k)')
plt.ylabel('WCSS')
plt.title('Elbow Method for K-Means Clustering')
plt.show()