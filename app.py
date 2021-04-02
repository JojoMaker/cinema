import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import numpy as np
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import plotly.io as pio
from plotly.colors import n_colors
from plotly.subplots import make_subplots


################################

#path = 'https://raw.githubusercontent.com/JojoMaker/Cinema/datasets/'

#df = pd.read_csv(path + 'movies.csv')

df = pd.read_csv('movies.csv', encoding = "ISO-8859-1")

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
    
###################### APP ############################

app = dash.Dash(__name__)

server = app.server

app.layout = html.Div([html.H1('How is the Movie Industry doing?' ,style={"text-align":"center"}),
                       
                       html.Label('Country Choice'),dropdown_country,
                       
                       html.Br(),
                       
                       html.Label('Genre Choice'),dropdown_genre,
                       
                       html.Br(),
                       
                       html.Label('Company Choice'),dropdown_company,
                       
                       html.Br(),
                       
                       html.Label('Year Slider'),slider_year,
                       
                       dcc.Graph(id='line_graph')                      
                       
                      ])

####################Callbacks#######################

@app.callback(
    [Output('line_graph', 'figure')
    ],
    [Input("year_slider", "value"),
     Input("country_drop", "value"),
     Input("genre_drop", "value"),
     Input("company_drop", "value")]
)
def plots(country, genre):
    df.columns = df.columns.str.capitalize()
    revenue_df = df.loc[(df.Country == country) & (df.Genre == genre)].groupby(by = ['Year'])['Gross','Budget'].sum()
    return px.line(revenue_df, x=revenue_df.index, y=revenue_df.columns, title = 'Which Country has the highest revenue by 			 category?',
                   labels=dict(x="Year", y= 'Amount of $ in billions'))


#Run App
if __name__ == '__main__': 
    app.run_server(debug=False)
