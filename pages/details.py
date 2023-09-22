import dash_bootstrap_components as dbc
from dash import html, callback, Output, Input
from components import cards

layout = html.Div([
    dbc.Row(
        [
            # SALES ANALYSIS OVERVIEW
            html.H3(id="overview_title", style={"color": "#FF7F50"}),
            dbc.Col(dbc.Card(cards.sale, color="info", outline=True, className="shadow")),
            dbc.Col(dbc.Card(cards.cost_sales, color="info", outline=True, className="shadow")),
            dbc.Col(dbc.Card(cards.gross_profit, color="info", outline=True, className="shadow")),
            dbc.Col(dbc.Card(cards.inv, color="info", outline=True, className="shadow")),
            dbc.Col(dbc.Card(cards.bottleSold, color="info", outline=True, className="shadow")),
            dbc.Col(dbc.Card(cards.volumeSold, color="info", outline=True, className="shadow"))
        ], className="m-4",
    ),

    dbc.Row(
        [
            dbc.Col(cards.month_graph, className="text-center border-end m-3"),
            dbc.Col(cards.m_dow_graph, className="text-center border-end m-3"),
            dbc.Col(cards.dow_graph, className="text-center border-end m-3"),
        ], className="m-4",
    ),

    dbc.Row(
        [
            html.H3("SALES ANALYSIS BY ITEM", style={"color": "#FF7F50"}),
            dbc.Col(cards.top_highestItem_graph, className="text-center border-end m-3"),
            dbc.Col(cards.top_mostItem_graph, className="text-center border-end m-3"),
        ], className="m-4",
    ),

    dbc.Row(
        [
            html.H3("SALES ANALYSIS BY CATEGORY", style={"color": "#FF7F50"}),
            dbc.Col(cards.top_highestCat_graph, className="text-center border-end m-3"),
            dbc.Col(cards.top_mostCat_graph, className="text-center border-end m-3"),
        ], className="m-4",
    ),

    dbc.Row(
        [
            html.H3("SALES ANALYSIS BY VENDOR", style={"color": "#FF7F50"}),
            dbc.Col(cards.top_highestVendor_graph, className="text-center border-end m-3"),
            dbc.Col(cards.top_mostVendor_graph, className="text-center border-end m-3"),
        ], className="m-4",
    ),

    dbc.Row(
        [
            html.H3("SALES ANALYSIS BY STORE", style={"color": "#FF7F50"}),
            dbc.Col(cards.top_highestStore_graph, className="text-center border-end m-3"),
            dbc.Col(cards.top_mostStore_graph, className="text-center border-end m-3"),
        ], className="m-4",
    ),

    dbc.Row(
        [
            html.H3("SALES ANALYSIS BY CITY", style={"color": "#FF7F50"}),
            dbc.Col(cards.top_highestCity_graph, className="text-center border-end m-3"),
            dbc.Col(cards.top_mostCity_graph, className="text-center border-end m-3"),
        ], className="m-4",
    ),

    dbc.Row(
        [
            html.H3("SALES ANALYSIS BY COUNTY", style={"color": "#FF7F50"}),
            dbc.Col(cards.top_highestCounty_graph, className="text-center border-end m-3"),
            dbc.Col(cards.top_mostCounty_graph, className="text-center border-end m-3"),
        ], className="m-4",
    ),
])


@callback(
    Output('overview_title', 'children'),
    Input('store_y', 'data'),
)
def selected_y(y_selected):
    global overview_title

    if y_selected is None:
        overview_title = f"SALES ANALYSIS OVERVIEW (N/A)"
    else:
        # 2012
        if y_selected == 1:
            overview_title = f"SALES ANALYSIS OVERVIEW (2012)"

        # 2013
        if y_selected == 2:
            overview_title = f"SALES ANALYSIS OVERVIEW (2013)"

        # 2014
        if y_selected == 3:
            overview_title = f"SALES ANALYSIS OVERVIEW (2014)"

        # 2015
        if y_selected == 4:
            overview_title = f"SALES ANALYSIS OVERVIEW (2015)"

        # 2016
        if y_selected == 5:
            overview_title = f"SALES ANALYSIS OVERVIEW (2016)"

        # 2017
        if y_selected == 6:
            overview_title = f"SALES ANALYSIS OVERVIEW (2017)"

        # 2018
        if y_selected == 7:
            overview_title = f"SALES ANALYSIS OVERVIEW (2018)"

        # 2019
        if y_selected == 8:
            overview_title = f"SALES ANALYSIS OVERVIEW (2019)"

        # 2020
        if y_selected == 9:
            overview_title = f"SALES ANALYSIS OVERVIEW (2020)"

        # 2021
        if y_selected == 10:
            overview_title = f"SALES ANALYSIS OVERVIEW (2021)"

        # 2022
        if y_selected == 11:
            overview_title = f"SALES ANALYSIS OVERVIEW (2022)"

    return overview_title
