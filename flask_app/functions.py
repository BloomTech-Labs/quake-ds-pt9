from bs4 import BeautifulSoup
from googlesearch import search
import pgeocode
import requests

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


def time_parser(time_arg):
    if time_arg == 'w':
        return 604800
    elif time_arg == '2w':
        return 1209600
    elif time_arg == 'm':
        return 2629743
    else:
        #returns one day
        return 86400
