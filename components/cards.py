import dash_bootstrap_components as dbc
from dash import html, callback, Output, Input, dcc

from functions import readData, calTotal, plotCharts

# Read Data
df_2012 = readData.data_2012()
df_2013 = readData.data_2013()
df_2014 = readData.data_2014()
df_2015 = readData.data_2015()
df_2016 = readData.data_2016()
df_2017 = readData.data_2017()
df_2018 = readData.data_2018()
df_2019 = readData.data_2019()
df_2020 = readData.data_2020()
df_2021 = readData.data_2021()
df_2022 = readData.data_2022()

# Total Sales
(sale2012, sale2013, sale2014, sale2015, sale2016, sale2017, sale2018, sale2019,
 sale2020, sale2021, sale2022) = calTotal.total_sales_allYear(df_2012, df_2013, df_2014, df_2015, df_2016, df_2017,
                                                              df_2018, df_2019, df_2020, df_2021, df_2022)

# Total invoices
(inv2012, inv2013, inv2014, inv2015, inv2016, inv2017, inv2018, inv2019,
 inv2020, inv2021, inv2022) = calTotal.total_inv_allYear(df_2012, df_2013, df_2014, df_2015, df_2016, df_2017,
                                                         df_2018, df_2019, df_2020, df_2021, df_2022)

# Total Cost
(cost2012, cost2013, cost2014, cost2015, cost2016, cost2017, cost2018, cost2019,
 cost2020, cost2021, cost2022) = calTotal.total_cost_allYear(df_2012, df_2013, df_2014, df_2015, df_2016, df_2017,
                                                             df_2018, df_2019, df_2020, df_2021, df_2022)

# Total grossProfit
(grossProfit2012, grossProfit2013, grossProfit2014, grossProfit2015, grossProfit2016, grossProfit2017,
 grossProfit2018, grossProfit2019, grossProfit2020, grossProfit2021,
 grossProfit2022) = calTotal.total_grossProfit_allYear(sale2012, sale2013, sale2014, sale2015, sale2016, sale2017,
                                                       sale2018, sale2019, sale2020, sale2021, sale2022, cost2012,
                                                       cost2013, cost2014, cost2015, cost2016, cost2017, cost2018,
                                                       cost2019, cost2020, cost2021, cost2022)

# Total bottle sold
(bottleSold2012, bottleSold2013, bottleSold2014, bottleSold2015, bottleSold2016, bottleSold2017,
 bottleSold2018, bottleSold2019, bottleSold2020, bottleSold2021,
 bottleSold2022) = calTotal.total_bottleSold_allYear(df_2012, df_2013, df_2014, df_2015, df_2016, df_2017,
                                                     df_2018, df_2019, df_2020, df_2021, df_2022)

# Total volume sold
(volumeSold2012, volumeSold2013, volumeSold2014, volumeSold2015, volumeSold2016, volumeSold2017,
 volumeSold2018, volumeSold2019, volumeSold2020, volumeSold2021,
 volumeSold2022) = calTotal.total_volumeSold_allYear(df_2012, df_2013, df_2014, df_2015, df_2016,
                                                    df_2017, df_2018, df_2019, df_2020, df_2021, df_2022)

# General Calculation (string format)
(s_2012, c_2012, p_2012, i_2012, b_2012, v_2012) = calTotal.total_general_byYear(sale2012, cost2012, grossProfit2012, inv2012, bottleSold2012, volumeSold2012)
(s_2013, c_2013, p_2013, i_2013, b_2013, v_2013) = calTotal.total_general_byYear(sale2013, cost2013, grossProfit2013, inv2013, bottleSold2013, volumeSold2013)
(s_2014, c_2014, p_2014, i_2014, b_2014, v_2014) = calTotal.total_general_byYear(sale2014, cost2014, grossProfit2014, inv2014, bottleSold2014, volumeSold2014)
(s_2015, c_2015, p_2015, i_2015, b_2015, v_2015) = calTotal.total_general_byYear(sale2015, cost2015, grossProfit2015, inv2015, bottleSold2015, volumeSold2015)
(s_2016, c_2016, p_2016, i_2016, b_2016, v_2016) = calTotal.total_general_byYear(sale2016, cost2016, grossProfit2016, inv2016, bottleSold2016, volumeSold2016)
(s_2017, c_2017, p_2017, i_2017, b_2017, v_2017) = calTotal.total_general_byYear(sale2017, cost2017, grossProfit2017, inv2017, bottleSold2017, volumeSold2017)
(s_2018, c_2018, p_2018, i_2018, b_2018, v_2018) = calTotal.total_general_byYear(sale2018, cost2018, grossProfit2018, inv2018, bottleSold2018, volumeSold2018)
(s_2019, c_2019, p_2019, i_2019, b_2019, v_2019) = calTotal.total_general_byYear(sale2019, cost2019, grossProfit2019, inv2019, bottleSold2019, volumeSold2019)
(s_2020, c_2020, p_2020, i_2020, b_2020, v_2020) = calTotal.total_general_byYear(sale2020, cost2020, grossProfit2020, inv2020, bottleSold2020, volumeSold2020)
(s_2021, c_2021, p_2021, i_2021, b_2021, v_2021) = calTotal.total_general_byYear(sale2021, cost2021, grossProfit2021, inv2021, bottleSold2021, volumeSold2021)
(s_2022, c_2022, p_2022, i_2022, b_2022, v_2022) = calTotal.total_general_byYear(sale2022, cost2022, grossProfit2022, inv2022, bottleSold2022, volumeSold2022)

(diff_sale_2013_2012, diff_sale_2014_2013, diff_sale_2015_2014, diff_sale_2016_2015,
 diff_sale_2017_2016, diff_sale_2018_2017, diff_sale_2019_2018, diff_sale_2020_2019,
 diff_sale_2021_2020, diff_sale_2022_2021) = calTotal.diff_sales_yearAfterBefore(sale2012, sale2013, sale2014, sale2015, sale2016,
                                                                        sale2017, sale2018, sale2019, sale2020, sale2021, sale2022)

(diff_cost_2013_2012, diff_cost_2014_2013, diff_cost_2015_2014, diff_cost_2016_2015,
 diff_cost_2017_2016, diff_cost_2018_2017, diff_cost_2019_2018, diff_cost_2020_2019,
 diff_cost_2021_2020, diff_cost_2022_2021) = calTotal.diff_cost_yearAfterBefore(cost2012, cost2013, cost2014, cost2015, cost2016,
                                                                     cost2017, cost2018, cost2019, cost2020, cost2021, cost2022)

(diff_grossProfit_2013_2012, diff_grossProfit_2014_2013, diff_grossProfit_2015_2014, diff_grossProfit_2016_2015,
 diff_grossProfit_2017_2016, diff_grossProfit_2018_2017, diff_grossProfit_2019_2018, diff_grossProfit_2020_2019,
 diff_grossProfit_2021_2020, diff_grossProfit_2022_2021) = calTotal.diff_grossProfit_yearAfterBefore(grossProfit2012, grossProfit2013, grossProfit2014, grossProfit2015, grossProfit2016,
                                                                     grossProfit2017, grossProfit2018, grossProfit2019, grossProfit2020, grossProfit2021, grossProfit2022)

(diff_inv_2013_2012, diff_inv_2014_2013, diff_inv_2015_2014, diff_inv_2016_2015,
 diff_inv_2017_2016, diff_inv_2018_2017, diff_inv_2019_2018, diff_inv_2020_2019,
 diff_inv_2021_2020, diff_inv_2022_2021) = calTotal.diff_inv_yearAfterBefore(inv2012, inv2013, inv2014, inv2015, inv2016,
                                                                     inv2017, inv2018, inv2019, inv2020, inv2021, inv2022)

(diff_bottleSold_2013_2012, diff_bottleSold_2014_2013, diff_bottleSold_2015_2014, diff_bottleSold_2016_2015,
 diff_bottleSold_2017_2016, diff_bottleSold_2018_2017, diff_bottleSold_2019_2018, diff_bottleSold_2020_2019,
 diff_bottleSold_2021_2020, diff_bottleSold_2022_2021) = calTotal.diff_bottleSold_yearAfterBefore(bottleSold2012, bottleSold2013, bottleSold2014, bottleSold2015, bottleSold2016,
                                                                     bottleSold2017, bottleSold2018, bottleSold2019, bottleSold2020, bottleSold2021, bottleSold2022)

