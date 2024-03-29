import mysql.connector
from mysql.connector import Error
from functions.common.config import config

config = config()


# Establishes and returns a connection to the database
def connect(date):
    try:
        conn = mysql.connector.connect(
            host=config["Database"]["ip"],
            database=config["Database"]["db"],
            user=config["Database"]["user"],
            password=config["Database"]["password"],
        )
        if conn.is_connected():
            print(f"{date} Connected to MySQL database")
            return conn

    except Error as e:
        print(f"Error while connecting to the database: '{e}'")
        raise Exception
