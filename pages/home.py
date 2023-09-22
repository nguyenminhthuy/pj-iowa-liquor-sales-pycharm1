import dash_bootstrap_components as dbc
import pandas as pd
from dash import html, dcc
from functions import calTotal, plotCharts, readData

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
(sale2012, sale2013, sale2014, sale2015, sale2016, sale2017, sale2018,
 sale2019, sale2020, sale2021, sale2022) = calTotal.total_sales_allYear(df_2012, df_2013, df_2014, df_2015, df_2016,
                                                                        df_2017,
                                                                        df_2018, df_2019, df_2020, df_2021, df_2022)

# Total invoices
(inv2012, inv2013, inv2014, inv2015, inv2016, inv2017, inv2018, inv2019,
 inv2020, inv2021, inv2022) = calTotal.total_inv_allYear(df_2012, df_2013, df_2014, df_2015, df_2016, df_2017,
                                                         df_2018, df_2019, df_2020, df_2021, df_2022)

# Total Cost
(cost2012, cost2013, cost2014, cost2015, cost2016, cost2017, cost2018,
 cost2019, cost2020, cost2021, cost2022) = calTotal.total_cost_allYear(df_2012, df_2013, df_2014, df_2015, df_2016,
                                                                       df_2017,
                                                                       df_2018, df_2019, df_2020, df_2021, df_2022)

# Total grossProfit
(grossProfit2012, grossProfit2013, grossProfit2014, grossProfit2015, grossProfit2016,
 grossProfit2017, grossProfit2018, grossProfit2019, grossProfit2020, grossProfit2021,
 grossProfit2022) = calTotal.total_grossProfit_allYear(sale2012, sale2013, sale2014, sale2015, sale2016, sale2017,
                                                       sale2018,
                                                       sale2019, sale2020, sale2021, sale2022, cost2012, cost2013,
                                                       cost2014,
                                                       cost2015, cost2016, cost2017, cost2018, cost2019, cost2020,
                                                       cost2021, cost2022)

# % Different Sales with Previous Year
(pct_sale_2013_2012, pct_sale_2014_2013, pct_sale_2015_2014, pct_sale_2016_2015,
 pct_sale_2017_2016, pct_sale_2018_2017, pct_sale_2019_2018, pct_sale_2020_2019,
 pct_sale_2021_2020, pct_sale_2022_2021) = calTotal.pct_sales_yearAfterBefore(sale2012, sale2013, sale2014, sale2015,
                                                                              sale2016,
                                                                              sale2017, sale2018, sale2019, sale2020,
                                                                              sale2021, sale2022)

# % Different Sales with Previous Year
(pct_inv_2013_2012, pct_inv_2014_2013, pct_inv_2015_2014, pct_inv_2016_2015,
 pct_inv_2017_2016, pct_inv_2018_2017, pct_inv_2019_2018, pct_inv_2020_2019,
 pct_inv_2021_2020, pct_inv_2022_2021) = calTotal.pct_inv_yearAfterBefore(inv2012, inv2013, inv2014, inv2015, inv2016,
                                                                          inv2017, inv2018, inv2019, inv2020, inv2021,
                                                                          inv2022)

pct_sale_dict = {'2012': 'NA', '2013': pct_sale_2013_2012, '2014': pct_sale_2014_2013,
                 '2015': pct_sale_2015_2014, '2016': pct_sale_2016_2015, '2017': pct_sale_2017_2016,
                 '2018': pct_sale_2018_2017, '2019': pct_sale_2019_2018, '2020': pct_sale_2020_2019,
                 '2021': pct_sale_2021_2020, '2022': pct_sale_2022_2021}

pct_inv_dict = {'2012': 'NA', '2013': pct_inv_2013_2012, '2014': pct_inv_2014_2013,
                '2015': pct_inv_2015_2014, '2016': pct_inv_2016_2015, '2017': pct_inv_2017_2016,
                '2018': pct_inv_2018_2017, '2019': pct_inv_2019_2018, '2020': pct_inv_2020_2019,
                '2021': pct_inv_2021_2020, '2022': pct_inv_2022_2021}

sale_dict = {'2012': sale2012, '2013': sale2013, '2014': sale2014,
             '2015': sale2015, '2016': sale2016, '2017': sale2017,
             '2018': sale2018, '2019': sale2019, '2020': sale2020,
             '2021': sale2021, '2022': sale2022}

