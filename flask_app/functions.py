from bs4 import BeautifulSoup
from googlesearch import search
import pgeocode
import requests
import plotly as py
import sklearn
import plotly.offline as offline
import plotly.graph_objs as go
import geopandas as gpd
import datetime
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from timezonefinder import TimezoneFinder
from datetime import datetime, timedelta
from pytz import timezone
import pytz

def latlong_finder(country, postalcode):
    '''
    This accepts a country from the following list:
    https://pgeocode.readthedocs.io/en/latest/overview.html#supported-countries
    as well as a postal code, both as strings.

    It returns the latitude and longitude (in that order) in a list.
    '''

    try:
        place = pgeocode.Nominatim(f'{country}')
    # Ideally the country selector is a dropdown list, so this is never an issue:
    except ValueError:
        message = 'Your country input did not match any supported country.\nPlease try again!'

    latlong = []
    latlong.append(place.query_postal_code(f'{postalcode}')['latitude'])
    latlong.append(place.query_postal_code(f'{postalcode}')['longitude'])

    return latlong

def wrangle():
    """ Wrangles the data 
    Step 1: imports all the postgres data as a pandas dataframe
    Step 2: parsing the geojson structure into distinct columns
    Step 3: location/distance from epicenter into columns of distance, city, country
    Step 4: filling values with no city or distances
    Step 5: --  INCOMPLETE -- getting missing timezone value
    Step 6: parsing long, lat, and depth for each event
    Step 7: updating time to datetime format
    """ 

    # Connecting to the postgres database and dumping to json then pandas 
    quakes = db.session.query(Quake).all()
    result = quakes_schema.dump(quakes)
    df = pd.read_json(result)
    geo = df.copy()

    # Parse the city and country/state
    geo['dist_from_city'] = geo['place'].str.split('of ', expand=True)[0]
    geo['city'] = geo['place'].str.split('of ', expand=True)[1]
    geo['city'] = geo['city'].str.split(', ', expand=True)[0]
    geo['country_state'] = geo['place'].str.split(', ', expand=True)[1]

    # Accounting for values without distances or cities in raw data
    geo['city'].fillna(geo['place'], inplace=True)
    geo['country_state'].fillna(geo['place'], inplace=True)

    # # Working on this section currently
    # Getting value for any missing timezone ('tz') entries
    # tf = TimezoneFinder()
    # lat, lng = geo.loc[geo['tz'].isna(), 'lat'].item(), geo.loc[geo['tz'].isna(), 'long'].item()
    # tf.timezone_at(lng=lng, lat=lat)
    
    # Parse the longitude, latitude, and the depth for each seismic event
    geo['long'] = [geo['geometry'][i].x for i in range(len(geo['geometry']))]
    geo['lat'] = [geo['geometry'][i].y for i in range(len(geo['geometry']))]
    geo['longlat'] = list(zip(geo['long'], geo['lat']))
    geo['depth'] = [geo['geometry'][i].z for i in range(len(geo['geometry']))]

    # Convert time columns to datetime format
    geo['time_dt'] = [datetime.fromtimestamp(
        i / 1000) for i in geo['time']]
    geo['updated_dt'] = [datetime.fromtimestamp(
        i / 1000) for i in geo['updated']]

    # Return wrangled dataframe 
    return geo

# This is still a work in progress
def find_emergency_site(postalcode):
    '''
    This returns the first .gov site in a google search for that zip code's
    earthquake emergency sites.
    '''
    site = []
    for ii in search(f'{postalcode} earthquake emergency', num=10, start=0, stop=10):
        if '.gov' in ii:
            site.append(ii)

    return site[0]

# This is still a work in progress, and builds off of find_emergency_site
def get_emergency_info(site='https://www.ready.gov/earthquakes'):
    '''

    '''
    # BS4 logic


    return text
