from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State

import dash_bootstrap_components as dbc


from app import server
from app import app
# import all pages in the app
from apps import sales ,consoles, tops


dropdown = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem("Sales", href="/sales"),
        dbc.DropdownMenuItem("Games & Consoles", href="/consoles"),
        dbc.DropdownMenuItem("Tops!", href="/tops"),
    ],
    nav = True,
    in_navbar = True,
    label = "Explore Pages",
)

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src="/assets/console1.jpg", height="130px")),
                        dbc.Col(dbc.NavbarBrand("Video Games Dashboard", className="ml-2")),
                    ],
                    align="center",
                ),
                href="/sales",
            ),
            dbc.NavbarToggler(id="navbar-toggler2"),
            dbc.Collapse(
                dbc.Nav(
                    # right align dropdown menu with ml-auto className
                    [dropdown], className="ml-auto", navbar=True
                ),
                id="navbar-collapse2",
                navbar=True,
            ),
        ]
    ),
    color="dark",
    dark=True,
    className="mb-4",
)

def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

for i in [2]:
    app.callback(
        Output(f"navbar-collapse{i}", "is_open"),
        [Input(f"navbar-toggler{i}", "n_clicks")],
        [State(f"navbar-collapse{i}", "is_open")],
    )(toggle_navbar_collapse)

# embedding the navigation bar
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/tops':
        return tops.layout
    elif pathname == '/consoles':
        return consoles.layout
    else:
        return sales.layout

if __name__ == '__main__':
    app.run_server(port = 8079, debug=True)