import socket
import threading
import time
from get_ipaddress import *


#Global Variables
servers = []

def broadcast_message():
    broadcast_message = "Discovering"
    client_socket.sendto(broadcast_message.encode(), ('<broadcast>', port))

# Server configuration
ip_address = getIPAdress()[0]
port = 5555
client_address = (ip_address, port)

# Create a UDP socket so that it can send and recieve messages without a connection
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
client_socket.bind(client_address)

# Setting a timeout so that socket doesnt wait for message indefinitely
client_socket.settimeout(1)

print(f"Client at {client_address}")

def listen_for_servers():
    broadcast = True
    for x in range(0, 30):
        print(f"{x} - running", end = " - ")
        # Placing a try catch here to catch timeout error by socket.timout

        if broadcast: 
            broadcast_message()
            broadcast = False

        try:
            message, address = client_socket.recvfrom(1024)    
            if address == client_address:
                print("I found myself")
                continue        
            if address not in servers: 
                print(f"Discovered server at {address}: {message.decode()}")
                servers.append(address)
            else:
                print(f"{address} is already discovered")
                continue
        except:
            print("Time out")
            broadcast = True
            continue
    print("stoppping")


# Start a thread to listen for servers
server_listener_thread = threading.Thread(target=listen_for_servers)
server_listener_thread.start()





server_listener_thread.join()

print(servers)