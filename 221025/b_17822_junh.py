import sys

input = sys.stdin.readline
N, M, T = map(int, input().split())
pans = [list(map(int, input().split())) for _ in range(N)]

def bfs(y, x):
    dY = (0, 1, 0, -1)
    dX = (1, 0, -1, 0)

    q = [(y, x)]
    idx = 0
    while idx < len(q):
        y, x = q[idx]
        idx += 1
        for d in range(4):
            ny, nx = y + dY[d], (x + dX[d]) % M

            if ny in range(N) and nx in range(M) and (ny, nx) not in q and pans[ny][nx] == pans[y][x]:
                q.append((ny, nx))

    if len(q) > 1:
        for y, x in q:
            pans[y][x] = None
        return True
    return False



for _ in range(T):
    x, d, k = map(int, input().split())

    for i in range(x-1, N, x):
        if d == 0:
            pans[i] = pans[i][M-k:] + pans[i][:M-k]
        else:
            pans[i] = pans[i][k:] + pans[i][:k]

    delete = False
    for i in range(N):
        for j in range(M):
            if pans[i][j] is not None:
                if bfs(i, j):
                    delete = True

    if not delete:
        avg = 0
        cnt = 0
        for i in range(N):
            for j in range(M):
                if pans[i][j] is not None:
                    avg += pans[i][j]
                    cnt += 1
        if cnt == 0:
            continue
        avg /= cnt
        for i in range(N):
            for j in range(M):
                if pans[i][j] is None: continue
                elif pans[i][j] > avg:
                    pans[i][j] -= 1
                elif pans[i][j] < avg:
                    pans[i][j] += 1

answer = 0
for i in range(N):
    for j in range(M):
        if pans[i][j] is not None:
            answer += pans[i][j]
print(answer)
