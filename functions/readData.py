import pandas as pd

url_2012 = "data/2012_Iowa_Liquor_Sales.csv"
url_2013 = "data/2013_Iowa_Liquor_Sales.csv"
url_2014 = "data/2014_Iowa_Liquor_Sales.csv"
url_2015 = "data/2015_Iowa_Liquor_Sales.csv"
url_2016 = "data/2016_Iowa_Liquor_Sales.csv"
url_2017 = "data/2017_Iowa_Liquor_Sales.csv"
url_2018 = "data/2018_Iowa_Liquor_Sales.csv"
url_2019 = "data/2019_Iowa_Liquor_Sales.csv"
url_2020 = "data/2020_Iowa_Liquor_Sales.csv"
url_2021 = "data/2021_Iowa_Liquor_Sales.csv"
url_2022 = "data/2022_Iowa_Liquor_Sales.csv"


def data_2012():
    df = pd.read_csv(url_2012, low_memory=False)
    return df

def data_2013():
    df = pd.read_csv(url_2013, low_memory=False)
    return df

def data_2014():
    df = pd.read_csv(url_2014, low_memory=False)
    return df

def data_2015():
    df = pd.read_csv(url_2015, low_memory=False)
    return df

def data_2016():
    df = pd.read_csv(url_2016, low_memory=False)
    return df

def data_2017():
    df = pd.read_csv(url_2017, low_memory=False)
    return df

def data_2018():
    df = pd.read_csv(url_2018, low_memory=False)
    return df

def data_2019():
    df = pd.read_csv(url_2019, low_memory=False)
    return df

def data_2020():
    df = pd.read_csv(url_2020, low_memory=False)
    return df

def data_2021():
    df = pd.read_csv(url_2021, low_memory=False)
    return df

def data_2022():
    df = pd.read_csv(url_2022, low_memory=False)
    return df
