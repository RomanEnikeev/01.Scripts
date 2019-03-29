fin = open('input.txt')

#count = int(input())
count = int(fin.readline()[:-1])
print(count)

dict = {}

for i in range(count):
    #word = input()
    word = fin.readline()[:-1]
    print(word)
    low_word = word.lower()
    if low_word not in dict:
        dict[low_word] = []
    if word not in dict[low_word]:
        dict[low_word].append(word)


print(dict)
work = fin.readline()[:-1].split()
miss = 0
for word in work:
    low_word = word.lower()
    if low_word in dict:
        if word not in dict[low_word]:
            miss += 1
    elif low_word not in dict:
        sup_letter = sum(map(str.isupper, word))
        if sup_letter != 1:
            miss += 1

print(work)
print(miss)
