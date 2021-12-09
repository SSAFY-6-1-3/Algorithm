import sys

sys.stdin = open('s_1795_input.txt')



def diks(a, tree):
    dist = [99999] * (N+1)
    visited = [False] * (N+1)
    dist[a] = 0
    visited[a] = True

    for route in range(1, N+1):
        if tree[a][route]:
            dist[route] = tree[a][route]

    def get_nearest():
        min_dist = 99999
        idx = 0
        for i in range(1, N+1):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                idx = i
        return idx


    for _ in range(N-1):
        node = get_nearest()
        visited[node] = True

        for next in range(1, N+1):
            if not tree[node][next] : continue
            cost = dist[node] + tree[node][next]
            if cost < dist[next]:
                dist[next] = cost

    return dist


T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split())
    go = [[0 for _ in range(N+1)] for _ in range(N+1)]
    back = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for _ in range(M):
        x, y, c = map(int, input().split())
        go[x][y] = c
        back[y][x] = c
    max_val = 0
    go_diks = diks(X, go)
    back_diks = diks(X, back)

    for i in range(1, N+1):
        max_val = max(max_val, go_diks[i]+back_diks[i])
    print('#{} {}'.format(tc, max_val))
