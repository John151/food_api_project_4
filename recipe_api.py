import requests
import os

APP_ID = os.getenv("APP_ID")

APP_KEY = os.getenv("APP_KEY")

# query name, example 'chicken'. cannot be used with recipe id
q = 'burger'
# recipe ID, used with another edamam API. cannot be used with query_name
r = ''
# maximum number of ingredients
ingr = 5
# default number of results is 10, can be changed
url = f'https://api.edamam.com/search?q={q}&app_id={APP_ID}&app_key={APP_KEY}'

data = requests.get(url).json()
results = data['hits']
for result in results:
    recipe = result['recipe']
    name = recipe['label']
    url = recipe['url']
    image = recipe['image']
    ingredient_strings = recipe['ingredientLines']
    calories = recipe['calories']
    print(f'name: {name}, url: {url}\n'
          f'ingredients: {ingredient_strings}\n'
          f'calories: {calories}\n\n')
