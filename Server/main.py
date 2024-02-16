import socket
import json

HOST = None
PORT = None
MAX_CLIENTS = None
MAX_REQ_SIZE = None

chat = [1, 5, 6]
#Read init values from ./values.json
with open("values.json", "r") as json_stream:
    val: dict = json.load(json_stream)
    MAX_CLIENTS = val["MAX_CLIENTS"]
    HOST = val["HOST"]
    PORT = val["PORT"]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(MAX_CLIENTS)
    conn, addr = s.accept()
    with conn:
        print(f"Connected by: {addr}")
        while True:
            req = conn.recv(1024)
            if not req: break
            print(req)
            req = req.decode()
            if req == "GET_CHAT":
                conn.sendall(str(chat).encode("utf-8"))

            else:
                conn.sendall("Unknown request".encode())