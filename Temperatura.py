import time

from functions.connect import connect
from functions.date import get_date
from functions.temperature.get import temp_getter
from functions.outputs.get import out_getter
from functions.insert import insert
from functions.config import config

print(f"{get_date()} Starting data collection")

config = config()

try:
    connection = connect(get_date())
except Exception:
    quit()

writer = connection.cursor()

temperatures = [
    {
        "name": "Camera_Francesco",
        "node": "nodo33",
        "input": 1,
        "values": [],
        "value": None
    },
    {
        "name": "Camera_Valentina",
        "node": "nodo33",
        "input": 2,
        "values": [],
        "value": None
    },
    {
        "name": "Studio",
        "node": "nodo34",
        "input": 1,
        "values": [],
        "value": None
    },
    {
        "name": "Salone",
        "node": "nodo34",
        "input": 3,
        "values": [],
        "value": None
    },
    {
        "name": "Camera_genitori",
        "node": "nodo34",
        "input": 2,
        "values": [],
        "value": None
    },
    {
        "name": "Esterna",
        "node": "nodo34",
        "input": 4,
        "values": [],
        "value": None
    },
    {
        "name": "Collettore",
        "node": "nodo2",
        "input": 1,
        "values": [],
        "value": None
    },
    {
        "name": "Accumulo_raffreddamento",
        "node": "nodo2",
        "input": 2,
        "values": [],
        "value": None
    },
    {
        "name": "Inferiore_boiler",
        "node": "nodo2",
        "input": 3,
        "values": [],
        "value": None
    },
    {
        "name": "Ricircolo",
        "node": "nodo2",
        "input": 4,
        "values": [],
        "value": None
    },
    {
        "name": "Ritorno_circuito_lato_puffer",
        "node": "nodo2",
        "input": 5,
        "values": [],
        "value": None
    },
    {
        "name": "Mandata_PDC",
        "node": "nodo1",
        "input": 1,
        "values": [],
        "value": None
    },
    {
        "name": "Ritorno_PDC",
        "node": "nodo1",
        "input": 2,
        "values": [],
        "value": None
    },
    {
        "name": "Accumulatore_superiore",
        "node": "nodo1",
        "input": 4,
        "values": [],
        "value": None
    },
    {
        "name": "Accumulatore_inferiore",
        "node": "nodo1",
        "input": 3,
        "values": [],
        "value": None
    },
    {
        "name": "Mandata_riscaldamento_sotto",
        "node": "nodo1",
        "input": 5,
        "values": [],
        "value": None
    },
    {
        "name": "Mandata_riscaldamento_sopra",
        "node": "nodo1",
        "input": 6,
        "values": [],
        "value": None
    },
    {
        "name": "Ritorno_riscaldamento",
        "node": "nodo2",
        "input": 5,
        "values": [],
        "value": None
    }
]

outputs = [
    {
        "name": "Pompa_riscaldamento_sotto",
        "node": "nodo1",
        "output": 1,
        "value": None
    },
    {
        "name": "Pompa_riscaldamento_sopra",
        "node": "nodo1",
        "output": 2,
        "value": None
    },
    {
        "name": "Miscelatrice_riscaldamento_sotto",
        "node": "nodo1",
        "output": 3,
        "value": None
    },
    {
        "name": "Miscelatrice_riscaldamento_sopra",
        "node": "nodo1",
        "output": 5,
        "value": None
    },
    {
        "name": "Pompa_ricircolo",
        "node": "nodo2",
        "output": 1,
        "value": None
    },
    {
        "name": "Pompa_solare",
        "node": "nodo2",
        "output": 2,
        "value": None
    },
    {
        "name": "Valvole_deviatrici",
        "node": "nodo2",
        "output": 3,
        "value": None
    },
    {
        "name": "Pompa_VMC",
        "node": "nodo2",
        "output": 4,
        "value": None
    },
    {
        "name": "PDC_h_c",
        "node": "nodo2",
        "output": 5,
        "value": None
    },
    {
        "name": "PDC_on_off",
        "node": "nodo2",
        "output": 6,
        "value": None
    },
    {
        "name": "Camera_Francesco",
        "node": "nodo33",
        "output": 1,
        "value": None
    },
    {
        "name": "Camera_Valentina",
        "node": "nodo33",
        "output": 2,
        "value": None
    },
    {
        "name": "Studio",
        "node": "nodo34",
        "output": 1,
        "value": None
    },
    {
        "name": "Camera_genitori",
        "node": "nodo34",
        "output": 2,
        "value": None
    },
    {
        "name": "Salone",
        "node": "nodo34",
        "output": 3,
        "value": None
    },
]

baselink = config['Cmi']['ip']+config['Cmi']['link']

for i in range (0, 5):
    for sonda in temperatures:
        link = baselink + config['Cmi']['Inputs'][sonda["node"]]
        sonda["values"].append(temp_getter(link, sonda["input"]))

    if i != 4:
        time.sleep(50)

for sonda in temperatures:
    sonda["value"] = round(sum(sonda['values']) / len(sonda['values']), 1)
    #print(f"{sonda['name']}\n\tMisure:{sonda['values']}\n\tMedia:{sonda['value']}\n")

for sonda in outputs:
    link = baselink + config['Cmi']['Outputs'][sonda["node"]]
    if sonda["output"] == 5 and sonda["node"] == "nodo1":
        sonda["value"] = out_getter(link, 4)
    else:
        sonda["value"] = out_getter(link, sonda["output"])

print(f"{get_date()} Inserting temperatures in the database")
insert(temperatures, writer, get_date(), "TEMPERATURES")

print(f"{get_date()} Inserting outputs in the database")
insert(outputs, writer, get_date(), "OUTPUTS")

connection.close()
print(get_date() + " Done!")
