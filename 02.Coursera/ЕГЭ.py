def passScore(bank, places, j):
    minScore = 0
    for score in range(300, -1, -1):
        if bank[score] <= places and places != 0 and bank[score] != 0:
            places -= bank[score]
            minScore = score
            j -= bank[score]
            if places == 0 and j != 0:
                return score
            elif j == 0:
                return 0
        elif bank[score] > places or places == 0:
            if minScore != 0:
                return minScore
            else:
                return 1
        elif score == 40:
            return 0


inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
bank = [0] * 301
places = int(inFile.readline())
j = 0
for i in inFile:
    now = i.split()
    (uno, duas, trebo) = map(int, (now[-1], now[-2], now[-3]))
    if uno >= 40 and duas >= 40 and trebo >= 40:
        bank[uno + duas + trebo] += 1
        j += 1
print(passScore(bank, places, j), file=outFile)
inFile.close()
outFile.close()
