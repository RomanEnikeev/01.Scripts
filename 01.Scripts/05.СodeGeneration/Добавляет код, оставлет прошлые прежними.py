inFile = open('1.csv', 'r', encoding='utf8')
dic = dict()
all_codes = list()
with open('1.csv') as f:
    for line in f:
        line = inFile.readline()[:-1]
        f_part = line[0:5]
        all_codes.append(line)

        if len(line) == 8:
            line = line[0:5]
            a = dic.get(line, [0, 0])[0]
            dic[line] = [dic.get(line, [0, 0])[0] + 1, dic.get(line, [0, 0])[1]]
        elif len(line) == 5:
            dic[line] = [dic.get(line, [0, 0])[0] + 1, dic.get(line, [0, 0])[1] + 1]


print(dic)
print(all_codes)
inFile.close()

outFile = open('2.csv', 'w', encoding='utf8')

#############     dic[key][0] = sum_of_codes
#############     dic[key][1] = where 5 simbols



for code in all_codes:
    if code in dic:

        now_codes = dic[code][0]
        sum_codes = dic[code][1]
        added = str(now_codes - sum_codes + 1)
        if len(added) == 1:
            added = '0' + added

        print(added)
        new_code = code + '_' + added
        print(new_code, file=outFile)

        dic[code][1] -= 1
    else:
        print(code, file=outFile)


outFile.close()

