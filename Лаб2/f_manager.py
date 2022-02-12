import os
import shutil

def creatFolder(main_folder):
    try:
        nameFolder=(input('Введите имя новой папки: '))
        os.mkdir('C:' + '/' + main_folder + '/'+ nameFolder)
    except FileExistsError:
        print(f"Файл {nameFolder} уже существует")
    print('Папка создана')

def removeFolder(main_folder):
    try:
        nameFolderDel=(input('Введите имя папки, которую хотите удалить: '))
        os.rmdir('C:' + '/' + main_folder + '/'+nameFolderDel)
    except FileNotFoundError:
        print(f"Файл {nameFolderDel} не найден")
    print('Папка удалена')

def movingBetweenFolders(main_folder):
    while True:
        os.chdir('C:' + '/' + main_folder)
        listM_folder = os.listdir()
        print(f'Содержимое корневой папки: {listM_folder}')
        movechoise = int(input('1- (Спуститься в папку), 2-(Закончить):'))
        if movechoise==1:
            try:
                move = input('Введите имя папки, в которую хотите спуститься: ')
                os.chdir('C:' + '/' + main_folder + '/' + move)
                print(f"Содержимое корневой папки {move}")
                print(os.listdir())
            except FileNotFoundError:
                print(f"Папка {move} не найдена")
                move = input('Повторно введите имя папки, в которую хотите спуститься: ')
                os.chdir('C:' + '/' + main_folder + '/' + move)
            movechoise2 = int(input('1-(Вернуться в корневую папку), 2-(Закончить):'))
            if movechoise2 == 1:
                continue
            else:
                break
        else:
            break

def creatEmptyFile(main_folder):
        choice=int(input('Eсли хотите создать файл в корневой папке введите "1", если в другой папке: "2": '))
        if choice==1:
            try:
                nameFile = (input('Введите имя файла: '))
                file = open('C:' + '/' + main_folder + '/' + nameFile + '.txt', "w")
            except FileExistsError:
                print(f"Файд {nameFile} не найден")
        else:
            try:
                dir=input('Введите название папки: ')
                nameFile = (input('Введите имя файла: '))
                file = open('C:' + '/' + main_folder + '/'+dir+'/' + nameFile + '.txt', "w")
            except FileExistsError:
                print(f"Файд {nameFile} не найден")
        file.close()
        print('Файл создан!')
def writingFile(main_folder):
    choice = int(input('Eсли хотите записать в файл в корневой папке введите "1", если в другой папке: "2": '))
    if choice == 1:
        try:
            nameFile = (input('Введите имя файла: '))
            fileСontent = input('Введите содержимое файла: ')
            file = open('C:' + '/' + main_folder + '/' + nameFile + '.txt', "a+")
        except FileNotFoundError:
            print(f"Файл {nameFile} не найден")
    else:
        try:
            dir = input('Введите имя папки: ')
            nameFile = (input('Введите имя файла: '))
            fileСontent = input('Введите содержимое файла: ')
            file = open('C:' + '/' + main_folder + '/' + dir + '/' + nameFile + '.txt', "a+")
        except FileNotFoundError:
            print(f"Файл {nameFile} не найден")
    file.write(fileСontent)
    file.close()
    print('Запись произведена!')

def viewingFileContent(main_folder):
    choice = int(input('Eсли хотите посмотреть содержимое файла в корневой папке введите "1", если в другой папке: "2": '))
    if choice == 1:
        try:
            nameFile = (input('Введите имя файла: '))
            file = open('C:' + '/' + main_folder + '/' + nameFile + '.txt', "r")
        except FileNotFoundError:
            print(f"Файл {nameFile} не найден")
    else:
        try:
            dir = input('Введите имя папки: ')
            nameFile = (input('Введите имя файла: '))
            file = open('C:' + '/' + main_folder + '/' + dir + '/' + nameFile + '.txt', "r")
        except FileNotFoundError:
            print(f"Файл {nameFile} не найден")
    print(file.read())
    print('Файл прочитан!')
def removeFile(main_folder):
    choice = int(input('Eсли хотите удалить файл в корневой папке введите "1", если в другой папке: "2": '))
    if choice == 1:
        try:
            nameFile = (input('Введите имя файла: '))
            os.remove('C:' + '/' + main_folder + '/' + nameFile + '.txt')
        except FileNotFoundError:
            print(f"Файл {nameFile} не найден")
    else:
        try:
            dir = input('Введите имя папки: ')
            nameFile = (input('Введите имя файла: '))
            os.remove('C:' + '/' + main_folder + '/' + dir + '/' + nameFile + '.txt')
        except FileNotFoundError:
            print(f"Файл {nameFile} не найден")
    print('Файл удален!')
