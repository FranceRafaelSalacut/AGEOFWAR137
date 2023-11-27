import socket

def getIPAdress():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    s.settimeout(0)
    ip_address = s.getsockname()
    s.close()     
    return ip_address