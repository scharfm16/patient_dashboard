# -*- coding: utf-8 -*-

# Run this app with `python app.py` and

import dash
import dash_core_components as dcc
import dash_html_components as html
import webbrowser

def run_server(fig, port=8050):

    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

    colors = {
    'background': '#111111',
    'text': '#7FDBFF'
    }


    app.layout = html.Div(children=[
    html.H1(children='Patient Dashboard'),

    html.Div(children='''
        A Dashboard for displaying patient GAD7 results over time
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
        )
    ])
    
    webbrowser.open_new("http://localhost:{}".format(port))
    app.run_server(debug=True,port=port)