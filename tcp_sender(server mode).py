import socket
import threading
import time

HOST = "127.0.0.1"  # IP for local host
PORT = 9971         # Listen port

MESSAGE = b'\x00\xff\xff\x00\x00\x63\x00\x14\x00\x00\x00\x03[\xbf\x01\xb4\x10\x00\x00\x03\x0068911237\x00\x00\x00\x00\x00\x00\x0013381030442\x00\x00\x00\x000\x000\x001538129974\x001538129974\x00'
TIME = 10 # s

# new thread
class StartThread(threading.Thread):
    '''New Thread'''

    def __init__(self, clientSocket, addr):
        threading.Thread.__init__(self)
        self.clientSocket = clientSocket
        self.addr = addr

    def run(self):
        print("accept tcp connection from: " + str(self.addr))
        while(True):
            clientSocket.sendall(MESSAGE)
            print("send message to: " + str(addr))
            time.sleep(TIME)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
counter = 0                 # counter for receive
server.bind((HOST, PORT))   # bind port
server.listen(5)            # set max connections
while(True):
    clientSocket, addr = server.accept()
    thread = StartThread(clientSocket, addr)
    thread.start()