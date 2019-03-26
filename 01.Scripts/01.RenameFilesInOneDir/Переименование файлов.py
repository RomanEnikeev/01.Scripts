outFile = open('output.txt', 'r', encoding='utf8')
inFile = open('input.txt', 'r', encoding='utf8')
# -*- coding: utf-8 -*-
import os
#print(dir(os))
directory = r"C:\Users\r.enikeev\pythochik"
path = os.path.abspath(directory)
files_names = os.listdir(path)
allNames = list()

for oName, iName in zip(outFile, inFile):
    now = [oName[:-1], iName[:-1]]
    allNames.append(now)
print(allNames)

for name_now in files_names:
    for i in allNames:
        if i[1] == name_now:
            print(i)
            name_new = i[0]
            os.rename(directory + '\\' + name_now, directory + '\\' + name_new)
            break

