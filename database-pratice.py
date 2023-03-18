import sqlite3

database = './static/data/stockwatchlist.db'

def add_user(name, password):
    conn = sqlite3.connect(database)
    curs = conn.cursor()
    curs.execute("INSERT INTO users(name, password) VALUES ((?),(?))", (name, password))

    conn.commit()
    conn.close()

def 