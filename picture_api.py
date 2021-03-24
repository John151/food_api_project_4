import requests
import os
import random



def request_images(search_term):
    """takes a search term, requests images from unsplash and picks one out of the top 5 results
    at random and returns that image after opening"""
    # pick = random.randint(1, 5)
    key = os.environ.get('UNSPLASH_KEY')
    unsplash_url = 'https://api.unsplash.com/search/photos?'
    query = {'query': search_term, 'client_id': key}
    data = requests.get(unsplash_url, params=query).json()
    # image = data['results']
    image = data['results'][0]['urls']['regular'] 
    if image:
        return image
    else:
        pass


