# source env/bin/activate
import requests
import os
from dotenv import load_dotenv
load_dotenv()

def recipe_call(search_term):

    RECIPE_API_KEY = os.getenv('RECIPE_API_KEY')

    #first API request gets data based on keyword. It stores the name if the food and an id.
    # ID is used in second request, user will choose which result they want

    url = f'https://api.spoonacular.com/recipes/complexSearch?query={search_term}&apiKey={RECIPE_API_KEY}'
    data_recipes = requests.get(url).json()
    results = data_recipes['results']
    # takes first result
    result = results[0]

    # container for 1 recipe
    recipe = []
    recipe_id = result['id']
    recipe_title = result['title']
    # add the title to the recipe list
    recipe.append(recipe_title)

    recipe_instructions_url = f'https://api.spoonacular.com/recipes/{recipe_id}/information?apiKey={RECIPE_API_KEY}&analyzedInstructions=true.'
    # reguest that gets instructions based on recipe id
    data = requests.get(recipe_instructions_url).json()

    extended_ingredients = data['extendedIngredients']
    ingredient_list = []
    for ingredient in extended_ingredients:
        # pulls ingredients and puts them in a list
        original = ingredient['original']
        ingredient_list.append(original)

    # add the list of ingredients to the recipe list
    recipe.append(ingredient_list)

    list_analyzed_instructions = data['analyzedInstructions']
    # container for steps to be added below
    full_step_list = []
    # loops to fill list with steps
    for item in list_analyzed_instructions:
        steps = item['steps']
        for instruction in steps:
            step = instruction['step']
            full_step_list.append(step)
    recipe.append(full_step_list)

    return recipe

# returns info in list with following format: [string, [ingredient list], [preparation step list]]
# ['Title', ['ingredient 1', 'ingredient 2', etc], ['step 1', 'step 2', etc]]
# example of real return below

"""['Falafel Burger',

['540 ml can of chickpeas, drained and rinsed', '2 ts
p tahini', '½ tsp sriracha sauce', '3 cloves garlic', '3 tbsp fresh parsley, roughly chopped', '¼ large red onion, diced', '4 tbsp peanut oil', '8 slices of cucumber', '8 slices of
tomato', "4 hamburger buns (I used President's Choice multi-grain thins)", 'Tzatziki for topping'], 

['Pat the chickpeas dry with a paper towel and throw them into a food processor a
long with the garlic.', 'Puree until smooth.', 'Using your clean hands incorporate tahini, sriracha, parsley and onion into the chickpea mixture.', 'Form mixture into four patties a
nd set aside.', 'Heat peanut oil in a large skillet over medium heat.', 'Once the oil begins to shimmer add the patties and cook for three minutes per side or until golden brown.',
'Remove from and place in a hamburger bun.', 'Top each burger with 2 slices of tomato, 2 slices of cucumber and a dollop of tzatziki.', 'Serve immediately.']"""