import mysql.connector
from mysql.connector import Error
from functions.config import config

config = config()


# Establishes and returns a connection to the database
def connect(date, database):
    try:
        conn = mysql.connector.connect(host=config['Database'][database]['ip'], database=config['Database'][database]['db'], user=config['Database'][database]['user'], password=config['Database'][database]['password'])
        if conn.is_connected():
            print(date + ' Connected to MySQL database')
            return conn

    except Error as e:
        print("Error while connecting to the database: '" + str(e) + "'")
        conn.close()
