from collections import deque
import sys
input = sys.stdin.readline
M, N = map(int, input().split())

flag = [input().split() for _ in range(M)]

def delete(r, c, flag):
    q = deque([(r, c)])
    dR = (1, 0, -1, 0, 1, 1, -1, -1)
    dC = (0, 1, 0, -1, 1, -1, 1, -1)
    flag[r][c] = '0'
    while q:
        r, c = q.popleft()

        for d in range(8):
            nr, nc = r+dR[d], c+dC[d]
            if nr not in range(M) or nc not in range(N) or flag[nr][nc] != '1':
                continue
            q.append((nr, nc))
            flag[nr][nc] = '0'
cnt = 0
for r in range(M):
    for c in range(N):
        if flag[r][c] == '1':
            cnt += 1
            delete(r, c, flag)
print(cnt)