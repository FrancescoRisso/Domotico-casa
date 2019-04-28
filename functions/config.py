import json


# Returns a file in which there are all the configs of Settings.json
def config():
    with open('Settings.json', 'r') as settings_file:
        return json.load(settings_file)
