import geocoder

from decouple import config

def find_coords(location):
    '''Return Tuple of longitude, lattitude (float, float) for given location (str) using Geocode.xyz API'''

    g = geocoder.mapquest(location, key=config('GEOCODE_AUTH'))

    return (g.json['lng'], g.json['lat'])