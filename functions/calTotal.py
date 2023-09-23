import pandas as pd
from pandas import CategoricalDtype

month_category = CategoricalDtype(categories=["January", "February", "March", "April", "May", "June",
                                              "July", "August", "September", "October", "November",
                                              "December"], ordered=True)

dow_category = CategoricalDtype(categories=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
                                            "Saturday", "Sunday"], ordered=True)


def total_sales_allYear(df_2012, df_2013, df_2014, df_2015, df_2016, df_2017, df_2018, df_2019, df_2020, df_2021,
                        df_2022):
    sale2012 = df_2012['Sale (Dollars)'].sum().round(1)
    sale2013 = df_2013['Sale (Dollars)'].sum().round(1)
    sale2014 = df_2014['Sale (Dollars)'].sum().round(1)
    sale2015 = df_2015['Sale (Dollars)'].sum().round(1)
    sale2016 = df_2016['Sale (Dollars)'].sum().round(1)
    sale2017 = df_2017['Sale (Dollars)'].sum().round(1)
    sale2018 = df_2018['Sale (Dollars)'].sum().round(1)
    sale2019 = df_2019['Sale (Dollars)'].sum().round(1)
    sale2020 = df_2020['Sale (Dollars)'].sum().round(1)
    sale2021 = df_2021['Sale (Dollars)'].sum().round(1)
    sale2022 = df_2022['Sale (Dollars)'].sum().round(1)

    return sale2012, sale2013, sale2014, sale2015, sale2016, sale2017, sale2018, sale2019, sale2020, sale2021, sale2022


def total_inv_allYear(df_2012, df_2013, df_2014, df_2015, df_2016, df_2017, df_2018, df_2019, df_2020, df_2021,
                      df_2022):
    inv2012 = len(df_2012['Invoice/Item Number'])
    inv2013 = len(df_2013['Invoice/Item Number'])
    inv2014 = len(df_2014['Invoice/Item Number'])
    inv2015 = len(df_2015['Invoice/Item Number'])
    inv2016 = len(df_2016['Invoice/Item Number'])
    inv2017 = len(df_2017['Invoice/Item Number'])
    inv2018 = len(df_2018['Invoice/Item Number'])
    inv2019 = len(df_2019['Invoice/Item Number'])
    inv2020 = len(df_2020['Invoice/Item Number'])
    inv2021 = len(df_2021['Invoice/Item Number'])
    inv2022 = len(df_2022['Invoice/Item Number'])

    return inv2012, inv2013, inv2014, inv2015, inv2016, inv2017, inv2018, inv2019, inv2020, inv2021, inv2022


def total_cost_allYear(df_2012, df_2013, df_2014, df_2015, df_2016, df_2017, df_2018, df_2019, df_2020, df_2021,
                       df_2022):
    cost2012 = (df_2012['State Bottle Cost'] * df_2012['Bottles Sold']).sum().round(1)
    cost2013 = (df_2013['State Bottle Cost'] * df_2013['Bottles Sold']).sum().round(1)
    cost2014 = (df_2014['State Bottle Cost'] * df_2014['Bottles Sold']).sum().round(1)
    cost2015 = (df_2015['State Bottle Cost'] * df_2015['Bottles Sold']).sum().round(1)
    cost2016 = (df_2016['State Bottle Cost'] * df_2016['Bottles Sold']).sum().round(1)
    cost2017 = (df_2017['State Bottle Cost'] * df_2017['Bottles Sold']).sum().round(1)
    cost2018 = (df_2018['State Bottle Cost'] * df_2018['Bottles Sold']).sum().round(1)
    cost2019 = (df_2019['State Bottle Cost'] * df_2019['Bottles Sold']).sum().round(1)
    cost2020 = (df_2020['State Bottle Cost'] * df_2020['Bottles Sold']).sum().round(1)
    cost2021 = (df_2021['State Bottle Cost'] * df_2021['Bottles Sold']).sum().round(1)
    cost2022 = (df_2022['State Bottle Cost'] * df_2022['Bottles Sold']).sum().round(1)

    return cost2012, cost2013, cost2014, cost2015, cost2016, cost2017, cost2018, cost2019, cost2020, cost2021, cost2022


