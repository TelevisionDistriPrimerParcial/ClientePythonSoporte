#!/usr/bin/python
import socket
import sys
import select

HOST = '127.0.0.1'
PORT = 9001

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.settimeout(2)
try:
    s.connect((HOST, PORT))
except:
    print "No se pudo conectar"
    sys.exit()
while True:
    socket_list = [sys.stdin,s]
    read_sockets, write_sockets, error_sockets = select.select(socket_list,[],[])
    for sock in read_sockets:
        if sock == s:
            data = sock.recv(4096)
            if not data:
                print "\n Se a desconectado del servidor"
                sys.exit()
            else:
                sys.stdout.write(data)
                sys.stdout.write('[Support] '); sys.stdout.flush()
        else:
            msg = sys.stdin.readline()
            s.send(msg)
            sys.stdout.write('[Support] '); sys.stdout.flush()