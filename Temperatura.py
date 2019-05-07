from xml.etree.ElementTree import ParseError

from functions.connect import connect
from functions.date import get_date
from functions.temperature.get import temp_getter
from functions.outputs.get import out_getter
from functions.config import config

date = get_date()
print(date + " Starting data collection")

config = config()
connection = connect(date, "Temperatures")
writer = connection.cursor()

temp_getter(config['Cmi']['ip']+config['Cmi']['link']+config['Cmi']['Inputs']['nodo1'], 1, date, writer)
temp_getter(config['Cmi']['ip']+config['Cmi']['link']+config['Cmi']['Inputs']['nodo2'], 2, date, writer)
temp_getter(config['Cmi']['ip']+config['Cmi']['link']+config['Cmi']['Inputs']['nodo33'], 33, date, writer)
temp_getter(config['Cmi']['ip']+config['Cmi']['link']+config['Cmi']['Inputs']['nodo34'], 34, date, writer)

out_getter(config['Cmi']['ip']+config['Cmi']['link']+config['Cmi']['Outputs']['nodo1'], 1, writer, date)
out_getter(config['Cmi']['ip']+config['Cmi']['link']+config['Cmi']['Outputs']['nodo2'], 2, writer, date)
out_getter(config['Cmi']['ip']+config['Cmi']['link']+config['Cmi']['Outputs']['nodo33'], 33, writer, date)
out_getter(config['Cmi']['ip']+config['Cmi']['link']+config['Cmi']['Outputs']['nodo34'], 34, writer, date)

connection.close()
print(date + " Done!")
