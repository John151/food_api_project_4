from flask import Flask, request, render_template

import picture_api
import search_util
import yelp_api

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

    # if len(search_input) < 1 or type(search_input) == int:
    #     print("You can't enter a number, enter a food item with letters")
    # else:
    return render_template('food.html', search_term=search_input, food_img=food_img)

if __name__ == '__main__':
    app.run(debug=True) # turn on developer mode, shows us actual errors when they pop up
    