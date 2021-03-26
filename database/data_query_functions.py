import sqlite3

# create or connect to database
conn = sqlite3.connect('food_db.sqlite')
cursor = conn.cursor()

def create_database():
    conn.execute('''CREATE TABLE api_search (search_term TEXT UNIQUE, image BLOB,  
                    recipe TEXT, restaurant TEXT);''')
    conn.commit()

def add_new_data(search_term, image, recipe, restaurant):
    query = 'insert into api_search values (?, ?, ?, ?)'
    try:
        conn = sqlite3.connect('food_db.sqlite')
        cursor = conn.cursor()
        with open:
            cursor.execute(query, (search_term, image, recipe, restaurant))
            conn.commit()
            
    except Exception as e:
        print(e)
        

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
