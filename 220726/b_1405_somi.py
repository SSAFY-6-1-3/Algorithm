move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def go_simple(cnt, now, percentage):
    global ans
    now_x, now_y = now

    if cnt == N:
        ans += percentage
        return

    for i in range(4):
        next_x = now_x + move[i][0]
        next_y = now_y + move[i][1]
        if direction[i] and not visited[next_x][next_y]:
            visited[next_x][next_y] = True
            go_simple(cnt + 1, (next_x, next_y), percentage * (direction[i]))
            visited[next_x][next_y] = False


N, east, west, south, north = map(int, input().split())
direction = [east, west, south, north]
visited = [[False for _ in range(30)] for _ in range(30)]
visited[15][15] = True

ans = 0.0
go_simple(0, (15, 15), 1)

print(ans * (0.01 ** N))
