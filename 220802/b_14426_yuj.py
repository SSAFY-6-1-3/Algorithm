N, M = map(int, input().split())
S = set()
ans = 0
for _ in range(N):
    words = str(input())
    w = ''
    for word in words:
        w += word
        S.add(w)

for _ in range(M):
    if str(input()) in S:
       ans += 1

print(ans)