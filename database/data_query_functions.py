import sqlite3

# create or connect to database
conn = sqlite3.connect('food_db.sqlite')

# function checks if table exists, count will = 1 if there is a table, zero if not
def check_if_table_exists():
    table_check = "SELECT count(*) FROM sqlite_schema WHERE type='table' AND name='api_search';"
    with sqlite3.connect('food_db.sqlite') as conn:
        cursor = conn.cursor()
        result = cursor.execute(table_check)
        table_exists = result.fetchone()[0]
        return table_exists

def create_api_table():
    with sqlite3.connect('food_db.sqlite') as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS api_search_bookmark (
                        search_term TEXT UNIQUE,
                        image TEXT,
                        recipe_title text,
                        recipe_ingredients text,
                        recipe_instructions text,
                        restaurant Text,
                        bookmark Text);
                        ''')
        conn.commit()

def add_new_data(search_term, food_img, recipe_title, recipe_ingredients, recipe_instructions, restaurant):
    query = """insert into api_search_bookmark (search_term, image, recipe_title, 
    recipe_ingredients, recipe_instructions, restaurant, bookmark) values (?, ?, ?, ?, ?, ?, ?)"""
    try:
        recipe_title = str(recipe_title)
        recipe_ingredients = str(recipe_ingredients)
        recipe_instructions = str(recipe_instructions)
        with sqlite3.connect('food_db.sqlite') as conn:
            cursor = conn.cursor()
            updated = cursor.execute(query, (search_term, food_img, recipe_title, recipe_ingredients, recipe_instructions, restaurant, 'True'))
            rows_modified = updated.rowcount
            return rows_modified
    except sqlite3.Error as e:
        print('Error adding new entry')
        print(e)


def bookmark_page():
    query = """update api_search_bookmark 
               set bookmark = 'True'
               where rowid = 
               (select max(rowid) from api_search"""
    with sqlite3.connect('food_db.sqlite') as conn:
        cursor = conn.cursor()
        bookmark = cursor.execute(query, (bookmark_me,))
        conn.commit()


def search_for_all_bookmarks():
    query = "select * from api_search where bookmark = 'True'"
    with sqlite3.connect('food_db.sqlite') as conn:    
        row = conn.execute(query)
        result = row.fetchall()
        return result
