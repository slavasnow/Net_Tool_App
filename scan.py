# -----------------------------------------------------------
# Файл для объявления функций общего назначения.
#
#
# -----------------------------------------------------------


import socket, os, osfunc

# Функция проверки портов

def scan_port(hostname,port):
    ip = socket.gethostbyname(hostname)
    Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Sock.settimeout(0.5)
    try:
        Connect = Sock.connect((ip, port))
        print('port :',Port,' its open.')
        Connect.close()
    except:
        pass

# Функция преобразования ip в имя и имя в ip

def ip_with_info_all(hostname):
    try:
        print(socket.gethostbyname_ex(hostname))
        print(socket.gethostbyaddr(hostname))
    except:
        pass

# функция ping и дополнительные условия

def ping_system(hostname, num):
    if os.name == "nt":
        response = osfunc.nt_ping(num, hostname)
    elif os.name == "posix":
        response = osfunc.posix_ping(num, hostname)
    
    if response == 0:
        print (hostname, ": host is up")
    else:
        print (hostname, ": host is down")

# Функция 

# import pyping

# response = pyping.ping('Your IP')

# if response.ret_code == 0:
#     print("reachable")
# else:
#     print("unreachable")