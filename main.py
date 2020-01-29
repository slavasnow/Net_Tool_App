import scan, os, osfunc


while True:
    
    osfunc.clean_monitor_system()
    
    hostname = input("Введите имя хоста или его IP:  ")#ввод имени хоста

    # защита от неправильного ввода данных
    while True:
        num = input("Введите кол-во отправляемых пакетов:  ") #кол-во проходов
        if not num.isdigit():
            print("Вы должны ввести число, попробуйте снова.")
        else:
            break

    scan.ping_system(hostname, num) # ping системы
    scan.ip_with_info_all(hostname) # все ip хоста
    
    qwe = input("Хотите продолжить работу(Y ,N)  ")#Выход из программы 
    if qwe == "N" or qwe == "n":
        break

