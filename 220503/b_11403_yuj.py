def move(i):
    global check
    for j in range(N):
        if not check[j] and G[i][j]:
            check[j] = 1
            move(j)

N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    check = [0] * N
    move(i)
    print(*check)