(diff_volumeSold_2013_2012, diff_volumeSold_2014_2013, diff_volumeSold_2015_2014, diff_volumeSold_2016_2015,
 diff_volumeSold_2017_2016, diff_volumeSold_2018_2017, diff_volumeSold_2019_2018, diff_volumeSold_2020_2019,
 diff_volumeSold_2021_2020, diff_volumeSold_2022_2021) = calTotal.diff_volumeSold_yearAfterBefore(volumeSold2012, volumeSold2013, volumeSold2014, volumeSold2015, volumeSold2016,
                                                                     volumeSold2017, volumeSold2018, volumeSold2019, volumeSold2020, volumeSold2021, volumeSold2022)

sale = [
    dbc.CardHeader(html.H6(id="card_sale_title", className="text-center")),
    dbc.CardBody([
        dbc.Row(html.H3(id="card_total_sales",
                        className="card-title text-center",
                        style={"color": "#FF1493"})),
        dbc.Row([
            dbc.Col([
                html.P("Previous", className="text-center"),
                html.H5(id="card_sales_previous", className="text-center",
                       style={"color": "#1E90FF"})
            ]),
            dbc.Col([
                html.P("Different", className="text-center"),
                html.H5(id="card_sales_diff", className="text-center",
                       style={"color": "#1E90FF"})
            ]),
        ])
    ])
]

cost_sales = [
    dbc.CardHeader(html.H6(id="card_cost_title", className="text-center")),
    dbc.CardBody([
        dbc.Row(html.H3(id="card_total_cost",
                        className="card-title text-center",
                        style={"color": "#FF1493"})),
        dbc.Row([
            dbc.Col([
                html.P("Previous", className="text-center"),
                html.H5(id="card_cost_previous", className="text-center",
                        style={"color": "#1E90FF"})
            ]),
            dbc.Col([
                html.P("Different", className="text-center"),
                html.H5(id="card_cost_diff", className="text-center",
                        style={"color": "#1E90FF"})
            ]),
        ])
    ])
]

gross_profit = [
    dbc.CardHeader(html.H6(id="card_grossProfit_title", className="text-center")),
    dbc.CardBody([
        dbc.Row(html.H3(id="card_total_grossProfit",
                        className="card-title text-center",
                        style={"color": "#FF1493"})),
        dbc.Row([
            dbc.Col([
                html.P("Previous", className="text-center"),
                html.H5(id="card_profit_previous", className="text-center",
                        style={"color": "#1E90FF"})
            ]),
            dbc.Col([
                html.P("Different", className="text-center"),
                html.H5(id="card_profit_diff", className="text-center",
                        style={"color": "#1E90FF"})
            ]),
        ])
    ])
]

inv = [
    dbc.CardHeader(html.H6(id="card_inv_title", className="text-center")),
    dbc.CardBody([
        dbc.Row(html.H3(id="card_total_inv",
                        className="card-title text-center",
                        style={"color": "#FF1493"})),
        dbc.Row([
            dbc.Col([
                html.P("Previous", className="text-center"),
                html.H5(id="card_inv_previous", className="text-center",
                        style={"color": "#1E90FF"})
            ]),
            dbc.Col([
                html.P("Different", className="text-center"),
                html.H5(id="card_inv_diff", className="text-center",
                        style={"color": "#1E90FF"})
            ]),
        ])
    ])
]

bottleSold = [
    dbc.CardHeader(html.H6(id="card_bottle_title", className="text-center")),
    dbc.CardBody([
        dbc.Row(html.H3(id="card_total_bottle",
                        className="card-title text-center",
                        style={"color": "#FF1493"})),
        dbc.Row([
            dbc.Col([
                html.P("Previous", className="text-center"),
                html.H5(id="card_bottle_previous", className="text-center",
                        style={"color": "#1E90FF"})
            ]),
            dbc.Col([
                html.P("Different", className="text-center"),
                html.H5(id="card_bottle_diff", className="text-center",
                        style={"color": "#1E90FF"})
            ]),
        ])
    ])
]

volumeSold = [
    dbc.CardHeader(html.H6(id="card_volume_title", className="text-center")),
    dbc.CardBody([
        dbc.Row(html.H3(id="card_total_volume",
                        className="card-title text-center",
                        style={"color": "#FF1493"})),
        dbc.Row([
            dbc.Col([
                html.P("Previous", className="text-center"),
                html.H5(id="card_volume_previous", className="text-center",
                        style={"color": "#1E90FF"})
            ]),
            dbc.Col([
                html.P("Different", className="text-center"),
                html.H5(id="card_volume_diff", className="text-center",
                        style={"color": "#1E90FF"})
            ]),
        ])
    ])
]

# -------------------------------------------------
# Get Total sale, number of invoices by months, day of week
month_sale_2012, month_cost_2012, month_profit_2012, month_inv_2012, dow_sale_2012, dow_inv_2012, month_dow_2012 = calTotal.graph_general_byyear(df_2012)
month_sale_2013, month_cost_2013, month_profit_2013, month_inv_2013, dow_sale_2013, dow_inv_2013, month_dow_2013 = calTotal.graph_general_byyear(df_2013)
month_sale_2014, month_cost_2014, month_profit_2014, month_inv_2014, dow_sale_2014, dow_inv_2014, month_dow_2014 = calTotal.graph_general_byyear(df_2014)
month_sale_2015, month_cost_2015, month_profit_2015, month_inv_2015, dow_sale_2015, dow_inv_2015, month_dow_2015 = calTotal.graph_general_byyear(df_2015)
month_sale_2016, month_cost_2016, month_profit_2016, month_inv_2016, dow_sale_2016, dow_inv_2016, month_dow_2016 = calTotal.graph_general_byyear(df_2016)
month_sale_2017, month_cost_2017, month_profit_2017, month_inv_2017, dow_sale_2017, dow_inv_2017, month_dow_2017 = calTotal.graph_general_byyear(df_2017)
month_sale_2018, month_cost_2018, month_profit_2018, month_inv_2018, dow_sale_2018, dow_inv_2018, month_dow_2018 = calTotal.graph_general_byyear(df_2018)
month_sale_2019, month_cost_2019, month_profit_2019, month_inv_2019, dow_sale_2019, dow_inv_2019, month_dow_2019 = calTotal.graph_general_byyear(df_2019)
month_sale_2020, month_cost_2020, month_profit_2020, month_inv_2020, dow_sale_2020, dow_inv_2020, month_dow_2020 = calTotal.graph_general_byyear(df_2020)
month_sale_2021, month_cost_2021, month_profit_2021, month_inv_2021, dow_sale_2021, dow_inv_2021, month_dow_2021 = calTotal.graph_general_byyear(df_2021)
month_sale_2022, month_cost_2022, month_profit_2022, month_inv_2022, dow_sale_2022, dow_inv_2022, month_dow_2022 = calTotal.graph_general_byyear(df_2022)

df_sale_cost_profit_2012 = calTotal.df_sale_cost_profit(month_cost_2012, month_profit_2012)
fig_monthly_sales_2012 = plotCharts.plot_monthly_sale_cost_profit(df_sale_cost_profit_2012)
#fig_dow_sales_2012 = plotCharts.plot_dow_sales_bydf(dow_sale_2012, dow_inv_2012)
fig_month_dow_2012 = plotCharts.plot_heatmap_month_dow(month_dow_2012)

df_sale_cost_profit_2013 = calTotal.df_sale_cost_profit(month_cost_2013, month_profit_2013)
fig_monthly_sales_2013 = plotCharts.plot_monthly_sale_cost_profit(df_sale_cost_profit_2013)
#fig_dow_sales_2013 = plotCharts.plot_dow_sales_bydf(dow_sale_2013, dow_inv_2013)
fig_month_dow_2013 = plotCharts.plot_heatmap_month_dow(month_dow_2013)

df_sale_cost_profit_2014 = calTotal.df_sale_cost_profit(month_cost_2014, month_profit_2014)
fig_monthly_sales_2014 = plotCharts.plot_monthly_sale_cost_profit(df_sale_cost_profit_2014)
#fig_dow_sales_2014 = plotCharts.plot_dow_sales_bydf(dow_sale_2014, dow_inv_2014)
fig_month_dow_2014 = plotCharts.plot_heatmap_month_dow(month_dow_2014)

