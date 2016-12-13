#!/usr/bin/python
import socket
import sys
import time
import os

#HOST, PORT = "localhost", 9001
HOST, PORT = "181.39.211.117", 7000
def send_recived(data):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    received = ''
    try:
        sock.connect((HOST, PORT))
        sub = 'SOPORT'
        while True:
            sock.sendall((bytes(sub + "\n")))
            break
        sock.sendall(bytes(data + "\n"))
        received = str(sock.recv(4096))
    except :
        print 'No se ha conectado con el Servidor'
        sys.exit()
    finally:
        sock.close()
        return received

def date_format():
    date = time.strftime("%Y%m%d%H%M%S")
    return date

def get_peti_login(result):
    fecha = date_format()
    petic_login = 'RQSOPORT00000LOGIN0'+fecha
    t_init = len(petic_login)
    t_fina = len(result)
    petic = result[t_init:t_fina]
    size = len(petic)
    num_id = petic[6:11]
    request = petic[0:6]
    data = petic[11:size]
    return request,num_id,data

def set_peti_login(user_name,user_password):
    fecha = date_format()
    petic_login = 'RQSOPORT00000LOGIN0'+fecha+user_name+'|'+user_password
    return petic_login

def print_init_session():
    print 30 * "-" , "INICIAR SECION" , 30 * "-"
    print 'Nombre de Usuario:'
    name = sys.stdin.readline()
    print 'Clave:'
    password = sys.stdin.readline()
    return name.strip(),password.strip()

def get_peti_InfoCli(result,user_num):
    fecha = date_format()
    petic_login = 'RQSOPORT'+user_num+'CLICED'+fecha
    t_init = len(petic_login)
    t_fina = len(result)
    petic = result[t_init:t_fina]
    size = len(petic)
    request = petic[0:6]
    data = petic[6:size]
    client = data
    return request,data

#RQENROLL00001CLICED201612032330181721557823
def set_peti_InfoCli(cli_cedula,user_num):
    fecha = date_format()
    petic_login = 'RQSOPORT'+user_num+'CLICED'+fecha+cli_cedula
    return petic_login

name,password = print_init_session()
data = set_peti_login(name,password)
us = send_recived(data)
peti,num,data = get_peti_login(us)
print peti
print num
print data

cedula = set_peti_InfoCli("1721557824",num)
print cedula
cli = send_recived(cedula)
print cli
petiCli,dataCli = get_peti_InfoCli(cli,num)
print petiCli
print dataCli




