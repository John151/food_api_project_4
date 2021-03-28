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
        cursor.execute('''CREATE TABLE IF NOT EXISTS api_search (
                        search_term TEXT UNIQUE,
                        image TEXT,
                        recipe BLOB,
                        restaurant Text);
                        ''')
        conn.commit()


def add_new_data(search_term, food_img, recipe, restaurant):
    query = 'insert into api_search (search_term, image, recipe, restaurant) values (?, ?, ?, ?)'
    try:
        recipe = str(recipe)
        with sqlite3.connect('food_db.sqlite') as conn:
            cursor = conn.cursor()
            updated = cursor.execute(query, (search_term, food_img, recipe, restaurant))
            rows_modified = updated.rowcount
            return rows_modified
    except sqlite3.Error as e:
        print('Error adding new entry')
        print(e)
    finally:
        conn.close()

def search_for_all():
    query = 'select * from api_search'
    with sqlite3.connect('food_db.sqlite') as conn:    
        row = conn.execute(query)
        result = row.fetchall()
        if result:
            return result
        else:
            return False