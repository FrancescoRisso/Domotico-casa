import requests
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

try: dl_connect()
except Exception as e: print("Error while connecting to the datalogger: '" + str(e) + "'")

config = config()
connection = connect(date, "Electricity")
writer = connection.cursor()

site_config = requests.get(config['Datalogger']['ip'] + config['Datalogger']['configs'], auth=HTTPBasicAuth('', config['Datalogger']['password'])).text
root = ET.fromstring(site_config.encode('ascii', 'ignore'))

day = root[10].text[0] + root[10].text[1]
month = root[10].text[2] + root[10].text[3]
year = root[10].text[4] + root[10].text[5]
hour = int(root[11].text[0] + root[11].text[1])

last_path = os.path.dirname(os.path.realpath(__file__)) + "/functions/electricity/Day_last_execution.txt"

last_execution = open(last_path, "r")
day_last_exe = last_execution.read()
last_execution.close()

last_execution = open(last_path, "w")
last_execution.write(root[10].text)
last_execution.close()

if (day_last_exe[0] != day[0]) or (day_last_exe[1] != day[1]):
    # LAST EXE HAS BEEN YESTERDAY
    day = day_last_exe[0] + day_last_exe[1]
    month = day_last_exe[2] + day_last_exe[3]
    year = day_last_exe[4]+ day_last_exe[5]
    hour = 23

if int(month) < 11:
    link_general = config['Datalogger']['ip'] + "/grap_0100" + day + "0" + str(int(month) - 1) + year + ".xml"
    link_house = config['Datalogger']['ip'] + "/grap_0101" + day + "0" + str(int(month) - 1) + year + ".xml"
    link_downstairs = config['Datalogger']['ip'] + "/grap_0102" + day + "0" + str(int(month) - 1) + year + ".xml"
    link_warming = config['Datalogger']['ip'] + "/grap_0103" + day + "0" + str(int(month) - 1) + year + ".xml"
    link_hot_water = config['Datalogger']['ip'] + "/grap_0104" + day + "0" + str(int(month) - 1) + year + ".xml"
else:
    link_general = config['Datalogger']['ip'] + "/grap_0100" + day + str(int(month) - 1) + year + ".xml"
    link_house = config['Datalogger']['ip'] + "/grap_0101" + day + str(int(month) - 1) + year + ".xml"
    link_downstairs = config['Datalogger']['ip'] + "/grap_0102" + day + str(int(month) - 1) + year + ".xml"
    link_warming = config['Datalogger']['ip'] + "/grap_0103" + day + str(int(month) - 1) + year + ".xml"
    link_hot_water = config['Datalogger']['ip'] + "/grap_0104" + day + str(int(month) - 1) + year + ".xml"

get(link_general, writer, day, month, year, hour-1, config, 1)
get(link_house, writer, day, month, year, hour-1, config, 2)
get(link_downstairs, writer, day, month, year, hour-1, config, 3)
get(link_warming, writer, day, month, year, hour-1, config, 4)
get(link_hot_water, writer, day, month, year, hour-1, config, 5)

connection.close()
print(date + " Done!")
