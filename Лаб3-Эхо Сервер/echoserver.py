import socket, random,os
l_ports=[]
f=open('l_ports.txt','w')
def server():
    while True:
        while os.stat('l_ports.txt').st_size == 0:
            True
        host = ''
        with open("l_ports.txt", "r") as f:
            lines = f.readlines()
            port = int(lines[-1])
        if port not in l_ports:
            l_ports.append(port)
        else:
            while True:
                port = random.randint(1024, 65535)
                if port not in l_ports:
                    l_ports.append(port)
                    f = open("l_ports.txt", "a+")
                    f.write("\n" + str(port))
                    f.close()
                    break
        with open("l_ports.txt", "r") as f:
            lines = f.readlines()
            port = int(lines[-1])
        with socket.socket() as sock:
            sock.bind((host, port))
            print("Начало прослушивания порта:", port)
            sock.listen()
            conn, addr = sock.accept()
            print('Подключение клиента', host)
            with conn:
                msg = ''
                while True:
                    data = conn.recv(1024)
                    print("Прием данных от клиента", data)
                    if not data:
                        break
                    msg = data.decode()
                    print("Отправка данных клиенту")
                    conn.send(data)
        print("Отключение клиента")
        choose = input(
            'Нажмите "enter" для продолжения работы сервера; для прекращения работы сервера введите - "end":')
        if choose == 'end':
            break
        else:
            continue

print('Запуск сервера')
server()
print("Остановка сервера")
f.close()

