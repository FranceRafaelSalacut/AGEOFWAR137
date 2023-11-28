import socket 
import threading
from src.get_ipaddress import * 
from gameClasses.text import *


client = 0
c_clients = []

class Server():
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


    def Backgroundrun(self):
        global client, c_clients
        while self.running:
            print("Running", end = " - ")
            # Waiting to recieve a message anonymously
            try:
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
            except:
                print("Timeout")
                continue
        print("Stopping")

    def startServer(self, display:Text):
        if self.running == True:
            display.changeText("Server Already Running")
            return
        
        display.changeText(f"Server at {self.address}")

        self.running = True
        self.background_thread = threading.Thread(target=self.Backgroundrun)
        self.background_thread.start()

    def stopServer(self, display:Text):
        if self.running == False:
            display.changeText("Server not Running")
            return

        display.changeText("Stopping Server")
        self.running = False
        if self.background_thread:
            self.background_thread.join()
        
