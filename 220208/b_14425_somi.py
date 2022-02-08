N, M = map(int, input().split())
words = {input() for _ in range(N)}
cnt = 0
for _ in range(M):
    w = input()
    if w in words:
        cnt += 1
print(cnt)
