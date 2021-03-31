import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

#connecting to the main app.py file
from app import app

from app import server

#connecting app pages

from apps import vgames, sales

app.layout = html.Div([
    dcc.Location(id ='url', refresh = False, pathname = '',
    html.Div([
        dcc.Link('Video Games', href = '/apps/videogames'),
], className = 'row'),
    html.Div(id='page-content', children = [])
    
]))


@app.callback(Output('page-content', 'children')
            Input('url', 'pathname')])

def display_page(pathname):
    if pathname == '/apps/videogames':
        return videogames.layout()
    else:
        return "404 Page Error! Please choose a link"

if __name__ == '__main__':
    app.run_server(debug = False)


