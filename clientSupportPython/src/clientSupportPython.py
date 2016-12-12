#!/usr/bin/python
import socket, sys

HOST, PORT = "localhost", 9001

def send_recived(data):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((HOST, PORT))
        sub = 'SOPORT'
        while True:
            sock.sendall((bytes(sub + "\n")))
            break
        sock.sendall(bytes(data + "\n"))
        received = str(sock.recv(4096))
    finally:
        sock.close()
        return received

us = send_recived("RQSOPORT00000LOGIN020161203233018alias123|pass")
print (us)

u = send_recived("RQSOPORT00000LOGIN020161203233018test_emp|123.456")
print (u)