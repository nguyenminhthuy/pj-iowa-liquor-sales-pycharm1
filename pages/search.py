import dash_bootstrap_components as dbc
from dash import html, dcc, Output, Input, callback, ALL, ctx, State

from components import cards_search
from functions import searchResult, calTotal, plotCharts, foliumMap

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
            dcc.Dropdown(
                ['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022'],
                placeholder="Select year...", id="dropdown_year_search"
            ), width=3,
        ),
        dbc.Col(
            dbc.Input(type="text", id="txt_keyword",
                      placeholder="Search by keyword", size="md"),
        ),
        dbc.Col(
            dbc.Button("SUBMIT", id="btnSubmit",
                       className='btn-search p-2',
                       style={
                           'background-color': 'rgb(237, 201, 72)',
                           'color': 'rgb(30, 51, 118)',
                           'border': '0px', 'font-weight': 'bold'
                       }),
            width=2, className="d-grid gap-2"
        ),
    ], className="m-4"),

    dbc.Row([
        # html.H6("Your input:"),
        html.Div(id="lstSearch_group"),
    ], className="m-5"),

    dbc.Row([
        html.H4(id="rs_title", style={"color": "#FF7F50"}),
        dbc.Col(
            dbc.Card([
                dbc.CardHeader(html.H6("SALES", className="text-center")),
                dbc.CardBody([
                    dbc.Row(html.H3(id='rs_totalSale',
                                    className="card-title text-center",
                                    style={"color": "#FF1493"})),
                ]),
            ], color="info", outline=True, className="shadow")
        ),

        dbc.Col(
            dbc.Card([
                dbc.CardHeader(html.H6("COST", className="text-center")),
                dbc.CardBody([
                    dbc.Row(html.H3(id='rs_totalCost',
                                    className="card-title text-center", style={"color": "#FF1493"})),
                ]),
            ], color="info", outline=True, className="shadow")),

        dbc.Col(
            dbc.Card([
                dbc.CardHeader(html.H6("GROSS PROFIT", className="text-center")),
                dbc.CardBody([
                    dbc.Row(html.H3(id='rs_grossProfit',
                                    className="card-title text-center", style={"color": "#FF1493"})),
                ]),
            ], color="info", outline=True, className="shadow")),

        dbc.Col(
            dbc.Card([
                dbc.CardHeader(html.H6("NUMBER OF INVOICES", className="text-center")),
                dbc.CardBody([
                    dbc.Row(html.H3(id='rs_inv',
                                    className="card-title text-center",
                                    style={"color": "#FF1493"})),
                ]),
            ], color="info", outline=True, className="shadow")),

        dbc.Col(
            dbc.Card([
                dbc.CardHeader(html.H6("BOTTLE SOLD", className="text-center")),
                dbc.CardBody([
                    dbc.Row(html.H3(id='rs_bottleSold',
                                    className="card-title text-center", style={"color": "#FF1493"})),
                ]),
            ], color="info", outline=True, className="shadow")),

        dbc.Col(
            dbc.Card([
                dbc.CardHeader(html.H6("VOLUME SOLD", className="text-center")),
                dbc.CardBody([
                    dbc.Row(html.H3(id='rs_volumeSold',
                                    className="card-title text-center", style={"color": "#FF1493"})),
                ]),
            ], color="info", outline=True, className="shadow"))
    ], className="m-4",
    ),

    dbc.Row([
        dbc.Col([
            dcc.Graph(id="r_monthly_sales_graph")
        ], className="text-center border-end m-3"),

        dbc.Col([
            dcc.Graph(id="r_month_dow_graph")
        ], className="text-center border-end m-3"),
    ], className="m-4",
    ),

    html.Div(
        dbc.Row([
            dbc.Col(html.H4("SALES ANALYSIS", style={"color": "#FF7F50"})),
        ], className="m-5")
    ),

    html.Div(
        dbc.Row([
            dbc.Col([
                dcc.Tabs([
                    dcc.Tab(label='TOP 10 ITEMS', children=[
                        dbc.Row([
                            dbc.Badge("Success", color="success", className="me-1"),
                            dbc.Col([
                                dcc.Graph(id="r_highestItem_graph")
                            ], className="m-4"),

                            dbc.Col([
                                dcc.Graph(id="r_mostItem_graph")
                            ], className="m-3"),
                        ])
                    ], style=tab_style, selected_style=tab_selected_style),

                    dcc.Tab(label='TOP 10 CATEGORIES', children=[
                        dbc.Row([
                            dbc.Col([
                                dcc.Graph(id="r_highestCat_graph")
                            ], className="m-4"),

                            dbc.Col([
                                dcc.Graph(id="r_mostCat_graph")
                            ], className="m-4"),
                        ])
                    ], style=tab_style, selected_style=tab_selected_style),

                    dcc.Tab(label='TOP 10 VENDORS', children=[
                        dbc.Row([
                            dbc.Col([
                                dcc.Graph(id="r_highestVendor_graph")
                            ], className="m-4"),

                            dbc.Col([
                                dcc.Graph(id="r_mostVendor_graph")
                            ], className="m-4"),
                        ])
                    ], style=tab_style, selected_style=tab_selected_style),

                    dcc.Tab(label='TOP 10 STORES', children=[
                        dbc.Row([
                            dbc.Col([
                                dcc.Graph(id="r_highestStore_graph")
                            ], className="m-4"),

                            dbc.Col([
                                dcc.Graph(id="r_mostStore_graph")
                            ], className="m-4"),
                        ])
                    ], style=tab_style, selected_style=tab_selected_style),
                ])
            ])
        ], className="m-5"
        )
    ),

    dbc.Row([
        html.H3("STORE LOCATION", style={"color": "#FF7F50"}),
        html.Div(id='folium-map-rs')
    ], className="m-5",
    ),

    dbc.Button(children=html.Span([html.I(className="fa fa-arrow-up fa-lg")]),
               href="#backtotop", n_clicks=0,
               style=dict(fontSize="35px", backgroundColor="rgb(237, 201, 72)",
                          textAlign="right", color="rgb(30, 51, 118)",
                          border="none", marginLeft="90%")),
])

