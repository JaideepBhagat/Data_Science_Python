import kagglehub
import pandas as pd
import plotly.express as px

# Download the dataset
path = kagglehub.dataset_download("beridzeg45/food-nutritional-facts")
dataset_file = f"{path}/foodstruct_nutritional_facts.csv"

# Load the dataset
data = pd.read_csv(dataset_file)

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
fig = px.imshow(  # Create a heatmap of correlations using plotly express
    correlation_matrix,
    labels=dict(x="Nutrients/Indices", y="Nutrients/Indices", color="Correlation"),
    x=columns_of_interest,
    y=columns_of_interest,
    color_continuous_scale="RdYlGn",
    title="Correlation Matrix of Nutrients and Health Indices",
)

fig.show()