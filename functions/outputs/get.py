import requests
from requests.auth import HTTPBasicAuth
import xml.etree.ElementTree as ET

from functions.outputs.processer import out_processer


# Get all the info about outputs from the websites and for each info runs insert_temp()
def out_getter(link, cmi, writer, date):
    reader = requests.get(link, auth=HTTPBasicAuth('admin', 'admin')).text
    data = '<data> <div>' + reader + '</data>'

    root = ET.fromstring(data.encode('ascii', 'ignore'))

    try:
        if cmi == 1:
            out_processer(root, 1, 0, 1, writer, date)
            out_processer(root, 2, 0, 2, writer, date)
            out_processer(root, 3, 0, 3, writer, date)
            out_processer(root, 4, 0, 4, writer, date)

        elif cmi == 2:
            out_processer(root, 1, 0, 5, writer, date)
            out_processer(root, 2, 0, 6, writer, date)
            out_processer(root, 3, 0, 7, writer, date)
            out_processer(root, 4, 0, 8, writer, date)
            out_processer(root, 5, 0, 9, writer, date)
            out_processer(root, 6, 0, 10, writer, date)

        elif cmi == 33:
            out_processer(root, 1, 0, 11, writer, date)
            out_processer(root, 2, 0, 12, writer, date)

        elif cmi == 34:
            out_processer(root, 1, 0, 13, writer, date)
            out_processer(root, 2, 0, 14, writer, date)
            out_processer(root, 3, 0, 15, writer, date)

    except Exception as e:
        if e == "Writing to the db pt.2":
            print(data)
        else:
            print("Error: '" + str(e) + "'")
