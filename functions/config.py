import json


# Returns a file in which there are all the configs of Settings.json
def config():
    try:
        with open('./Settings.json', 'r') as settings_file:
            return json.load(settings_file)
    except Exception as e:
        print("Error while opening config file: '" + str(e) + "'")
