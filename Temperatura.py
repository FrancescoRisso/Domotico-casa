# coding: latin-1

import mysql.connector
import requests
from requests.auth import HTTPBasicAuth
from mysql.connector import Error
import datetime
import xml.etree.ElementTree as ET

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


# Get the actual date and time in the format "YYYY-MM-DD HH:MM:SS"
def get_date():
    now = datetime.datetime.today()

    second = now.second
    minute = now.minute
    hour = now.hour
    day = now.day
    month = now.month
    year = now.year

    date = str(year) + "-"
    if month < 10: date = date + "0" + str(month) + "-"
    else: date = date + str(month) + "-"
    if day < 10: date = date + "0" + str(day) + "-"
    else: date = date + str(day) + " "
    if hour < 10: date = date + "0" + str(hour) + ":"
    else: date = date + str(hour) + ":"
    if minute < 10: date = date + "0" + str(minute) + ":"
    else: date = date + str(minute) + ":"
    if second < 10: date = date + "0" + str(second)
    else: date = date + str(second)

    return date


# Insert a certain value in the database
def insert(value, date, writer, source):
    try:
        writer.execute("INSERT INTO DATA(Date, Temperature, InputID) VALUES('" + date + "', " + str(value) + ", " + source + ")")
        writer.execute("UPDATE ACTUAL_DATA SET Temperature = " + str(value) + " WHERE InputID = " + source)

    except Error as e:
        print("Error while putting data in the database")
        print(e)


# Get all the info from the websites and for each info runs insert()
def data_getter(link, cmi, writer, date):

    reader = requests.get(link, auth=HTTPBasicAuth('admin', 'admin')).text

    data= '<data>' + reader + '</data>'
    root = ET.fromstring( data.encode('ascii', 'ignore') )

    ind = 0
    for line_divs in root.findall('div'):
        if line_divs.get('class') == 'BOX BOX_IN':
            for value_divs in line_divs:
                ind = ind + 0.5
                for value in value_divs:
                    text = value.text
                    tmp = ''
                    if text != 'ON' and text != 'OFF':
                        tmp = text[0: len(text) - 2]
                        text = float(tmp)

                        if cmi == 33 and ind == 1: insert(text, date, writer, '1')
                        elif cmi == 33 and ind == 2: insert(text, date, writer, '2')
                        elif cmi == 34 and ind == 3: insert(text, date, writer, '3')
                        elif cmi == 34 and ind == 1: insert(text, date, writer, '4')
                        elif cmi == 34 and ind == 2: insert(text, date, writer, '5')
                        elif cmi == 34 and ind == 4: insert(text, date, writer, '6')
                        elif cmi == 2 and ind == 1: insert(text, date, writer, '7')
                        elif cmi == 2 and ind == 2: insert(text, date, writer, '8')
                        elif cmi == 2 and ind == 3: insert(text, date, writer, '9')
                        elif cmi == 2 and ind == 4: insert(text, date, writer, '10')
                        elif cmi == 1 and ind == 1: insert(text, date, writer, '11')
                        elif cmi == 1 and ind == 2: insert(text, date, writer, '12')
                        elif cmi == 1 and ind == 3: insert(text, date, writer, '13')
                        elif cmi == 1 and ind == 4: insert(text, date, writer, '14')
                        elif cmi == 1 and ind == 5: insert(text, date, writer, '15')
                        elif cmi == 1 and ind == 6: insert(text, date, writer, '16')


# Main, that sets all the constant values and calls all the needed methods
if 1 > 0:
    host_url = "192.168.0.2"
    db = "Temperatures"
    usr = "prova"
    pwd = "prova"

    date = get_date()
    print(date + " Starting data collection")

    connection = connect(date)
    writer = connection.cursor()

    link_nodo_1 = "http://192.168.0.195/INCLUDE/devpagex.cgi?pagex2=01025800"
    link_nodo_2 = "http://192.168.0.195/INCLUDE/devpagex.cgi?pagex2=02025800"
    link_nodo_33 = "http://192.168.0.195/INCLUDE/devpagex.cgi?pagex2=21025800"
    link_nodo_34 = "http://192.168.0.195/INCLUDE/devpagex.cgi?pagex2=22025800"

    data_getter(link_nodo_1, 1, writer, date)
    data_getter(link_nodo_2, 2, writer, date)
    data_getter(link_nodo_33, 33, writer, date)
    data_getter(link_nodo_34, 34, writer, date)

    connection.close()
    print(date + " Done!")
