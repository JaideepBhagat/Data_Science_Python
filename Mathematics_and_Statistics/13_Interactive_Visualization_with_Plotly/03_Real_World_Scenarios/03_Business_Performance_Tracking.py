import pandas as pd
import plotly.express as px

# Load the dataset
file_path = "Sales.csv"  # Replace with the path to your dataset
data = pd.read_csv(file_path)

# Convert "Order Date" to datetime
data["Order Date"] = pd.to_datetime(data["Order Date"], errors="coerce")

# Drop rows with invalid or missing dates
data = data.dropna(subset=["Order Date"])

# Ensure proper date parsing and create "Order Month"
data["Order Month"] = data["Order Date"].dt.to_period("M").astype(str)

# Analyze Churn Rate (New vs. Repeat Customers)
# A repeat customer is defined as someone with more than one order in different months
customer_first_order = data.groupby("Customer ID")["Order Date"].min().reset_index()
customer_first_order.columns = ["Customer ID", "First Purchase Date"]

data = data.merge(customer_first_order, on="Customer ID", how="left")
data["Is New Customer"] = data["Order Date"] == data["First Purchase Date"]



churn_data = (
    data.groupby(["Order Month", "Is New Customer"])["Customer ID"].nunique().reset_index()
    )
churn_data.columns = ["Month", "Is New Customer", "Customer Count"]

fig2 = px.bar(
    churn_data,
    x="Month",
    y="Customer Count",
    color="Is New Customer",
    title="Customer Churn Analysis (New vs. Repeat)",
    barmode="group",
    labels={"Month": "Month", "Customer Count": "Number of Customers"},
    color_discrete_map={True: "green", False: "orange"},
)
fig2.show()