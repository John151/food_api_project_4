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
    full_results_list = []

    for id_title_pair in results:
        # container for 1 recipe
        recipe = []
        recipe_id = id_title_pair['id']
        recipe_title = id_title_pair['title']
        # add the title to the recipe list
        recipe.append(recipe_title)
        print(recipe_title)
        print('8' * 50)
        recipe_instructions_url = f'https://api.spoonacular.com/recipes/{recipe_id}/information?apiKey={RECIPE_API_KEY}&analyzedInstructions=true.'
        # reguest that gets instructions based on recipe id
        data = requests.get(recipe_instructions_url).json()
        summary = data['summary']
        # add the summary to the recipe list
        recipe.append(summary)

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
        full_results_list.append(recipe)

    return full_results_list

# returns info in list with following format: [string, string, [ingredient list], [preparation step list]]
# ['Title', 'Description', ['ingredient 1', 'ingredient 2', etc], ['step 1', 'step 2', etc]]
# example of real return below

"""['Falafel Burger',

 'You can never have too many middl eastern recipes, so give Falafel Burger a try. For <b>$1.37 per serving</b>, this recipe <b>covers 19%</b> of your daily requi
rements of vitamins and minerals. One portion of this dish contains around <b>12g of protein</b>, <b>20g of fat</b>, and a total of <b>402 calories</b>. This recipe serves 4. It is
brought to you by Foodista. 4 people were impressed by this recipe. Head to the store and pick up onion, garlic, sriracha sauce, and a few other things to make it today. Only a few
people really liked this main course. From preparation to the plate, this recipe takes about <b>about 45 minutes</b>. It is a good option if you\'re following a <b>dairy free and la
cto ovo vegetarian</b> diet. With a spoonacular <b>score of 81%</b>, this dish is spectacular. Try <a href="https://spoonacular.com/recipes/clean-eating-falafel-burger-1063020">Clea
n eating falafel burger</a>, <a href="https://spoonacular.com/recipes/clean-eating-falafel-burger-848720">Clean eating falafel burger</a>, and <a href="https://spoonacular.com/recip
es/falafel-veggie-burger-with-feta-yogurt-sauce-559036">Falafel Veggie Burger with Feta Yogurt Sauce</a> for similar recipes.', 

['540 ml can of chickpeas, drained and rinsed', '2 ts
p tahini', '½ tsp sriracha sauce', '3 cloves garlic', '3 tbsp fresh parsley, roughly chopped', '¼ large red onion, diced', '4 tbsp peanut oil', '8 slices of cucumber', '8 slices of
tomato', "4 hamburger buns (I used President's Choice multi-grain thins)", 'Tzatziki for topping'], 

['Pat the chickpeas dry with a paper towel and throw them into a food processor a
long with the garlic.', 'Puree until smooth.', 'Using your clean hands incorporate tahini, sriracha, parsley and onion into the chickpea mixture.', 'Form mixture into four patties a
nd set aside.', 'Heat peanut oil in a large skillet over medium heat.', 'Once the oil begins to shimmer add the patties and cook for three minutes per side or until golden brown.',
'Remove from and place in a hamburger bun.', 'Top each burger with 2 slices of tomato, 2 slices of cucumber and a dollop of tzatziki.', 'Serve immediately.']"""