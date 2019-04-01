def family_member(name, level, dict, father):
    if name == father:
        return level
    for i in dict:
        if name in dict[i]:
            level += 1
            return family_member(i, level, dict, father)


fin = open('input.txt', 'r', encoding='utf8')
count = int(input())

dict = {}
inital = list()

for i in range(count - 1):
    line = input().split()
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

lenDict = len(dict)
for parent in dict:
    i = 0
    for find in dict:
        if parent not in dict[find]:
            i += 1
    if i == lenDict:
        father = parent
result = list()
for i in sorted(inital):
    print(' '.join(map(str, [i, family_member(i, 0, dict, father)])))
