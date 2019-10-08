#!/usr/bin/python3

import PowerBoxConfig
import socket
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
inList = [4, 17, 27, 22, 5, 6, 13, 19]

class PowerBox:
    def __init__(self):
        self.cfg = PowerBoxConfig.PowerBoxConfig()
        self.mySocket = socket.socket()
        self.mySocket.bind((self.cfg.getAddress(),int(self.cfg.getPort())))

    def Main(self):

        for i in pinList:
            GPIO.setup(i, GPIO.OUT)
            GPIO.output(i, GPIO.HIGH)

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
                tokens = data.split(',')
                print("Token 1: ", tokens[0])
                print("Token 2: ", tokens[1])

                #GPIO.output()



                conn.send(str("ACK").encode())

            #        data = input(" ? ")
            #        conn.send(data.encode())

            conn.close()
            print("Connection closed.")


if __name__ == '__main__':
    powerBox = PowerBox()
    powerBox.Main()
