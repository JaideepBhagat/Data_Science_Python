import plotly.express as px
# Load the Gapminder dataset
data = px.data.gapminder()
# Plot the pie chart
fig = px.pie(data, values='pop', names='continent', color='continent')
# Change the title of the plot
fig.update_layout(title_text='Gapminder Data')
# Change the background color of the plot
fig.update_layout(template='plotly_dark')
# Show the plot
fig.show()
