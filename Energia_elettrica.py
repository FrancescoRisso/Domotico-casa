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
from functions.insert import insert

print(f"{get_date()} Starting data collection")

try:
    conn = dl_connect()
except Exception as e:
    print(f"Unable to connect to the datalogger: '{e}'")
    quit()


config = config()
try:
    connection = connect(get_date())
except Exception:
    quit()

writer = connection.cursor()

site_config = requests.get(
    config["Datalogger"]["ip"] + config["Datalogger"]["configs"],
    auth=HTTPBasicAuth("", config["Datalogger"]["password"]),
).text
root = ET.fromstring(site_config.encode("ascii", "ignore"))

day = int(root[10].text[0] + root[10].text[1])
month = int(root[10].text[2] + root[10].text[3])
year = int(root[10].text[4] + root[10].text[5])
hour = int(root[11].text[0] + root[11].text[1])

now = datetime.datetime(year, month, day, hour)

writer.execute("SELECT Data FROM CONSUMPTIONS_LAST_EXE WHERE Id = 1")
last_exe = writer.fetchall()[0][0]

day_last_exe = int(last_exe[0] + last_exe[1])
month_last_exe = int(last_exe[2] + last_exe[3])
year_last_exe = int(last_exe[4] + last_exe[5])
hour_last_exe = int(last_exe[7] + last_exe[8])

lastexe = datetime.datetime(year_last_exe, month_last_exe, day_last_exe, hour_last_exe)

print(f"{get_date()} Saving data from 20{lastexe.year}-{lastexe.month:02}-{lastexe.day:02} {lastexe.hour:02}:00")
onehour = datetime.timedelta(0, 0, 0, 0, 0, 1)

now = now - onehour

# Since we're not sure that Bticino saved all data already, we have to store data in the database
# till one hour ago
print(f"{get_date()} Saving data till 20{now.year}-{now.month:02}-{now.day:02} {now.hour:02}:00")

values = [
    {"name": "General", "value": None, "baselink": f"{config['Datalogger']['ip']}/grap_0100"},
    {"name": "House", "value": None, "baselink": f"{config['Datalogger']['ip']}/grap_0101"},
    {"name": "Downstairs", "value": None, "baselink": f"{config['Datalogger']['ip']}/grap_0102"},
    {"name": "Warming", "value": None, "baselink": f"{config['Datalogger']['ip']}/grap_0103"},
    {"name": "Hot_water", "value": None, "baselink": f"{config['Datalogger']['ip']}/grap_0104"},
    {"name": "Solar_panel", "value": None, "baselink": f"{config['Datalogger']['ip']}/grap_0105"},
    {"name": "WallBox", "value": None, "baselink": f"{config['Datalogger']['ip']}/grap_0106"},
    {"name": "Cooker", "value": None, "baselink": f"{config['Datalogger']['ip']}/grap_0107"},
    {"name": "Oven", "value": None, "baselink": f"{config['Datalogger']['ip']}/grap_0108"},
]

print(f"{get_date()} Inserting consumptions in the database")

while lastexe <= now:
    for value in values:
        link = f"{value['baselink']}{lastexe.day:02}{(lastexe.month-1):02}{lastexe.year}.xml"
        value["value"] = get(link, lastexe, config)

    insert(values, writer, lastexe.replace(year=2000 + lastexe.year), "CONSUMPTIONS")

    lastexe = lastexe + onehour

newLastExe = f"{root[10].text} {root[11].text}"
writer.execute("UPDATE CONSUMPTIONS_LAST_EXE SET Data = %s WHERE Id = 1", (newLastExe, ))

connection.close()
logout = config["Datalogger"]["ip"] + config["Datalogger"]["logout"]
conn_logout = requests.get(logout)
conn_logout.close()

print(get_date() + " Done!")
