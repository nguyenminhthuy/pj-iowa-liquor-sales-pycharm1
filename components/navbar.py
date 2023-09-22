import dash_bootstrap_components as dbc
from PIL import Image
from dash import html, dcc, Output, Input, callback
from components import canvas

year_dict = {1: '2012', 2: '2013', 3: '2014',
             4: '2015', 5: '2016', 6: '2017',
             7: '2018', 8: '2019', 9: '2020',
             10: '2021', 11: '2022'}

# Header
header = dbc.Navbar(
    dbc.Container([
        dbc.Row([
            dbc.Col(
                html.Img(
                    id="logo",
                    src=Image.open("img/logo.png"),
                    height="60px",
                ),
                md="auto",
            ),

            dbc.Col([
                html.Div(
                    [
                        html.H3("IOWA LIQUOR SALES"),
                        html.P("Based on sales 2012-2022"),
                    ],
                    id="app-title",
                )
            ], md=True, align="center",
            ),

        ],
            align="center",
        ),

        dbc.Row([
            dbc.Col([
                html.Div(dcc.Store(id='store_y', storage_type='session')),
                dcc.Dropdown(
                    id='year-dropdown',
                    options=[
                        {'label': dcc.Link(children=v, href="/details",
                                           style={"text-decoration": "none", "color": "black"}),
                         'value': k} for k, v in year_dict.items()
                    ], style={"width": "200px"}, clearable=True),
            ]),

            dbc.Col(
                dbc.Button(children=[html.I(className="fa fa-home fa-lg")],
                           href="/",
                           style=dict(fontSize="20px", backgroundColor="rgb(237, 201, 72)",
                                      textAlign="center", color="black", border="none")
                           ), md="auto",
            ),

            dbc.Col(canvas.off_canvas,
                    md="auto")  # Filter data functions
        ], align="center"),
    ], className='m-2', fluid=True
    ),
    # dark=True,
    color="rgb(30 51 118)",
    sticky="top",
)


@callback(
    Output('store_y', 'data'),
    Input(component_id='year-dropdown', component_property='value'),
)
def update_text(chosen_val):  # the function argument comes from the component property of the Input
    return chosen_val
