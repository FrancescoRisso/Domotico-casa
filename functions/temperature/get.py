import requests
from requests.auth import HTTPBasicAuth
import xml.etree.ElementTree as ET

from functions.temperature.processer import temp_processer


# Get all the temperatures info from the websites and for each info runs temp_processer()
# def temp_getter (link, cmi, date, writer):
def temp_getter(link, input):
    reader = requests.get(link, auth=HTTPBasicAuth("admin", "admin")).text
    data = "<data>" + reader + "</data>"

    root = ET.fromstring(data.encode("ascii", "ignore"))

    try:
        return float(temp_processer(root, input))

    except Exception as e:
        print(f"Error: '{e}'")
