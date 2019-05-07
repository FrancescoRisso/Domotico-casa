import requests
from requests.auth import HTTPBasicAuth
import xml.etree.ElementTree as ET

from functions.electricity.insert import insert


def get(link, writer, day, month, year, hour, config, source):
    data = requests.get(link, auth=HTTPBasicAuth('', config['Datalogger']['password'])).text
    root = ET.fromstring(data.encode('ascii', 'ignore'))

    i = 5

    try:
        while int(root[i][2].text) != hour:
            i = i + 9

        date = "20" + str(year) + "-" + str(month) + "-" + str(day) + "-" + str(hour) + ":00:00"
        insert(root[i][3].text, source, writer, date)

    except Exception as e:
        print("Error while getting the data: '" + str(e) + "'")

