
import sys

sys.stdin = open('s_1795.txt')

def check(start, tree):
    dist = [100*N] * (N+1)
    dist[start] = 0
    checked = [False] * (N+1)

    for _ in range(N):
        # tmp = sorted(range(1, N+1), key= lambda x: dist[x])
        # for i in tmp:
        #     if not checked[i]:
        #         node = i
        #         break
        node = min(range(1, N+1), key= lambda x: dist[x] + checked[x]*99999999)
        checked[node] = True
        for next in range(1, N+1):
            d = tree[node][next]
            if d and not checked[next] and dist[node]+d < dist[next]:
                dist[next] = dist[node] + d
    return dist


T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split())
    gotree = [[0 for _ in range(N+1)] for _ in range(N+1)]
    backtree = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for _ in range(M):
        x, y, c = map(int,input().split())
        gotree[x][y] = c
        backtree[y][x] = c
    max_dist = 0
    backs = check(X, backtree)
    go = check(X, gotree)
    for i in range(1, N+1):
        max_dist = max(max_dist, go[i]+backs[i])
    print('#{} {}'.format(tc, max_dist))



