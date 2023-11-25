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