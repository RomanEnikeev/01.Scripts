import pandas as pd
import numpy as np
import os
import csv

dir_r = r'C:\Users\r.enikeev\Desktop\test\read'
dir_w = r'C:\Users\r.enikeev\Desktop\test\write'

names_files = os.listdir(dir_r)

words = dict()

# for name_file in names_files:
#
#     way = dir + '\\' + name_file
#     with open(way, 'r', encoding='windows-1251') as file:
#
#         for line in file:
#             line = line.split(';')[0].split(' ')
#
#             for word in line:
#                 if '?' in word:
#                     words[word] = words.get(word)
# print(words)
#
#
#
with open('lol.csv', 'r', encoding='windows-1251') as file:

    for line in file:
        line = line[:-1].split('        ')
        do = line[0]
        posle = line[1]

        words[do] = words.get(do, posle)


#print(len(words))
csv_file = list()

for name_file in names_files:

    way_r = dir_r + '\\' + name_file
    with open(way_r, 'r', encoding='windows-1251') as file_r:
        for line in file_r:
            line = line[:-1]
            n_line = line.split(';')[0].split(' ')

            for word in n_line:
                if '?' in word:
                    line = line.replace(word, words[word])
            csv_file.append(line)

    way_w = dir_w + '\\' + name_file
    with open(way_w, 'w+', encoding='windows-1251') as file_w:
        for line in csv_file:
            print(line, file=file_w)
    csv_file = list()
