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
    search_input = request.args.get('food_input')

    food_img = picture_api.request_images(search_input)
    food_yelp = yelp_api.yelp_call(search_input)
    food_recipe = recipe_api.recipe_call(search_input)

    return render_template('food.html', search_term=search_input, food_img=food_img, food_yelp=food_yelp, food_recipe=food_recipe)

if __name__ == '__main__':
    app.run(debug=True) # turn on developer mode, shows us actual errors when they pop up
    