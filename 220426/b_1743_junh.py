
N, M, K = map(int, input().split())
mat = [[0]*M for _ in range(N)]

wastes = []

for _ in range(K):
    r, c = map(int, input().split())
    r, c = r-1, c-1
    mat[r][c] = 1
    wastes.append((r, c))

def bfs(r, c, mat):
    global max_waste
    q = [(r, c)]
    idx = 0

    dR = (1, 0, -1, 0)
    dC = (0, 1, 0, -1)

    while idx < len(q):
        r, c = q[idx]
        idx += 1

        for d in range(4):
            nr, nc = r+dR[d], c+dC[d]
            if nr not in range(N) or nc not in range(M) or not mat[nr][nc]:
                continue
            if (nr, nc) not in q:
                q.append((nr, nc))

    for r, c in q:
        mat[r][c] = len(q)
        max_waste = max(max_waste, len(q))

max_waste = 1
for waste in wastes:
    r, c = waste
    if mat[r][c] == 1:
        bfs(r, c, mat)
print(max_waste)