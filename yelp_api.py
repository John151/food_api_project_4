    #possible URL`s
    # 'https://api.yelp.com/v3/businesses/search'
    # 'https://api.yelp.com/v3/businesses/matches'
    # 'https://api.yelp.com/v3/businesses/search/phone'
    # 'https://api.yelp.com/v3/businesses/{id}'
    # 'https://api.yelp.com/v3/businesses/{id}/reviews'
    #inspired by claraj/python_api_workshop

import os 
import requests
import logging
import shelve #used for caching api responses 

def yelp_call(search_term):
    cached_response = check_cache(search_term)
    
    if cached_response is not None:
        print("Item found in cache.\n")
        return cached_response
    
    
    url = 'https://api.yelp.com/v3/businesses/search'
    # query = input('What type of restaurants? ')
    key = os.environ.get('YELP_API_KEY')
    log = logging.getLogger()

    try:
        headers = {'Authorization':'Bearer %s'% key}
        params = { 
            'term' : search_term,
            'categories': 'restaurants',
            'location': 'Minneapolis,MN',
            'radius': '10000',
            'offset': 50,
            'price': 1,
            'limit': 50
        }

        response = requests.get(url, headers=headers, params=params).json()
        restaurants = response['businesses']
        data = response.json

        for r in restaurants:
            name = r['name']
            rating = r['rating']
            location = r['location']
            display_phone = r['display_phone']
            address = ','.join(location['display_address'])

        return(f'{name}, {rating}, {address} {display_phone}')
        add_cache(search_term, data)
        return get_business_name(data)
  
    except requests.exceptions.Timeout:
        log.warning('Request Timed Out: ' + response)
    except requests.exceptions.TooManyRedirects:
        log.warning('Error- URL may be bad. Check URL, headers and params')
    except requests.exceptions.RequestException as e:
        log.critical('Error - exiting program')
        
        
def check_cache(search_term):
    s = shelve.open("yelp_cache")

    item_found = s.get(search_term)
    s.close()
    if item_found:
        result = get_business_name(item_found)
        return result
    else:
        return item_found


def add_cache(search_term, data):
    s = shelve.open("yelp_cache")
    s[search_term] = data



def get_business_name(data):
    business_name = data['businesses'][0]['name']
    return business_name
