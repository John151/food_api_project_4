    #possible URL`s
    # 'https://api.yelp.com/v3/businesses/search'
    # 'https://api.yelp.com/v3/businesses/matches'
    # 'https://api.yelp.com/v3/businesses/search/phone'
    # 'https://api.yelp.com/v3/businesses/{id}'
    # 'https://api.yelp.com/v3/businesses/{id}/reviews'
    #inspired by claraj/python_api_workshop

import os 
import requests
from api_key import api_key

url = 'https://api.yelp.com/v3/businesses/search'

query = input('What type of restaurants? ')

headers = {'Authorization':'Bearer %s' % api_key}

params = { 
    'term' : query,
    'categories': 'restaurants',
    'location': 'Minneapolis,MN',
    'radius': '10000',
    'offset': 50,
    'price': 1,
    'limit': 50
}

response = requests.get(url, headers=headers, params=params).json()

restaurants = response['businesses']

for r in restaurants:
    name = r['name']
    rating = r['rating']
    location = r['location']
    display_phone = r['display_phone']
    address = ','.join(location['display_address'])

    print(f'{name}, {rating}, {address} {display_phone}')