df_sale_cost_profit_2015 = calTotal.df_sale_cost_profit(month_cost_2015, month_profit_2015)
fig_monthly_sales_2015 = plotCharts.plot_monthly_sale_cost_profit(df_sale_cost_profit_2015)
#fig_dow_sales_2015 = plotCharts.plot_dow_sales_bydf(dow_sale_2015, dow_inv_2015)
fig_month_dow_2015 = plotCharts.plot_heatmap_month_dow(month_dow_2015)

df_sale_cost_profit_2016 = calTotal.df_sale_cost_profit(month_cost_2016, month_profit_2016)
fig_monthly_sales_2016 = plotCharts.plot_monthly_sale_cost_profit(df_sale_cost_profit_2016)
#fig_dow_sales_2016 = plotCharts.plot_dow_sales_bydf(dow_sale_2016, dow_inv_2016)
fig_month_dow_2016 = plotCharts.plot_heatmap_month_dow(month_dow_2016)

df_sale_cost_profit_2017 = calTotal.df_sale_cost_profit(month_cost_2017, month_profit_2017)
fig_monthly_sales_2017 = plotCharts.plot_monthly_sale_cost_profit(df_sale_cost_profit_2017)
#fig_dow_sales_2017 = plotCharts.plot_dow_sales_bydf(dow_sale_2017, dow_inv_2017)
fig_month_dow_2017 = plotCharts.plot_heatmap_month_dow(month_dow_2017)

df_sale_cost_profit_2018 = calTotal.df_sale_cost_profit(month_cost_2018, month_profit_2018)
fig_monthly_sales_2018 = plotCharts.plot_monthly_sale_cost_profit(df_sale_cost_profit_2018)
#fig_dow_sales_2018 = plotCharts.plot_dow_sales_bydf(dow_sale_2018, dow_inv_2018)
fig_month_dow_2018 = plotCharts.plot_heatmap_month_dow(month_dow_2018)

df_sale_cost_profit_2019 = calTotal.df_sale_cost_profit(month_cost_2019, month_profit_2019)
fig_monthly_sales_2019 = plotCharts.plot_monthly_sale_cost_profit(df_sale_cost_profit_2019)
#fig_dow_sales_2019 = plotCharts.plot_dow_sales_bydf(dow_sale_2019, dow_inv_2019)
fig_month_dow_2019 = plotCharts.plot_heatmap_month_dow(month_dow_2019)

df_sale_cost_profit_2020 = calTotal.df_sale_cost_profit(month_cost_2020, month_profit_2020)
fig_monthly_sales_2020 = plotCharts.plot_monthly_sale_cost_profit(df_sale_cost_profit_2020)
#fig_dow_sales_2020 = plotCharts.plot_dow_sales_bydf(dow_sale_2020, dow_inv_2020)
fig_month_dow_2020 = plotCharts.plot_heatmap_month_dow(month_dow_2020)

df_sale_cost_profit_2021 = calTotal.df_sale_cost_profit(month_cost_2021, month_profit_2021)
fig_monthly_sales_2021 = plotCharts.plot_monthly_sale_cost_profit(df_sale_cost_profit_2021)
#fig_dow_sales_2021 = plotCharts.plot_dow_sales_bydf(dow_sale_2021, dow_inv_2021)
fig_month_dow_2021 = plotCharts.plot_heatmap_month_dow(month_dow_2021)

df_sale_cost_profit_2022 = calTotal.df_sale_cost_profit(month_cost_2022, month_profit_2022)
fig_monthly_sales_2022 = plotCharts.plot_monthly_sale_cost_profit(df_sale_cost_profit_2022)
#fig_dow_sales_2022 = plotCharts.plot_dow_sales_bydf(dow_sale_2022, dow_inv_2022)
fig_month_dow_2022 = plotCharts.plot_heatmap_month_dow(month_dow_2022)

month_graph = ([
    dcc.Graph(id="card_monthly_sales_graph")
])

"""
dow_graph = ([
    dcc.Graph(id="card_dow_sales_graph")
])
"""

m_dow_graph = ([
    dcc.Graph(id="card_month_dow_graph")
])

# -------------------------------------------------
# Get top 10 grossing dataframe
(top10_highestItem_2012, top10_highestCat_2012, top10_highestVendor_2012, 
 top10_highestStore_2012, top10_highestCity_2012, top10_highestCounty_2012) = calTotal.top_Grossing(df_2012)

(top10_highestItem_2013, top10_highestCat_2013, top10_highestVendor_2013,
top10_highestStore_2013, top10_highestCity_2013, top10_highestCounty_2013) = calTotal.top_Grossing(df_2013)

(top10_highestItem_2014, top10_highestCat_2014, top10_highestVendor_2014,
top10_highestStore_2014, top10_highestCity_2014, top10_highestCounty_2014) = calTotal.top_Grossing(df_2014)

(top10_highestItem_2015, top10_highestCat_2015, top10_highestVendor_2015,
top10_highestStore_2015, top10_highestCity_2015, top10_highestCounty_2015) = calTotal.top_Grossing(df_2015)

(top10_highestItem_2016, top10_highestCat_2016, top10_highestVendor_2016,
top10_highestStore_2016, top10_highestCity_2016, top10_highestCounty_2016) = calTotal.top_Grossing(df_2016)

(top10_highestItem_2017, top10_highestCat_2017, top10_highestVendor_2017,
top10_highestStore_2017, top10_highestCity_2017, top10_highestCounty_2017) = calTotal.top_Grossing(df_2017)

(top10_highestItem_2018, top10_highestCat_2018, top10_highestVendor_2018,
top10_highestStore_2018, top10_highestCity_2018, top10_highestCounty_2018) = calTotal.top_Grossing(df_2018)

(top10_highestItem_2019, top10_highestCat_2019, top10_highestVendor_2019,
top10_highestStore_2019, top10_highestCity_2019, top10_highestCounty_2019) = calTotal.top_Grossing(df_2019)

(top10_highestItem_2020, top10_highestCat_2020, top10_highestVendor_2020,
top10_highestStore_2020, top10_highestCity_2020, top10_highestCounty_2020) = calTotal.top_Grossing(df_2020)

(top10_highestItem_2021, top10_highestCat_2021, top10_highestVendor_2021,
top10_highestStore_2021, top10_highestCity_2021, top10_highestCounty_2021) = calTotal.top_Grossing(df_2021)

(top10_highestItem_2022, top10_highestCat_2022, top10_highestVendor_2022,
top10_highestStore_2022, top10_highestCity_2022, top10_highestCounty_2022) = calTotal.top_Grossing(df_2022)

# Get top 10 the most popular consumed item dataframe
(top10_mostItem_2012, top10_mostCat_2012, top10_mostVendor_2012,
top10_mostStore_2012, top10_mostCity_2012, top10_mostCounty_2012) = calTotal.top_Consuming(df_2012)

(top10_mostItem_2013, top10_mostCat_2013, top10_mostVendor_2013,
top10_mostStore_2013, top10_mostCity_2013, top10_mostCounty_2013) = calTotal.top_Consuming(df_2013)

(top10_mostItem_2014, top10_mostCat_2014, top10_mostVendor_2014,
top10_mostStore_2014, top10_mostCity_2014, top10_mostCounty_2014) = calTotal.top_Consuming(df_2014)

(top10_mostItem_2015, top10_mostCat_2015, top10_mostVendor_2015,
top10_mostStore_2015, top10_mostCity_2015, top10_mostCounty_2015) = calTotal.top_Consuming(df_2015)

(top10_mostItem_2016, top10_mostCat_2016, top10_mostVendor_2016,
top10_mostStore_2016, top10_mostCity_2016, top10_mostCounty_2016) = calTotal.top_Consuming(df_2016)

(top10_mostItem_2017, top10_mostCat_2017, top10_mostVendor_2017,
top10_mostStore_2017, top10_mostCity_2017, top10_mostCounty_2017) = calTotal.top_Consuming(df_2017)

(top10_mostItem_2018, top10_mostCat_2018, top10_mostVendor_2018,
top10_mostStore_2018, top10_mostCity_2018, top10_mostCounty_2018) = calTotal.top_Consuming(df_2018)

