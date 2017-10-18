#!/usr/bin/python3.6
import json
from ast import literal_eval

def config_dict():
    """
    Opens config.json as a string and then converts it to a dictionary, then returns the dectionary
    """
    with open('config.json') as config_file:
        conf_dict = json.loads(config_file.read())
    return conf_dict

conf_dict = config_dict()

LOG_LEVEL = conf_dict['logging_level']
FLASK_DEBUG = False
THREADED = True
USE_SSL = literal_eval(conf_dict['ssl'])
BASE_URL = False
PROCESSES = 1