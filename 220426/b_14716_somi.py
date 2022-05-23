direction = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]

def dfs(r, c):
    global cnt
    banner[r][c] = 0
    stack = [(r, c)]
    while stack:
        now_r, now_c = stack.pop()
        for i in range(8):
            next_r = now_r + direction[i][0]
            next_c = now_c + direction[i][1]

            if 0 <= next_r < M and 0 <= next_c < N and banner[next_r][next_c]:
                banner[next_r][next_c] = 0
                stack.append((next_r, next_c))
    cnt += 1

M, N = map(int, input().split())
banner = list(list(map(int, input().split(' '))) for _ in range(M))

cnt = 0
for r in range(M):
    for c in range(N):
        if banner[r][c]:
            dfs(r, c)

print(cnt)