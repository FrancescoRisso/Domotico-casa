# coding: latin-1

# Flask example: https://realpython.com/flask-by-example-part-1-project-setup/
import mysql.connector
import requests
from requests.auth import HTTPBasicAuth
from mysql.connector import Error
import datetime
import xml.etree.ElementTree as ET
from flask import Flask
app = Flask(__name__)

header = '<html>\n\t<header>\n\t\t<title>\n\t\t\tHome control panel\n\t\t</title>\n\t\t<script type="text/JavaScript">\n\t\t\t<!--\n\t\t\t\tfunction reload(){\n\t\t\t\t\tsetTimeout("location.reload(true);", 5*1000);\n\t\t\t\t}\n\t\t\t//-->\n\t\t</script>\n\t</header>\n\n\t<body>'
footer = '\n\n\t\t<p>\n\t\t\tLast modified: April 9, 2019\n\t\t</p>\n\t</body>\n</html>'


# Get the instantaneous date and time in the format "YYYY-MM-DD HH:MM:SS"
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
    if day < 10: date = date + "0" + str(day) + " "
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


# Read a certain temperature from the database
def read(index):
    reader.execute("SELECT Temperature FROM ACTUAL_DATA WHERE InputID = " + str(index))
    var = str(reader.fetchone()).replace("(Decimal('", "").replace("'),)","")
    return var


def page_add(page, stanza, temp):
    page = page + "\n\t\t\t\t<tr>\n\t\t\t\t\t<td>" + stanza + "</td>\n\t\t\t\t\t<td>" + temp + "</td>\n\t\t\t\t</tr>"
    return page


@app.route('/')
def hello():
    page= header
    page = page + "\n\t\t<h1>\n\t\t\tTemperature " + get_date() + "\n\t\t</h1>"
    page = page + "\n\n\t\t<table>\n\t\t\t<thead>\n\t\t\t\t<tr>\n\t\t\t\t\t<th>Stanza</th>\n\t\t\t\t\t<th>Temperatura</th>\n\t\t\t\t</tr>\n\t\t\t</thead>\n\t\t\t<tbody>"
    page = page_add(page, "Camera Francesco", read(1))
    page = page_add(page, "Camera Valentina", read(2))
    page = page_add(page, "Camera Genitori", read(5))
    page = page_add(page, "Studio", read(4))
    page = page_add(page, "Salone", read(3))
    page = page + "\n\t\t\t</tbody>"
    page = page + footer
    return page

if __name__ == '__main__':
# https://stackoverflow.com/questions/7023052/configure-flask-dev-server-to-be-visible-across-the-network
# Note: since port 80 is a privileged port, this program has to be started with root permissions.
    host_url = "192.168.0.2"
    db = "Temperatures"
    usr = "prova"
    pwd = "prova"

    date = get_date()
    connection = connect()
    reader = connection.cursor()

#    Camera_di_francesco = read(1)
#    Camera_di_valentina = read(2)
#    Salone = read(3)
#    Studio = read(4)
#    Camera_genitori = read(5)
#    Esterna = read(6)
#    Collettore = read(7)
#    Accumulo_raffreddamento = read(8)
#    Inferiore_boiler = read(9)
#    Ricircolo = read(10)
#    Mandata_pompa_di_calore = read(11)
#    Ritorno_pompa_di_calore = read(12)
#    Accumulatore_inferiore = read(13)
#    Accumulatore_superiore = read(14)
#    Mnadata_riscaldametno_circuito_1 = read(15)
#    Mandata_riscaldamento_circuito_2 = read(16)

#    page_add(date, "Camera Francesco", Camera_di_francesco);

    app.run(host= '0.0.0.0', port=80)
#   Default call to this app
#   app.run()
