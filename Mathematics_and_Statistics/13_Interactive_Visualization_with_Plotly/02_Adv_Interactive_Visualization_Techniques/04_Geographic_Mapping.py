import plotly.express as px
data = px.data.gapminder()
fig = px.choropleth(data, locations='iso_alpha', color='pop', hover_name='country',
                    animation_frame='year' , title='Population by Country')
fig.show()