(top10_mostItem_2019, top10_mostCat_2019, top10_mostVendor_2019,
top10_mostStore_2019, top10_mostCity_2019, top10_mostCounty_2019) = calTotal.top_Consuming(df_2019)

(top10_mostItem_2020, top10_mostCat_2020, top10_mostVendor_2020,
top10_mostStore_2020, top10_mostCity_2020, top10_mostCounty_2020) = calTotal.top_Consuming(df_2020)

(top10_mostItem_2021, top10_mostCat_2021, top10_mostVendor_2021,
top10_mostStore_2021, top10_mostCity_2021, top10_mostCounty_2021) = calTotal.top_Consuming(df_2021)

(top10_mostItem_2022, top10_mostCat_2022, top10_mostVendor_2022,
top10_mostStore_2022, top10_mostCity_2022, top10_mostCounty_2022) = calTotal.top_Consuming(df_2022)


# -------------------------------------------------
fig_highestItem_2012 = plotCharts.plot_topGrossing(top10_highestItem_2012, "TOP 10 OF HIGHEST-GROSSING ITEMS")
fig_highestItem_2013 = plotCharts.plot_topGrossing(top10_highestItem_2013, "TOP 10 OF HIGHEST-GROSSING ITEMS")
fig_highestItem_2014 = plotCharts.plot_topGrossing(top10_highestItem_2014, "TOP 10 OF HIGHEST-GROSSING ITEMS")
fig_highestItem_2015 = plotCharts.plot_topGrossing(top10_highestItem_2015, "TOP 10 OF HIGHEST-GROSSING ITEMS")
fig_highestItem_2016 = plotCharts.plot_topGrossing(top10_highestItem_2016, "TOP 10 OF HIGHEST-GROSSING ITEMS")
fig_highestItem_2017 = plotCharts.plot_topGrossing(top10_highestItem_2017, "TOP 10 OF HIGHEST-GROSSING ITEMS")
fig_highestItem_2018 = plotCharts.plot_topGrossing(top10_highestItem_2018, "TOP 10 OF HIGHEST-GROSSING ITEMS")
fig_highestItem_2019 = plotCharts.plot_topGrossing(top10_highestItem_2019, "TOP 10 OF HIGHEST-GROSSING ITEMS")
fig_highestItem_2020 = plotCharts.plot_topGrossing(top10_highestItem_2020, "TOP 10 OF HIGHEST-GROSSING ITEMS")
fig_highestItem_2021 = plotCharts.plot_topGrossing(top10_highestItem_2021, "TOP 10 OF HIGHEST-GROSSING ITEMS")
fig_highestItem_2022 = plotCharts.plot_topGrossing(top10_highestItem_2022, "TOP 10 OF HIGHEST-GROSSING ITEMS")

fig_mostItem_2012 = plotCharts.plot_topConsuming(top10_mostItem_2012, "THE 10 MOST POPULAR CONSUMED LIQUOR")
fig_mostItem_2013 = plotCharts.plot_topConsuming(top10_mostItem_2013, "THE 10 MOST POPULAR CONSUMED LIQUOR")
fig_mostItem_2014 = plotCharts.plot_topConsuming(top10_mostItem_2014, "THE 10 MOST POPULAR CONSUMED LIQUOR")
fig_mostItem_2015 = plotCharts.plot_topConsuming(top10_mostItem_2015, "THE 10 MOST POPULAR CONSUMED LIQUOR")
fig_mostItem_2016 = plotCharts.plot_topConsuming(top10_mostItem_2016, "THE 10 MOST POPULAR CONSUMED LIQUOR")
fig_mostItem_2017 = plotCharts.plot_topConsuming(top10_mostItem_2017, "THE 10 MOST POPULAR CONSUMED LIQUOR")
fig_mostItem_2018 = plotCharts.plot_topConsuming(top10_mostItem_2018, "THE 10 MOST POPULAR CONSUMED LIQUOR")
fig_mostItem_2019 = plotCharts.plot_topConsuming(top10_mostItem_2019, "THE 10 MOST POPULAR CONSUMED LIQUOR")
fig_mostItem_2020 = plotCharts.plot_topConsuming(top10_mostItem_2020, "THE 10 MOST POPULAR CONSUMED LIQUOR")
fig_mostItem_2021 = plotCharts.plot_topConsuming(top10_mostItem_2021, "THE 10 MOST POPULAR CONSUMED LIQUOR")
fig_mostItem_2022 = plotCharts.plot_topConsuming(top10_mostItem_2022, "THE 10 MOST POPULAR CONSUMED LIQUOR")

top_highestItem_graph = ([
    dcc.Graph(id="card_highestItem_graph")
])

top_mostItem_graph = ([
    dcc.Graph(id="card_mostItem_graph")
])

# -------------------------------------------------
fig_highestCat_2012 = plotCharts.plot_topGrossing(top10_highestCat_2012, "TOP 10 OF HIGHEST-GROSSING CATEGORIES")
fig_highestCat_2013 = plotCharts.plot_topGrossing(top10_highestCat_2013, "TOP 10 OF HIGHEST-GROSSING CATEGORIES")
fig_highestCat_2014 = plotCharts.plot_topGrossing(top10_highestCat_2014, "TOP 10 OF HIGHEST-GROSSING CATEGORIES")
fig_highestCat_2015 = plotCharts.plot_topGrossing(top10_highestCat_2015, "TOP 10 OF HIGHEST-GROSSING CATEGORIES")
fig_highestCat_2016 = plotCharts.plot_topGrossing(top10_highestCat_2016, "TOP 10 OF HIGHEST-GROSSING CATEGORIES")
fig_highestCat_2017 = plotCharts.plot_topGrossing(top10_highestCat_2017, "TOP 10 OF HIGHEST-GROSSING CATEGORIES")
fig_highestCat_2018 = plotCharts.plot_topGrossing(top10_highestCat_2018, "TOP 10 OF HIGHEST-GROSSING CATEGORIES")
fig_highestCat_2019 = plotCharts.plot_topGrossing(top10_highestCat_2019, "TOP 10 OF HIGHEST-GROSSING CATEGORIES")
fig_highestCat_2020 = plotCharts.plot_topGrossing(top10_highestCat_2020, "TOP 10 OF HIGHEST-GROSSING CATEGORIES")
fig_highestCat_2021 = plotCharts.plot_topGrossing(top10_highestCat_2021, "TOP 10 OF HIGHEST-GROSSING CATEGORIES")
fig_highestCat_2022 = plotCharts.plot_topGrossing(top10_highestCat_2022, "TOP 10 OF HIGHEST-GROSSING CATEGORIES")

fig_mostCat_2012 = plotCharts.plot_topConsuming(top10_mostCat_2012, "THE 10 MOST POPULAR CONSUMED LIQUOR CATEGORIES")
fig_mostCat_2013 = plotCharts.plot_topConsuming(top10_mostCat_2013, "THE 10 MOST POPULAR CONSUMED LIQUOR CATEGORIES")
fig_mostCat_2014 = plotCharts.plot_topConsuming(top10_mostCat_2014, "THE 10 MOST POPULAR CONSUMED LIQUOR CATEGORIES")
fig_mostCat_2015 = plotCharts.plot_topConsuming(top10_mostCat_2015, "THE 10 MOST POPULAR CONSUMED LIQUOR CATEGORIES")
fig_mostCat_2016 = plotCharts.plot_topConsuming(top10_mostCat_2016, "THE 10 MOST POPULAR CONSUMED LIQUOR CATEGORIES")
fig_mostCat_2017 = plotCharts.plot_topConsuming(top10_mostCat_2017, "THE 10 MOST POPULAR CONSUMED LIQUOR CATEGORIES")
fig_mostCat_2018 = plotCharts.plot_topConsuming(top10_mostCat_2018, "THE 10 MOST POPULAR CONSUMED LIQUOR CATEGORIES")
fig_mostCat_2019 = plotCharts.plot_topConsuming(top10_mostCat_2019, "THE 10 MOST POPULAR CONSUMED LIQUOR CATEGORIES")
fig_mostCat_2020 = plotCharts.plot_topConsuming(top10_mostCat_2020, "THE 10 MOST POPULAR CONSUMED LIQUOR CATEGORIES")
fig_mostCat_2021 = plotCharts.plot_topConsuming(top10_mostCat_2021, "THE 10 MOST POPULAR CONSUMED LIQUOR CATEGORIES")
fig_mostCat_2022 = plotCharts.plot_topConsuming(top10_mostCat_2022, "THE 10 MOST POPULAR CONSUMED LIQUOR CATEGORIES")

