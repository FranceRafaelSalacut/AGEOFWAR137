import socket

# Getting the Local IP address
def getIPAdress():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    s.settimeout(0)
    ip_address = s.getsockname()
    s.close()
    return ip_address

# Getting both IP address and Port
def getIPAddressAndPort():
    return getIPAdress()


if __name__ == "__main__":
    # print(getIPAdress())
    # print(find_unused_ports('127.0.0.1'))
    print('//'.join([str(x) for x in getIPAddressAndPort()]))
    # print(find_unused_ips(101,110)[0])
    # print('.'.join(getIPAdress()[0].split('.')[:-1]))
    pass