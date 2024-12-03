import plotly.express as px
# Load the Gapminder dataset
data = px.data.gapminder()
# Plot the box plot
fig = px.box(data, x='continent', y='lifeExp', color='continent')
# Change the title of the plot
fig.update_layout(title_text='Gapminder Data')
# Change the background color of the plot
fig.update_layout(template='plotly_dark')
# Show the plot
fig.show()