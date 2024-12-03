# Combine multiple plots into a grid using make_subplots.
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# Load the Gapminder dataset
data = px.data.gapminder()

# Create subplots
fig = go.Figure()
fig.add_trace(go.Scatter(x=data['gdpPercap'], y=data['lifeExp'], mode='markers', name='Life Expectancy'))
fig.add_trace(go.Scatter(x=data['gdpPercap'], y=data['pop'], mode='markers', name='Population'))
fig.add_trace(go.Scatter(x=data['gdpPercap'], y=data['pop'], mode='markers', name='Population', text=data['country'], hovertemplate='%{text}<br>Population: %{y}'))
fig.add_trace(go.Scatter(x=data['gdpPercap'], y=data['lifeExp'], mode='markers', name='Life Expectancy', text=data['country'], hovertemplate='%{text}<br>Life Expectancy: %{y}'))

# Update layout
fig.update_layout(title_text='Gapminder Data', template = 'plotly_dark')
fig.update_layout(width=800, height=600, showlegend=True)
fig.update_layout(xaxis_title='GDP Per Capita', yaxis_title='Life Expectancy')
fig.show()