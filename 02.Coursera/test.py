inFile = open('input.txt', 'r', encoding='utf8')
maxNum = inFile.readline()[:-1]
maybeY = set()
now = set()
for i in range(1, int(maxNum) + 1):
    maybeY.add(str(i))
for line in inFile:
    if line[:-1] == 'YES':
        if maybeY == set():
            maybeY = set(now)
        else:
            maybeY &= now
    elif line[:-1] == 'NO':
        maybeY -= now
    elif line[:-1] == 'HELP':
        break
    now = set(line.split())
a = list(maybeY - {' '})
a = map(int, a)
print(' '.join(map(str, sorted(a))))
