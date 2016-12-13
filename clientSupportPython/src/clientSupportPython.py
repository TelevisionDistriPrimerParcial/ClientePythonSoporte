#!/usr/bin/python
import socket
import sys
import time
import os

HOST, PORT = "10.2.121.2", 7000

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

def close_connection_server(user_num):
    petic_close = 'RQENROLL'+user_num+'CERSES'+date_format()+'OUT'
    request = send_recived(petic_close)
    return request

def confirm_close_connection_server(user_num,result):
    petic_close = 'RQENROLL'+user_num+'CERSES'+date_format()
    t_init = len(petic_close)
    t_fina = len(result)
    petic = result[t_init:t_fina]
    size = len(petic)
    request = petic[0:6]
    data = petic[11:size]
    return request,data

def finally_close_connection(user_num):
    data_close = close_connection_server(user_num)
    close,data_close = confirm_close_connection_server(user_num,data_close)


def date_format():
    date = time.strftime("%Y%m%d%H%M%S")
    return date

def get_peti_login(result):
    petic_login = 'RQSOPORT00000LOGIN0'+date_format()
    t_init = len(petic_login)
    t_fina = len(result)
    petic = result[t_init:t_fina]
    size = len(petic)
    num_id = petic[6:11]
    request = petic[0:6]
    data = petic[11:size]
    return request,num_id,data

def set_peti_login(user_name,user_password):
    petic_login = 'RQSOPORT00000LOGIN0'+date_format()+user_name+'|'+user_password
    return petic_login

def print_init_session():
    print 30 * "-" , "INICIAR SECION" , 30 * "-"
    print 'Nombre de Usuario:'
    name = sys.stdin.readline()
    print 'Clave:'
    password = sys.stdin.readline()
    return name.strip(),password.strip()

def get_peti_InfoCli(result,user_num):
    petic_login = 'RQSOPORT'+user_num+'CLICED'+date_format()
    t_init = len(petic_login)
    t_fina = len(result)
    petic = result[t_init:t_fina]
    size = len(petic)
    request = petic[0:6]
    data = petic[6:size]
    return request,data

def set_peti_InfoCli(cli_cedula,user_num):
    petic_login = 'RQSOPORT'+user_num+'CLICED'+date_format()+cli_cedula
    return petic_login

def get_peti_servicio_adicional(result,user_num):
    petic_login = 'RQSOPORT'+user_num+'CLICED'+date_format()
    t_init = len(petic_login)
    t_fina = len(result)
    petic = result[t_init:t_fina]
    size = len(petic)
    request = petic[0:6]
    data = petic[6:size]
    return request,data

#funcion logueo
def login_session():
    name,password = print_init_session()
    data = set_peti_login(name,password)
    us = send_recived(data)
    peti,num,data = get_peti_login(us)
    return peti,num,data

# envio peticion cliced
def ingreseClientByCedula(num_cli):
    print 30 * "-" , "BUSCAR CLIENTE" , 30 * "-"
    print 'Ingrese Cedula:'
    cedula = sys.stdin.readline()
    return cedula.strip()

def findClienteByCedula(cedula,num_cli):
     peti_ced = set_peti_InfoCli(cedula,num_cli)
     cli = send_recived(peti_ced)
     petiCli,dataCli = get_peti_InfoCli(cli,num_cli)
     return petiCli,dataCli

#funcion de parceo
def parceo_data_peti_list(data_cli):
    datalist_init = data_cli.replace(" ","_")
    datalist_init0 = datalist_init.replace("|"," ")
    datalist_midle = datalist_init0.replace("%","-")
    datalist_final = datalist_midle.replace("&"," ")

    enie ='\xc3\xb1'
    nin = 'n'

    datalist_encode = datalist_final.replace(enie,nin)

    list = datalist_encode.split()
    list_f = []

    for index, data in enumerate(list):
        list_f.insert(index,data)

    return list_f

