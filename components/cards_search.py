import dash_bootstrap_components as dbc
from dash import html, callback, Output, Input, dcc
import plotly.graph_objs as go

sale = [
    dbc.CardHeader(html.H6("SALES", className="text-center")),
    dbc.CardBody([
        dbc.Row(html.H3("100,000",
                        className="card-title text-center",
                        style={"color": "#FF1493"})),
        dbc.Row([
            dbc.Col([
                html.P("Previous", className="text-center"),
                html.H5("100,000", id="card_sales_previous", className="text-center",
                        style={"color": "#1E90FF"})
            ]),
            dbc.Col([
                html.P("Different", className="text-center"),
                html.H5("100,000", id="card_sales_diff", className="text-center",
                        style={"color": "#1E90FF"})
            ]),
        ])
    ])
]

cost_sales = [
    dbc.CardHeader(html.H6("COST", className="text-center")),
    dbc.CardBody([
        dbc.Row(html.H3("100,000",
                        className="card-title text-center",
                        style={"color": "#FF1493"})),
        dbc.Row([
            dbc.Col([
                html.P("Previous", className="text-center"),
                html.H5("100,000", id="card_cost_previous", className="text-center",
                        style={"color": "#1E90FF"})
            ]),
            dbc.Col([
                html.P("Different", className="text-center"),
                html.H5("100,000", id="card_cost_diff", className="text-center",
                        style={"color": "#1E90FF"})
            ]),
        ])
    ])
]

gross_profit = [
    dbc.CardHeader(html.H6("GROSS PROFIT", className="text-center")),
    dbc.CardBody([
        dbc.Row(html.H3("100,000",
                        className="card-title text-center",
                        style={"color": "#FF1493"})),
        dbc.Row([
            dbc.Col([
                html.P("Previous", className="text-center"),
                html.H5("100,000", id="card_profit_previous", className="text-center",
                        style={"color": "#1E90FF"})
            ]),
            dbc.Col([
                html.P("Different", className="text-center"),
                html.H5("100,000", id="card_profit_diff", className="text-center",
                        style={"color": "#1E90FF"})
            ]),
        ])
    ])
]

inv = [
    dbc.CardHeader(html.H6("NUMBER OF INVOICES", className="text-center")),
    dbc.CardBody([
        dbc.Row(html.H3("100,000",
                        className="card-title text-center",
                        style={"color": "#FF1493"})),
        dbc.Row([
            dbc.Col([
                html.P("Previous", className="text-center"),
                html.H5("100,000", id="card_inv_previous", className="text-center",
                        style={"color": "#1E90FF"})
            ]),
            dbc.Col([
                html.P("Different", className="text-center"),
                html.H5("100,000", id="card_inv_diff", className="text-center",
                        style={"color": "#1E90FF"})
            ]),
        ])
    ])
]

bottleSold = [
    dbc.CardHeader(html.H6("BOTTLE SOLD", className="text-center")),
    dbc.CardBody([
        dbc.Row(html.H3("100,000",
                        className="card-title text-center",
                        style={"color": "#FF1493"})),
        dbc.Row([
            dbc.Col([
                html.P("Previous", className="text-center"),
                html.H5("100,000", id="card_bottle_previous", className="text-center",
                        style={"color": "#1E90FF"})
            ]),
            dbc.Col([
                html.P("Different", className="text-center"),
                html.H5("100,000", id="card_bottle_diff", className="text-center",
                        style={"color": "#1E90FF"})
            ]),
        ])
    ])
]

volumeSold = [
    dbc.CardHeader(html.H6("VOLUME SOLD", className="text-center")),
    dbc.CardBody([
        dbc.Row(html.H3("100,000",
                        className="card-title text-center",
                        style={"color": "#FF1493"})),
        dbc.Row([
            dbc.Col([
                html.P("Previous", className="text-center"),
                html.H5("100,000", id="card_volume_previous", className="text-center",
                        style={"color": "#1E90FF"})
            ]),
            dbc.Col([
                html.P("Different", className="text-center"),
                html.H5("100,000", id="card_volume_diff", className="text-center",
                        style={"color": "#1E90FF"})
            ]),
        ])
    ])
]
# -------------------------------------------------
fig = go.Figure(data=[go.Scatter(x=[1, 2, 3], y=[4, 1, 2])])
month_graph = ([
    html.Div([
        dcc.Graph(figure=fig)
    ])
])

dow_graph = ([
    html.Div([
        dcc.Graph(figure=fig)
    ])
])

# -------------------------------------------------
top_highestItem_graph = ([
    html.Div(dcc.Graph(figure=fig))
])

top_mostItem_graph = ([
    html.Div(dcc.Graph(figure=fig))
])

# -------------------------------------------------
top_highestCat_graph = ([
    html.Div(dcc.Graph(figure=fig))
])

top_mostCat_graph = ([
    html.Div(dcc.Graph(figure=fig))
])

# -------------------------------------------------
top_highestVendor_graph = ([
    html.Div(dcc.Graph(figure=fig))
])

top_mostVendor_graph = ([
    html.Div(dcc.Graph(figure=fig))
])

# -------------------------------------------------
top_highestStore_graph = ([
    html.Div(dcc.Graph(figure=fig))
])

top_mostStore_graph = ([
    html.Div(dcc.Graph(figure=fig))
])
