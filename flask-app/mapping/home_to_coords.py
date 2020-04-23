import http.client
import urllib.parse

from decouple import config

def find_coords(location):
    '''Return coordinates for given location (str) using Geocode.xyz API'''
    conn = http.client.HTTPConnection('geocode.xyz')

    params = urllib.parse.urlencode({
        'auth': config('GEOCODE_AUTH'),
        'locate': city,
        'region': 'US,CA,MX',
        'json': 1,
        })

    conn.request('GET', '/?{}'.format(params))

    res = conn.getresponse()
    data = res.read()

    return data.decode('utf-8')