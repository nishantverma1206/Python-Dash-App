#import packages to create app
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

import plotly.express as px
import pandas as pd
import numpy as np
import pathlib

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

df = pd.read_csv(DATA_PATH.joinpath("dash_ca.csv"))

sales_list = ["North American Sales", "EU Sales", "Japan Sales", "Other Sales",	"World Sales"]

# needed only if running this as part of a multipage app
from app import app
#app = dash.Dash(__name__)
#change background and color text
colors = {
    'background': '#fdfffc',
    'text': '#1c1cbd'
}



# change to app.layout if running as single page app instead
layout = html.Div(style={'backgroundColor': colors['background']},children=[
    html.H1('Video Games Sales across the Globe',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    
    html.Div([
        html.Div([
            html.Label('Select Sale Zones'),
            dcc.Dropdown(id='cont_dropdown', value='World Sales',
                        options=[{'label': x, 'value': x} for x in sales_list],
                        multi=False
            )
        ],style={'width': '99%', 'display': 'inline-block'}),
    
    html.Div([
        html.Div([
            dcc.Graph(
                id='fig_1'
            )
        ],style={'width': '49%', 'display': 'inline-block'}),
        html.Div([
            dcc.Graph(
                id='fig_2',
            )
        ],style={'width': '49%', 'float': 'right', 'display': 'inline-block'}),
    ])

])
    ])
@app.callback(
    [Output(component_id='fig_1', component_property='figure'),
     Output(component_id='fig_2', component_property='figure')],
    [Input(component_id='cont_dropdown', component_property='value')]
)

def update_graph(selected_cont):
    if not selected_cont:
        return dash.no_update
    
    fig_1_bar = px.bar(data_frame=df, 
             x='Platform', 
             y= selected_cont, 
             title='Sales by Platform',
              color='Genre')

    fig_2_pie = px.pie(data_frame = df, values=selected_cont ,names='Genre',
            title='Sales by Genre', hover_data=['Genre'],
            hole = 0.2)

    return [fig_1_bar,fig_2_pie]





# needed only if running this as a single page app
#if __name__ == '__main__':
#    app.run_server(port=8097,debug=True)
