import json


def init():
    global data
    # Opening JSON file
    f = open("./data/distances.json")
    # returns JSON object as
    # a dictionary
    data = json.load(f)
    # Closing file
    f.close()