# create menu contratos
def create_menu_contratos(list_data_contratos):
    limit = len(list_data_contratos)
    print '\nCLIENTE: '+list_data_contratos[0]+' '+list_data_contratos[1]
    cont = 0
    list_menu = []
    for index in range(2,limit):
        list_menu.insert(cont,list_data_contratos[index])
        cont = cont +1

    return list_menu

def print_menu_contratos(list_contratos):
    print 30 * "-" , "CONTRATOS DEL CLIENTE" , 30 * "-"
    index = 0
    for contrato in list_contratos:
        print "<<",index,">>",contrato
        index = index +1

def seleccionar_contrato():
    print '\nSeleccionar Contrato:'
    num_contrato = sys.stdin.readline()
    return num_contrato.strip()

def parcear_lista_select_menu(select_list):
    contrato_select = select_list.replace("-"," ")
    list_c_s = contrato_select.split()
    list_c_c_f = []
    for index, data in enumerate(list_c_s):
        list_c_c_f.insert(index,data)
    return list_c_c_f[0]

def set_peti_servicio_adicional(num_us_code):
    peti_serv_adi = 'RQSOPORT'+num_us_code+'CONADI'+date_format()+'ADICIO'
    data_serv_adi = send_recived(peti_serv_adi)
    return data_serv_adi

def get_peti_servicio_adicional(result,user_num):
    petic_serv_adi = 'RQSOPORT'+user_num+'CONADI'+date_format()
    t_init = len(petic_serv_adi)
    t_fina = len(result)
    petic = result[t_init:t_fina]
    size = len(petic)
    request = petic[0:6]
    data = petic[6:size]
    return request,data

def print_menu_servicio_adicional(list_servicios):
    print 30 * "-" , "SERVICIOS ADICIONALES" , 30 * "-"
    index = 0
    for contrato in list_servicios:
        print "<<",index,">>",contrato
        index = index +1

def seleccionar_servicio_adicional():
    print '\nSeleccionar Servicio Adicional:'
    num_serv_adi = sys.stdin.readline()
    return num_serv_adi.strip()

def set_peti_canal_premiun(num_us_code):
    peti_canal_premiun = 'RQSOPORT'+num_us_code+'CONPRE'+date_format()+'PREMIU'
    data_canal_premiun = send_recived(peti_canal_premiun)
    return data_canal_premiun

def get_peti_canal_premiun(result,user_num):
    peti_canal_premiun = 'RQSOPORT'+user_num+'CONPRE'+date_format()
    t_init = len(peti_canal_premiun)
    t_fina = len(result)
    petic = result[t_init:t_fina]
    size = len(petic)
    request = petic[0:6]
    data = petic[6:size]
    return request,data

def print_menu_canal_premiun(list_canal):
    print 30 * "-" , "CANALES PREMIUN" , 30 * "-"
    index = 0
    for contrato in list_canal:
        print "<<",index,">>",contrato
        index = index +1

def seleccionar_canal_premiun():
    print '\nSeleccionar Servicio Adicional:'
    num_serv_adi = sys.stdin.readline()
    return num_serv_adi.strip()

def cliente_cedula_contratos(num_us_cli):
    cod_num_contrato = ''
    cedula_cli = ingreseClientByCedula(num_us)
    peti_cli,data_cli = findClienteByCedula(cedula_cli,num_us_cli)
    lis_data_cli = parceo_data_peti_list(data_cli)
    list_menu_contrato = create_menu_contratos(lis_data_cli)
    print_menu_contratos(list_menu_contrato)
    num_contrato_select = seleccionar_contrato()
    if num_contrato_select.isdigit():
        if 0 <= int(num_contrato_select) < len(list_menu_contrato):
            contrato_selection = list_menu_contrato[int(num_contrato_select)]
            cod_num_contrato = parcear_lista_select_menu(contrato_selection)
            print '\nContrato elegido: '+contrato_selection
        else:
            print "\nLa opcion seleccionada no es valida"
    else:
            print "\nLa opcion seleccionada no es valida"
    return cod_num_contrato

