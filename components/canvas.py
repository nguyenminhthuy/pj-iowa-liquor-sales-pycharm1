import dash_bootstrap_components as dbc
from dash import html, dcc

btn_filter = html.Span([html.I(className="fa fa-filter fa-lg"), " Filter Data"])

off_canvas = html.Div(
    [
        dbc.Button(children=btn_filter,
                   id="open-offcanvas-scrollable",
                   n_clicks=0, style=dict(fontSize="20px", backgroundColor="rgb(237, 201, 72)",
                                          textAlign="center", color="black", border="none")
                   ),
        dbc.Offcanvas([
                html.Div([
                        html.P("Item name"),
                        dcc.Dropdown(
                            ['New York City', 'Montreal', 'San Francisco'],
                            placeholder="Select...", multi=True
                        )], className="mb-3"),
                html.Div([
                        html.P("Store name"),
                        dcc.Dropdown(
                            ['New York City', 'Montreal', 'San Francisco'],
                            placeholder="Select...", multi=True
                        )], className="mb-3"),
                html.Div([
                        html.P("Category name"),
                        dcc.Dropdown(
                            ['New York City', 'Montreal', 'San Francisco'],
                            placeholder="Select...", multi=True
                        )], className="mb-3"),
                html.Div([
                        html.P("Vendor name"),
                        dcc.Dropdown(
                            ['New York City', 'Montreal', 'San Francisco'],
                            placeholder="Select...", multi=True
                        )], className="mb-3"),
                html.Div([
                        html.P("City name"),
                        dcc.Dropdown(
                            ['New York City', 'Montreal', 'San Francisco'],
                            placeholder="Select...", multi=True
                        )], className="mb-3"),
                html.Div([
                        html.P("County name"),
                        dcc.Dropdown(
                            ['New York City', 'Montreal', 'San Francisco'],
                            placeholder="Select...", multi=True
                        )], className="mb-3"),
                html.Div([
                        dbc.Button("SUBMIT",
                                   className='btn-search',
                                   style={
                                       'background-color': 'rgb(237, 201, 72)',
                                       'color': 'rgb(30, 51, 118)',
                                       'border': '0px', 'font-weight': 'bold'
                                   })
                     ], className="m-3 d-grid gap-2"),
            ],
            id="offcanvas-scrollable",
            scrollable=True,
            title="FILTER DATA",
            is_open=False,
        ),
    ]
)
