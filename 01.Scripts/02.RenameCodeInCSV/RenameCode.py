import os

#категории лотков
hdz = 'HDZ'
inox = 'INOX'
zl = 'ZL'


#папка с файлами
dir = r'C:\\Users\\r.enikeev\\PycharmProjects\\untitled\\01.Scripts\\02.RenameCodeInCSV\\csv\\'

files = os.listdir(dir)
before = list()
#ФАЙЛ С ОШИБОЧНЫМИ НАЗВАНИЯМИ!

error = open('ERROR!.txt', 'w', encoding='utf8', newline='')

for file in files:
    way = dir + file
    inFile = open(way, 'r', encoding='utf8')
    for i in inFile:
        x = i.split(';')
        before.append(x)
    for i in before[1:]:
        code = i[0]
        if hdz in code:
            index = code.find(hdz)
            i[0] = code[:index] + 'K' + code[index:]
        elif inox in code:
            index = code.find(inox)
            i[0] = code[:index] + 'K' + code[index:]
        elif zl in code:
            index = code.find(zl)
            i[0] = code[:index] + 'K' + code[index:]
        elif code.isdigit() == True:
            i[0] = code + 'K'
        else:
            print(file, code, file=error, sep=';')
    inFile.close()
    outFile = open(way, 'w', encoding='utf8', newline='')
    for i in before[0:]:
        outFile.writelines(';'.join(i))
    before = list()

error.close()
