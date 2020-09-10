#Runs the server and opens the browser to view the dashboard

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
    html.H1(children='GAD7 Results Patient Dashboard'),

    html.Div(children='''
        When screening for anxiety disorders, a recommended threshold for further clinical evaluation is a score of 10 or greater. 
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
        )
    ])
    webbrowser.open_new("http://localhost:{}".format(port))
    app.run_server(debug=True,port=port)
    
