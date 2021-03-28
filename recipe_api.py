# source env/bin/activate
import requests
import os
import shelve

def recipe_call(search_term):
    """ checks cache to see if exact search term has been used before
    if found, will return that value instead of making the request """
    cached_response = check_cache(search_term)
    if cached_response:
        print("Item found in cache.\n") # just to keep track of where response is coming from 
        return cached_response
    else:
        print('cache not accessed')
        # uses search term and returns most popular result (1, can be modified in url at the end '&number=')
        # returns results only containing an ingredients list and cooking instructions

        RECIPE_API_KEY = os.environ.get('RECIPE_API_KEY')

        url = f'https://api.spoonacular.com/recipes/complexSearch?query={search_term}&apiKey={RECIPE_API_KEY}&addRecipeInformation=True&fillIngredients=True&sort=popularity&number=1'
        data_recipes = requests.get(url).json()
        results = data_recipes['results'][0]

        # container for 1 recipe
        recipe = []
        recipe_title = results['title']
        # add the title to the recipe list
        recipe.append(recipe_title)

        extended_ingredients = results['extendedIngredients']
        ingredient_list = []
        for ingredient in extended_ingredients:
            # pulls ingredients and puts them in a list
            original = ingredient['original']
            ingredient_list.append(original)

        # add the list of ingredients to the recipe list
        recipe.append(ingredient_list)

        list_analyzed_instructions = results['analyzedInstructions']
        # container for steps to be added below
        full_step_list = []
        # loops to fill list with steps
        for item in list_analyzed_instructions:
            steps = item['steps']
            for instruction in steps:
                step = instruction['step']
                full_step_list.append(step)
        recipe.append(full_step_list)
        add_cache(search_term, recipe)
        return recipe

    # returns info in list with following format: [string, [ingredient list], [preparation step list]]
    # ['Title', ['ingredient 1', 'ingredient 2', etc], ['step 1', 'step 2', etc]]
    # example of real return below

    """['Slow Cooker Chicken Taco Soup', 

    ['1 (15 oz.) can black beans', '2 (10 oz.) cans diced tomatoes with green chilis', '1 (15 oz.) can
    diced tomatoes', '1 (15 oz.) can chili beans', '1 (15 oz.) can whole kernal corn', '1 large red onion (finely chopped)', '3 boneless
    skinless chicken breasts (cut into 1" cubes)'], 

    ['Once you have all of your ingredients added, allow it to cook all day for 8 hours o
    n low. If you are wanting to make this a little faster, turn it on high and cook for 4 hours.When your Chicken Taco Soup is ready to
    serve, add in some crushed tortilla shells, shredded cheddar cheese, and a little sour cream.']]
"""
""" Checks for search term in cache """       
def check_cache(search_term):
    with shelve.open("recipe_cache") as s:
        item_found = s.get(search_term)
        """ if the search term is in cache it will be returned, 
        if not a msg will print to console, and program will make API call """
        if item_found:
            result = item_found
            return result
        else:
            print('item not found')

""" If not already in cache, adds search term and results to cache """
def add_cache(search_term, recipe):
    with shelve.open("recipe_cache") as s:
        s[search_term] = recipe
        print(search_term, recipe)