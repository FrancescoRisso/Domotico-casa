import requests
from requests.auth import HTTPBasicAuth
import xml.etree.ElementTree as ET

from functions.outputs.processer import out_processer


# Get all the info about outputs from the websites and for each info runs insert_temp()
# def out_getter(link, cmi, writer, date):
def out_getter(link, output):
    reader = requests.get(link, auth=HTTPBasicAuth("admin", "admin")).text
    data = "<data> <div>" + reader + "</data>"

    root = ET.fromstring(data.encode("ascii", "ignore"))

    try:
        return out_processer(root, output, 0)

    except Exception as e:
        print(f"Error: '{e}'")
