import json
import os


# Returns a file in which there are all the configs of Settings.json
def config():
    try:
        file_path = os.path.dirname(os.path.realpath(__file__)) + "/../Settings.json"
        with open(file_path, "r") as settings_file:
            return json.load(settings_file)
    except Exception as e:
        print(f"Error while opening config file: '{e}'")
