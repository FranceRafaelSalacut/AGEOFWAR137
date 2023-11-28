import socket 
import threading 
from src.get_ipaddress import * 

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

    def Backgroundrun(self):
        broadcast = True
        while self.running:
            print("running", end = " - ")
            
            # Broadcast message again after time out
            if broadcast: 
                broadcast_message = "Discovering"
                self.socket.sendto(broadcast_message.encode(), ('<broadcast>', self.port))
                broadcast = False

            # Placing a try catch here to catch timeout error by socket.timout
            try:
                message, address = self.socket.recvfrom(1024)    
                if address == self.address:
                    print("I found myself")
                    continue        
                if address not in self.found_servers: 
                    print(f"Discovered server at {address}: {message.decode()}")
                    self.found_servers.append(address)
                else:
                    print(f"{address} is already discovered")
                    continue
            except:
                print("Time out")
                broadcast = True
                continue
        print("stoppping")

    def startFinding(self):
        if self.running == True:
            print("Server Already Running")
            return
        
        print(f"Client at {self.address}")

        self.running = True
        self.background_thread = threading.Thread(target=self.Backgroundrun)
        self.background_thread.start()

    def stopFinding(self):
        print("Im hererer")
        self.running = False
        if self.background_thread:
            self.background_thread.join()