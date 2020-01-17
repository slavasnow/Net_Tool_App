import scan, os
from progress.bar import IncrementalBar

print("Введите имя хоста или его IP  ") #ввод имени хоста
hostname = input()
print("Введите кол-во отправляемых пакетов  ") #ввод имени хоста
num = input() #кол-во проходов

scan.ping_system(hostname, num) # ping системы
scan.ip_with_info_all(hostname) # все ip хоста


#  Заменить ping прогресс баром для наиболее приятного вида.


# Настрить cui и собрать систему для проведения тестов

# Залить на git и создать новую ветку 



# if os.name == "nt":
#     #print(os.system("cls"))
#     scan.ping_system(Hostname) # ping системы
#     scan.ip_with_info_all(Hostname) # все ip хоста
# else:
#     #print(os.system("clear"))
#     scan.ping_system(Hostname) # ping системы
#     scan.ip_with_info_all(Hostname) # все ip хоста



# scan.ping_system(Hostname) # ping системы

# scan.ip_with_info_alllocal(Hostname) # все ip хоста


# *for i in range(1000):
#      scan.Scan_Port(Hostname, i)
