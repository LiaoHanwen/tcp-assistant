#!/usr/bin/python
# -*- coding: UTF-8 -*-
# file name: tcp_server.py

import socket
import threading
import time

HOST = "127.0.0.1"  # IP for local host
PORT = 9971  # Listen port


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))  # bind port
    server.listen(1)  # set max connections
    while True:
        clientSocket, addr = server.accept()
    
        print("accept tcp connection from: " + str(addr))

        # Start a receive thread
        receiveThread = ReceiveThread(clientSocket, addr)
        receiveThread.start()

        # Start an auto send thread
        bytesMessage = b"\x00\x01"  # form a bytes message
        stringMessage = "string".encode("utf-8")  # form a string message
        pauseTime = 10  # pause time (seconds)
        autoSendThread = AutoSendThread(clientSocket, addr, bytesMessage, pauseTime)
        autoSendThread.start()

        # Start a input send thread
        inputSendThread = InputSendThread(clientSocket, addr)
        inputSendThread.start()


class ReceiveThread(threading.Thread):
    """
    Receive Thread
    Receive message and print

    Parameters:
        clientSocket - a connected client tcp socket
        addr - addr infomation of clientSocket
    """

    def __init__(self, clientSocket, addr):
        threading.Thread.__init__(self)
        self.clientSocket = clientSocket
        self.addr = addr

    def run(self):
        print("ReceiveThread start")
        while True:
            message = self.clientSocket.recv(1024)  # receive message
            if len(message) == 0:
                # connection break
                print("close tcp connection from: " + str(self.addr))
                self.clientSocket.close()
                break
            print(str(self.addr) + ": ", end="")  # print message
            print(message)  # revert to utf-8: message.decode('utf-8')


class AutoSendThread(threading.Thread):
    """
    Auto send thread
    Send $message every $pauseTime seconds

    Parameters:
        clientSocket - a connected client tcp socket
        addr - addr infomation of clientSocket
        message - the message to send
        pauseTime - send message every pauseTime seconds
    """

    def __init__(self, clientSocket, addr, message, pauseTime):
        threading.Thread.__init__(self)
        self.clientSocket = clientSocket
        self.addr = addr
        self.message = message
        self.pauseTime = pauseTime

    def run(self):
        print("AutoSendThread start")
        while True:
            self.clientSocket.sendall(self.message)
            print("auto send message to: " + str(self.addr))  # print
            time.sleep(self.pauseTime)


class InputSendThread(threading.Thread):
    """
    Input send thread
    Send input message

    Parameters:
        clientSocket - a connected client tcp socket
        addr - addr infomation of clientSocket
    """

    def __init__(self, clientSocket, addr):
        threading.Thread.__init__(self)
        self.clientSocket = clientSocket
        self.addr = addr

    def run(self):
        while True:
            print("InputSendThread start")
            message = input("input message: ")
            self.clientSocket.sendall(message.encode())
            print("send message to: " + str(self.addr))


if __name__ == "__main__":
    main()
