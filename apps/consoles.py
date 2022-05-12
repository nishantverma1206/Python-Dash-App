#import packages to create app
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output


import plotly.express as px
import pandas as pd
import numpy as np
import pathlib

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

df = pd.read_csv(DATA_PATH.joinpath("dash_ca.csv"))


from app import app
#app = dash.Dash(__name__)
#change background and color text
colors = {
    #background to rgb(233, 238, 245)
    'background': '#fdfffc',
    'text': '#1c1cbd'
}

fig_2 = px.histogram(df, x="Platform",color="Genre", title='Games by platform')
fig_2.update_layout(yaxis_title="Number of Games")

fig_3 = px.histogram(df, x="Genre",title='Games by Genre')
fig_3.update_layout(yaxis_title="Number of Games")


# change to app.layout if running as single page app instead
layout = html.Div(style={'backgroundColor': colors['background']},children=[
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("Games and Consoles",        
             style={
            'textAlign': 'center',
            'color': colors['text']}), 
            className="mb-5 mt-5")
        ]),
        
        html.Div([
            dcc.Graph(
                id='fig_2',
                figure=fig_2
            ),
            ],style={'width': '100%','display': 'inline-block'}),
        html.Div([
            html.Div([
                dcc.Graph(
                        id='fig_3',
                        figure=fig_3
                ),
            ],style={'width': '100%', 'display': 'inline-block'}),
            
            ])
    ])
])

