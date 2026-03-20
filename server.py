import socket
from parser.request import Request
from parser.response import Response
from router import Router
import asyncio

class MicroEngine:
    __PORT = 8080
    __SERVER = "127.0.0.1"
    __ADDR = (__SERVER, __PORT)
    __FORMAT = "utf-8"

    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.__ADDR)
        self.server.setblocking(False)
        self.loop = None
        self.router = Router()




    async def _handle_client_connection(self, conn, addr):
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

        message = await self.loop.sock_recv(conn, 1024)
        decoded_message = message.decode(self.__FORMAT)
        request = Request(decoded_message)

        # check if request is a valid Http request
        if request.is_valid == False:
            response = Response(status_code=400, status_message="Bad Request", headers={"Content-Type": "text/html"}, message="<h1>Invalid Request</h1>")
            await self.loop.sock_sendall(conn, response.__str__().encode(self.__FORMAT))
            conn.close()
        else:
            function = self.router.routes.get((request.path, request.method))
            if function == None:
                response = Response(status_code=404, status_message="Not Found", headers={"Content-Type": "text/html"}, message="<h1>Resource not Found</h1>")
                await self.loop.sock_sendall(conn, response.__str__().encode(self.__FORMAT))
                conn.close()
            else:
                try:
                    response_obj = await function(request)
                except Exception:
                    print(Exception.with_traceback())
                    response = Response(status_code=500, status_message="Interal Server Error", headers={"Content-Type": "text/html"}, message="<h1>Interal Server Error</h1>")
                    await self.loop.sock_sendall(conn, response.__str__().encode(self.__FORMAT))
                    conn.close()
                else:
                    await self.loop.sock_sendall(conn, response_obj.__str__().encode(self.__FORMAT))
                    conn.close()



    async def start(self):
        """
        Configuring the socket to listen and accept calls
        """
        self.server.listen()
        print(f"[SERVER STARTED] Listening on {self.__SERVER}:{self.__PORT}")
        self.loop = asyncio.get_event_loop()
        try:
            while True:
                conn, addr =  await self.loop.sock_accept(self.server)
                self.loop.create_task(self._handle_client_connection(conn, addr))
        except (KeyboardInterrupt, asyncio.exceptions.CancelledError, ConnectionAbortedError):
            self.server.close()
        
