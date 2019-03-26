def rename(directory):
    #нормализованный путь к файлам
    directory = os.path.abspath(directory)

    #файлы в папке
    object_in_folder = os.listdir(directory)

    #перебираем объекты и проверяем: файл или папка
    for object in object_in_folder:
        way = directory + '\\' + object

        #если путь ведет к файлу:
        if os.path.isfile(way) == True:
            file = object

            #есть ли файл в списке
            for i in allNames:
                if i[1] == file:
                    print(file)
                    name_new = i[0]
                    try:
                        os.rename(directory + '\\' + file, directory + '\\' + name_new)
                        break
                    except FileExistsError:
                        break
        #если путь ведет к папке
        else:
            rename(way)

outFile = open('output.txt', 'r', encoding='utf8')
inFile = open('input.txt', 'r', encoding='utf8')

import os
#print(dir(os))
directory = r"C:\Users\r.enikeev\pythochik"
path = os.path.abspath(directory)
k = os.path.isdir(path)
#folder_names = os.listdir(path)
allNames = list()

for oName, iName in zip(outFile, inFile):
    now = [oName[:-1], iName[:-1]]
    allNames.append(now)
print(allNames)

rename(directory)
