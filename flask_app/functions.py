from bs4 import BeautifulSoup
from gensim.summarization import summarize
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

class EmergencyLookup:

    def __init__(self, city):
        self.city = city

    def find_site(self):
        '''
        This returns the first .gov or .org site in a google search for that zip code's
        earthquake emergency sites.
        '''
        self.site = []
        for ii in search(f'{self.city} earthquake emergency', num=10, start=0, stop=10):
            if ('.gov' in ii) or ('.org' in ii):
                self.site.append(ii)

        return self.site[0]

    # This is still a work in progress, and builds off of find_emergency_site
    def scrape_site(self):
        '''

        '''
        r = requests.get(self.site[0]).text
        # BS4 logic
        soup = BeautifulSoup(r, 'html.parser')

        if 'earthquake' in soup.get_text():
            #Scrape and summarize website
            body = soup.find('body').text
            content = summarize(body, word_count=200)
            self.default = False
            return content + f'\nSummarized from {self.site[0]}'
        else:
            # Scraping the default: ready.gov's earthquakes page
            info = soup.find_all('div', class_="clearfix text-formatted field field--name-body field--type-text-with-summary field--label-hidden field__item")
            content = str(info[1:]).replace(',', '').replace('[', '').replace(']', '')
            self.default = True
            return content


def time_parser(time_arg):
    """Filters time period based on Unix epoch time """
    if time_arg == 'w':
        return 604800
    elif time_arg == '2w':
        return 1209600
    elif time_arg == 'm':
        return 2629743
    else:
        #returns one day
        return 86400
