import requests
from pprint import pprint
import os
from PIL import Image

def request_images():
    search_term = 'pizza'
    key = os.environ.get('UNSPLASH_KEY')
    unsplash_url = 'https://api.unsplash.com/search/photos?'
    query = {'query': search_term, 'client_id': key}
    data = requests.get(unsplash_url, params=query).json()
    image = data['results'][3]['urls']['regular']
    print(image)
    # img1 = Image.open(image)
    # img1.show()





# def main():
#     request_images()
#
#
#
#
# if __name__ == '__main__':
#     main()