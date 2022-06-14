#!/usr/bin/env python
# coding: utf-8

# In[34]:


import streamlit as st
import pandas as pd
import plotly.express as px
import folium 
from folium.plugins import HeatMap
import seaborn as sns
import geopandas as gpd
import shapely
from shapely.geometry import *
from shapely import wkt


# In[29]:


st.set_page_config(
    page_title="EPIC request data",
    layout='wide',
    initial_sidebar_state='auto',
)


# In[ ]:


st.sidebar.title("About")
st.sidebar.info(
    """
    Web App URL: <https://geospatial.streamlitapp.com>
    GitHub repository: <https://github.com/giswqs/streamlit-geospatial>
    """
)
st.sidebar.selectbox(
    'Please select the required category',
    [
        'BY-LAW - ANIMALS',
        'COMMUNITY POLICING',
        'PATROLS',
        'INSPECTIONS & GENERAL',
        'ESCORTS & DUTIES',
        'BY-LAW - PUBLIC PLACES / STREETS',
        'STREET PEOPLE / VAGRANT',
        'STAFF',
        'CRIME',
        'GENERAL OPERATIONS',
        'BY-LAW - DUMPING',
        'SPORTS',
        'BY-LAW - INFORMAL TRADING',
        'BY-LAW - LIQUOR',
        'REPORT',
        'PARKING',
        'MOTOR VEHICLE ACCIDENT',
        'RESIDENTIAL FIRE',
        'ENVIRONMENTAL HAZARD',
        'TRAFFIC (GENERAL)',
        'SOCIAL ASSISTANCE',
        'PECC 107',
        'BY-LAW ELECTRICAL',
        'DRUGS OR NARCOTICS',
        'MOVING VIOLATIONS',
        'SELF-START',
        'FIREWORKS',
        'POLITICAL',
        'BY-LAW: PROBLEM BUILDINGS',
        'COMMERCIAL FIRE',
        'SPECIAL INCIDENTS - FIRE SERVICE',
        'MAJOR INCIDENTS',
        'BY-LAW - NUISANCE / NOISE',
        'BY-LAW ADVERTISING',
        'BY-LAW - SEASHORE',
        'MEDICAL EMERGENCY',
        'CULTURAL / MUSIC',
        'THEFT',
        'MARINE INCIDENT',
        'ATTACKS ON COUNCIL MEMBERS / STAFF',
        'PROJECTS',
        'TRAINING (EXTERNAL)',
        'BY-LAW - GRAFFITI',
        'TECHNICAL RESCUE',
        'INFORMATION',
        'TRAUMA EMERGENCY - ACCIDENTAL INJURY',
        'ALARMS',
        'MISCELLANEOUS HAZMAT',
        'BY-LAW - LAND USAGE',
        'MUTUAL AID RESCUE',
        'TRAUMA EMERGENCY - ASSAULT',
        'SPECIAL INCIDENTS',
        'LIQUID HAZMAT',
        'OTHER FIRE',
        'WILDERNESS SEARCH AND RESCUE',
        'VEHICLE MOVEMENT',
        'SITE VISIT',
        'CHEMICAL HAZMAT',
        'EDUCATION',
        'DAMAGE AND THEFT TO COCT PROPERTY',
        ]
    )


# In[25]:


# Get the data from url. Ensure it is cached.
@st.cache(persist=True, suppress_st_warning=True)
def load_data():
    df=pd.read_csv('https://raw.githubusercontent.com/wllrya002/request_types/main/20220614_190838geocoded_cleaned_dataset.csv', encoding='latin-1')
    df['geometry']=df['geometry'].apply(lambda x: wkt.loads(x))
    gdf=gpd.GeoDataFrame(df, geometry='geometry', crs='EPSG:4326')
    
    return gdf


# In[19]:


# @st.cache(persist=True, suppress_st_warning=True)
# def display_map(df):
#     st.subheader(" Displaying Point based map")
#     px.set_mapbox_access_token(
#         "pk.eyJ1Ijoic2hha2Fzb20iLCJhIjoiY2plMWg1NGFpMXZ5NjJxbjhlM2ttN3AwbiJ9.RtGYHmreKiyBfHuElgYq_w")
#     fig = px.scatter_mapbox(df, lat='lat_final', lon='lon_final', color="METHOD", zoom=10)
#     return fig


# In[14]:


def heat_map(df):
    locs = zip(df['lon_final'], df['lat_final'])
    m = folium.Map([18.459778, -34.270836], tiles='stamentoner', zoom_start=12)
    HeatMap(locs).add_to(m)
    return st.markdown(m._repr_html_(), unsafe_allow_html=True)


# In[ ]:


def main():
    df_data = load_data()
    
    #Categories list:
    cats=list(df_data['Category'].unique())
    
#     st.subheader(“Heat Map”)
    heat_map(df_data)


# In[ ]:


st.write("")
st.markdown('# COVID-19 Data and Reporting')
st.write("")
st.write("")
st.markdown("""
COVID-Local provides basic key metrics against which to assess pandemic response and progress toward reopening.  
Phase 2: Initial re-opening: Current esetimate of <25 cases per 100,000 population per day  
Phase 3: Economic recovery: Current estimate of <10 cases per 100,000 population per day   
*daily testing data currently available only for Los Angeles County, Orange County, and San Diego County  
for more details related to thresholds please see  
See more at https://www.covidlocal.org/metrics/.    
For additional information please contact *epicenter@ucdavis.edu* or visit https://ohi.vetmed.ucdavis.edu/centers/epicenter-disease-dynamics.  
""")


# In[20]:


if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:





# In[ ]:




