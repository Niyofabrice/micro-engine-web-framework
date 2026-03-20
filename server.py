import socket
from parser.request import Request
from parser.response import Response

PORT = 8080
SERVER = "127.0.0.1"
ADDR = (SERVER, PORT)
FORMAT = "utf-8"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(ADDR)

def handle_client(conn, addr):
    """
    Handle's client connection to the socket and printing the message 
    that was sent by the client
    Parameters:
        - conn : <Socket 'object'>
            socket object of the client
        - addr : <Tuple '(str, int)'>
            ip address of the client and port number
    """
    print(f"[NEW CONNECTION] Client{addr} connected.\n")

    message =  conn.recv(2048).decode(FORMAT)
    request = Request(message)
    print(request)
    print(f"Client{addr} sent:\n{request.body}")
    print(f"Message Length: {len(request.body)}")
    if request.is_valid == False:
        response = Response(status_code=400, status_message="Bad Request", headers={"Content-Type": "text/plain"}, message="Invalid Request")
        print(response)
        conn.send(response.__str__().encode(FORMAT))
        conn.close()
        return
    conn.close()


def start():
    """
    Configuring the socket to listen and accept calls
    """
    server.listen()
    print(f"[SERVER STARTED] Listening on {SERVER}:{PORT}")
    while True:
        conn, addr = server.accept()
        handle_client(conn, addr)
    

start()
