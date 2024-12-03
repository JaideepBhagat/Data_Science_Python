import plotly.express as px
# Load the Gapminder dataset
data = px.data.gapminder()
fig = px.scatter(data, x='gdpPercap', y='lifeExp', range_x=[100, 10000], color='continent', size='pop', animation_frame='year')
# Change the title of the plot
fig.update_layout(title_text='Gapminder Data', template = 'plotly_dark')
# Set the x-axis label
fig.update_xaxes(title_text='GDP Per Capita')
# Set the y-axis label
fig.update_yaxes(title_text='Life Expectancy')
# Show the plot
fig.show()
