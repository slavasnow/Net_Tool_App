import os

def nt_clean_monitor():
    print(os.system("cls"))

def posix_clean_monitor():
    print(os.system("clear"))

def nt_ping(num, hostname):
    return os.system ("ping -n " + num + " " + hostname)

def posix_ping(num, hostname):
     return os.system ("ping -c " + num + " " + hostname)