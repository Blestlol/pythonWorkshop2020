import socket
remoteServer = input("Enter the port to scan: ")
for port in range(1,8081):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((remoteServer, port))
    if result == 0:
        print("Port{}:Open".format(port))
    else:
        print("Port{}:Closed".format(port))
    sock.close()