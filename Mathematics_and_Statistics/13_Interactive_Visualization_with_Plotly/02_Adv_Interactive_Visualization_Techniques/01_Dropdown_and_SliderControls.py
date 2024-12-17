import plotly.graph_objects as go  # Import plotly graph objects
import plotly.express as px  # Import plotly express
# Load sample dataset
data = px.data.gapminder()
# Create a list of unique countries for the dropdown
countries = data['country'].unique()
# Set the initial country
initial_country = 'India'
filtered_data = data[data['country'] == initial_country]
# Create the figure
fig = go.Figure()
# Add scatter trace for the initial country
fig.add_trace(  # Add scatter trace
    go.Scatter(  # Create a scatter plot
        x=filtered_data['year'],  # x-axis values
        y=filtered_data['lifeExp'], # y-axis values
        mode='lines+markers',  # Set mode to lines+markers
        name=initial_country))  # Set the name of the trace
# Update layout to include dropdown and slider
fig.update_layout(  # Update layout
    updatemenus=[  # Add updatemenus
        dict(  # Create a dropdown menu
            buttons=[  # Add buttons
                dict(label=country,  # Set label
                     method="update",  # Set method
                     args=[
                         {"x": [data[data['country'] == country]['year']],  # Set x-axis values
                          "y": [data[data['country'] == country]['lifeExp']],  # Set y-axis values
                          "name": country}  # Set name
                     ])
                for country in countries  # Iterate over unique countries
            ],
            direction="down",  # Set direction.
            showactive=True,  # Set showactive. The purpose of this is to highlight the active menu item
            x=0.5,  # Set x
            y=1.15,  # Set y
            active=countries.tolist().index(initial_country),  # Set the active menu item
        )
    ],
    sliders=[  # Add slider
        dict(  # Create a slider
            steps=[  # Add steps
                dict(label=str(year),  # Set label
                     method="update",  # Set method. The purpose of this is to update the figure
                     args=[
                         {"x": [data[(data['country'] == initial_country) & (data['year'] <= year)]['year']],  # Set x-axis values
                          "y": [data[(data['country'] == initial_country) & (data['year'] <= year)]['lifeExp']]}  #
                     ])
                for year in sorted(data['year'].unique())  # Iterate over unique years
            ],
            active=len(data['year'].unique()) - 1,  # Set the active slider
            x=0.1,  # Set x
            y=-0.2,  # Set y
            currentvalue={"prefix": "Year: "}  # Set current value
        )
    ],
    title="Life Expectancy with Dropdown and Slider",
    xaxis_title="Year",
    yaxis_title="Life Expectancy"
)

fig.add_annotation(x=2007, y=75, text="Global Trend", showarrow=True)
# Show the figure
fig.show()