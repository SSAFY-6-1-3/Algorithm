import sys
sys.stdin = open('s_1795_input.txt')

def dij(arr, d):

    for i in range(1, N + 1):
        d[i] = arr[X][i]

    visited = [False] * (N + 1)
    visited[X] = True

    for _ in range(N - 1):
        minIdx = 0
        for j in range(1, N + 1):
            if not visited[j] and d[j] < d[minIdx]:
                minIdx = j
        visited[minIdx] = True

        for k in range(1, N + 1):
            if minIdx != k and arr[minIdx][k] < 1000000:
                d[k] = min(d[k], d[minIdx] + arr[minIdx][k])


T = int(input())
for tc in range(1, T + 1):

    N, M, X = map(int, input().split())

    go = [[1000000] * (N + 1) for _ in range(N + 1)]
    back = [[1000000] * (N + 1) for _ in range(N + 1)]
    for i in range(N + 1):
        go[i][i] = 0
        back[i][i] = 0

    for _ in range(M):
        x, y, c = map(int, input().split())
        go[x][y] = c
        back[y][x] = c

    d1 = [1000000] * (N + 1)
    d2 = [1000000] * (N + 1)
    dij(go, d1)
    dij(back, d2)

    maxV = 0
    for n in range(1, N + 1):
        if d1[n] + d2[n] > maxV:
            maxV = d1[n] + d2[n]
    print('#{} {}'.format(tc, maxV))