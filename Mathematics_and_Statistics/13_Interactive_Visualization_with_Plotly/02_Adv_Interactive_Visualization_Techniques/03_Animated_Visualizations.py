import plotly.express as px
data = px.data.gapminder()
fig = px.bar(data, x='continent', y='pop', color='continent', animation_frame='year')
fig.show()