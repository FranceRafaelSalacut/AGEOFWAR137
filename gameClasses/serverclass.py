import socket 
from src.get_ipaddress import * 

class Server():
    def __init__(self) -> None:
        self.ip_address = getIPAdress()[0]
        self.port = 5555
        self.address = (self.ip_address, self.port)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.socket.bind(self.address)

    def startServer(self):
        client = 0
        c_clients = []
        while True:
            # Waiting to recieve a message anonymously
            message, address = self.socket.recvfrom(1024)
            message = message.decode()
            if message == "Discovering":
                print(f"Received broadcast message from {address}: {message}")
                message = "I am a server!"
                self.socket.sendto(message.encode(), address)
            else:
                #Limiting the number of clients that connects with server.
                client+=1
                print(f"Client Connected from {address}: {message}")
                c_clients.append(address)

            
            if client == 1:
                print("I am Full")
                break
