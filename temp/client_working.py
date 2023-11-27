import socket
import threading
from get_ipaddress import *


servers = []
# Server configuration
ip_address = getIPAdress()[0]
port = 5555
address = (ip_address, port)

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
client_socket.bind(address)
client_socket.settimeout(1)

print(f"Client at {address}")

def listen_for_servers():
    for x in range(0,3):
        print(x)
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


# Start a thread to listen for servers
server_listener_thread = threading.Thread(target=listen_for_servers)
server_listener_thread.start()
# Broadcast a message to discover servers
broadcast_message = "Client discovering servers"
client_socket.sendto(broadcast_message.encode(), ('<broadcast>', 5555))

# Placing a try catch here to catch timeout error by sccket timeout
try:
    received_message = client_socket.recv(1024).decode()
    if received_message == broadcast_message:
        print("I found my own message")
    else:
        print(f"Server says: {received_message}")
except:
    print("nothing to see here")


# Keep the client alive
server_listener_thread.join()

print(servers)