def total_grossProfit_allYear(sale2012, sale2013, sale2014, sale2015, sale2016, sale2017, sale2018,
                              sale2019, sale2020, sale2021, sale2022, cost2012, cost2013, cost2014,
                              cost2015, cost2016, cost2017, cost2018, cost2019, cost2020, cost2021, cost2022):
    grossProfit2012 = (sale2012 - cost2012).round(1)
    grossProfit2013 = (sale2013 - cost2013).round(1)
    grossProfit2014 = (sale2014 - cost2014).round(1)
    grossProfit2015 = (sale2015 - cost2015).round(1)
    grossProfit2016 = (sale2016 - cost2016).round(1)
    grossProfit2017 = (sale2017 - cost2017).round(1)
    grossProfit2018 = (sale2018 - cost2018).round(1)
    grossProfit2019 = (sale2019 - cost2019).round(1)
    grossProfit2020 = (sale2020 - cost2020).round(1)
    grossProfit2021 = (sale2021 - cost2021).round(1)
    grossProfit2022 = (sale2022 - cost2022).round(1)

    return (grossProfit2012, grossProfit2013, grossProfit2014, grossProfit2015, grossProfit2016, grossProfit2017,
            grossProfit2018, grossProfit2019, grossProfit2020, grossProfit2021, grossProfit2022)


def total_bottleSold_allYear(df_2012, df_2013, df_2014, df_2015, df_2016, df_2017, df_2018, df_2019, df_2020, df_2021,
                             df_2022):
    bottleSold2012 = df_2012['Bottles Sold'].sum()
    bottleSold2013 = df_2013['Bottles Sold'].sum()
    bottleSold2014 = df_2014['Bottles Sold'].sum()
    bottleSold2015 = df_2015['Bottles Sold'].sum()
    bottleSold2016 = df_2016['Bottles Sold'].sum()
    bottleSold2017 = df_2017['Bottles Sold'].sum()
    bottleSold2018 = df_2018['Bottles Sold'].sum()
    bottleSold2019 = df_2019['Bottles Sold'].sum()
    bottleSold2020 = df_2020['Bottles Sold'].sum()
    bottleSold2021 = df_2021['Bottles Sold'].sum()
    bottleSold2022 = df_2022['Bottles Sold'].sum()

    return (bottleSold2012, bottleSold2013, bottleSold2014, bottleSold2015, bottleSold2016,
            bottleSold2017, bottleSold2018, bottleSold2019, bottleSold2020, bottleSold2021, bottleSold2022)


def total_volumeSold_allYear(df_2012, df_2013, df_2014, df_2015, df_2016, df_2017, df_2018, df_2019, df_2020, df_2021,
                             df_2022):
    volumeSold2012 = df_2012['Volume Sold (Gallons)'].sum().round(1)
    volumeSold2013 = df_2013['Volume Sold (Gallons)'].sum().round(1)
    volumeSold2014 = df_2014['Volume Sold (Gallons)'].sum().round(1)
    volumeSold2015 = df_2015['Volume Sold (Gallons)'].sum().round(1)
    volumeSold2016 = df_2016['Volume Sold (Gallons)'].sum().round(1)
    volumeSold2017 = df_2017['Volume Sold (Gallons)'].sum().round(1)
    volumeSold2018 = df_2018['Volume Sold (Gallons)'].sum().round(1)
    volumeSold2019 = df_2019['Volume Sold (Gallons)'].sum().round(1)
    volumeSold2020 = df_2020['Volume Sold (Gallons)'].sum().round(1)
    volumeSold2021 = df_2021['Volume Sold (Gallons)'].sum().round(1)
    volumeSold2022 = df_2022['Volume Sold (Gallons)'].sum().round(1)

    return (volumeSold2012, volumeSold2013, volumeSold2014, volumeSold2015, volumeSold2016,
            volumeSold2017, volumeSold2018, volumeSold2019, volumeSold2020, volumeSold2021, volumeSold2022)

