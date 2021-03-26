import sqlite3

# Creates or opens connection to db file
conn = sqlite3.connect('food_db.sqlite')


def create_api_table():
    cursor = conn.cursor()
    conn.execute('''CREATE TABLE IF NOT EXISTS api_search (
                    search_term TEXT UNIQUE,
                    image BLOB,  
                    recipe TEXT,
                    restaurant TEXT)
                    ''')
    conn.commit()

def add_new_data(search_term, image, recipe, restaurant):
    query = 'insert into api_search (search_term, image, recipe, restaurant) values (?, ?, ?, ?)'
    try:
        conn = sqlite3.connect('food_db.sqlite')
        cursor = conn.cursor()
        with conn:
            updated = cursor.execute(query, (search_term, image, recipe, restaurant))
            rows_modified = updated.rowcount
            return rows_modified
    except sqlite3.Error as e:
        print('Error adding new entry')
        print(e)
    finally:
        conn.close()
        

def search_for_search_term(search_term):
    query = '''select * from api_search where search_term = %'''
    row = conn.execute(query, (search_term,))
    result = row.fetchone()
    row.close()
    if result:
        return result
    else:
        return False

def search_for_all():
    query = 'select * from api_search'
    row = conn.execute(query)
    result = row.fetchall()
    row.close()
    if result:
        return result
    else:
        return False
