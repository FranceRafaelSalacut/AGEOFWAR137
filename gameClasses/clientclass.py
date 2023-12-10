import socket 
import threading 
from src.get_ipaddress import * 
from gameClasses.text import *

class Client():
    def __init__(self) -> None:
        self.ip_address = getIPAdress()[0]
        self.port = 5555
        self.address = (self.ip_address, self.port)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.socket.settimeout(1)
        self.socket.bind(self.address)
        self.background_thread = None
        self.running = False
        self.found_servers = []
    

    def waitToStart(self):
        while self.running:
            try:
                message, address = self.socket.recvfrom(1024)
                if message.decode() == "START":
                    break
            except:
                continue

    def startFinding(self, display:[], connect:[]):
        self.found_servers = []

        print(f"Client at {self.address}")

        broadcast_message = "Discovering"
        self.socket.sendto(broadcast_message.encode(), ('<broadcast>', self.port))

        # Turn this into a thread later
        while True:
            try:
                message, address = self.socket.recvfrom(1024)    
                if address == self.address:
                    print("I found myself")

                if message.decode() == "Discovering":
                    print("Another Client")
                    continue

                if address != self.address:
                    #print("I found myself")
                    if address not in self.found_servers: 
                        print(f"Discovered server at {address}: {message.decode()}")
                        self.found_servers.append(address)
                    else:
                        print(f"{address} is already discovered")
            except:
                break

        for index, address in enumerate(self.found_servers):
            connect[index+3].changeText(f"{address}")
            display.append(connect[index])
            display.append(connect[index+3])
        print(self.found_servers)

        if len(self.found_servers) == 0:
            connect[3].changeText("Cant find any Servers :(")
            display.append(connect[3])
    def stopFinding(self):
        print("unused function")


    def connect(self, index):
        connect_message = socket.gethostname()
        print(f"{self.found_servers} == {index}")
        print(f"{self.found_servers[index]}, {type(self.found_servers[index])}")
        self.socket.sendto(connect_message.encode(), self.found_servers[index])

        self.running = True
        self.background_thread = threading.Thread(target=self.waitToStart)
        self.background_thread.start()

    def stopwait(self):
        self.running = False
        if self.background_thread:
            self.background_thread.join()
    def close(self):
        self.socket.close()