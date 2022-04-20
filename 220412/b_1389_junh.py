
def bacon(a):
    q = [a]
    idx = 0
    dists = [-1]*(N+1)
    dists[a] = 0

    while idx < len(q):
        now = q[idx]
        idx += 1
        for i in range(1, N+1):
            if not rel[now][i] or dists[i] > -1: continue
            dists[i] = dists[now]+1
            q.append(i)
    return sum(dists)


N, M = map(int, input().split())
rel = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    rel[a][b] = rel[b][a] = 1


min_p, min_v = 0, float('inf')
for i in range(1, N+1):
    v = bacon(i)
    if v < min_v:
        min_p = i
        min_v = v

print(min_p)