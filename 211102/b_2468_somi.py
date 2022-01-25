dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def safe_zone(h, x, y):
    q = [(x, y)]
    while q:
        r, c = q.pop()
        for di in range(4):
            nr, nc = r + dr[di], c + dc[di]
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] > h and not visited[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = True


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
min_height = min(min(arr[i]) for i in range(N))
max_height = max(max(arr[j]) for j in range(N))

max_cnt = 1
for height in range(min_height, max_height):
    visited = [[False] * N for _ in range(N)]
    cnt = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] > height and not visited[r][c]:
                visited[r][c] = True
                cnt += 1
                safe_zone(height, r, c)
    if cnt > max_cnt:
        max_cnt = cnt

print(max_cnt)