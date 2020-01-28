inFile = open('1.csv', 'r', encoding='utf8')
dic = dict()
all_codes = list()
with open('1.csv') as f:
    for line in f:
        line = inFile.readline()[:-1]
        all_codes.append(line)
        if len(line) == 5:
            dic[line] = dic.get(line, 0) + 1
for num in dic:
    dic[num] = [dic[num], dic[num]]
print(dic)
print(all_codes)
inFile.close()

outFile = open('2.csv', 'w', encoding='utf8')

for code in all_codes:
    if code in dic:
        dic[code][1] -= 1
        added = str(dic[code][0] - dic[code][1])
        if len(added) == 1:
            added = '0' + added

        print(added)
        new_code = code + '_' + added
        print(new_code, file=outFile)
    else:
        print(code, file=outFile)


outFile.close()

