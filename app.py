import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import numpy as np
import pandas as pd
import plotly.graph_objs as go


################################



df = pd.read_csv('movies.csv')

###################################

company_options = [dict(label=company, value=company) for company in df['company'].unique()]

country_options = [dict(label=country, value=country) for country in df['country'].unique()]

genre_options = [dict(label=genre, value=genre) for genre in df['genre'].unique()]

dropdown_country = dcc.Dropdown(
        id='country_drop',
        options=country_options,
        value=['USA']
        
    )

dropdown_company = dcc.Dropdown(
        id='company_drop',
        options=company_options,
        value='Paramount Pictures'
    )

dropdown_genre = dcc.Dropdown(
        id='genre_drop',
        options=genre_options,
        value='Comedy'    
    )
    
    
slider_year = dcc.Slider(
        id='year_slider',
        min=df['year'].min(),
        max=df['year'].max(),
        marks={str(i): '{}'.format(str(i)) for i in
               [1990, 1995, 2000, 2005, 2010, 2015]},
        value=df['year'].min(),
        step=1
    )
    
######################APP############################

app = dash.Dash(__name__)

server = app.server

app.layout = html.Div([

    html.H1('How is the movie industry doing?'),

    html.Label('Country Choice'),
    dropdown_country,

    html.Br(),

    html.Label('Genre Choice'),
    dropdown_genre,

    html.Br(),

    html.Label('Company Choice'),
    dropdown_company,

    html.Br(),

    html.Label('Year Slider'),
    slider_year,


     dcc.Graph(id='choropleth')

])

####################Callbacks#######################

@app.callback(
    [
         Output("choropleth", "figure")
        
    ],
    [
        Input("year_slider", "value"),
        Input("country_drop", "value"),
        Input("genre_drop", "value"),
        Input("company_drop","value")
  
    ]
)

def plots(year, countries):
############################################First Bar Plot##########################################################
    data_bar = []
    for country in countries:
        df_bar = df.loc[(df['country'] == country)]

        x_bar = df_bar['year']
        y_bar = df_bar['gross']

        data_bar.append(dict(type='bar', x=x_bar, y=y_bar, name=country))

    layout_bar = dict(title=dict(text='Emissions from 1990 until 2015'),
                      yaxis=dict(title='Emissions'),
                      paper_bgcolor='#f9f9f9'
                      )
     return go.Figure(data=data_bar, layout=layout_bar)

           


if __name__ == '__main__':
    app.run_server(debug=True)
