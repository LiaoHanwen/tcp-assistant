import socket

HOST = "127.0.0.1"  # IP for local host
PORT = 9971         # Listen port

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
counter = 0  # counter for receive
server.bind((HOST, PORT))  # bind port
while(True):
    counter += 1
    data, addr = server.recvfrom(1024)
    print(str(counter) + ": ", addr, data)