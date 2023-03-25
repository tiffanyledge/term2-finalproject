import sqlite3

import requests

database = './static/data/stockwatchlist.db'
api_key = '8e6bcea38d244f3a9d0c276030645072'

# def add_user(name, password):
#     conn = sqlite3.connect(database)
#     curs = conn.cursor()
#     curs.execute("INSERT INTO users(name, password) VALUES ((?),(?))", (name, password))

#     conn.commit()
#     conn.close()


def validate_user(password):
    print("validating user...")
    user = {}

    conn = sqlite3.connect(database)
    curs = conn.cursor()
    #get all columns if there is a match
    result  = curs.execute("SELECT name FROM users WHERE AND password= (?)", [password])
  
    for row in result:
       user = {'name': row[0]}
         
    conn.close()
    return user

def store_user(name, pw):
    conn = sqlite3.connect(database)
    curs = conn.cursor()
    curs.execute("INSERT INTO users (name, password) VALUES((?),(?))",
        (name, pw))
    
    conn.commit()
    conn.close()

def get_all_users():
    conn = sqlite3.connect(database)
    curs = conn.cursor()
    all_users = [] # will store them in a list
    rows = curs.execute("SELECT rowid, * from users")
    for row in rows:
        user = {'rowid': row[0],
                'name' : row[1]
                }
        all_users.append(user)

    conn.close()

    return all_users

def get_api():
    response = requests.get(f'https://api.twelvedata.com/stocks?source=docs&apikey={api_key}')
    data = response.json()
    stocks = []

    entries = data["data"]

    for entry in entries:
        print(entry)
        stock = {
            "symbol": entry["symbol"],
            "name": entry["name"],
            "currency": entry["currency"],
            "exchange": entry["exchange"],
            "mic_code": entry["mic_code"],
            "country": entry["country"],
            "type": entry["type"]
        }

        stocks.append(stock)

    return stocks