import requests
import os
import random


def request_images(search_term):
    """takes a search term, requests images from unsplash and picks one out of the top 5 results
    at random and returns that image after opening"""
    pick = random.randint(1, 5)
    key = os.environ.get('UNSPLASH_KEY')
    unsplash_url = 'https://api.unsplash.com/search/photos?'
    query = {'query': search_term, 'client_id': key}
    data = requests.get(unsplash_url, params=query).json()
    image = data['results'][pick]['urls']['regular']
    image_pic = open(image, 'wb')
    return image_pic
