from components import cards

df12 = cards.df_2012
df13 = cards.df_2013
df14 = cards.df_2014
df15 = cards.df_2015
df16 = cards.df_2016
df17 = cards.df_2017
df18 = cards.df_2018
df19 = cards.df_2019
df20 = cards.df_2020
df21 = cards.df_2021
df22 = cards.df_2022

def lst_search_result(year_val, keyword):
    global lst_result
    if year_val== '2012':
        lst_key_cat_search = df12[df12['Category Name'].str.contains(keyword) == True].groupby('Category Name').size().index.tolist()
        lst_key_store_search = df12[df12['Store Name'].str.contains(keyword) == True].groupby('Store Name').size().index.tolist()
        lst_key_vendor_search = df12[df12['Vendor Name'].str.contains(keyword) == True].groupby('Vendor Name').size().index.tolist()
        lst_key_item_search = df12[df12['Item Description'].str.contains(keyword) == True].groupby('Item Description').size().index.tolist()

        lst_result = [x for n in (lst_key_cat_search, lst_key_store_search,
                                  lst_key_vendor_search, lst_key_item_search) for x in n]

    if year_val== '2013':
        lst_key_cat_search = df13[df13['Category Name'].str.contains(keyword) == True].groupby('Category Name').size().index.tolist()
        lst_key_store_search = df13[df13['Store Name'].str.contains(keyword) == True].groupby('Store Name').size().index.tolist()
        lst_key_vendor_search = df13[df13['Vendor Name'].str.contains(keyword) == True].groupby('Vendor Name').size().index.tolist()
        lst_key_item_search = df13[df13['Item Description'].str.contains(keyword) == True].groupby('Item Description').size().index.tolist()

        lst_result = [x for n in (lst_key_cat_search, lst_key_store_search,
                                  lst_key_vendor_search, lst_key_item_search) for x in n]

    if year_val== '2014':
        lst_key_cat_search = df14[df14['Category Name'].str.contains(keyword) == True].groupby('Category Name').size().index.tolist()
        lst_key_store_search = df14[df14['Store Name'].str.contains(keyword) == True].groupby('Store Name').size().index.tolist()
        lst_key_vendor_search = df14[df14['Vendor Name'].str.contains(keyword) == True].groupby('Vendor Name').size().index.tolist()
        lst_key_item_search = df14[df14['Item Description'].str.contains(keyword) == True].groupby('Item Description').size().index.tolist()

        lst_result = [x for n in (lst_key_cat_search, lst_key_store_search,
                                  lst_key_vendor_search, lst_key_item_search) for x in n]

    if year_val== '2015':
        lst_key_cat_search = df15[df15['Category Name'].str.contains(keyword) == True].groupby('Category Name').size().index.tolist()
        lst_key_store_search = df15[df15['Store Name'].str.contains(keyword) == True].groupby('Store Name').size().index.tolist()
        lst_key_vendor_search = df15[df15['Vendor Name'].str.contains(keyword) == True].groupby('Vendor Name').size().index.tolist()
        lst_key_item_search = df15[df15['Item Description'].str.contains(keyword) == True].groupby('Item Description').size().index.tolist()

        lst_result = [x for n in (lst_key_cat_search, lst_key_store_search,
                                  lst_key_vendor_search, lst_key_item_search) for x in n]

    if year_val== '2016':
        lst_key_cat_search = df16[df16['Category Name'].str.contains(keyword) == True].groupby('Category Name').size().index.tolist()
        lst_key_store_search = df16[df16['Store Name'].str.contains(keyword) == True].groupby('Store Name').size().index.tolist()
        lst_key_vendor_search = df16[df16['Vendor Name'].str.contains(keyword) == True].groupby('Vendor Name').size().index.tolist()
        lst_key_item_search = df16[df16['Item Description'].str.contains(keyword) == True].groupby('Item Description').size().index.tolist()

        lst_result = [x for n in (lst_key_cat_search, lst_key_store_search,
                                  lst_key_vendor_search, lst_key_item_search) for x in n]

    if year_val== '2017':
        lst_key_cat_search = df17[df17['Category Name'].str.contains(keyword) == True].groupby('Category Name').size().index.tolist()
        lst_key_store_search = df17[df17['Store Name'].str.contains(keyword) == True].groupby('Store Name').size().index.tolist()
        lst_key_vendor_search = df17[df17['Vendor Name'].str.contains(keyword) == True].groupby('Vendor Name').size().index.tolist()
        lst_key_item_search = df17[df17['Item Description'].str.contains(keyword) == True].groupby('Item Description').size().index.tolist()

        lst_result = [x for n in (lst_key_cat_search, lst_key_store_search,
                                  lst_key_vendor_search, lst_key_item_search) for x in n]

    if year_val== '2018':
        lst_key_cat_search = df18[df18['Category Name'].str.contains(keyword) == True].groupby('Category Name').size().index.tolist()
        lst_key_store_search = df18[df18['Store Name'].str.contains(keyword) == True].groupby('Store Name').size().index.tolist()
        lst_key_vendor_search = df18[df18['Vendor Name'].str.contains(keyword) == True].groupby('Vendor Name').size().index.tolist()
        lst_key_item_search = df18[df18['Item Description'].str.contains(keyword) == True].groupby('Item Description').size().index.tolist()

        lst_result = [x for n in (lst_key_cat_search, lst_key_store_search,
                                  lst_key_vendor_search, lst_key_item_search) for x in n]

    if year_val== '2019':
        lst_key_cat_search = df19[df19['Category Name'].str.contains(keyword) == True].groupby('Category Name').size().index.tolist()
        lst_key_store_search = df19[df19['Store Name'].str.contains(keyword) == True].groupby('Store Name').size().index.tolist()
        lst_key_vendor_search = df19[df19['Vendor Name'].str.contains(keyword) == True].groupby('Vendor Name').size().index.tolist()
        lst_key_item_search = df19[df19['Item Description'].str.contains(keyword) == True].groupby('Item Description').size().index.tolist()

        lst_result = [x for n in (lst_key_cat_search, lst_key_store_search,
                                  lst_key_vendor_search, lst_key_item_search) for x in n]

    if year_val== '2020':
        lst_key_cat_search = df20[df20['Category Name'].str.contains(keyword) == True].groupby('Category Name').size().index.tolist()
        lst_key_store_search = df20[df20['Store Name'].str.contains(keyword) == True].groupby('Store Name').size().index.tolist()
        lst_key_vendor_search = df20[df20['Vendor Name'].str.contains(keyword) == True].groupby('Vendor Name').size().index.tolist()
        lst_key_item_search = df20[df20['Item Description'].str.contains(keyword) == True].groupby('Item Description').size().index.tolist()

        lst_result = [x for n in (lst_key_cat_search, lst_key_store_search,
                                  lst_key_vendor_search, lst_key_item_search) for x in n]

    if year_val== '2021':
        lst_key_cat_search = df21[df21['Category Name'].str.contains(keyword) == True].groupby('Category Name').size().index.tolist()
        lst_key_store_search = df21[df21['Store Name'].str.contains(keyword) == True].groupby('Store Name').size().index.tolist()
        lst_key_vendor_search = df21[df21['Vendor Name'].str.contains(keyword) == True].groupby('Vendor Name').size().index.tolist()
        lst_key_item_search = df21[df21['Item Description'].str.contains(keyword) == True].groupby('Item Description').size().index.tolist()

        lst_result = [x for n in (lst_key_cat_search, lst_key_store_search,
                                  lst_key_vendor_search, lst_key_item_search) for x in n]

    if year_val== '2022':
        lst_key_cat_search = df22[df22['Category Name'].str.contains(keyword) == True].groupby('Category Name').size().index.tolist()
        lst_key_store_search = df22[df22['Store Name'].str.contains(keyword) == True].groupby('Store Name').size().index.tolist()
        lst_key_vendor_search = df22[df22['Vendor Name'].str.contains(keyword) == True].groupby('Vendor Name').size().index.tolist()
        lst_key_item_search = df22[df22['Item Description'].str.contains(keyword) == True].groupby('Item Description').size().index.tolist()

        lst_result = [x for n in (lst_key_cat_search, lst_key_store_search,
                                  lst_key_vendor_search, lst_key_item_search) for x in n]

    return lst_result