def select_servicios_adicionales(num_us_cli):
    cod_num_serv_adi = ''
    data_peti_ser_adi = set_peti_servicio_adicional(num_us)
    access_serv_adi, data_serv_adi = get_peti_servicio_adicional(data_peti_ser_adi,num_us_cli)
    list_servi_adi_menu = parceo_data_peti_list(data_serv_adi)
    print_menu_servicio_adicional(list_servi_adi_menu)
    num_serv_adi_select = seleccionar_servicio_adicional()
    if num_serv_adi_select.isdigit():
        if 0 <= int(num_serv_adi_select) < len(list_servi_adi_menu):
            serv_adi_selection = list_servi_adi_menu[int(num_serv_adi_select)]
            cod_num_serv_adi = parcear_lista_select_menu(serv_adi_selection)
            print '\nServicio Adicional elegido: '+serv_adi_selection
        else:
            print "\nLa opcion seleccionada no es valida"
    else:
        print "\nLa opcion seleccionada no es valida"
    return cod_num_serv_adi

def select_canales_premiun(num_us_cli):
    cod_num_can_pre = ''
    data_peti_can_pre = set_peti_canal_premiun(num_us)
    access_can_pre,data_can_pre = get_peti_canal_premiun(data_peti_can_pre,num_us_cli)
    list_can_pre_menu = parceo_data_peti_list(data_can_pre)
    print_menu_canal_premiun(list_can_pre_menu)
    num_can_pre_select = seleccionar_canal_premiun()
    if num_can_pre_select.isdigit():
        if 0 <= int(num_can_pre_select) < len(list_can_pre_menu):
            can_pre_selection = list_can_pre_menu[int(num_can_pre_select)]
            cod_num_can_pre = parcear_lista_select_menu(can_pre_selection)
            print '\nCanal Premiun elegido: '+can_pre_selection
        else:
            print "\nLa opcion seleccionada no es valida"
    else:
        print "\nLa opcion seleccionada no es valida"
    return cod_num_can_pre

def save_ticket_servicio_canal_1(num_us_cli,cod_cont,cod_serv_adi,cod_can_pre):
    peti_ticket_servicio_canal = 'RQSOPORT'+num_us_cli+'SERTEC'+date_format()+cod_cont+'|'+cod_serv_adi+'|'+cod_can_pre
    data_ticket_servicio_canal = send_recived(peti_ticket_servicio_canal)
    return data_ticket_servicio_canal

def save_ticket_servicio_canal_2(num_us_cli,cod_cont,cod_serv_adi):
    peti_ticket_servicio_canal = 'RQSOPORT'+num_us_cli+'SERTEC'+date_format()+cod_cont+'|'+cod_serv_adi
    data_ticket_servicio_canal = send_recived(peti_ticket_servicio_canal)
    return data_ticket_servicio_canal

def confirm_save_ticket_servicio_canal(result,user_num):
    petic_serv_adi = 'RQSOPORT'+user_num+'SERTEC'+date_format()
    t_init = len(petic_serv_adi)
    t_fina = len(result)
    petic = result[t_init:t_fina]
    size = len(petic)
    request = petic[0:6]
    data = petic[6:size]
    return request,data

def add_data_servicio_adicional():
    print 30 * "-" , "REGISTRAR SERVICIO ADICIONAL" , 30 * "-"
    print '\nDetalle Servicio Adicional:'
    det_serv_adi = sys.stdin.readline()
    loop_precio = True
    while loop_precio:
        print '\nPrecio Servicio Adicional:'
        pre_serv_adi = sys.stdin.readline()
        num_pre = pre_serv_adi.strip()
        if num_pre.isdigit():
            loop_precio = False
    return det_serv_adi.strip(),pre_serv_adi.strip()


def save_servicio_adicional(user_num,det_serv_adi,pre_serv_adi):
    petic_reg_serv_adi = 'RQSOPORT'+user_num+'REGSOP'+date_format()+det_serv_adi+'|'+pre_serv_adi
    data_reg_serv_adi = send_recived(petic_reg_serv_adi)
    return data_reg_serv_adi

