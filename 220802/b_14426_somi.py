N, M = map(int, input().split())
words = list(input() for _ in range(N))
words.sort()
pre = list(input() for _ in range(M))
pre.sort()

cnt = 0
idx = 0

for i in range(M):
    front = pre[i]
    length = len(front)
    for j in range(idx, N):
        if len(words[j]) >= length and words[j][: length] == front:
            cnt += 1
            idx = j
            break
print(cnt)


