import socket
from get_ipaddress import *


client = 0

# Server configuration
ip_address = getIPAdress()[0]
port = 5555
address = (ip_address, port)

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
server_socket.bind(address)

print(f"Server at {address}")


while True:
    message, address = server_socket.recvfrom(1024)
    if message == "Discovering":
         print(f"Received broadcast message from {address}: {message.decode()}")
    else:
        client+=6
        print(f"Client Connected from {address}: {message.decode()}")

    message = "I am a server!"
    server_socket.sendto(message.encode(), address)
    if client == 1:
        break