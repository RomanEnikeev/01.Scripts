import os

#категории лотков
hdz = ', горячеоцинкован'
inox = ', нержавеющ'
zl = ', цинк-ламельн'

#папка с файлами
dir = r'C:\\Users\\r.enikeev\\PycharmProjects\\untitled\\01.Scripts\\03.RenameNameInCSV\\csv\\'

files = os.listdir(dir)
before = list()

#добавочный элемент
k = ' в комплекте с крепежными элементами и соединительными пластинами, необходимыми для монтажа'

for file in files:
    way = dir + file
    inFile = open(way, 'r+', encoding='windows-1251')
    for i in inFile:
        x = i.split(';')
        before.append(x)
    for i in before[1:]:
        code = i[0]

        if hdz in code:
            index = code.find(hdz)
            i[0] = code[:index] + k + code[index:]
        elif inox in code:
            index = code.find(inox)
            i[0] = code[:index] + k + code[index:]
        elif zl in code:
            index = code.find(zl)
            i[0] = code[:index] + k + code[index:]
        else:
            code = code.rstrip()
            i[0] = code + k
    inFile.close()
    outFile = open(way, 'w', newline='')
    for i in before[0:]:
        outFile.writelines(';'.join(i))
    before = list()
    outFile.close()
