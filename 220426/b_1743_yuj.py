from collections import deque

def cal(i, j):
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    deq = deque([[i, j]])
    temp = 1
    while deq:
        i, j = deq.popleft()
        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if ni in range(N) and nj in range(M) and matrix[ni][nj]:
                deq.append([ni, nj])
                matrix[ni][nj] = 0
                temp += 1
    return temp

N, M, K = map(int, input().split())
matrix = [[0] * M for _ in range(N)]
ans = 0
for _ in range(K):
    r, c = map(int, input().split())
    matrix[r-1][c-1] = 1

for i in range(N):
    for j in range(M):
        if matrix[i][j]:
            matrix[i][j] = 0
            ans = max(cal(i, j), ans)
print(ans)