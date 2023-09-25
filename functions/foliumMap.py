import geopandas as gpd # pip install geopandas
import folium # pip install folium
from shapely import wkt # no need install


def convert_gpd_groupBy(df):
    df_gpd_map = df[['Store Name', 'Address', 'Zip Code', 'City', 'County', 'Store Location']]

    # need to drop nan values before doing anything
    df_gpd_map = df_gpd_map.dropna(subset=['Store Location'])

    # convert to str
    df_gpd_map['Store Location'] = df_gpd_map['Store Location'].astype(str)

    # use shapely.wkt sub-module to parse wkt format
    df_gpd_map['geometry'] = gpd.GeoSeries.from_wkt(df_gpd_map['Store Location'])

    # Turn geometry column into lat/long columns in Geodataframe
    df_gpd_map['Longitude'] = df_gpd_map.geometry.apply(lambda p: p.x)
    df_gpd_map['Latitude'] = df_gpd_map.geometry.apply(lambda p: p.y)

    df_gpd_map_groupBy = df_gpd_map.groupby('Store Name').value_counts().reset_index()
    return df_gpd_map_groupBy

def map_of_stores(df):
    m = folium.Map(tiles="OpenStreetMap",
                     location=[df['Latitude'].mean(), df['Longitude'].mean()],
                     zoom_start=5)

    for i in range(len(df)):
        html = f"""
            <h5>Store Name:<br>{df.iloc[i]['Store Name']}</h5>
            <p>{df.iloc[i]['Address']}<br>
               {df.iloc[i]['City']}, IOWA, {df.iloc[i]['Zip Code']}<br>
               USA, {df.iloc[i]['County']}
            </p>
            """

        iframe = folium.IFrame(html=html, width=280, height=180)
        popup = folium.Popup(iframe, max_width=2650)

        folium.Marker(
            location=[df.iloc[i]['Latitude'], df.iloc[i]['Longitude']],
            popup=popup,
            icon=folium.DivIcon(html=f"""
                <div><svg>
                    <circle cx="5" cy="5" r="5" fill="#69b3a2" opacity="0.8"/>
                    <rect x="3", y="3" width="3" height="4", fill="red", opacity=".8" 
                </svg></div>""")
        ).add_to(m)

    return m