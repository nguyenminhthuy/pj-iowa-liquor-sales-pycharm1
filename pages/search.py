import dash_bootstrap_components as dbc
from dash import html, dcc

from components import cards_search

tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'fontWeight': 'bold'
}

tab_selected_style = {
    'borderTop': '3px solid #BF00BF',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': 'white',
    'color': 'black',
}

layout = html.Div([
    html.Img(id="backtotop"),
    dbc.Row([
        dbc.Col(
            html.Div([
                html.P("Year"),
                dcc.Dropdown(
                    ['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022'],
                    placeholder="Select...", multi=True
                )])
        ),
        dbc.Col(
            html.Div([
                html.P("Item name"),
                dcc.Dropdown(
                    ['New York City', 'Montreal', 'San Francisco'],
                    placeholder="Select...", multi=True
                )]),
        ),
        dbc.Col(
            html.Div([
                html.P("Store name"),
                dcc.Dropdown(
                    ['New York City', 'Montreal', 'San Francisco'],
                    placeholder="Select...", multi=True
                )])
        ),
        dbc.Col(
            html.Div([
                html.P("Category name"),
                dcc.Dropdown(
                    ['New York City', 'Montreal', 'San Francisco'],
                    placeholder="Select...", multi=True
                )])
        ),
        dbc.Col(
            html.Div([
                html.P("Vendor name"),
                dcc.Dropdown(
                    ['New York City', 'Montreal', 'San Francisco'],
                    placeholder="Select...", multi=True
                )]),
        ),
        dbc.Col(
            html.Div([
                # html.P(),
                dbc.Button("SUBMIT",
                           className='btn-search p-3',
                           style={
                               'background-color': 'rgb(237, 201, 72)',
                               'color': 'rgb(30, 51, 118)',
                               'border': '0px', 'font-weight': 'bold'
                           })
            ], className="mt-3 d-grid gap-2"),
        ),
    ], className="m-2"),

    dbc.Row(
        [
            html.H4("Result:", style={"color": "#FF7F50"}),
            dbc.Col(dbc.Card(cards_search.sale, color="info", outline=True, className="shadow")),
            dbc.Col(dbc.Card(cards_search.cost_sales, color="info", outline=True, className="shadow")),
            dbc.Col(dbc.Card(cards_search.gross_profit, color="info", outline=True, className="shadow")),
            dbc.Col(dbc.Card(cards_search.inv, color="info", outline=True, className="shadow")),
            dbc.Col(dbc.Card(cards_search.bottleSold, color="info", outline=True, className="shadow")),
            dbc.Col(dbc.Card(cards_search.volumeSold, color="info", outline=True, className="shadow"))
        ], className="m-4",
    ),

    dbc.Row(
        [
            dbc.Col(cards_search.month_graph, className="text-center border-end m-3"),
            dbc.Col(cards_search.dow_graph, className="text-center border-end m-3"),
        ], className="m-4",
    ),

    html.Div(
        dbc.Row([
                dbc.Col(html.H4("SALES ANALYSIS", style={"color": "#FF7F50"})),
            ], className="m-5"
        )
    ),

    html.Div(
        dbc.Row([
            dbc.Col([
                dcc.Tabs([
                    dcc.Tab(label='TOP 10 ITEMS', children=[
                        dbc.Row([
                            dbc.Badge("Success", color="success", className="me-1"),
                            dbc.Col(cards_search.top_highestItem_graph, className="m-4"),
                            dbc.Col(cards_search.top_mostItem_graph, className="m-3"),
                        ])
                    ], style=tab_style, selected_style=tab_selected_style),

                    dcc.Tab(label='TOP 10 CATEGORIES', children=[
                        dbc.Row([
                            dbc.Col(cards_search.top_highestCat_graph, className="m-4"),
                            dbc.Col(cards_search.top_mostCat_graph, className="m-4"),
                        ])
                    ], style=tab_style, selected_style=tab_selected_style),

                    dcc.Tab(label='TOP 10 VENDORS', children=[
                        dbc.Row([
                            dbc.Col(cards_search.top_highestVendor_graph, className="m-4"),
                            dbc.Col(cards_search.top_mostVendor_graph, className="m-4"),
                        ])
                    ], style=tab_style, selected_style=tab_selected_style),

                    dcc.Tab(label='TOP 10 STORES', children=[
                        dbc.Row([
                            dbc.Col(cards_search.top_highestStore_graph, className="m-4"),
                            dbc.Col(cards_search.top_mostStore_graph, className="m-4"),
                        ])
                    ], style=tab_style, selected_style=tab_selected_style),
                ])
            ])
        ], className="m-5"
        )
    ),

    dbc.Row(
        [
            html.H3("STORE LOCATION", style={"color": "#FF7F50"}),
            html.Div(id='folium-map-rs')
        ], className="m-5",
    ),

        dbc.Button(children=html.Span([html.I(className="fa fa-arrow-up fa-lg")]),
               href="#backtotop",n_clicks=0,
               style=dict(fontSize="35px", backgroundColor="rgb(237, 201, 72)",
                          textAlign="right", color="rgb(30, 51, 118)", border="none",
                          marginLeft = "90%")),

])