@callback(
    Output('lstSearch_group', 'children'),
    Input('btnSubmit', 'n_clicks'),
    [State('dropdown_year_search', 'value'),
     State('txt_keyword', 'value')])
def btnSubmit_click(n_clicks, year_val, key_val):
    global rs_group

    # lst_rs = 'Year: {}. Keyword: {}'.format(year_val, key_val)
    # cat FLAVORED
    # store DUBUQUE
    # vendor RICARD
    # item COCONUT
    lst_item = searchResult.lst_search_result(year_val, key_val)
    if len(lst_item) <= 0:
        rs_group = [
            dbc.Alert("We couldn't find a match for {} in {}. Please try another search".format(key_val, year_val),
                      color="danger"),
        ]
    else:
        rs_group = [
            dbc.Alert("About {} results.".format(len(lst_item)),
                      color="info"),
            html.Label("{}".format(year_val), id='lb-list-keyword-rs1',
                       style={"visibility": "hidden"}),
            dbc.ListGroup([
                dbc.ListGroupItem(
                    f"{i}",
                    id={"type": "list-keyword-rs1", "index": i},
                    action=True
                )
                for i in list(lst_item)
            ], id="list-group1")
        ]
    return rs_group

@callback(
    Output("rs_title", "children"),
    Output("rs_totalSale", "children"),
    Output("rs_totalCost", "children"),
    Output("rs_grossProfit", "children"),
    Output("rs_inv", "children"),
    Output("rs_bottleSold", "children"),
    Output("rs_volumeSold", "children"),
    Output('r_monthly_sales_graph', 'figure'),
    Output('r_month_dow_graph', 'figure'),
    Output('r_highestItem_graph', 'figure'), # top 10 graph
    Output('r_mostItem_graph', 'figure'),
    Output('r_highestCat_graph', 'figure'),
    Output('r_mostCat_graph', 'figure'),
    Output('r_highestVendor_graph', 'figure'),
    Output('r_mostVendor_graph', 'figure'),
    Output('r_highestStore_graph', 'figure'),
    Output('r_mostStore_graph', 'figure'),
    Output('folium-map-rs', 'children'),
    Input({'type': 'list-keyword-rs1', 'index': ALL}, 'n_clicks'),
    Input('lb-list-keyword-rs1', 'children'),
    prevent_initial_call=True
)
def searchResult_selected(_, lb_year):
    global r_title, r_totalSale, r_totalCost, r_grossProfit, r_inv, r_bottleSold, r_volumeSold, \
        r_monthly_sales_graph, r_month_dow_graph, r_highestItem_graph, r_mostItem_graph, r_highestCat_graph, \
        r_mostCat_graph, r_highestVendor_graph, r_mostVendor_graph, r_highestStore_graph, r_mostStore_graph, \
        map_store_f

    full_key = ctx.triggered_id.index # what is selected by user
    df_filter = searchResult.filter_df_byFullKeyword(lb_year, full_key)
    sales, cost, grossProfit, inv, bottleSold, volumeSold = searchResult.filter_overall(df_filter)

    month_sale_f, month_cost_f, month_profit_f, month_inv_f, dow_sale_f, dow_inv_f, month_dow_f = calTotal.graph_general_byyear(df_filter)
    df_sale_cost_profit_f = calTotal.df_sale_cost_profit(month_cost_f, month_profit_f)

    top10_highestItem_f, top10_highestCat_f, top10_highestVendor_f, top10_highestStore_f, top10_highestCity_f, top10_highestCounty_f = calTotal.top_Grossing(df_filter)
    top10_mostItem_f, top10_mostCat_f, top10_mostVendor_f, top10_mostStore_f, top10_mostCity_f, top10_mostCounty_f = calTotal.top_Consuming(df_filter)

    url_map_filter = "img/map_filter.html"
    """ 
    df_gpd = foliumMap.convert_gpd_groupBy(df_filter)
    map_store = foliumMap.map_of_stores(df_gpd)
    map_store.save(url_map_filter)
    """

    if full_key is None:
        r_title = "N/A"
        r_totalSale="N/A"
        r_totalCost = "N/A"
        r_grossProfit = "N/A"
        r_inv = "N/A"
        r_bottleSold = "N/A"
        r_volumeSold = "N/A"
    else:
        r_title = 'Report for: {}'.format(full_key) #lst_rs = 'sales: {}. cost: {}'.format(r_totalSale, r_totalCost)
        # convert to human format: K, M, B
        r_totalSale, r_totalCost, r_grossProfit, r_inv, r_bottleSold, r_volumeSold = calTotal.total_general_byYear(sales, cost, grossProfit, inv, bottleSold, volumeSold)

        r_monthly_sales_graph = plotCharts.plot_monthly_sale_cost_profit(df_sale_cost_profit_f)
        r_month_dow_graph = plotCharts.plot_heatmap_month_dow(month_dow_f)

        r_highestItem_graph = plotCharts.plot_topGrossing(top10_highestItem_f, "TOP 10 OF HIGHEST-GROSSING ITEMS")
        r_highestCat_graph = plotCharts.plot_topGrossing(top10_highestCat_f, "TOP 10 OF HIGHEST-GROSSING CATEGORIES")
        r_highestVendor_graph = plotCharts.plot_topGrossing(top10_highestVendor_f, "TOP 10 OF HIGHEST-GROSSING VENDORS")
        r_highestStore_graph = plotCharts.plot_topGrossing(top10_highestStore_f, "TOP 10 OF HIGHEST-GROSSING STORES")

        r_mostItem_graph = plotCharts.plot_topConsuming(top10_mostItem_f, "THE 10 MOST POPULAR CONSUMED ITEMS")
        r_mostCat_graph = plotCharts.plot_topConsuming(top10_mostCat_f, "THE 10 MOST POPULAR CONSUMED CATEGORIES")
        r_mostVendor_graph = plotCharts.plot_topConsuming(top10_mostVendor_f, "THE 10 MOST POPULAR CONSUMED VENDORS")
        r_mostStore_graph = plotCharts.plot_topConsuming(top10_mostStore_f, "THE 10 MOST POPULAR CONSUMED STORES")

        map_store_f = html.Iframe(srcDoc=open(url_map_filter, 'r').read(), width='100%', height=500)

    return (r_title, r_totalSale, r_totalCost, r_grossProfit, r_inv, r_bottleSold, r_volumeSold,
            r_monthly_sales_graph, r_month_dow_graph, r_highestItem_graph, r_mostItem_graph, r_highestCat_graph,
            r_mostCat_graph, r_highestVendor_graph, r_mostVendor_graph, r_highestStore_graph, r_mostStore_graph,
            map_store_f)
