import socket, threading,csv,sys,os
from time import sleep
fi=open('log.txt','a+')
fi.close()
clients = []
logins = []
def sending(msg): #Отправка сообщения от одного клиента всем
    for client in clients:
        client.send(msg)

def receiving(client): #Обработка сообщений клиентов
    while True:
        try:
            msg = client.recv(1024)
            mess=msg.decode('utf-8')
            mess=mess.split(':')
            with open('msg_history.csv', mode="a+", encoding='ascii', newline='') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow((mess))
            sending(msg)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            name = logins[index]
            logins.remove(name)
            break

host = '127.0.0.1'
port = 9090
print('SERVER WORKS!')
fi = open('log.txt', 'a')
fi.write('SERVER WORKS!'+'\n')
fi.close()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen()

def server():
    while True:
        comand = input('If you want to stop server, write (shutdown) or (nxt) to continue>')
        if comand == 'shutdown':
            for client in clients:
                msg = b'SERVER IS STOPED!'
                client.send(msg)
            break
        ip_add, addr = sock.accept()
        print('Client > ' + str(addr))
        ip_add.send('login'.encode('utf-8'))
        login = ip_add.recv(1024).decode('utf-8')
        logins.append(login)
        clients.append(ip_add)
        fi = open('log.txt', 'a+')
        fi.write('Client > ' + str(addr) + '\n')
        fi.write('Login > ' + login + '\n')
        fi.close()
        print('Login > ' + login)
        sending("{} -> entered the chat!".format(login).encode('utf-8'))
        threading.Thread(target=receiving, args=(ip_add,)).start()

server()
print('SERVER DOESNT WORK!')
print('show-log - to show log; clear-log - to clear log file; clear-file - to clear clients list; exit-to stop')
while True:
    command = input('Choose command>')
    if command == 'show-log':
        if os.stat("log.txt").st_size == 0:
            print('File is empty!')
        else:
            file = open('log.txt', 'r')
            file_contents = file.read()
            print(file_contents)
            file.close()
    if command == 'clear-log':
        f = open('log.txt', 'w')
        f.close()
    if command == 'clear-file':
        f = open("msg_history.csv", "w")
        f.truncate()
        f.close()
        print('Done')
    if command=='exit':
        break
fi = open('log.txt', 'a')
fi.write('SERVER DOESNT WORK!'+'\n')
fi.close()