fin = open('input.txt', 'r', encoding='utf8')
count = int(fin.readline()[:-1])
lol = set()
lul = set()


for i in range(count - 1):
    line = fin.readline()[:-1].split()
    parent = line[0]
    son = line[1]
    lol.add(parent)
    lul.add(son)
print(lol & lul)