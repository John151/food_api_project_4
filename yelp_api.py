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
    """ checks cache to see if exact search term has been used before
    if found, will return that value instead of making the request """    
    cached_response = check_cache(search_term)
    if cached_response:
        print("Item found in cache.\n") # just to keep track of where response is coming from
        return cached_response
    else:
        print('cache not accessed')
    
        # if no result from cache, make request to the API using the search_term as a parameter
        url = 'https://api.yelp.com/v3/businesses/search'
        #stores api key
        key = os.environ.get('YELP_API_KEY')
        #loggs
        log = logging.getLogger()

        try:
            headers = {'Authorization':'Bearer %s'% key} #sets headers 
            params = { #sets params 
                'term' : search_term,
                'categories': 'restaurants',
                'location': 'Minneapolis,MN',
                'radius': '10000',
                'sort_by': 'rating',
                'open_now': True,
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
                yelp_results = f'{name}, rated {rating} stars, {address}, {display_phone}'
                add_cache(search_term, yelp_results)
                return yelp_results
            
        except requests.exceptions.Timeout:
            log.warning('Request Timed Out: ' + response)
        except requests.exceptions.TooManyRedirects:
            log.warning('Error- URL may be bad. Check URL, headers and params')
        except requests.exceptions.RequestException as e:
            log.critical('Error - exiting program')
        
""" Checks for search term in cache """      
def check_cache(search_term):
    with shelve.open("yelp_cache") as s:
        item_found = s.get(search_term)
        """ if the search term is in cache it will be returned, 
        if not a msg will print to console, and program will make API call """
        if item_found:
            result = item_found
            return result
        else:
            print('item not found')


""" If not already in cache, adds search term and results to cache """
def add_cache(search_term, data):
    with shelve.open("yelp_cache") as s:
        s[search_term] = data
        print(search_term, data)


