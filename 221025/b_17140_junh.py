import collections

r, c, k = map(int, input().split())
r -= 1
c -= 1
A = [list(map(int, input().split())) for _ in range(3)]

def my_sort(li):
    dic = collections.Counter(li)
    tmp = []
    for i in sorted(dic.keys(), key= lambda x:(dic[x], x)):
        if len(tmp) >= 100: break
        if i == 0: continue
        tmp.append(i)
        tmp.append(dic[i])
    return tmp


def try_sort():
    max_col = 0
    for i in range(len(A)):
        A[i] = my_sort(A[i])
        max_col = max(max_col, len(A[i]))
    for i in range(len(A)):
        while len(A[i]) < max_col:
            A[i].append(0)


sec = 0
while sec <= 100 and ((r >= len(A) or c >= len(A[r])) or A[r][c] != k) :
    if len(A) < len(A[0]):
        A = list(map(list, zip(*A)))
        try_sort()
        A = list(map(list, zip(*A)))
    else:
        try_sort()
    sec += 1

if sec == 101:
    print(-1)
else:
    print(sec)



li = [2, 1, 1, 3]
print(my_sort(li))
