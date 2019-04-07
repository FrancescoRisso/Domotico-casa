# coding: latin-1

import mysql.connector
import requests
from requests.auth import HTTPBasicAuth
from mysql.connector import Error
import datetime
import xml.etree.ElementTree as ET


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


# Establish a connection to the database
def connect():
    try:
        conn = mysql.connector.connect(host=host_url, database=db, user=usr, password=pwd)
        if conn.is_connected():
            print(date + ' Connected to MySQL database')
            return conn

    except Error as e:
        print("Error while connecting to the database")
        print(e)
        conn.close()


def read(index):
    reader.execute("SELECT Temperature FROM ACTUAL_DATA WHERE InputID = " + str(index))
    var = str(reader.fetchone()).replace("(Decimal('", "").replace("'),)","")
    print(var)
    return var


if 1 > 0:
    host_url = "192.168.0.2"
    db = "Temperatures"
    usr = "prova"
    pwd = "prova"

    date = get_date()
    connection = connect()
    reader = connection.cursor()

    Camera_di_francesco = read(1)
    Camera_di_valentina = read(2)
    Salone = read(3)
    Studio = read(4)
    Camera_genitori = read(5)
    Esterna = read(6)
    Collettore = read(7)
    Accumulo_raffreddamento = read(8)
    Inferiore_boiler = read(9)
    Ricircolo = read(10)
    Mandata_pompa_di_calore = read(11)
    Ritorno_pompa_di_calore = read(12)
    Accumulatore_inferiore = read(13)
    Accumulatore_superiore = read(14)
    Mnadata_riscaldametno_circuito_1 = read(15)
    Mandata_riscaldamento_circuito_2 = read(16)

    connection.close()
    print("Done!")
