import sys
sys.stdin=open('input.txt')
sys.setrecursionlimit(1000000)

def protect(i, j):

    di = [-1, +1, 0, 0]
    dj = [0, 0, -1, +1]

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < M:
            if field[ni][nj] == 1:
                field[ni][nj] = 0
                protect(ni, nj)


T = int(input())
for tc in range(T):
    M, N, K = map(int, input().split())
    field = [[0] * M for _ in range(N)]
    for _ in range(K):
        y, x = map(int, input().split())
        field[x][y] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if field[i][j] == 1:
                protect(i, j)
                cnt += 1

    print(cnt)