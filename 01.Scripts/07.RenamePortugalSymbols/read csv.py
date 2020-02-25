import pandas as pd
import numpy as np
import os

dir = r'C:\Users\r.enikeev\Desktop\csvParsing'
names_files = os.listdir(dir)
#print(names_files)
words = dict()

for name_file in names_files:

    way = dir + '\\' + name_file
    with open(way, 'r', encoding='windows-1251') as file:

        for line in file:
            line = line.split(';')[0].split(' ')

            for word in line:
                if '?' in word:
                    words[word] = words.get(word)
print(words)



