from flask import Flask, request, render_template

# TODO import all the api files when they are done

app = Flask(__name__)

""" Home page which is our index file """
@app.route('/')
def home_page():
    return render_template('index.html')

""" Page that displays the result of API request """
@app.route('/get-food')
def get_food():
    search_input = request.args.get('food_input')

    if len(search_input) < 1 or type(search_input) == int:
        print("You can't enter a number, enter a food item with letters")
    else:
        return render_template('food.html')
    
    # TODO write code for api requests and what to do with the responses

if __name__ == '__main__':
    app.run()
    