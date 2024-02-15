import socket
import json

HOST = None
PORT = None
MAX_CLIENTS = None

#Read init values from ./values.json
with open("values.json", "r") as json_stream:
    val: dict = json.load(json_stream)
    MAX_CLIENTS = val["MAX_CLIENTS"]
    HOST = val["HOST"]
    PORT = val["PORT"]