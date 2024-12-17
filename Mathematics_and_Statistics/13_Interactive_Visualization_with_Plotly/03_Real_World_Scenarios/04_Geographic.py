import pandas as pd
import plotly.graph_objects as go

# Load the dataset with appropriate adjustments
file_path = 'WHO-COVID-19-global-data.csv'  # Update with the correct path if needed
df = pd.read_csv(file_path, delimiter=',')  # Use appropriate delimiter

# Convert 'Date_reported' to datetime format
df['Date_reported'] = pd.to_datetime(df['Date_reported'], format='%d-%m-%Y')

# Aggregate the data for global trends (group by date for global new cases and deaths)
global_data = df.groupby('Date_reported').agg(
    total_new_cases=('New_cases', 'sum'),
    total_cumulative_cases=('Cumulative_cases', 'max'),
    total_new_deaths=('New_deaths', 'sum'),
    total_cumulative_deaths=('Cumulative_deaths', 'max')
).reset_index()

# Plot global trends of COVID-19 cases and deaths over time
fig = go.Figure()

# Plot New Cases
fig.add_trace(go.Scatter(x=global_data['Date_reported'],
                         y=global_data['total_new_cases'],
                         mode='lines',
                         name='New Cases'))

# Plot Cumulative Cases
fig.add_trace(go.Scatter(x=global_data['Date_reported'],
                         y=global_data['total_cumulative_cases'],
                         mode='lines',
                         name='Cumulative Cases'))

# Plot New Deaths
fig.add_trace(go.Scatter(x=global_data['Date_reported'],
                         y=global_data['total_new_deaths'],
                         mode='lines',
                         name='New Deaths'))

# Plot Cumulative Deaths
fig.add_trace(go.Scatter(x=global_data['Date_reported'],
                         y=global_data['total_cumulative_deaths'],
                         mode='lines',
                         name='Cumulative Deaths'))

# Update layout
fig.update_layout(
    title="Global COVID-19 Trends Over Time",
    xaxis_title="Date",
    yaxis_title="Count",
    template="plotly_dark"
)

fig.show()

# Now, create an interactive map showing the evolution of cases by country
# Filter the data for a specific date, for example, the latest date
latest_data = df[df['Date_reported'] == df['Date_reported'].max()]

# Create a choropleth map for new cases by country
import plotly.express as px

fig_map = px.choropleth(
    latest_data,
    locations="Country",
    locationmode="country names",
    color="New_cases",
    hover_name="Country",
    color_continuous_scale="Viridis",
    title="New COVID-19 Cases by Country (Latest Report)"
)

fig_map.update_geos(showcoastlines=True, coastlinecolor="Black")
fig_map.update_layout(
    geo=dict(showland=True, landcolor="lightgray"),
    template="plotly_dark"
)

fig_map.show()
