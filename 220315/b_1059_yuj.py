from itertools import combinations
L = int(input())
S = sorted(list(map(int, input().split())))
n = int(input())

if n in S:
    print(0)
    exit(0)

res = []
if n < S[0]:
    res = [i for i in range(1, S[0])]
else:
    for idx in range(L-1):
        if S[idx] < n < S[idx+1]:
            res = [i for i in range(S[idx]+1, S[idx+1])]
            break

combs = list(combinations(res, 2))

cnt = 0
for comb in combs:
    if n in range(comb[0], comb[1]+1):
       cnt += 1

print(cnt)
