import socket

PORT = 8080
SERVER = "127.0.0.1"
ADDR = (SERVER, PORT)

FORMAT = "utf-8"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(ADDR)

message = "Hello World!"

client.send(message.encode(FORMAT))
