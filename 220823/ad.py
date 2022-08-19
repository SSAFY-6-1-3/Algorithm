import sys

input = sys.stdin.readline
print = sys.stdout.write

S = input()
q = int(input())

dic = {c:[] for c in S}
Qs = [0] * q

for idx in range(q):
    a, l, r = input().split()
    if a not in dic.keys():
        continue
    l, r = map(int, (l, r))
    dic[a].append((idx, l, r))

for i in range(len(S)):
    c = S[i]
    for j in range(len(dic[c])):
        idx, l, r = dic[c][j]
        if l <= i <= r:
            Qs[idx] += 1

for cnt in Qs:
    print(str(cnt) + '\n')

