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

sys.stdout.flush()

def connect_server(mensaje):
    data = ''
    send_m = True
    stop_b = True
    while stop_b:
        socket_list = [sys.stdin, s]
        ready_to_read,ready_to_write,in_error = select.select(socket_list , [], [])
        for sock in ready_to_read:
            if sock == s:
                data = sock.recv(4096)
                if not data:
                    print '\nSe ha desconectado del Servidor'
                    sys.exit()
                else:
                    data = data
                    stop_b = False
            else:
                msg = mensaje
                if send_m:
                    s.send(msg)
                    send_m = False

    s.close()
    return data

print "Hacer una peticion: "
msg = sys.stdin.readline()
res = connect_server(msg)
print res
