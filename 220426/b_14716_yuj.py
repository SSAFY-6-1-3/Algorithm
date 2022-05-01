from collections import deque

def check(i, j):
    words[i][j] = 0
    dr = [-1, 1, 0, 0, -1, -1, 1, 1]
    dc = [0, 0, -1, 1, -1, 1, -1, 1]
    deq = deque([[i, j]])
    while deq:
        r, c = deq.popleft()
        for k in range(8):
            nr, nc = r+dr[k], c +dc[k]
            if nr in range(M) and nc in range(N) and words[nr][nc]:
                words[nr][nc] = 0
                deq.append([nr, nc])

M, N = map(int, input().split())
words = [list(map(int, input().split())) for _ in range(M)]
ans = 0
for i in range(M):
    for j in range(N):
        if words[i][j]:
            ans += 1
            check(i, j)

print(ans)