top_highestCat_graph = ([
    dcc.Graph(id="card_highestCat_graph")
])

top_mostCat_graph = ([
    dcc.Graph(id="card_mostCat_graph")
])

# -------------------------------------------------
fig_highestVendor_2012 = plotCharts.plot_topGrossing(top10_highestVendor_2012, "TOP 10 OF HIGHEST-GROSSING VENDORS")
fig_highestVendor_2013 = plotCharts.plot_topGrossing(top10_highestVendor_2013, "TOP 10 OF HIGHEST-GROSSING VENDORS")
fig_highestVendor_2014 = plotCharts.plot_topGrossing(top10_highestVendor_2014, "TOP 10 OF HIGHEST-GROSSING VENDORS")
fig_highestVendor_2015 = plotCharts.plot_topGrossing(top10_highestVendor_2015, "TOP 10 OF HIGHEST-GROSSING VENDORS")
fig_highestVendor_2016 = plotCharts.plot_topGrossing(top10_highestVendor_2016, "TOP 10 OF HIGHEST-GROSSING VENDORS")
fig_highestVendor_2017 = plotCharts.plot_topGrossing(top10_highestVendor_2017, "TOP 10 OF HIGHEST-GROSSING VENDORS")
fig_highestVendor_2018 = plotCharts.plot_topGrossing(top10_highestVendor_2018, "TOP 10 OF HIGHEST-GROSSING VENDORS")
fig_highestVendor_2019 = plotCharts.plot_topGrossing(top10_highestVendor_2019, "TOP 10 OF HIGHEST-GROSSING VENDORS")
fig_highestVendor_2020 = plotCharts.plot_topGrossing(top10_highestVendor_2020, "TOP 10 OF HIGHEST-GROSSING VENDORS")
fig_highestVendor_2021 = plotCharts.plot_topGrossing(top10_highestVendor_2021, "TOP 10 OF HIGHEST-GROSSING VENDORS")
fig_highestVendor_2022 = plotCharts.plot_topGrossing(top10_highestVendor_2022, "TOP 10 OF HIGHEST-GROSSING VENDORS")

fig_mostVendor_2012 = plotCharts.plot_topConsuming(top10_mostVendor_2012, "THE 10 MOST POPULAR CONSUMED LIQUOR VENDORS")
fig_mostVendor_2013 = plotCharts.plot_topConsuming(top10_mostVendor_2013, "THE 10 MOST POPULAR CONSUMED LIQUOR VENDORS")
fig_mostVendor_2014 = plotCharts.plot_topConsuming(top10_mostVendor_2014, "THE 10 MOST POPULAR CONSUMED LIQUOR VENDORS")
fig_mostVendor_2015 = plotCharts.plot_topConsuming(top10_mostVendor_2015, "THE 10 MOST POPULAR CONSUMED LIQUOR VENDORS")
fig_mostVendor_2016 = plotCharts.plot_topConsuming(top10_mostVendor_2016, "THE 10 MOST POPULAR CONSUMED LIQUOR VENDORS")
fig_mostVendor_2017 = plotCharts.plot_topConsuming(top10_mostVendor_2017, "THE 10 MOST POPULAR CONSUMED LIQUOR VENDORS")
fig_mostVendor_2018 = plotCharts.plot_topConsuming(top10_mostVendor_2018, "THE 10 MOST POPULAR CONSUMED LIQUOR VENDORS")
fig_mostVendor_2019 = plotCharts.plot_topConsuming(top10_mostVendor_2019, "THE 10 MOST POPULAR CONSUMED LIQUOR VENDORS")
fig_mostVendor_2020 = plotCharts.plot_topConsuming(top10_mostVendor_2020, "THE 10 MOST POPULAR CONSUMED LIQUOR VENDORS")
fig_mostVendor_2021 = plotCharts.plot_topConsuming(top10_mostVendor_2021, "THE 10 MOST POPULAR CONSUMED LIQUOR VENDORS")
fig_mostVendor_2022 = plotCharts.plot_topConsuming(top10_mostVendor_2022, "THE 10 MOST POPULAR CONSUMED LIQUOR VENDORS")

top_highestVendor_graph = ([
    dcc.Graph(id="card_highestVendor_graph")
])

top_mostVendor_graph = ([
    dcc.Graph(id="card_mostVendor_graph")
])

# -------------------------------------------------
fig_highestStore_2012 = plotCharts.plot_topGrossing(top10_highestStore_2012, "TOP 10 OF HIGHEST-GROSSING STORES")
fig_highestStore_2013 = plotCharts.plot_topGrossing(top10_highestStore_2013, "TOP 10 OF HIGHEST-GROSSING STORES")
fig_highestStore_2014 = plotCharts.plot_topGrossing(top10_highestStore_2014, "TOP 10 OF HIGHEST-GROSSING STORES")
fig_highestStore_2015 = plotCharts.plot_topGrossing(top10_highestStore_2015, "TOP 10 OF HIGHEST-GROSSING STORES")
fig_highestStore_2016 = plotCharts.plot_topGrossing(top10_highestStore_2016, "TOP 10 OF HIGHEST-GROSSING STORES")
fig_highestStore_2017 = plotCharts.plot_topGrossing(top10_highestStore_2017, "TOP 10 OF HIGHEST-GROSSING STORES")
fig_highestStore_2018 = plotCharts.plot_topGrossing(top10_highestStore_2018, "TOP 10 OF HIGHEST-GROSSING STORES")
fig_highestStore_2019 = plotCharts.plot_topGrossing(top10_highestStore_2019, "TOP 10 OF HIGHEST-GROSSING STORES")
fig_highestStore_2020 = plotCharts.plot_topGrossing(top10_highestStore_2020, "TOP 10 OF HIGHEST-GROSSING STORES")
fig_highestStore_2021 = plotCharts.plot_topGrossing(top10_highestStore_2021, "TOP 10 OF HIGHEST-GROSSING STORES")
fig_highestStore_2022 = plotCharts.plot_topGrossing(top10_highestStore_2022, "TOP 10 OF HIGHEST-GROSSING STORES")

fig_mostStore_2012 = plotCharts.plot_topConsuming(top10_mostStore_2012, "THE 10 MOST POPULAR CONSUMED LIQUOR STORES")
fig_mostStore_2013 = plotCharts.plot_topConsuming(top10_mostStore_2013, "THE 10 MOST POPULAR CONSUMED LIQUOR STORES")
fig_mostStore_2014 = plotCharts.plot_topConsuming(top10_mostStore_2014, "THE 10 MOST POPULAR CONSUMED LIQUOR STORES")
fig_mostStore_2015 = plotCharts.plot_topConsuming(top10_mostStore_2015, "THE 10 MOST POPULAR CONSUMED LIQUOR STORES")
fig_mostStore_2016 = plotCharts.plot_topConsuming(top10_mostStore_2016, "THE 10 MOST POPULAR CONSUMED LIQUOR STORES")
fig_mostStore_2017 = plotCharts.plot_topConsuming(top10_mostStore_2017, "THE 10 MOST POPULAR CONSUMED LIQUOR STORES")
fig_mostStore_2018 = plotCharts.plot_topConsuming(top10_mostStore_2018, "THE 10 MOST POPULAR CONSUMED LIQUOR STORES")
fig_mostStore_2019 = plotCharts.plot_topConsuming(top10_mostStore_2019, "THE 10 MOST POPULAR CONSUMED LIQUOR STORES")
fig_mostStore_2020 = plotCharts.plot_topConsuming(top10_mostStore_2020, "THE 10 MOST POPULAR CONSUMED LIQUOR STORES")
fig_mostStore_2021 = plotCharts.plot_topConsuming(top10_mostStore_2021, "THE 10 MOST POPULAR CONSUMED LIQUOR STORES")
fig_mostStore_2022 = plotCharts.plot_topConsuming(top10_mostStore_2022, "THE 10 MOST POPULAR CONSUMED LIQUOR STORES")

