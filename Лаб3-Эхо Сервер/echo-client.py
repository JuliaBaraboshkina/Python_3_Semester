import socket,random
while True:
    port = input('Введите порт для подключения клиента: ')
    if port.isdigit():
        if 1024 <= int(port) <= 65535:
            port = int(port)
            with open("l_ports.txt", "r+") as f:
                f.write(str(port))
            break
        else:
            print('Введите порт (1024-65535)')
    else:
        print('Порт-число!')

while True:
    flag=False
    host=input('Введите ip адрес: ')
    prov_host=host.split('.')
    for i in range(len(prov_host)):
            if  len(prov_host) == 4:
                if prov_host[i].isdigit():
                    if 0 <= int(prov_host[i]) <= 255:
                        flag = True
                    else:
                        flag = False
                        break
                else:
                    flag=False
                    break
            else:
                break
    if flag==True:
        break

    print('Неправильный ввод!')
file=open('Name_password.txt', 'a+')
chet=0
with open('Name_password.txt','r') as fi:
    for line in fi:
        list_words = line.split()
        if host in line:
            name = list_words[-2]
            password=list_words[-1]
            chet = 1
if chet!=1:
    name = input('Введите ваше имя:')
    password = input('Придумайте пароль:')
    file.write(host + ' ')
    file.write(name + ' ')
    file.write(password+ ' ')
file.close()
while True:
    check_password=input('Введите пароль:')
    if check_password!=password:
        print('Неверный пароль!')
    else:
        break
while True:
    with open("l_ports.txt", "r") as f:
        lines = f.readlines()
        port = int(lines[-1])
    with socket.socket() as sock:
        print('Здравствуйте,'+name+'!')
        sock.connect((host, port))
        print("Прием данных от клиента:")
        while True:
            msg = input('Введите сообщение: ')
            if msg == 'exit':
                break
            sock.send(msg.encode())
            print("Отправка данных серверу")
            data = sock.recv(1024)
            print('Прием данных от сервера:', repr(data))
    print("Разрыв соединения с сервером")
    break
f=open('l_ports.txt','w')
f.close()

