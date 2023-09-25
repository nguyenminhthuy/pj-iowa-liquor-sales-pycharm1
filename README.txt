Link dataset: https://data.iowa.gov/Sales-Distribution/Iowa-Liquor-Sales/m3tr-qhgy 
Software needs to be installed
1. Install Python
2. Install Pycharm
-----------------------------------------------------------
3. Install libs needs (open terminal in pycharm to install):

pip install dash dash-bootstrap-components Pillow pandas dash-ag-grid geopandas folium
-----------------------------------------------------------
4. Run project without doing anything

import pandas as pd
from pandas.api.types import CategoricalDtype

import numpy as np

import matplotlib
from matplotlib import pyplot as plt

import datetime as dt

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import geopandas as gpd # pip install geopandas
import folium # pip install folium
from shapely import wkt # no need install