import kagglehub
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Download the dataset
path = kagglehub.dataset_download("beridzeg45/food-nutritional-facts")
dataset_file = f"{path}/foodstruct_nutritional_facts.csv"

# Load the dataset
data = pd.read_csv(dataset_file)

# Inspect the dataset structure
print(data.head())
print(data.info())

# Select specific nutrients and health indices for analysis
columns_of_interest = [
    'Protein', 'Sugar', 'Calories', 'Fats', 'Fiber',
    'Vitamin C', 'Sodium', 'Iron', 'Potassium', 'Calcium'
]
filtered_data = data[columns_of_interest]

# Drop rows with missing values
filtered_data = filtered_data.dropna()

# Compute correlation matrix
correlation_matrix = filtered_data.corr()

# Heatmap of correlations
fig = px.imshow(
    correlation_matrix,
    labels=dict(x="Nutrients/Indices", y="Nutrients/Indices", color="Correlation"),
    x=columns_of_interest,
    y=columns_of_interest,
    color_continuous_scale="RdBu",
    title="Correlation Matrix of Nutrients and Health Indices",
)
fig.update_layout(height=600, width=600)
fig.show()