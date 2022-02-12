from f_manager import creatFolder
from f_manager import removeFolder
from f_manager import movingBetweenFolders
from f_manager import creatEmptyFile
from f_manager import writingFile
from f_manager import viewingFileContent
from f_manager import removeFile
from f_manager import copyingFilesFromFolder
from f_manager import removeFilesFromFolder
from f_manager import renameFile
import os

check=input('Если хотите создать корневую папку, введите "1", если она уже существует "2": ')
while check.isdigit()!=True:
    print('Неверный ввод!')
    check = input('Введите выбранную ЦИФРУ повторно: ')
if check=='1':
    root_folder=input('Введите название новой корневой папки: ')
    os.mkdir('C:' + '/' + root_folder)
    print('Корневая папка создана!')
else:
    root_folder = input('Введите название корневой папки: ')
while True:
    print("Достпуные функции: "
          "1-(создать папку),2-(удалить папку), 3-(Перемещение между папками), 4-(создать пустой файл), 5-(записать в файл), 6-(прочитать файл),"
          "7-(удалить файл), 8-(копировать файл), 9-(переместить файл), 10-(переименовать файл)")
    print('00-(Чтобы закончить работу)')
    move=input('Введите выбранную цифру: ')
    if move.isdigit()==False:
        print('Неверный ввод!')
        move = input('Введите выбранную ЦИФРУ повторно: ')
    elif move=='1':
        creatFolder(root_folder)
    elif move=='2':
        removeFolder(root_folder)
    elif move=='3':
        movingBetweenFolders(root_folder)
    elif move=='4':
        creatEmptyFile(root_folder)
    elif move=='5':
        writingFile(root_folder)
    elif move=='6':
        viewingFileContent(root_folder)
    elif move=='7':
        removeFile(root_folder)
    elif move=='8':
        copyingFilesFromFolder(root_folder)
    elif move=='9':
        removeFilesFromFolder(root_folder)
    elif move=='10':
        renameFile(root_folder)
    elif move=='00':
        break
    else:
        print('Такой команды не сущетсвует, повторите попытку!')