def pct_sales_yearAfterBefore(sale2012, sale2013, sale2014, sale2015, sale2016, sale2017, sale2018, sale2019, sale2020, sale2021, sale2022):
    pct_sale_2013_2012 = str(((sale2013 - sale2012) / sale2012 * 100).round(1)) + '%'
    pct_sale_2014_2013 = str(((sale2014 - sale2013) / sale2013 * 100).round(1)) + '%'
    pct_sale_2015_2014 = str(((sale2015 - sale2014) / sale2014 * 100).round(1)) + '%'
    pct_sale_2016_2015 = str(((sale2016 - sale2015) / sale2015 * 100).round(1)) + '%'
    pct_sale_2017_2016 = str(((sale2017 - sale2016) / sale2016 * 100).round(1)) + '%'
    pct_sale_2018_2017 = str(((sale2018 - sale2017) / sale2017 * 100).round(1)) + '%'
    pct_sale_2019_2018 = str(((sale2019 - sale2018) / sale2018 * 100).round(1)) + '%'
    pct_sale_2020_2019 = str(((sale2020 - sale2019) / sale2019 * 100).round(1)) + '%'
    pct_sale_2021_2020 = str(((sale2021 - sale2020) / sale2020 * 100).round(1)) + '%'
    pct_sale_2022_2021 = str(((sale2022 - sale2021) / sale2021 * 100).round(1)) + '%'

    return (pct_sale_2013_2012, pct_sale_2014_2013, pct_sale_2015_2014, pct_sale_2016_2015, pct_sale_2017_2016,
            pct_sale_2018_2017, pct_sale_2019_2018, pct_sale_2020_2019, pct_sale_2021_2020, pct_sale_2022_2021)

def pct_inv_yearAfterBefore(inv2012, inv2013, inv2014, inv2015, inv2016, inv2017, inv2018, inv2019, inv2020, inv2021, inv2022):
    pct_inv_2013_2012 = str(round(((inv2013 - inv2012) / inv2012 * 100), 1)) + '%'
    pct_inv_2014_2013 = str(round(((inv2014 - inv2013) / inv2013 * 100), 1)) + '%'
    pct_inv_2015_2014 = str(round(((inv2015 - inv2014) / inv2014 * 100), 1)) + '%'
    pct_inv_2016_2015 = str(round(((inv2016 - inv2015) / inv2015 * 100), 1)) + '%'
    pct_inv_2017_2016 = str(round(((inv2017 - inv2016) / inv2016 * 100), 1)) + '%'
    pct_inv_2018_2017 = str(round(((inv2018 - inv2017) / inv2017 * 100), 1)) + '%'
    pct_inv_2019_2018 = str(round(((inv2019 - inv2018) / inv2018 * 100), 1)) + '%'
    pct_inv_2020_2019 = str(round(((inv2020 - inv2019) / inv2019 * 100), 1)) + '%'
    pct_inv_2021_2020 = str(round(((inv2021 - inv2020) / inv2020 * 100), 1)) + '%'
    pct_inv_2022_2021 = str(round(((inv2022 - inv2021) / inv2021 * 100), 1)) + '%'

    return (pct_inv_2013_2012, pct_inv_2014_2013, pct_inv_2015_2014, pct_inv_2016_2015, pct_inv_2017_2016,
            pct_inv_2018_2017, pct_inv_2019_2018, pct_inv_2020_2019, pct_inv_2021_2020, pct_inv_2022_2021)

def human_format(num):
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    # add more suffixes if you need them
    return '%.1f%s' % (num, ['', 'K', 'M', 'G', 'T', 'P'][magnitude])

def total_general_byYear(sale, cost, grossProfit, inv, bottleSold, volumeSold):
    sale_str = '$' + human_format(sale)
    cost_str = '$' + human_format(cost)
    grossProfit_str = '$' + human_format(grossProfit)
    inv_str = human_format(inv)
    bottleSold_str = human_format(bottleSold)
    volumeSold_str = human_format(volumeSold)

    return sale_str, cost_str, grossProfit_str, inv_str, bottleSold_str, volumeSold_str

