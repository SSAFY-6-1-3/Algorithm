# 0 청소 전 1 벽, 2 청소 완료
N, M = map(int, input().split())
r, c, d = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
ans = 1
matrix[r][c] = 2
while True:

    for _ in range(4):
        d += 3
        d %= 4
        nr, nc = r+direction[d][0], c+direction[d][1]
        if nr in range(N) and nc in range(M) and not matrix[nr][nc]:
            matrix[nr][nc] = 2
            ans += 1
            r, c = nr, nc
            break
    else:
        temp = (d+2) % 4
        nr, nc = r + direction[temp][0], c + direction[temp][1]
        if nr in range(N) and nc in range(M) and matrix[nr][nc] != 1:
            if matrix[nr][nc] == 0:
                matrix[nr][nc] = 2
                ans += 1
            r, c = nr, nc
        else:
            break

print(ans)