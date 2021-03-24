import sqlite3

# create or connect to database
conn = sqlite3.connect('food_db.sqlite')

def create_database():
    conn.execute('''create table api_search (search_term text, image blob,  
                    recipe text, restaurant text)''')
    conn.commit()
## TODO  look at this and fix
def add_new_data(search_term, image, recipe, restaurant):
    query = '''insert into api_search values (%, %, %, %)'''
    try:
        with open:
            conn.execute(query, (search_term, image, recipe, restaurant))
            conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()


def search_for_search_term(search_term):
    query = '''select * from api_search where search_term = %'''
    row = conn.execute(query, (search_term,))
    result = row.fetchone()
    row.close()
    if result:
        return result
    else:
        return False

# def search_for_search_term(search_term):
#     query = '''select * from api_search where search_term = %'''
#     row = conn.execute(query, (search_term,))
#     result = row.fetchone()
#     row.close()
#     if result:
#         return result
#     else:
#         return False