def filter_df_byFullKeyword(year_val, keyword):
    # if year == '2012':
    # To prevent the warning SettingWithCopyWarning, the solution is to explicitly tell
    # pandas to make a copy when we create the new dataframe:
    global df_filter

    if year_val== '2012':
        df_item = df12.loc[df12['Item Description'] == keyword].copy()
        df_cat = df12.loc[df12['Category Name'] == keyword].copy()
        df_vendor = df12.loc[df12['Vendor Name'] == keyword].copy()
        df_store = df12.loc[df12['Store Name'] == keyword].copy()

        if len(df_item) > 0:
            df_filter = df_item
        elif len(df_cat) > 0:
            df_filter = df_cat
        elif len(df_vendor) > 0:
            df_filter = df_vendor
        elif len(df_store) > 0:
            df_filter = df_store

    if year_val == '2013':
        df_item = df13.loc[df13['Item Description'] == keyword].copy()
        df_cat = df13.loc[df13['Category Name'] == keyword].copy()
        df_vendor = df13.loc[df13['Vendor Name'] == keyword].copy()
        df_store = df13.loc[df13['Store Name'] == keyword].copy()

        if len(df_item) > 0:
            df_filter = df_item
        elif len(df_cat) > 0:
            df_filter = df_cat
        elif len(df_vendor) > 0:
            df_filter = df_vendor
        elif len(df_store) > 0:
            df_filter = df_store

    if year_val == '2014':
        df_item = df14.loc[df14['Item Description'] == keyword].copy()
        df_cat = df14.loc[df14['Category Name'] == keyword].copy()
        df_vendor = df14.loc[df14['Vendor Name'] == keyword].copy()
        df_store = df14.loc[df14['Store Name'] == keyword].copy()

        if len(df_item) > 0:
            df_filter = df_item
        elif len(df_cat) > 0:
            df_filter = df_cat
        elif len(df_vendor) > 0:
            df_filter = df_vendor
        elif len(df_store) > 0:
            df_filter = df_store

    if year_val == '2015':
        df_item = df15.loc[df15['Item Description'] == keyword].copy()
        df_cat = df15.loc[df15['Category Name'] == keyword].copy()
        df_vendor = df15.loc[df15['Vendor Name'] == keyword].copy()
        df_store = df15.loc[df15['Store Name'] == keyword].copy()

        if len(df_item) > 0:
            df_filter = df_item
        elif len(df_cat) > 0:
            df_filter = df_cat
        elif len(df_vendor) > 0:
            df_filter = df_vendor
        elif len(df_store) > 0:
            df_filter = df_store

    if year_val == '2016':
        df_item = df16.loc[df16['Item Description'] == keyword].copy()
        df_cat = df16.loc[df16['Category Name'] == keyword].copy()
        df_vendor = df16.loc[df16['Vendor Name'] == keyword].copy()
        df_store = df16.loc[df16['Store Name'] == keyword].copy()

        if len(df_item) > 0:
            df_filter = df_item
        elif len(df_cat) > 0:
            df_filter = df_cat
        elif len(df_vendor) > 0:
            df_filter = df_vendor
        elif len(df_store) > 0:
            df_filter = df_store

    if year_val == '2017':
        df_item = df17.loc[df17['Item Description'] == keyword].copy()
        df_cat = df17.loc[df17['Category Name'] == keyword].copy()
        df_vendor = df17.loc[df17['Vendor Name'] == keyword].copy()
        df_store = df17.loc[df17['Store Name'] == keyword].copy()

        if len(df_item) > 0:
            df_filter = df_item
        elif len(df_cat) > 0:
            df_filter = df_cat
        elif len(df_vendor) > 0:
            df_filter = df_vendor
        elif len(df_store) > 0:
            df_filter = df_store

    if year_val == '2018':
        df_item = df18.loc[df18['Item Description'] == keyword].copy()
        df_cat = df18.loc[df18['Category Name'] == keyword].copy()
        df_vendor = df18.loc[df18['Vendor Name'] == keyword].copy()
        df_store = df18.loc[df18['Store Name'] == keyword].copy()

        if len(df_item) > 0:
            df_filter = df_item
        elif len(df_cat) > 0:
            df_filter = df_cat
        elif len(df_vendor) > 0:
            df_filter = df_vendor
        elif len(df_store) > 0:
            df_filter = df_store

    if year_val == '2019':
        df_item = df19.loc[df19['Item Description'] == keyword].copy()
        df_cat = df19.loc[df19['Category Name'] == keyword].copy()
        df_vendor = df19.loc[df19['Vendor Name'] == keyword].copy()
        df_store = df19.loc[df19['Store Name'] == keyword].copy()

        if len(df_item) > 0:
            df_filter = df_item
        elif len(df_cat) > 0:
            df_filter = df_cat
        elif len(df_vendor) > 0:
            df_filter = df_vendor
        elif len(df_store) > 0:
            df_filter = df_store

    if year_val == '2020':
        df_item = df20.loc[df20['Item Description'] == keyword].copy()
        df_cat = df20.loc[df20['Category Name'] == keyword].copy()
        df_vendor = df20.loc[df20['Vendor Name'] == keyword].copy()
        df_store = df20.loc[df20['Store Name'] == keyword].copy()

        if len(df_item) > 0:
            df_filter = df_item
        elif len(df_cat) > 0:
            df_filter = df_cat
        elif len(df_vendor) > 0:
            df_filter = df_vendor
        elif len(df_store) > 0:
            df_filter = df_store

    if year_val == '2021':
        df_item = df21.loc[df21['Item Description'] == keyword].copy()
        df_cat = df21.loc[df21['Category Name'] == keyword].copy()
        df_vendor = df21.loc[df21['Vendor Name'] == keyword].copy()
        df_store = df21.loc[df21['Store Name'] == keyword].copy()

        if len(df_item) > 0:
            df_filter = df_item
        elif len(df_cat) > 0:
            df_filter = df_cat
        elif len(df_vendor) > 0:
            df_filter = df_vendor
        elif len(df_store) > 0:
            df_filter = df_store

    if year_val == '2022':
        df_item = df22.loc[df22['Item Description'] == keyword].copy()
        df_cat = df22.loc[df22['Category Name'] == keyword].copy()
        df_vendor = df22.loc[df22['Vendor Name'] == keyword].copy()
        df_store = df22.loc[df22['Store Name'] == keyword].copy()

        if len(df_item) > 0:
            df_filter = df_item
        elif len(df_cat) > 0:
            df_filter = df_cat
        elif len(df_vendor) > 0:
            df_filter = df_vendor
        elif len(df_store) > 0:
            df_filter = df_store

    return df_filter


def filter_overall(df_filter):
    sales = df_filter['Sale (Dollars)'].sum().round(1)
    cost = (df_filter['State Bottle Cost'] * df_filter['Bottles Sold']).sum().round(1)
    grossProfit = (sales - cost).round(1)
    inv = len(df_filter['Invoice/Item Number'])
    bottleSold = df_filter['Bottles Sold'].sum()
    volumeSold = df_filter['Volume Sold (Gallons)'].sum().round(1)

    return sales, cost, grossProfit, inv, bottleSold, volumeSold