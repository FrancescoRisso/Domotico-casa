import requests
from requests.auth import HTTPBasicAuth
import xml.etree.ElementTree as ET

from functions.temperature.processer import temp_processer


# Get all the temperatures info from the websites and for each info runs temp_processer()
def temp_getter (link, cmi, date, writer):
    reader = requests.get(link, auth=HTTPBasicAuth('admin', 'admin')).text
    data = '<data>' + reader + '</data>'

    root = ET.fromstring(data.encode('ascii', 'ignore')) 

    try:
        if cmi == 1:
            temp_processer(root, 1, 11, writer, date)
            temp_processer(root, 2, 12, writer, date)
            temp_processer(root, 3, 13, writer, date)
            temp_processer(root, 4, 14, writer, date)
            temp_processer(root, 5, 15, writer, date)
            temp_processer(root, 6, 16, writer, date)

        elif cmi == 2:
            temp_processer(root, 1, 7, writer, date)
            temp_processer(root, 2, 8, writer, date)
            temp_processer(root, 3, 9, writer, date)
            temp_processer(root, 4, 10, writer, date)

        elif cmi == 33:
            temp_processer(root, 1, 1, writer, date)
            temp_processer(root, 2, 2, writer, date)

        elif cmi == 34:
            temp_processer(root, 1, 3, writer, date)
            temp_processer(root, 2, 5, writer, date)
            temp_processer(root, 3, 4, writer, date)
            temp_processer(root, 4, 6, writer, date)

    except Exception as e:
        if e == "Writing to the db pt.2":
            print(data)
        else:
            print("Error: '" + str(e) + "'")
