#!/usr/bin/python3

import PowerBoxConfig
import socket

class PowerBox:
    def __init__(self):
        self.cfg = PowerBoxConfig.PowerBoxConfig()
        self.mySocket = socket.socket()
        self.mySocket.bind((self.cfg.getAddress(),int(self.cfg.getPort())))

    def Main(self):
        while True:

            print("Waiting for connection on port " + self.cfg.getPort() + "...")
            self.mySocket.listen(1)
            conn, addr = self.mySocket.accept()
            print("Connection from: " + str(addr))

            while True:
                print("Waiting for message...")
                data = conn.recv(1024).decode()
                if not data:
                    break
                print("Received from User: " + data)
                conn.send(str("ACK").encode())

            #        data = input(" ? ")
            #        conn.send(data.encode())

            conn.close()
            print("Connection closed.")


if __name__ == '__main__':
    powerBox = PowerBox()
    powerBox.Main()
