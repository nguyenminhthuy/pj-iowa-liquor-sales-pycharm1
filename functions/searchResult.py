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

        return lst_result