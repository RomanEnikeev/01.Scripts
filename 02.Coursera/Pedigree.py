def family_member(name, level, dict, father):
    if name == father:
        return level
    for i in dict:
        if name in dict[i]:
            level += 1
            return family_member(i, level, dict, father)



fin = open('input.txt', 'r', encoding='utf8')
#count = int(input())
count = int(fin.readline()[:-1])

dict = {}
inital = list()

for i in range(count - 1):
    line = fin.readline()[:-1].split()
    son = line[0]
    parent = line[1]

#    print(line)
    if son not in inital:
        inital.append(son)
    if parent not in inital:
        inital.append(parent)
    if parent not in dict:
        dict[parent] = []

    dict[parent].append(son)
    # if son not in dict:
    #     dict[son] = []

i = 0
#поиск старшего
for parent in dict:
    for find in dict:
        if parent not in dict[find]:
            i += 1
    if i == len(dict):
        father = parent
        print(father)
for i in sorted(inital):
    print(family_member(i, 0, dict, father))
    print(i)
