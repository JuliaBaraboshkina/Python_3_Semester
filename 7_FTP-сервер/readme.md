FTP сервер (5_FTP_server)

Демонстрация работы программы:

1. Создать папку:

![image](https://user-images.githubusercontent.com/90133237/144722827-384d2ffa-a78e-4ffb-b353-362ca6e8b18e.png)

![image](https://user-images.githubusercontent.com/90133237/144722798-59f35978-f9f7-418a-9b40-2e47f8ad753d.png)

![image](https://user-images.githubusercontent.com/90133237/144722824-e98ea2d4-1613-425b-8afe-efc108785f01.png)

2. Создать файл:

![image](https://user-images.githubusercontent.com/90133237/144722965-fb68a5bb-ad6e-4932-8434-016e5a02f34f.png)

![image](https://user-images.githubusercontent.com/90133237/144722968-90fcf4bc-663a-4e7e-b534-21bf5088554a.png)

3. Посмотреть содержимое папки:

![image](https://user-images.githubusercontent.com/90133237/144722978-9d807b27-8310-4a30-9ba0-c10927f69daf.png)

![image](https://user-images.githubusercontent.com/90133237/144722968-90fcf4bc-663a-4e7e-b534-21bf5088554a.png)

4. Содержимое файла: 

![image](https://user-images.githubusercontent.com/90133237/144723010-b69c773b-22d1-4e15-9b72-3c47501ca8ed.png)

![image](https://user-images.githubusercontent.com/90133237/144723019-a547bb45-fcc7-4bdf-87a1-8da71673e4cd.png)

5. Перемещение:

![image](https://user-images.githubusercontent.com/90133237/144723071-fe4905b3-6ef4-4f76-b36e-a565333aed91.png)

![image](https://user-images.githubusercontent.com/90133237/144723078-e890f10b-6c70-4c24-8a7d-9c8e1b9a0cbd.png)

![image](https://user-images.githubusercontent.com/90133237/144723082-3d1d43f8-f8d9-450e-96fb-baa042796317.png)

6. Удалить файл:

![image](https://user-images.githubusercontent.com/90133237/144723111-fc5ad378-4fd7-4c47-ab61-1900afc34791.png)

![image](https://user-images.githubusercontent.com/90133237/144723085-078d9f73-f23b-455c-8dbf-4ecc7503eadd.png)

![image](https://user-images.githubusercontent.com/90133237/144723120-03c2f170-bc90-4ae6-adad-51aa6bd12478.png)

7. Удалить папку:

![image](https://user-images.githubusercontent.com/90133237/144723149-66a6d597-af52-4d3d-bb27-10f1ed575896.png)

![image](https://user-images.githubusercontent.com/90133237/144723127-92204753-593f-463e-9763-32983b5891da.png)

![image](https://user-images.githubusercontent.com/90133237/144723154-fb2d4263-0963-48cd-8710-802f14e35415.png)

8. Выход (отключение клиента от сервера):

![image](https://user-images.githubusercontent.com/90133237/144723162-96f7ca50-2590-40fb-bcb9-3cd349c9d5bb.png)

Дополнительные задания:
1. Ограничьте возможности пользователя рамками одной определенной директории. Внутри нее он может делать все, что хочет: создавать и удалять любые файлы и папки. Нужно проследить, чтобы пользователь не мог совершить никаких действий вне пределов этой директории. Пользователь, в идеале, вообще не должен догадываться, что за пределами этой директории что-то есть.

client.py:

![image](https://user-images.githubusercontent.com/90133237/144723634-3f50dcee-4723-43d3-b8f1-882d770c125c.png)

ЕСли Host и Port не указаны, они используются по умолчанию (Host=localhost, Port=9090)

server.py:

![image](https://user-images.githubusercontent.com/90133237/144723648-45dd6bc4-60ad-441a-a8e7-6de4db94db81.png)

Содерджимое папки:

![image](https://user-images.githubusercontent.com/90133237/144723659-ded9c831-45e1-44f9-8c8d-06d54317f5af.png)

2. Добавьте логирование всех действий сервера в файл. Можете использовать разные файлы для разных действий, например: подключения, авторизации, операции с файлами.

log.txt:

![image](https://user-images.githubusercontent.com/90133237/144723185-5fb3159c-ab2a-47f5-bdf6-f8e2cee8335f.png)

3. Добавьте возможность авторизации пользователя на сервере.

client.py:

![image](https://user-images.githubusercontent.com/90133237/144723265-101fbc77-a07a-4f53-b209-d71d448d644e.png)

server.py:

![image](https://user-images.githubusercontent.com/90133237/144723289-f15283ba-aaaf-44a0-99fd-dd4adc0faca4.png)

Users.txt:

![image](https://user-images.githubusercontent.com/90133237/144723326-5e6204a9-5d30-4209-82d5-6312ab00d28a.png)

4. Добавьте возможность регистрации новых пользователей на сервере. При регистрации для пользователя создается новая рабочая папка (проще всего для ее имени использовать логин пользователя) и сфера деятельности этого пользователя ограничивается этой папкой.

client.py:

![image](https://user-images.githubusercontent.com/90133237/144723446-9bb36c6a-4d4d-44f4-ad9c-a35344574e09.png)

![image](https://user-images.githubusercontent.com/90133237/144723522-ebad1283-ec54-47dd-971d-65c2afe1029a.png)

server.py:

![image](https://user-images.githubusercontent.com/90133237/144723527-9e5ebff9-5774-4c01-a079-652e13295dc0.png)

Users.txt:

![image](https://user-images.githubusercontent.com/90133237/144723473-75dc4774-6c55-4f9f-989d-32afc7418eb6.png)

Появление папки:

![image](https://user-images.githubusercontent.com/90133237/144723542-13c4e56f-a3f1-4f40-b9f9-acedfe35690a.png)

6. Реализуйте учётную запись администратора сервера.

![image](https://user-images.githubusercontent.com/90133237/144723545-d2a988e8-33bc-4be7-a8a8-bd1aab0b2ca8.png)

![image](https://user-images.githubusercontent.com/90133237/144723556-276df165-a8d6-407b-8b65-303a3d57a154.png)
