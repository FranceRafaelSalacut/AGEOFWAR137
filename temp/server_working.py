import socket
from get_ipaddress import *

#Global Variables
client = 0
c_clients = []

# Server configuration
ip_address = getIPAdress()[0]
port = 5555
address = (ip_address, port)

# Create a UDP socket so that it can send and recieve messages without a connection
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
server_socket.bind(address)

print(f"Server at {address}")


while True:
    message, address = server_socket.recvfrom(1024)
    message = message.decode()
    if message == "Discovering":
         print(f"Received broadcast message from {address}: {message}")
         message = "I am a server!"
         server_socket.sendto(message.encode(), address)
    else:
        client+=1
        print(f"Client Connected from {address}: {message}")
        c_clients.append(address)

    
    if client == 1:
        print("I am Full")
        break


print(c_clients)
