N = int(input())
pnts = list(map(int, input().split()))

s = sorted(set(pnts))
dic = {}

for i in range(len(s)):
    dic[s[i]] = i
for i in range(N):
    pnts[i] = dic[pnts[i]]
print(*pnts)