def diff_sales_yearAfterBefore(sale2012, sale2013, sale2014, sale2015, sale2016, sale2017, sale2018, sale2019, sale2020, sale2021, sale2022):
    diff_sale_2013_2012 = '$' + human_format(sale2013 - sale2012)
    diff_sale_2014_2013 = '$' + human_format(sale2014 - sale2013)
    diff_sale_2015_2014 = '$' + human_format(sale2015 - sale2014)
    diff_sale_2016_2015 = '$' + human_format(sale2016 - sale2015)
    diff_sale_2017_2016 = '$' + human_format(sale2017 - sale2016)
    diff_sale_2018_2017 = '$' + human_format(sale2018 - sale2017)
    diff_sale_2019_2018 = '$' + human_format(sale2019 - sale2018)
    diff_sale_2020_2019 = '$' + human_format(sale2020 - sale2019)
    diff_sale_2021_2020 = '$' + human_format(sale2021 - sale2020)
    diff_sale_2022_2021 = '$' + human_format(sale2022 - sale2021)

    return (diff_sale_2013_2012, diff_sale_2014_2013, diff_sale_2015_2014, diff_sale_2016_2015, diff_sale_2017_2016,
            diff_sale_2018_2017, diff_sale_2019_2018, diff_sale_2020_2019, diff_sale_2021_2020, diff_sale_2022_2021)

def diff_cost_yearAfterBefore(cost2012, cost2013, cost2014, cost2015, cost2016, cost2017, cost2018, cost2019, cost2020, cost2021, cost2022):
    diff_cost_2013_2012 = human_format(cost2013 - cost2012)
    diff_cost_2014_2013 = human_format(cost2014 - cost2013)
    diff_cost_2015_2014 = human_format(cost2015 - cost2014)
    diff_cost_2016_2015 = human_format(cost2016 - cost2015)
    diff_cost_2017_2016 = human_format(cost2017 - cost2016)
    diff_cost_2018_2017 = human_format(cost2018 - cost2017)
    diff_cost_2019_2018 = human_format(cost2019 - cost2018)
    diff_cost_2020_2019 = human_format(cost2020 - cost2019)
    diff_cost_2021_2020 = human_format(cost2021 - cost2020)
    diff_cost_2022_2021 = human_format(cost2022 - cost2021)

    return (diff_cost_2013_2012, diff_cost_2014_2013, diff_cost_2015_2014, diff_cost_2016_2015, diff_cost_2017_2016,
            diff_cost_2018_2017, diff_cost_2019_2018, diff_cost_2020_2019, diff_cost_2021_2020, diff_cost_2022_2021)

def diff_grossProfit_yearAfterBefore(grossProfit2012, grossProfit2013, grossProfit2014, grossProfit2015, grossProfit2016, grossProfit2017, grossProfit2018, grossProfit2019, grossProfit2020, grossProfit2021, grossProfit2022):
    diff_grossProfit_2013_2012 = human_format(grossProfit2013 - grossProfit2012)
    diff_grossProfit_2014_2013 = human_format(grossProfit2014 - grossProfit2013)
    diff_grossProfit_2015_2014 = human_format(grossProfit2015 - grossProfit2014)
    diff_grossProfit_2016_2015 = human_format(grossProfit2016 - grossProfit2015)
    diff_grossProfit_2017_2016 = human_format(grossProfit2017 - grossProfit2016)
    diff_grossProfit_2018_2017 = human_format(grossProfit2018 - grossProfit2017)
    diff_grossProfit_2019_2018 = human_format(grossProfit2019 - grossProfit2018)
    diff_grossProfit_2020_2019 = human_format(grossProfit2020 - grossProfit2019)
    diff_grossProfit_2021_2020 = human_format(grossProfit2021 - grossProfit2020)
    diff_grossProfit_2022_2021 = human_format(grossProfit2022 - grossProfit2021)

    return (diff_grossProfit_2013_2012, diff_grossProfit_2014_2013, diff_grossProfit_2015_2014, diff_grossProfit_2016_2015, diff_grossProfit_2017_2016,
            diff_grossProfit_2018_2017, diff_grossProfit_2019_2018, diff_grossProfit_2020_2019, diff_grossProfit_2021_2020, diff_grossProfit_2022_2021)


