import sqlite3
from sqlite3 import Error

# DB 연결
def connection():
    try:
        con = sqlite3.connect('database.db')
        return con
    except Error:
        print(Error)

#