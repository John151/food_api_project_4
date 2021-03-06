from flask import Flask, request, render_template

import recipe_api
import picture_api
import search_util
import yelp_api
import database.data_query_functions as dbq

from recipe_api import recipe_call
from picture_api import request_images
from search_util import prep_search_term
from yelp_api import yelp_call

app = Flask(__name__) # __name__ references this file

""" Home page which is our index file """
@app.route('/')
def home_page():
    db_exists = dbq.check_if_table_exists()
    if not db_exists:
        print('creating db')
        dbq.create_api_table()
    return render_template('index.html')

""" Page that displays the result of API request """
@app.route('/get-food')
def get_food():
    error = None

    search_input = request.args.get('food_input').lower()

    try:
        search_term = str(search_input)

        food_img = picture_api.request_images(search_input)
        food_yelp = yelp_api.yelp_call(search_input)
        food_recipe = recipe_api.recipe_call(search_input)
        recipe_title = food_recipe[0]
        recipe_ingredients = food_recipe[1]
        recipe_instructions = food_recipe[2]

        dbq.add_new_data(search_term, food_img, recipe_title, recipe_ingredients, recipe_instructions, food_yelp)
        
        return render_template(
            'food.html',
            search_term=search_term, 
            food_img=food_img, 
            food_yelp=food_yelp, 
            recipe_title=recipe_title,
            recipe_ingredients=recipe_ingredients, 
            recipe_instructions=recipe_instructions,
            search_success=True
        )
    except KeyError: 
        return render_template(
            'index.html',
            search_term=search_term, 
            search_success=False,
            error="Cannot perform search with provided input"
        )
    except TypeError: 
        return render_template(
            'index.html',
            search_term=search_term, 
            search_success=False,
            error="Cannot perform search with special charcters or numbers"
        )
    except IndexError: 
        return render_template(
            'index.html',
            search_term=search_term, 
            search_success=False,
            error=f"Food with the name {search_input} cannot be found in the APIs. Try searching a term with no special characters or numbers."
        )


""" Page that displays the bookmarks """
@app.route('/get-bookmarks')
def get_bookmarks():
    try:
        bookmarks = dbq.search_for_all_bookmarks()
        return render_template('bookmarks.html', 
                                bookmark=bookmarks,)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    app.run(debug=True) # turn on developer mode, shows us actual errors when they pop up

