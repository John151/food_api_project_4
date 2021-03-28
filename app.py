from flask import Flask, request, render_template

import recipe_api
import picture_api
import search_util
import yelp_api

from recipe_api import recipe_call
from picture_api import request_images
from search_util import prep_search_term
from yelp_api import yelp_call

app = Flask(__name__) # __name__ references this file

""" Home page which is our index file """
@app.route('/')
def home_page():
    return render_template('index.html')

""" Page that displays the result of API request """
@app.route('/get-food')
def get_food():
    error = None
    result = None

    search_input = request.args.get('food_input')

    food_img = picture_api.request_images(search_input)
    food_yelp = yelp_api.yelp_call(search_input)
    food_recipe = recipe_api.recipe_call(search_input)
    recipe_title = food_recipe[0]
    recipe_ingredients = food_recipe[1]
    recipe_instructions = food_recipe[2]

    try:
        return render_template(
            'food.html',
            search_term=search_input, 
            food_img=food_img, 
            food_yelp=food_yelp, 
            recipe_title=recipe_title,
            recipe_ingredients=recipe_ingredients, 
            recipe_instructions=recipe_instructions,
            result=result,
            search_success=True
        )
    except ValueError:
        return render_template(
            'food.html',
            search_term=search_input, 
            food_img=food_img, 
            food_yelp=food_yelp, 
            recipe_title=recipe_title,
            recipe_ingredients=recipe_ingredients, 
            recipe_instructions=recipe_instructions,
            result="Bad input",
            search_success=False,
            error="Cannot perform search with provided input"
        )

if __name__ == '__main__':
    app.run(debug=True) # turn on developer mode, shows us actual errors when they pop up

