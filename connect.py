import mysql.connector
from mysql.connector import Error

host_url = "192.168.0.2"
db = "Temperatures"
usr = "prova"
pwd = "prova"


# Establish a connection to the database
def connect(date):
    try:
        conn = mysql.connector.connect(host=host_url, database=db, user=usr, password=pwd)
        if conn.is_connected():
            print(date + ' Connected to MySQL database')
            return conn

    except Error as e:
        print("Error while connecting to the database")
        print(e)
        conn.close()