def confirm_servicio_adicional(result,user_num):
    petic_reg_serv_adi = 'RQSOPORT'+user_num+'REGSOP'+date_format()
    t_init = len(petic_reg_serv_adi)
    t_fina = len(result)
    petic = result[t_init:t_fina]
    size = len(petic)
    request = petic[0:6]
    data = petic[6:size]
    return request,data

def print_menu_principal():
    print 30 * "-" , "SERVICIOS ADICIONALES" , 30 * "-"
    print "<< 1 >> INICAIR SECION"
    print "<< 2 >> SALIR"
    print 67 * "-"

def print_menu_usuario():
    print 30 * "-" , "SERVICIOS ADICIONALES" , 30 * "-"
    print "<< 1 >> BUSCAR CLIENTE"
    print "<< 2 >> AGREGAR TIPO DE SERVICIO ADICIONAL"
    print "<< 3 >> SALIR"
    print 67 * "-"

def resp_pregunta():
    exito = False
    bucle = True
    while bucle:
        print '\nDesea registrar el Servicio Adicional (S/N):'
        resp = sys.stdin.readline()
        if resp.strip() == 'S' or resp.strip() == 's':
            bucle = False
            exito = True
        elif resp.strip() == 'N' or resp.strip() == 'n':
            bucle = False
    return exito


loop=True

while loop:
    print_menu_principal()
    print "Seleccionar Opcion: "
    choice_r = sys.stdin.readline()
    choice = choice_r.strip()
    if choice.isdigit():
        if int(choice)==1 :
            peti_us,num_us,data_us = login_session()
            finally_close_connection(num_us)
            print '\n'+peti_us+' '+num_us+' '+data_us
            loop_cedula = True
            while loop_cedula:
                print_menu_usuario()
                print "Seleccionar Opcion: "
                choice_cedula_r = sys.stdin.readline()
                choice_cedula = choice_cedula_r.strip()
                if int(choice_cedula) == 1:
                    cod_num_contrato_select = cliente_cedula_contratos(num_us)
                    finally_close_connection(num_us)
                    cod_num_serv_adi_select = select_servicios_adicionales(num_us)
                    finally_close_connection(num_us)
                    if int(cod_num_serv_adi_select) == 1:
                        cod_num_can_prem_select = select_canales_premiun(num_us)
                        exito1 = resp_pregunta()
                        if exito1:
                            data_ticket_servicio_canal_1 = save_ticket_servicio_canal_1(num_us,cod_num_contrato_select,cod_num_serv_adi_select,cod_num_can_prem_select)
                            accept1,data = confirm_save_ticket_servicio_canal(data_ticket_servicio_canal_1,num_us)
                            print accept1
                            finally_close_connection(num_us)
                    else:
                        exito2 = resp_pregunta()
                        if exito2:
                            data_ticket_servicio_canal_2 = save_ticket_servicio_canal_2(num_us,cod_num_contrato_select,cod_num_serv_adi_select)
                            accept2,data2 = confirm_save_ticket_servicio_canal(data_ticket_servicio_canal_2,num_us)
                            print accept2
                            finally_close_connection(num_us)
                elif int(choice_cedula) == 2:
                    det_serv_adi_n , pre_serv_adi_n = add_data_servicio_adicional()
                    exito3 = resp_pregunta()
                    if exito3:
                        data_reg_servicio_adicional = save_servicio_adicional(num_us,det_serv_adi_n,pre_serv_adi_n)
                        accept3, data3 = confirm_servicio_adicional(data_reg_servicio_adicional,num_us)
                        print accept3
                        finally_close_connection(num_us)
                elif int(choice_cedula) == 3:
                    loop_cedula = False
            else:
                print ">>>"
        elif int(choice)==2:
            loop=False
        else:
            print ">>>"
    else:
        os.system("clear")