def diff_inv_yearAfterBefore(inv2012, inv2013, inv2014, inv2015, inv2016, inv2017, inv2018, inv2019, inv2020, inv2021, inv2022):
    diff_inv_2013_2012 = human_format(inv2013 - inv2012)
    diff_inv_2014_2013 = human_format(inv2014 - inv2013)
    diff_inv_2015_2014 = human_format(inv2015 - inv2014)
    diff_inv_2016_2015 = human_format(inv2016 - inv2015)
    diff_inv_2017_2016 = human_format(inv2017 - inv2016)
    diff_inv_2018_2017 = human_format(inv2018 - inv2017)
    diff_inv_2019_2018 = human_format(inv2019 - inv2018)
    diff_inv_2020_2019 = human_format(inv2020 - inv2019)
    diff_inv_2021_2020 = human_format(inv2021 - inv2020)
    diff_inv_2022_2021 = human_format(inv2022 - inv2021)

    return (diff_inv_2013_2012, diff_inv_2014_2013, diff_inv_2015_2014, diff_inv_2016_2015, diff_inv_2017_2016,
            diff_inv_2018_2017, diff_inv_2019_2018, diff_inv_2020_2019, diff_inv_2021_2020, diff_inv_2022_2021)

def diff_bottleSold_yearAfterBefore(bottleSold2012, bottleSold2013, bottleSold2014, bottleSold2015, bottleSold2016, bottleSold2017, bottleSold2018, bottleSold2019, bottleSold2020, bottleSold2021, bottleSold2022):
    diff_bottleSold_2013_2012 = human_format(bottleSold2013 - bottleSold2012)
    diff_bottleSold_2014_2013 = human_format(bottleSold2014 - bottleSold2013)
    diff_bottleSold_2015_2014 = human_format(bottleSold2015 - bottleSold2014)
    diff_bottleSold_2016_2015 = human_format(bottleSold2016 - bottleSold2015)
    diff_bottleSold_2017_2016 = human_format(bottleSold2017 - bottleSold2016)
    diff_bottleSold_2018_2017 = human_format(bottleSold2018 - bottleSold2017)
    diff_bottleSold_2019_2018 = human_format(bottleSold2019 - bottleSold2018)
    diff_bottleSold_2020_2019 = human_format(bottleSold2020 - bottleSold2019)
    diff_bottleSold_2021_2020 = human_format(bottleSold2021 - bottleSold2020)
    diff_bottleSold_2022_2021 = human_format(bottleSold2022 - bottleSold2021)

    return (diff_bottleSold_2013_2012, diff_bottleSold_2014_2013, diff_bottleSold_2015_2014, diff_bottleSold_2016_2015, diff_bottleSold_2017_2016,
            diff_bottleSold_2018_2017, diff_bottleSold_2019_2018, diff_bottleSold_2020_2019, diff_bottleSold_2021_2020, diff_bottleSold_2022_2021)

def diff_volumeSold_yearAfterBefore(volumeSold2012, volumeSold2013, volumeSold2014, volumeSold2015, volumeSold2016, volumeSold2017, volumeSold2018, volumeSold2019, volumeSold2020, volumeSold2021, volumeSold2022):
    diff_volumeSold_2013_2012 = human_format(volumeSold2013 - volumeSold2012)
    diff_volumeSold_2014_2013 = human_format(volumeSold2014 - volumeSold2013)
    diff_volumeSold_2015_2014 = human_format(volumeSold2015 - volumeSold2014)
    diff_volumeSold_2016_2015 = human_format(volumeSold2016 - volumeSold2015)
    diff_volumeSold_2017_2016 = human_format(volumeSold2017 - volumeSold2016)
    diff_volumeSold_2018_2017 = human_format(volumeSold2018 - volumeSold2017)
    diff_volumeSold_2019_2018 = human_format(volumeSold2019 - volumeSold2018)
    diff_volumeSold_2020_2019 = human_format(volumeSold2020 - volumeSold2019)
    diff_volumeSold_2021_2020 = human_format(volumeSold2021 - volumeSold2020)
    diff_volumeSold_2022_2021 = human_format(volumeSold2022 - volumeSold2021)

    return (diff_volumeSold_2013_2012, diff_volumeSold_2014_2013, diff_volumeSold_2015_2014, diff_volumeSold_2016_2015, diff_volumeSold_2017_2016,
            diff_volumeSold_2018_2017, diff_volumeSold_2019_2018, diff_volumeSold_2020_2019, diff_volumeSold_2021_2020, diff_volumeSold_2022_2021)

