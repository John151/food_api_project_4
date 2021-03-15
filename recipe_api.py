import requests
import os
# from dotenv import load_dotenv
# load_dotenv()

RECIPE_API_KEY = os.getenv('RECIPE_API_KEY')
# query name, example 'chicken'
search_term = 'burger'
# first API request gets data based on keyword. It stores the name if the food and an id.
# ID is used in second request, user will choose which result they want

url = f'https://api.spoonacular.com/recipes/complexSearch?query={search_term}&apiKey={RECIPE_API_KEY}'
data_recipes = requests.get(url).json()
results = data_recipes['results']
id_title_dictionary = {}

for id_title_pair in results:
    recipe_id = id_title_pair['id']
    recipe_title = id_title_pair['title']
    id_title_dictionary.update({recipe_title: recipe_id})


# example for $50,000 burger, id = 631814
recipe_id = '631814'
recipe_instructions_url = f'https://api.spoonacular.com/recipes/{recipe_id}/information?apiKey={RECIPE_API_KEY}&analyzedInstructions=true.'

# reguest that gets instructions based on recipe id
data = requests.get(recipe_instructions_url).json()

summary = data['summary']
extended_ingredients = data['extendedIngredients']

ingredient_list = []
for ingredient in extended_ingredients:
    # pulls ingredients and puts them in a list
    original = ingredient['original']
    ingredient_list.append(original)

list_analyzed_instructions = data['analyzedInstructions']

# container for steps to be added below
full_step_list = []

# loops to fill list with steps
for item in list_analyzed_instructions:
    steps = item['steps']
    for instruction in steps:
        number = instruction['number']
        step = instruction['step']
        full_step_list.append(step)

# testing print statement
# print(full_step_list)