inv_dict = {'2012': inv2012, '2013': inv2013, '2014': inv2014,
            '2015': inv2015, '2016': inv2016, '2017': inv2017,
            '2018': inv2018, '2019': inv2019, '2020': inv2020,
            '2021': inv2021, '2022': inv2022}

cost_dict = {'2012': cost2012, '2013': cost2013, '2014': cost2014,
             '2015': cost2015, '2016': cost2016, '2017': cost2017,
             '2018': cost2018, '2019': cost2019, '2020': cost2020,
             '2021': cost2021, '2022': cost2022}

grossProfit_dict = {'2012': grossProfit2012, '2013': grossProfit2013, '2014': grossProfit2014,
                    '2015': grossProfit2015, '2016': grossProfit2016, '2017': grossProfit2017,
                    '2018': grossProfit2018, '2019': grossProfit2019, '2020': grossProfit2020,
                    '2021': grossProfit2021, '2022': grossProfit2022}

# create series from dictionary
sale_ser = pd.Series(sale_dict)
pct_sale_ser = pd.Series(pct_sale_dict)
inv_ser = pd.Series(inv_dict)
pct_inv_ser = pd.Series(pct_inv_dict)
cost_dict_ser = pd.Series(cost_dict)
grossProfit_dict_ser = pd.Series(grossProfit_dict)

fr_overall_sale_inv = {'Year': sale_ser.index,
                       'Total Sales (USD)': sale_ser.values,
                       'Sales Variance': pct_sale_ser,
                       'No. of Invoices': inv_ser.values,
                       'Invoices Variance': pct_inv_ser}

fr_overall_cost_profit = {'Year': sale_ser.index,
                          'Total Sales (USD)': sale_ser.values,
                          'Total Cost (USD)': cost_dict_ser.values,
                          'Gross Profit (USD)': grossProfit_dict_ser.values}

# ------------------------------------------------
# Sales, No. of Invoices Historical Trend 2012-2022
df_overall_sale_inv_graph = pd.DataFrame(fr_overall_sale_inv)
df_overall_sale_inv_graph.reset_index(inplace=True, drop=True)
fig_overall_sale_inv = plotCharts.plot_Overall_Sale_Inv(df_overall_sale_inv_graph)

# Different Sales vs the previous year (table)
df_overall_sale_inv_table = df_overall_sale_inv_graph.copy()
df_overall_sale_inv_table['Total Sales (USD)'] = df_overall_sale_inv_table['Total Sales (USD)'].map('${:,.0f}'.format)
df_overall_sale_inv_table['No. of Invoices'] = df_overall_sale_inv_table['No. of Invoices'].map('{:,.0f}'.format)
fig_table_diffSales = plotCharts.table_diffSales_previousYear(df_overall_sale_inv_table)

# ------------------------------------------------
# Cost and Gross Profit Trend 2012-2022
df_overall_cost_profit_graph = pd.DataFrame(fr_overall_cost_profit)
df_overall_cost_profit_graph.reset_index(inplace=True, drop=True)
fig_overall_cost_profit = plotCharts.plot_Overall_Cost_Profit(df_overall_cost_profit_graph)

# Table Cost and Gross Profit Trend 2012-2022
df_overall_cost_profit_table = df_overall_cost_profit_graph.copy()
df_overall_cost_profit_table['Total Sales (USD)'] = df_overall_cost_profit_table['Total Sales (USD)'].map('${:,.0f}'.format)
df_overall_cost_profit_table['Total Cost (USD)'] = df_overall_cost_profit_table['Total Cost (USD)'].map('${:,.0f}'.format)
df_overall_cost_profit_table['Gross Profit (USD)'] = df_overall_cost_profit_table['Gross Profit (USD)'].map('${:,.0f}'.format)
fig_table_cost_profit = plotCharts.table_cost_profit(df_overall_cost_profit_table)

layout = html.Div([
    dbc.Row(
        [
            dbc.Col([
                dbc.Row([
                    html.H5("SALES HISTORICAL TREND 2012-2022"),
                    dcc.Graph(figure=fig_overall_sale_inv),
                ], className="text-center m-4"),
                dbc.Row(
                    dcc.Graph(figure=fig_table_diffSales),
                    className="text-center m-4"),
            ]),

            dbc.Col([
                dbc.Row([
                    html.H5("COST AND GROSS PROFIT HISTORICAL TREND 2012-2022"),
                    dcc.Graph(figure=fig_overall_cost_profit),
                ], className="text-center m-4"),
                dbc.Row(
                    dcc.Graph(figure=fig_table_cost_profit),
                    className="text-center m-4"),
            ]),
        ], className="m-4",
    ),
])
