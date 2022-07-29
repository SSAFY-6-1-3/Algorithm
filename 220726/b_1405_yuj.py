def dfs(i, j, cnt, per):
    global ans

    if cnt == num:
        ans += per
        return

    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]
    for k in range(4):
        ni, nj = i+di[k], j+dj[k]
        if ni in range(30) and nj in range(30) and not matrix[ni][nj]:
            matrix[ni][nj] = 1
            dfs(ni, nj, cnt+1, per*percent[k])
            matrix[ni][nj] = 0

num, E, W, S, N = map(int, input().split())
percent = {0: 0.01 * E, 1: 0.01 * W, 2: 0.01 * S, 3: 0.01 * N}
matrix = [[0] * 30 for _ in range(30)]
matrix[14][14] = 1
ans = 0
dfs(14, 14, 0, 1)
print(ans)