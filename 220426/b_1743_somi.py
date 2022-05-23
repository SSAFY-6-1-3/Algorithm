dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def dfs(now_r, now_c):
    cnt = 0
    stack = [(now_r, now_c)]
    while stack:
        r, c = stack.pop()
        for i in range(4):
            next_r = r + dr[i]
            next_c = c + dc[i]
            if 0 <= next_r < N and 0 <= next_c < M and hallway[next_r][next_c]:
                cnt += 1
                hallway[next_r][next_c] = 0
                stack.append((next_r, next_c))
    return cnt


N, M, K = map(int, input().split())

hallway = list(list(0 for _ in range(M)) for _ in range(N))
for _ in range(K):
    r, c = map(int, input().split())
    hallway[r - 1][c - 1] = 1  # 쓰레기 1로 표시

max_cnt = 0
for i in range(N):
    for j in range(M):
        if hallway[i][j]:
            max_cnt = max(max_cnt, dfs(i, j))

print(max_cnt)