def dijkstra(road, d):
    for i in range(1, N + 1):
        d[i] = road[X][i]

    visited = [False] * (N + 1)
    visited[X] = True

    for _ in range(N - 1):
        minIdx = 0
        for j in range(1, N + 1):
            if not visited[j] and d[j] < d[minIdx]:
                minIdx = j

        visited[minIdx] = True

        for k in range(1, N + 1):
            if minIdx != k and road[minIdx][k] < float('inf'):
                d[k] = min(d[k], d[minIdx] + road[minIdx][k])


N, M, X = map(int, input().split())
go_road = list([float('inf')] * (N + 1) for _ in range(N + 1))
back_road = list([float('inf')] * (N + 1) for _ in range(N + 1))

for _ in range(M):
    s, e, t = map(int, input().split())
    go_road[s][e] = t
    back_road[e][s] = t

for j in range(N + 1):
    go_road[j][j] = 0
    back_road[j][j] = 0

go = [float('inf')] * (N + 1)
back = [float('inf')] * (N + 1)

dijkstra(go_road, go)
dijkstra(back_road, back)

maxV = 0
for n in range(1, N + 1):
    if go[n] + back[n] > maxV:
        maxV = go[n] + back[n]

print(maxV)
