import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Dataset 'Processing'

df = pd.read_csv('movies.csv')

# Building our Graphs (nothing new here)

df_2 = df.loc[df['year']==2000]
data_choropleth = dict(type='choropleth',
                       locations=df_2['country'],  #There are three ways to 'merge' your data with the data pre embedded in the map
                       locationmode='country names',
                       z=df_2['gross'],
                       text=df_2['country'],
                       colorscale='inferno',
                       colorbar=dict(title='Gross')
                      )

layout_choropleth = dict(geo=dict(scope='world',  #default
                                  projection=dict(type='orthographic'
                                                 ),
                                  #showland=True,   # default = True
                                  landcolor='black',
                                  lakecolor='white',
                                  showocean=True,   # default = False
                                  oceancolor='azure'
                                 ),
                         
                         title=dict(text='World Choropleth Map',
                                    x=.5 # Title relative position according to the xaxis, range (0,1)
                                   )
                        )

fig = go.Figure(data=data_choropleth, layout=layout_choropleth)



# The App itself

app = dash.Dash(__name__)

server = app.server




app.layout = html.Div(children=[
    html.H1(children='Movies'),

    html.Div(children='''
        Example of html Container
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])




if __name__ == '__main__':
    app.run_server(debug=True)
