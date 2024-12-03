import plotly.express as px
# Load the Gapminder dataset
data = px.data.gapminder()
fig = px.line(data, x='year', y='lifeExp', color='continent', line_group='country')
# Change the title of the plot
fig.update_layout(title_text='Line Chart of Life Expectancy over Time')
# Set the x-axis label
fig.update_xaxes(title_text='Year')
# Set the y-axis label
fig.update_yaxes(title_text='Life Expectancy')
# Show the plot
fig.show()