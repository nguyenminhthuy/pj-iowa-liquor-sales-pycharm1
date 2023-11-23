def get_listItem(df):
    df['Item Description'] = df['Item Description'].str.upper()
    lst_item = list(set(df['Item Description']))
    return lst_item

def combined_lst_allYear(lst_2012,lst_2013,lst_2014,lst_2015,lst_2016,lst_2017,lst_2018,lst_2019,lst_2020,lst_2021,lst_2022):
    lst_allTemp = lst_2012+lst_2013+lst_2014+lst_2015+lst_2016+lst_2017+lst_2018+lst_2019+lst_2020+lst_2021+lst_2022
    lst_allItem = sorted(list(set(lst_allTemp)))
    return lst_allItem