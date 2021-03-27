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
    # image = data['results']
    # print(status)
    try:
        image = data['results'][pick]['urls']['regular'] 
        return image
        
    except:
        image = 'https://images.unsplash.com/photo-1517870662726-c1d98ee36250?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwyMTEyMTJ8MHwxfHNlYXJjaHw0fHxlbXB0eSUyMHBsYXRlfGVufDB8fHx8MTYxNjgyMjkzMg&ixlib=rb-1.2.1&q=80&w=1080'
        return image


