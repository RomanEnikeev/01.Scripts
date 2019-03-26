def mod(home, shelt, k):
    rez = list()
    for i in shelt[k:]:
        d = i[0] - home[0]
        if d < 0:
            d = -d
        rez.append(d)
    m = rez.index(min(rez))         #номер ближайшего убежища в отсортированном списке
    k = m + k                           #next search will be start with k
    return (home[1], shelt[k][1], k)#vozvrashaet nomer ubezhisha, nomer doma, k


#a1 = int(input())
A = [60, 20, 10, 100]         #[int(x) for x in input().split(' ')]
#b1 = int(input())
B = [1, 2, 3, 70, 30]                #[int(x) for x in input().split(' ')]


for i in range(len(A)):
    A[i] = [A[i], i]
for i in range(len(B)):
    B[i] = [B[i], i]

B.sort()
A.sort()

n = 0
C = list()
D = list()
G = list()


k = 0
for i in A:
    C = mod(i, B, k)
    k = C[2]
    D.append((C[0], C[1]))


D.sort()
for i in D:
    G.append(i[1] + 1)
print(' '.join(map(str, G)))
# for i in A:
#     for j in range(0, len(B)):
#         C.append(B[j][0] - i[0])
#     k = min(map(abs, C))
#     mod(C)
#     n = C.index(k)
#     D.append(B[n][1] + 1)
#     C = list()
# print(' '.join(map(str, D)))
