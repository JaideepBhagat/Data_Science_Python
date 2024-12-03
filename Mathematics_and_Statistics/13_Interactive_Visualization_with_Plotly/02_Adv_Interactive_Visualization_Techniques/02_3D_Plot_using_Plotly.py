import plotly.express as px

data = px.data.gapminder()
fig = px.scatter_3d(data, x='gdpPercap', y='lifeExp', z='pop', color='continent')
fig.show()
