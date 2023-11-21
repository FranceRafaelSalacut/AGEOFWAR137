import socket

client = 0

# Server configuration
host = '192.168.1.4'
port = 5555

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
server_socket.bind(('', port))

while True:
    message, address = server_socket.recvfrom(1024)
    client+=1
    print(f"Received broadcast message from {address}: {message.decode()}")

    message = "HI welcome to server!"
    server_socket.sendto(message.encode(), address)
    if client == 1:
        break