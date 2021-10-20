import sys
sys.stdin = open('s_1795.txt')

def dijkstra(adj, time):
    checked = [False] * (N + 1)
    checked[X] = 1

    for i in range(N + 1):
        time[i] = adj[X][i]

    for _ in range(N - 1):
        min_idx = 0
        for j in range(1, N + 1):
            if not checked[j] and time[j] < time[min_idx]:
                min_idx = j
        checked[min_idx] = True
        for w in range(1, N + 1):
            if min_idx != w and adj[min_idx][w] + time[min_idx] < time[w]:
                time[w] = adj[min_idx][w] + time[min_idx]

T = int(input())
for tc in range(1, T + 1):
    N, M, X = map(int, input().split())
    inf = 1000000
    go = [[inf] * (N + 1) for _ in range(N + 1)]
    back = [[inf] * (N + 1) for _ in range(N + 1)]
    for _ in range(M):
        x, y, c = map(int, input().split())
        go[x][y] = c
        back[y][x] = c

    for i in range(N + 1):
        go[i][i] = 0
        back[i][i] = 0

    time_go = [inf] * (N + 1)
    time_back = [inf] * (N + 1)

    dijkstra(go, time_go)
    dijkstra(back, time_back)

    max_value = 0
    for i in range(1, N + 1):
        if time_go[i] + time_back[i] > max_value:
            max_value = time_go[i] + time_back[i]
    print('#{} {}'.format(tc, max_value))

