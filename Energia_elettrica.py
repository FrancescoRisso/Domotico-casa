import requests
import datetime
from requests.auth import HTTPBasicAuth
import xml.etree.ElementTree as ET
import os

from functions.date import get_date
from functions.config import config
from functions.connect import connect
from functions.electricity.get import get
from functions.electricity.datalogger_connecter import dl_connect

date = get_date()
print(date + " Starting data collection")


try:
    conn = dl_connect()
except Exception:
    print("Unable to connect to the datalogger")
    quit()

config = config()
connection = connect(date, "Temperatures")
writer = connection.cursor()

site_config = requests.get(config['Datalogger']['ip'] + config['Datalogger']['configs'], auth=HTTPBasicAuth('', config['Datalogger']['password'])).text
root = ET.fromstring(site_config.encode('ascii', 'ignore'))

day = int(root[10].text[0] + root[10].text[1])
month = int(root[10].text[2] + root[10].text[3])
year = int(root[10].text[4] + root[10].text[5])
hour = int(root[11].text[0] + root[11].text[1])

now = datetime.datetime(year, month, day, hour)

last_path = os.path.dirname(os.path.realpath(__file__)) + "/functions/electricity/Day_last_execution.txt"

last_execution = open(last_path, "r")
last_exe = last_execution.read()
last_execution.close()

day_last_exe = int(last_exe[0] + last_exe[1])
month_last_exe = int(last_exe[2] + last_exe[3])
year_last_exe = int(last_exe[4] + last_exe[5])
hour_last_exe = int(last_exe[7] + last_exe[8])

lastexe = datetime.datetime(year_last_exe, month_last_exe, day_last_exe, hour_last_exe)
onehour = datetime.timedelta(0, 0, 0, 0, 0, 1)

while lastexe <= now:
    link_general = config['Datalogger']['ip'] + "/grap_0100" + str(lastexe.day).zfill(2) + str(lastexe.month-1).zfill(2) + str(lastexe.year) + ".xml"
    link_house = config['Datalogger']['ip'] + "/grap_0101" + str(lastexe.day).zfill(2) + str(lastexe.month-1).zfill(2) + str(lastexe.year) + ".xml"
    link_downstairs = config['Datalogger']['ip'] + "/grap_0102" + str(lastexe.day).zfill(2) + str(lastexe.month-1).zfill(2) + str(lastexe.year) + ".xml"
    link_warming = config['Datalogger']['ip'] + "/grap_0103" + str(lastexe.day).zfill(2) + str(lastexe.month-1).zfill(2) + str(lastexe.year) + ".xml"
    link_hot_water = config['Datalogger']['ip'] + "/grap_0104" + str(lastexe.day).zfill(2) + str(lastexe.month-1).zfill(2) + str(lastexe.year) + ".xml"

    get(link_general, writer, lastexe.day, lastexe.month, lastexe.year, lastexe.hour-1, config, 1)
    get(link_house, writer, lastexe.day, lastexe.month, lastexe.year, lastexe.hour-1, config, 2)
    get(link_downstairs, writer, lastexe.day, lastexe.month, lastexe.year, lastexe.hour-1, config, 3)
    get(link_warming, writer, lastexe.day, lastexe.month, lastexe.year, lastexe.hour-1, config, 4)
    get(link_hot_water, writer, lastexe.day, lastexe.month, lastexe.year, lastexe.hour-1, config, 5)

    lastexe = lastexe + onehour


last_execution = open(last_path, "w")
last_execution.write(root[10].text + " " + root[11].text)
last_execution.close()

connection.close()
conn.close()
conn.close()

logout = config['Datalogger']['ip'] + config['Datalogger']['logout']
conn_logout = requests.get(logout)
conn_logout.close()

print(date + " Done!")