top_highestStore_graph = ([
    dcc.Graph(id="card_highestStore_graph")
])

top_mostStore_graph = ([
    dcc.Graph(id="card_mostStore_graph")
])

# -------------------------------------------------
url_map_2012 = "img/map_2012.html"
url_map_2013 = "img/map_2013.html"
url_map_2014 = "img/map_2014.html"
url_map_2015 = "img/map_2015.html"
url_map_2016 = "img/map_2016.html"
url_map_2017 = "img/map_2017.html"
url_map_2018 = "img/map_2018.html"
url_map_2019 = "img/map_2019.html"
url_map_2020 = "img/map_2020.html"
url_map_2021 = "img/map_2021.html"
url_map_2022 = "img/map_2022.html"

"""
# Waiting time is very long, run the 1st time only
def folium_map_html(df, url_html):
    df_gpd = foliumMap.convert_gpd_groupBy(df)
    map_store = foliumMap.map_of_stores(df_gpd)
    map_store.save(url_html)

    folium_map_Iframe = html.Iframe(srcDoc=open(url_html, 'r').read(), width='100%', height=500)
    return folium_map_Iframe
"""

store_map_2012 = html.Iframe(srcDoc=open(url_map_2012, 'r').read(), width='100%', height=500)
store_map_2013 = html.Iframe(srcDoc=open(url_map_2013, 'r').read(), width='100%', height=500)
store_map_2014 = html.Iframe(srcDoc=open(url_map_2014, 'r').read(), width='100%', height=500)
store_map_2015 = html.Iframe(srcDoc=open(url_map_2015, 'r').read(), width='100%', height=500)
store_map_2016 = html.Iframe(srcDoc=open(url_map_2016, 'r').read(), width='100%', height=500)
store_map_2017 = html.Iframe(srcDoc=open(url_map_2017, 'r').read(), width='100%', height=500)
store_map_2018 = html.Iframe(srcDoc=open(url_map_2018, 'r').read(), width='100%', height=500)
store_map_2019 = html.Iframe(srcDoc=open(url_map_2019, 'r').read(), width='100%', height=500)
store_map_2020 = html.Iframe(srcDoc=open(url_map_2020, 'r').read(), width='100%', height=500)
store_map_2021 = html.Iframe(srcDoc=open(url_map_2021, 'r').read(), width='100%', height=500)
store_map_2022 = html.Iframe(srcDoc=open(url_map_2022, 'r').read(), width='100%', height=500)

