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
    r = requests.get(site).text
    # BS4 logic
    soup = BeautifulSoup(r, 'html.parser')

    # Info: before earthquake
    before_quake = soup.find_all('div', class_="clearfix text-formatted field field--name-body field--type-text-with-summary field--label-hidden field__item")

    emergency_info = {}

    emergency_info['before_quake'] = before_quake

    return before_quake
