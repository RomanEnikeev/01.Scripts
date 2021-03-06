import os

# папка с файлами
dir = r'C:\Users\r.enikeev\Desktop\csvParsing\2015\tables'
iskl = list()
files = os.listdir(dir)
pechat = list()

for file in files:
    try:
        way = dir + '\\' + file
        inFile = open(way, 'r', encoding='windows-1251')

        for line in inFile:
            if line != '':
                line = line[:-1].split(';')

                bar_material = line[1]
                el_current_code = line[2]
                el_current = line[3]

                if bar_material == '1' and el_current == '5000':
                    el_current_code = '51'  # el_current_code для алюминия 5000 А
                    line[2] = el_current_code

                elif bar_material == '2' and el_current == '5000':
                    el_current_code = '50'  # el_current_code для меди 5000 А
                    line[2] = el_current_code

                elif bar_material == '2' and el_current == '2500':
                    el_current_code = '27'  # el_current_code для меди 2500 А
                    line[2] = el_current_code

                outline = ';'.join(line)

                if bar_material == '2' and el_current_code == '21' and el_current == '2250':  # так удаляем (в данном случае не добавляем) строки с данными параметрами
                    pass
                elif bar_material == '2' and el_current_code == '43' and el_current == '4250':
                    pass
                else:
                    pechat.append(outline)
        inFile.close()

        outFile = open(way, 'w', newline='')
        for line in pechat:
            print(line, file=outFile)
        outFile.close()
        pechat = list()
    except:
        iskl.append(file)
        try:
            inFile.close()
        except:
            pass
        try:
            outFile.close()
        except:
            pass

print(iskl)