store_map = ([
    html.Div(id="folium_store_map")
])
# -------------------------------------------------
@callback(
    Output('card_sale_title', 'children'), # sale
    Output('card_total_sales', 'children'),
    Output('card_sales_previous', 'children'),
    Output('card_sales_diff', 'children'),
    Output('card_cost_title', 'children'), # cost
    Output('card_total_cost', 'children'),
    Output('card_cost_previous', 'children'),
    Output('card_cost_diff', 'children'),
    Output('card_grossProfit_title', 'children'), # retail
    Output('card_total_grossProfit', 'children'),
    Output('card_profit_previous', 'children'),
    Output('card_profit_diff', 'children'),
    Output('card_inv_title', 'children'), # inv
    Output('card_total_inv', 'children'),
    Output('card_inv_previous', 'children'),
    Output('card_inv_diff', 'children'),
    Output('card_bottle_title', 'children'), # bottle sold
    Output('card_total_bottle', 'children'),
    Output('card_bottle_previous', 'children'),
    Output('card_bottle_diff', 'children'),
    Output('card_volume_title', 'children'), # volume sold
    Output('card_total_volume', 'children'),
    Output('card_volume_previous', 'children'),
    Output('card_volume_diff', 'children'),
    Output('card_monthly_sales_graph', 'figure'), # sales graphs
    #Output('card_dow_sales_graph', 'figure'),
    Output('card_month_dow_graph', 'figure'),
    Output('card_highestItem_graph', 'figure'), # top 10 graph
    Output('card_mostItem_graph', 'figure'),
    Output('card_highestCat_graph', 'figure'),
    Output('card_mostCat_graph', 'figure'),
    Output('card_highestVendor_graph', 'figure'),
    Output('card_mostVendor_graph', 'figure'),
    Output('card_highestStore_graph', 'figure'),
    Output('card_mostStore_graph', 'figure'),
    Output('folium_store_map', 'children'),
    Input('store_y', 'data'),
)
def selected_y(y_selected):
    global sale_title, total_sales, sales_previous, sales_diff, \
        cost_title, total_cost, cost_previous, cost_diff,\
        grossProfit_title, total_grossProfit, profit_previous, profit_diff, \
        inv_title, total_inv, inv_previous, inv_diff, \
        bottle_title, total_bottle, bottle_previous, bottle_diff, \
        volume_title, total_volume, volume_previous, volume_diff,\
        monthly_sales_graph, month_dow_graph, highestItem_graph, \
        mostItem_graph, highestCat_graph, mostCat_graph, highestVendor_graph, \
        mostVendor_graph, highestStore_graph, mostStore_graph, store_map

    if y_selected is None:
        sale_title = f"SALES N/A"
        total_sales = "$0"
        sales_previous = "$0"
        sales_diff = "0"
        cost_title = f"COST OF SALES N/A"
        total_cost = "$0"
        cost_previous = "$0"
        cost_diff = "$0"
        grossProfit_title = f"GROSS PROFIT N/A"
        total_grossProfit = "$0"
        profit_previous = "$0"
        profit_diff = "$0"
        inv_title = f"NO. OF INVOICES N/A"
        total_inv = "$0"
        inv_previous = "$0"
        inv_diff = "$0"
        bottle_title = f"BOTTLE SOLD N/A"
        total_bottle = "$0"
        bottle_previous = "$0"
        bottle_diff = "$0"
        volume_title = f"VOLUME SOLD N/A"
        total_volume = "$0"
        volume_previous = "$0"
        volume_diff = "$0"
        monthly_sales_graph = "N/A"
        #dow_sales_graph = "N/A"
        month_dow_graph = "N/A"
        highestItem_graph = "N/A"
        mostItem_graph  = "N/A"
        highestCat_graph  = "N/A"
        mostCat_graph = "N/A"
        highestVendor_graph = "N/A"
        mostVendor_graph = "N/A"
        highestStore_graph = "N/A"
        mostStore_graph = "N/A"
        store_map = "N/A"

    else:
        # 2012
        if y_selected == 1:
            sale_title = f"SALES 2012"
            total_sales = s_2012
            sales_previous = "N/A"
            sales_diff = "N/A"
            cost_title = f"COST OF SALES 2012"
            total_cost = c_2012
            cost_previous = "N/A"
            cost_diff = "N/A"
            grossProfit_title = f"GROSS PROFIT 2012"
            total_grossProfit = p_2012
            profit_previous = "N/A"
            profit_diff = "N/A"
            inv_title = f"NO. OF INVOICES 2012"
            total_inv = i_2012
            inv_previous = "N/A"
            inv_diff = "N/A"
            bottle_title = f"BOTTLE SOLD 2012"
            total_bottle = b_2012
            bottle_previous = "N/A"
            bottle_diff = "N/A"
            volume_title = f"VOLUME SOLD 2012"
            total_volume = v_2012
            volume_previous = "N/A"
            volume_diff = "N/A"
            monthly_sales_graph = fig_monthly_sales_2012
            #dow_sales_graph = fig_dow_sales_2012
            month_dow_graph = fig_month_dow_2012
            highestItem_graph = fig_highestItem_2012
            mostItem_graph = fig_mostItem_2012
            highestCat_graph = fig_highestCat_2012
            mostCat_graph = fig_mostCat_2012
            highestVendor_graph = fig_highestVendor_2012
            mostVendor_graph = fig_mostVendor_2012
            highestStore_graph = fig_highestStore_2012
            mostStore_graph = fig_mostStore_2012
            store_map = store_map_2012

        # 2013
        if y_selected == 2:
            sale_title = f"SALES 2013"
            total_sales = s_2013
            sales_previous = s_2012
            sales_diff = diff_sale_2013_2012
            cost_title = f"COST OF SALES 2013"
            total_cost = c_2013
            cost_previous = c_2012
            cost_diff = diff_cost_2013_2012
            grossProfit_title = f"GROSS PROFIT 2013"
            total_grossProfit = p_2013
            profit_previous = p_2012
            profit_diff = diff_grossProfit_2013_2012
            inv_title = f"NO. OF INVOICES 2013"
            total_inv = i_2013
            inv_previous = i_2012
            inv_diff = diff_inv_2013_2012
            bottle_title = f"BOTTLE SOLD 2013"
            total_bottle = b_2013
            bottle_previous = b_2012
            bottle_diff = diff_bottleSold_2013_2012
            volume_title = f"VOLUME SOLD 2013"
            total_volume = v_2013
            volume_previous = v_2012
            volume_diff = diff_volumeSold_2013_2012
            monthly_sales_graph = fig_monthly_sales_2013
            #dow_sales_graph = fig_dow_sales_2013
            month_dow_graph = fig_month_dow_2013
            highestItem_graph = fig_highestItem_2013
            mostItem_graph = fig_mostItem_2013
            highestCat_graph = fig_highestCat_2013
            mostCat_graph = fig_mostCat_2013
            highestVendor_graph = fig_highestVendor_2013
            mostVendor_graph = fig_mostVendor_2013
            highestStore_graph = fig_highestStore_2013
            mostStore_graph = fig_mostStore_2013
            store_map = store_map_2013

        # 2014
        if y_selected == 3:
            sale_title = f"SALES 2014"
            total_sales = s_2014
            sales_previous = s_2013
            sales_diff = diff_sale_2014_2013
            cost_title = f"COST OF SALES 2014"
            total_cost = c_2014
            cost_previous = c_2013
            cost_diff = diff_cost_2014_2013
            grossProfit_title = f"GROSS PROFIT 2014"
            total_grossProfit = p_2014
            profit_previous = p_2013
            profit_diff = diff_grossProfit_2014_2013
            inv_title = f"NO. OF INVOICES 2014"
            total_inv = i_2014
            inv_previous = i_2013
            inv_diff = diff_inv_2014_2013
            bottle_title = f"BOTTLE SOLD 2014"
            total_bottle = b_2014
            bottle_previous = b_2013
            bottle_diff = diff_bottleSold_2014_2013
            volume_title = f"VOLUME SOLD 2014"
            total_volume = v_2014
            volume_previous = v_2013
            volume_diff = diff_volumeSold_2014_2013
            monthly_sales_graph = fig_monthly_sales_2014
            #dow_sales_graph = fig_dow_sales_2014
            month_dow_graph = fig_month_dow_2014
            highestItem_graph = fig_highestItem_2014
            mostItem_graph = fig_mostItem_2014
            highestCat_graph = fig_highestCat_2014
            mostCat_graph = fig_mostCat_2014
            highestVendor_graph = fig_highestVendor_2014
            mostVendor_graph = fig_mostVendor_2014
            highestStore_graph = fig_highestStore_2014
            mostStore_graph = fig_mostStore_2014
            store_map = store_map_2014

        # 2015
        if y_selected == 4:
            sale_title = f"SALES 2015"
            total_sales = s_2015
            sales_previous = s_2014
            sales_diff = diff_sale_2015_2014
            cost_title = f"COST OF SALES 2015"
            total_cost = c_2015
            cost_previous = c_2014
            cost_diff = diff_cost_2015_2014
            grossProfit_title = f"GROSS PROFIT 2015"
            total_grossProfit = p_2015
            profit_previous = p_2014
            profit_diff = diff_grossProfit_2015_2014
            inv_title = f"NO. OF INVOICES 2015"
            total_inv = i_2015
            inv_previous = i_2014
            inv_diff = diff_inv_2015_2014
            bottle_title = f"BOTTLE SOLD 2015"
            total_bottle = b_2015
            bottle_previous = b_2014
            bottle_diff = diff_bottleSold_2015_2014
            volume_title = f"VOLUME SOLD 2015"
            total_volume = v_2015
            volume_previous = v_2014
            volume_diff = diff_volumeSold_2015_2014
            monthly_sales_graph = fig_monthly_sales_2015
            #dow_sales_graph = fig_dow_sales_2015
            month_dow_graph = fig_month_dow_2015
            highestItem_graph = fig_highestItem_2015
            mostItem_graph = fig_mostItem_2015
            highestCat_graph = fig_highestCat_2015
            mostCat_graph = fig_mostCat_2015
            highestVendor_graph = fig_highestVendor_2015
            mostVendor_graph = fig_mostVendor_2015
            highestStore_graph = fig_highestStore_2015
            mostStore_graph = fig_mostStore_2015
            store_map = store_map_2015

        # 2016
        if y_selected == 5:
            sale_title = f"SALES 2016"
            total_sales = s_2016
            sales_previous = s_2015
            sales_diff = diff_sale_2016_2015
            cost_title = f"COST OF SALES 2016"
            total_cost = c_2016
            cost_previous = c_2015
            cost_diff = diff_cost_2016_2015
            grossProfit_title = f"GROSS PROFIT 2016"
            total_grossProfit = p_2016
            profit_previous = p_2015
            profit_diff = diff_grossProfit_2016_2015
            inv_title = f"NO. OF INVOICES 2016"
            total_inv = i_2016
            inv_previous = i_2015
            inv_diff = diff_inv_2016_2015
            bottle_title = f"BOTTLE SOLD 2016"
            total_bottle = b_2016
            bottle_previous = b_2015
            bottle_diff = diff_bottleSold_2016_2015
            volume_title = f"VOLUME SOLD 2016"
            total_volume = v_2016
            volume_previous = v_2015
            volume_diff = diff_volumeSold_2016_2015
            monthly_sales_graph = fig_monthly_sales_2016
            #dow_sales_graph = fig_dow_sales_2016
            month_dow_graph = fig_month_dow_2016
            highestItem_graph = fig_highestItem_2016
            mostItem_graph = fig_mostItem_2016
            highestCat_graph = fig_highestCat_2016
            mostCat_graph = fig_mostCat_2016
            highestVendor_graph = fig_highestVendor_2016
            mostVendor_graph = fig_mostVendor_2016
            highestStore_graph = fig_highestStore_2016
            mostStore_graph = fig_mostStore_2016
            store_map = store_map_2016

        # 2017
        if y_selected == 6:
            sale_title = f"SALES 2017"
            total_sales = s_2017
            sales_previous = s_2016
            sales_diff = diff_sale_2017_2016
            cost_title = f"COST OF SALES 2017"
            total_cost = c_2017
            cost_previous = c_2016
            cost_diff = diff_cost_2017_2016
            grossProfit_title = f"GROSS PROFIT 2017"
            total_grossProfit = p_2017
            profit_previous = p_2016
            profit_diff = diff_grossProfit_2017_2016
            inv_title = f"NO. OF INVOICES 2017"
            total_inv = i_2017
            inv_previous = i_2016
            inv_diff = diff_inv_2017_2016
            bottle_title = f"BOTTLE SOLD 2017"
            total_bottle = b_2017
            bottle_previous = b_2016
            bottle_diff = diff_bottleSold_2017_2016
            volume_title = f"VOLUME SOLD 2017"
            total_volume = v_2017
            volume_previous = v_2016
            volume_diff = diff_volumeSold_2017_2016
            monthly_sales_graph = fig_monthly_sales_2017
            #dow_sales_graph = fig_dow_sales_2017
            month_dow_graph = fig_month_dow_2017
            highestItem_graph = fig_highestItem_2017
            mostItem_graph = fig_mostItem_2017
            highestCat_graph = fig_highestCat_2017
            mostCat_graph = fig_mostCat_2017
            highestVendor_graph = fig_highestVendor_2017
            mostVendor_graph = fig_mostVendor_2017
            highestStore_graph = fig_highestStore_2017
            mostStore_graph = fig_mostStore_2017
            store_map = store_map_2017

        # 2018
        if y_selected == 7:
            sale_title = f"SALES 2018"
            total_sales = s_2018
            sales_previous = s_2017
            sales_diff = diff_sale_2018_2017
            cost_title = f"COST OF SALES 2018"
            total_cost = c_2018
            cost_previous = c_2017
            cost_diff = diff_cost_2018_2017
            grossProfit_title = f"GROSS PROFIT 2018"
            total_grossProfit = p_2018
            profit_previous = p_2017
            profit_diff = diff_grossProfit_2018_2017
            inv_title = f"NO. OF INVOICES 2018"
            total_inv = i_2018
            inv_previous = i_2017
            inv_diff = diff_inv_2018_2017
            bottle_title = f"BOTTLE SOLD 2018"
            total_bottle = b_2018
            bottle_previous = b_2017
            bottle_diff = diff_bottleSold_2018_2017
            volume_title = f"VOLUME SOLD 2018"
            total_volume = v_2018
            volume_previous = v_2017
            volume_diff = diff_volumeSold_2018_2017
            monthly_sales_graph = fig_monthly_sales_2018
            #dow_sales_graph = fig_dow_sales_2018
            month_dow_graph = fig_month_dow_2018
            highestItem_graph = fig_highestItem_2018
            mostItem_graph = fig_mostItem_2018
            highestCat_graph = fig_highestCat_2018
            mostCat_graph = fig_mostCat_2018
            highestVendor_graph = fig_highestVendor_2018
            mostVendor_graph = fig_mostVendor_2018
            highestStore_graph = fig_highestStore_2018
            mostStore_graph = fig_mostStore_2018
            store_map = store_map_2018

        # 2019
        if y_selected == 8:
            sale_title = f"SALES 2019"
            total_sales = s_2019
            sales_previous = s_2018
            sales_diff = diff_sale_2019_2018
            cost_title = f"COST OF SALES 2019"
            total_cost = c_2019
            cost_previous = c_2018
            cost_diff = diff_grossProfit_2019_2018
            grossProfit_title = f"GROSS PROFIT 2019"
            total_grossProfit = p_2019
            profit_previous = p_2018
            inv_title = f"NO. OF INVOICES 2019"
            total_inv = i_2019
            inv_previous = i_2018
            inv_diff = diff_inv_2019_2018
            bottle_title = f"BOTTLE SOLD 2019"
            total_bottle = b_2019
            bottle_previous = b_2018
            bottle_diff = diff_bottleSold_2019_2018
            volume_title = f"VOLUME SOLD 2019"
            total_volume = v_2019
            volume_previous = v_2018
            volume_diff = diff_volumeSold_2019_2018
            monthly_sales_graph = fig_monthly_sales_2019
            #dow_sales_graph = fig_dow_sales_2019
            month_dow_graph = fig_month_dow_2019
            highestItem_graph = fig_highestItem_2019
            mostItem_graph = fig_mostItem_2019
            highestCat_graph = fig_highestCat_2019
            mostCat_graph = fig_mostCat_2019
            highestVendor_graph = fig_highestVendor_2019
            mostVendor_graph = fig_mostVendor_2019
            highestStore_graph = fig_highestStore_2019
            mostStore_graph = fig_mostStore_2019
            store_map = store_map_2019

        # 2020
        if y_selected == 9:
            sale_title = f"SALES 2020"
            total_sales = s_2020
            sales_previous = s_2019
            sales_diff = diff_sale_2020_2019
            cost_title = f"COST OF SALES 2020"
            total_cost = c_2020
            cost_previous = c_2019
            cost_diff = diff_cost_2020_2019
            grossProfit_title = f"GROSS PROFIT 2020"
            total_grossProfit = p_2020
            profit_previous = p_2019
            profit_diff = diff_grossProfit_2020_2019
            inv_title = f"NO. OF INVOICES 2020"
            total_inv = i_2020
            inv_previous = i_2019
            inv_diff = diff_inv_2020_2019
            bottle_title = f"BOTTLE SOLD 2020"
            total_bottle = b_2020
            bottle_previous = b_2019
            bottle_diff = diff_bottleSold_2020_2019
            volume_title = f"VOLUME SOLD 2020"
            total_volume = v_2020
            volume_previous = v_2019
            volume_diff = diff_volumeSold_2020_2019
            monthly_sales_graph = fig_monthly_sales_2020
            #dow_sales_graph = fig_dow_sales_2020
            month_dow_graph = fig_month_dow_2020
            highestItem_graph = fig_highestItem_2020
            mostItem_graph = fig_mostItem_2020
            highestCat_graph = fig_highestCat_2020
            mostCat_graph = fig_mostCat_2020
            highestVendor_graph = fig_highestVendor_2020
            mostVendor_graph = fig_mostVendor_2020
            highestStore_graph = fig_highestStore_2020
            mostStore_graph = fig_mostStore_2020
            store_map = store_map_2020

        # 2021
        if y_selected == 10:
            sale_title = f"SALES 2021"
            total_sales = s_2021
            sales_previous = s_2020
            sales_diff = diff_sale_2021_2020
            cost_title = f"COST OF SALES 2021"
            total_cost = c_2021
            cost_previous = c_2020
            cost_diff = diff_cost_2021_2020
            grossProfit_title = f"GROSS PROFIT 2021"
            total_grossProfit = p_2021
            profit_previous = p_2020
            profit_diff = diff_grossProfit_2021_2020
            inv_title = f"NO. OF INVOICES 2021"
            total_inv = i_2021
            inv_previous = i_2020
            inv_diff = diff_inv_2021_2020
            bottle_title = f"BOTTLE SOLD 2021"
            total_bottle = b_2021
            bottle_previous = b_2020
            bottle_diff = diff_bottleSold_2021_2020
            volume_title = f"VOLUME SOLD 2021"
            total_volume = v_2021
            volume_previous = v_2020
            volume_diff = diff_volumeSold_2021_2020
            monthly_sales_graph = fig_monthly_sales_2021
            #dow_sales_graph = fig_dow_sales_2021
            month_dow_graph = fig_month_dow_2021
            highestItem_graph = fig_highestItem_2021
            mostItem_graph = fig_mostItem_2021
            highestCat_graph = fig_highestCat_2021
            mostCat_graph = fig_mostCat_2021
            highestVendor_graph = fig_highestVendor_2021
            mostVendor_graph = fig_mostVendor_2021
            highestStore_graph = fig_highestStore_2021
            mostStore_graph = fig_mostStore_2021
            store_map = store_map_2021

        # 2022
        if y_selected == 11:
            sale_title = f"SALES 2022"
            total_sales = s_2022
            sales_previous = s_2021
            sales_diff = diff_sale_2022_2021
            cost_title = f"COST OF SALES 2022"
            total_cost = c_2022
            cost_previous = c_2021
            cost_diff = diff_cost_2022_2021
            grossProfit_title = f"GROSS PROFIT 2022"
            total_grossProfit = p_2022
            profit_previous = p_2021
            profit_diff = diff_grossProfit_2022_2021
            inv_title = f"NO. OF INVOICES 2022"
            total_inv = i_2022
            inv_previous = i_2021
            inv_diff = diff_inv_2022_2021
            bottle_title = f"BOTTLE SOLD 2022"
            total_bottle = b_2022
            bottle_previous = b_2021
            bottle_diff = diff_bottleSold_2022_2021
            volume_title = f"VOLUME SOLD 2022"
            total_volume = v_2022
            volume_previous = v_2021
            volume_diff = diff_volumeSold_2022_2021
            monthly_sales_graph = fig_monthly_sales_2022
            #dow_sales_graph = fig_dow_sales_2022
            month_dow_graph = fig_month_dow_2022
            highestItem_graph = fig_highestItem_2022
            mostItem_graph = fig_mostItem_2022
            highestCat_graph = fig_highestCat_2022
            mostCat_graph = fig_mostCat_2022
            highestVendor_graph = fig_highestVendor_2022
            mostVendor_graph = fig_mostVendor_2022
            highestStore_graph = fig_highestStore_2022
            mostStore_graph = fig_mostStore_2022
            store_map = store_map_2022

    return (sale_title, total_sales, sales_previous, sales_diff,
            cost_title, total_cost, cost_previous, cost_diff,
            grossProfit_title, total_grossProfit, profit_previous, profit_diff,
            inv_title, total_inv, inv_previous, inv_diff,
            bottle_title, total_bottle, bottle_previous, bottle_diff,
            volume_title, total_volume, volume_previous, volume_diff,
            monthly_sales_graph, month_dow_graph, highestItem_graph,
            mostItem_graph, highestCat_graph, mostCat_graph, highestVendor_graph,
            mostVendor_graph, highestStore_graph, mostStore_graph, store_map)
