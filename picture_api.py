import requests
import os
import shelve


def request_images(search_term):
    """ checks cache to see if exact search term has been used before
    if found, will return that value instead of making the request """    
    cached_response = check_cache(search_term)
    if cached_response:
        print("Item found in cache.\n") # just to keep track of where response is coming from
        return cached_response
    else:
        print('cache not accessed')
        """ If no result in cache, will takes search term, request image from unsplash and 
        returns the top result while storing it in cache """
        key = os.environ.get('UNSPLASH_KEY') # calls env variable
        unsplash_url = 'https://api.unsplash.com/search/photos?'
        query = {'query': search_term, 'client_id': key}
        data = requests.get(unsplash_url, params=query).json()

        try:
            image = data['results'][0]['urls']['regular']
            add_cache(search_term, image)
            print(image)
            return image
            
        except:
            image = 'https://images.unsplash.com/photo-1517870662726-c1d98ee36250?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwyMTEyMTJ8MHwxfHNlYXJjaHw0fHxlbXB0eSUyMHBsYXRlfGVufDB8fHx8MTYxNjgyMjkzMg&ixlib=rb-1.2.1&q=80&w=1080'
            return image

""" Checks for search term in cache """     
def check_cache(search_term):
    with shelve.open("image_cache") as s:
        item_found = s.get(search_term)
        """ if the search term is in cache it will be returned, 
        if not a msg will print to console, and program will make API call """   
        if item_found:
            result = item_found
            return result
        else:
            print('item not found')


""" If not already in cache, adds search term and results to cache """
def add_cache(search_term, image):
    with shelve.open("image_cache") as s:
        s[search_term] = image
        print(search_term, image)
