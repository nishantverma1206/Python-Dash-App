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
sales_list = ["North American Sales", "EU Sales", "Japan Sales", "Other Sales",	"World Sales"]

from app import app
#change background and color text
colors = {
    'background': '#fdfffc',
    'text': '#1c1cbd'
    }

layout = html.Div(style={'backgroundColor': colors['background']},children=[
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("Top Games and Publishers!",        
             style={
            'textAlign': 'center',
            'color': colors['text']}), 
            className="mb-5 mt-5")
        ]),
        html.Div([
            html.Div(dcc.Dropdown(
                id='genre-dropdown', value='Strategy', clearable=False,
                options=[{'label': x, 'value': x} for x in sorted(df.Genre.unique())]
            ), className='six columns'),
    
            html.Div(dcc.Dropdown(
                id='sales-dropdown', value='EU Sales', clearable=False,
                persistence=True, persistence_type='memory',
                options=[{'label': x, 'value': x} for x in sales_list]
            ), className='six columns'),
        ], className='row'),

    dcc.Graph(id='my-bar'),
    dcc.Graph(id='my-bar2')
])
    ])

@app.callback(
    [Output(component_id='my-bar', component_property='figure'),
    Output(component_id='my-bar2', component_property='figure')],
    [Input(component_id='genre-dropdown', component_property='value'),
     Input(component_id='sales-dropdown', component_property='value')]
)
def display_value(genre_chosen, sales_chosen):
    df_fltrd = df[df['Genre'] == genre_chosen]
    df_fltrd = df_fltrd.nlargest(10, sales_chosen)
    fig_1 = px.bar(df_fltrd, x='Video Game', y=sales_chosen, color='Platform')
    fig_1 = fig_1.update_yaxes(tickprefix="$", ticksuffix="M")
    
    fig_2 = px.bar(df_fltrd, x='Publisher', y=sales_chosen, color='Platform')
    fig_2 = fig_2.update_yaxes(tickprefix="$", ticksuffix="M")
    return [fig_1,fig_2]
    