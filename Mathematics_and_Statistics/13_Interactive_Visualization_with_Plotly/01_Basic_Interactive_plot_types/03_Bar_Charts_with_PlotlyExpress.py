import plotly.express as px
# Load the Gapminder dataset
data = px.data.gapminder()
fig = px.bar(data, x='continent', y='pop', color='continent', animation_frame='year')
# Change the title of the plot
fig.update_layout(title_text='Gapminder Data')
# Set the x-axis label
fig.update_xaxes(title_text='Continent')
# Set the y-axis label
fig.update_yaxes(title_text='Population')
# Change the background color of the plot
fig.update_layout(template='plotly_white')
# Show the plot
fig.show()