def copyingFilesFromFolder(main_folder):
    choice = int(input('Eсли хотите копировать файл из корневой папки в не корневую введите "1", если из не корневой в корневую : "2", если не из корневой в не корневую "3" : '))
    if choice == 1:
        try:
            destinationFolder = input('Введите имя папки куда переносится файл: ')
            nameFile = (input('Введите имя файла: '))
            shutil.copy('C:' + '/' + main_folder + '/' + nameFile + '.txt', 'C:' + '/' + main_folder + '/'+destinationFolder)
        except FileNotFoundError:
            print(f"Файл {nameFile} не найден")
    elif choice == 2:
        try:
            dir = input('Введите имя папки: ')
            nameFile = (input('Введите имя файла: '))
            shutil.copy('C:' + '/' + main_folder +'/' +dir+'/'+nameFile + '.txt', 'C:' + '/' + main_folder)
        except FileNotFoundError:
            print(f"Файл {nameFile} не найден")
    else:
        try:
            initialFolder=input('Введите имя папки откуда переносится файл: ')
            destinationFolder=input('Введите имя папки куда переносится файл: ')
            nameFile=input('Введите имя файла: ')
            shutil.copy('C:' + '/' + main_folder +'/' +initialFolder+'/'+nameFile + '.txt', 'C:' + '/' + main_folder+'/'+destinationFolder)
        except FileNotFoundError:
            print(f"Файл {nameFile} не найден")
    print('Файл скопирован!')
def removeFilesFromFolder(main_folder):
    choice = int(input(
            'Eсли хотите перенести файл из корневой папки в не корневую введите "1", если из не корневой в корневую : "2", если не из корневой в не корневую "3" : '))
    if choice == 1:
        try:
            destinationFolder = input('Введите имя папки куда переносится файл: ')
            nameFile = (input('Введите имя файла: '))
            shutil.move('C:' + '/' + main_folder + '/' + nameFile + '.txt',
                    'C:' + '/' + main_folder + '/' + destinationFolder)
        except FileNotFoundError:
            print(f"Файл {nameFile} не найден")
    elif choice == 2:
        try:
            dir = input('Введите имя папки: ')
            nameFile = (input('Введите имя файла: '))
            shutil.move('C:' + '/' + main_folder + '/' + dir + '/' + nameFile + '.txt', 'C:' + '/' + main_folder)
        except FileNotFoundError:
            print(f"Файл {nameFile} не найден")
    else:
        try:
            initialFolder = input('Введите имя папки откуда переносится файл: ')
            destinationFolder = input('Введите имя папки куда переносится файл: ')
            nameFile = input('Введите имя файла: ')
            shutil.move('C:' + '/' + main_folder + '/' + initialFolder + '/' + nameFile + '.txt',
                    'C:' + '/' + main_folder + '/' + destinationFolder)
        except FileNotFoundError:
            print(f"Файл {nameFile} не найден")
    print('Файл перенесен!')
def renameFile(main_folder):
    choice = int(input('Eсли хотите переименовать файл в корневой папке введите "1", если в другой папке: "2": '))
    if choice == 1:
        try:
            nameFile = (input('Введите имя файла: '))
            new_nameFile = (input('Введите новое имя файла: '))
            os.rename('C:' + '/' + main_folder + '/' + nameFile + '.txt', 'C:' + '/' + main_folder + '/' + new_nameFile + '.txt')
        except FileNotFoundError:
            print(f"Файл {nameFile} не найден")
        except FileExistsError:
            print(f"Файл {nameFile} уже существует")
    else:
        try:
            dir = input('Введите имя папки: ')
            nameFile = (input('Введите имя файла: '))
            new_nameFile = (input('Введите новое имя файла: '))
            os.rename('C:' + '/' + main_folder + '/'  + dir + '/'+nameFile + '.txt', 'C:' + '/' + main_folder + '/'  + dir + '/'+new_nameFile + '.txt')
        except FileNotFoundError:
            print(f"Файл {nameFile} не найден")
        except FileExistsError:
            print(f"Файл {nameFile} уже существует")
    print('Файл переименован!')
