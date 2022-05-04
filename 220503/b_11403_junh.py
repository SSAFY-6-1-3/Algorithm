
N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]
checked = [False]*N

def dfs(n):
    checked[n] = True
    for i in range(N):
        if mat[n][i]:
            if checked[i]:
                for j in range(N):
                    if mat[i][j]:
                        mat[n][j] = 1
            else:
                dfs(i)

for i in range(N):
    dfs(i)
dfs(0)

for i in range(N):
    print(*mat[i])
