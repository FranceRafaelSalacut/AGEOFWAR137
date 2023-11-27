import socket
import threading
import time
from get_ipaddress import *


#Global Variables
stop_flag = False
servers = []

# Server configuration
ip_address = getIPAdress()[0]
port = 5555
client_address = (ip_address, port)

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
client_socket.bind(client_address)
client_socket.settimeout(1)

print(f"Client at {client_address}")

def listen_for_servers():
    while not stop_flag:
        print("running", end = " - ")
        # Placing a try catch here to catch timeout error by socket.timout
        try:
            message, address = client_socket.recvfrom(1024)    
            if address == client_address:
                print("I found myself")
                continue        
            print(f"Discovered server at {address}: {message.decode()}")
            servers.append(address)
        except:
            print("Time out")
            continue
        time.sleep(1)

    print("stoppping")

for x in range(0,3):
    stop_flag = False

    # Start a thread to listen for servers
    server_listener_thread = threading.Thread(target=listen_for_servers)
    server_listener_thread.start()

    # Broadcast a message to discover servers
    broadcast_message = "Discovering"
    client_socket.sendto(broadcast_message.encode(), ('<broadcast>', port))

    time.sleep(5)

    stop_flag = True

    # Wait for the client to finish
    server_listener_thread.join()

print(servers)