def graph_general_byyear(df):
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.strftime('%B').astype(month_category)
    df['Day of Week'] = df['Date'].dt.dayofweek.map({0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday',
                                                     4: 'Friday', 5: 'Saturday', 6: 'Sunday'}).astype(dow_category)

    # Details sale, number of invoices by months in a year
    month_sale = df['Sale (Dollars)'].groupby(df['Month'], observed=True).sum()
    month_inv = df['Month'].value_counts(sort=False)

    # Details sale, number of invoices by day of week
    dow_sale = df['Sale (Dollars)'].groupby(df['Day of Week'], observed=True).sum()
    dow_inv = df['Day of Week'].value_counts(sort=False)

    # sales of months, day of week for heatmap
    m_dow = df['Sale (Dollars)'].groupby([df['Month'], df['Day of Week']], observed=True).sum().reset_index()
    m_dow_df = m_dow.pivot(index='Month', columns='Day of Week')['Sale (Dollars)'].fillna(0)

    return month_sale, month_inv, dow_sale, dow_inv, m_dow_df

def top_Grossing(df):
    top10Item = df.groupby('Item Description')['Sale (Dollars)'].agg(['sum','count'])
    top10_highestItem = top10Item.sort_values(['sum', 'count'], ascending=[False, True]).head(10)

    top10Cat = df.groupby('Category Name')['Sale (Dollars)'].agg(['sum', 'count'])
    top10_highestCat = top10Cat.sort_values(['sum', 'count'], ascending=[False, True]).head(10)

    top10Vendor = df.groupby('Vendor Name')['Sale (Dollars)'].agg(['sum', 'count'])
    top10_highestVendor = top10Vendor.sort_values(['sum', 'count'], ascending=[False, True]).head(10)

    top10Store = df.groupby('Store Name')['Sale (Dollars)'].agg(['sum', 'count'])
    top10_highestStore = top10Store.sort_values(['sum', 'count'], ascending=[False, True]).head(10)

    top10City = df.groupby('City')['Sale (Dollars)'].agg(['sum', 'count'])
    top10_highestCity = top10City.sort_values(['sum', 'count'], ascending=[False, True]).head(10)

    top10County = df.groupby('County')['Sale (Dollars)'].agg(['sum', 'count'])
    top10_highestCounty = top10County.sort_values(['sum', 'count'], ascending=[False, True]).head(10)

    return top10_highestItem, top10_highestCat, top10_highestVendor, top10_highestStore,  top10_highestCity, top10_highestCounty

def top_Consuming(df):
    top10Item = df.groupby('Item Description')['Sale (Dollars)'].agg(['count', 'sum'])
    top10_mostItem = top10Item.sort_values(['count', 'sum'], ascending=[False, True]).head(10)

    top10Cat = df.groupby('Category Name')['Sale (Dollars)'].agg(['count', 'sum'])
    top10_mostCat = top10Cat.sort_values(['count', 'sum'], ascending=[False, True]).head(10)

    top10Vendor = df.groupby('Vendor Name')['Sale (Dollars)'].agg(['count', 'sum'])
    top10_mostVendor = top10Vendor.sort_values(['count', 'sum'], ascending=[False, True]).head(10)

    top10Store = df.groupby('Store Name')['Sale (Dollars)'].agg(['count', 'sum'])
    top10_mostStore = top10Store.sort_values(['count', 'sum'], ascending=[False, True]).head(10)

    top10City = df.groupby('City')['Sale (Dollars)'].agg(['count', 'sum'])
    top10_mostCity = top10City.sort_values(['count', 'sum'], ascending=[False, True]).head(10)

    top10County = df.groupby('County')['Sale (Dollars)'].agg(['count', 'sum'])
    top10_mostCounty = top10County.sort_values(['count', 'sum'], ascending=[False, True]).head(10)

    return top10_mostItem, top10_mostCat, top10_mostVendor, top10_mostStore, top10_mostCity, top10_mostCounty

