N = int(input())
student = dict()
total = N*N
matrix = [[0] * N for _ in range(N)]
dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
for _ in range(total):
    lst = list(map(int, input().split()))
    num = lst[0]
    likes = lst[1:5]
    student[num] = likes
    temp = []
    for r in range(N):
        for c in range(N):
            if not matrix[r][c]:
                cnt, zero = 0, 0
                for k in range(4):
                    nr, nc = r+dr[k], c+dc[k]
                    if nr in range(N) and nc in range(N):
                        if matrix[nr][nc] in likes:
                            cnt += 1
                        elif not matrix[nr][nc]:
                            zero += 1
                temp.append((cnt, zero, r, c))
    temp.sort(key=lambda x: (x[0], x[1], -x[2], -x[3]))
    result = temp[-1]
    matrix[result[2]][result[3]] = num

ans = 0
good = [0, 1, 10, 100, 1000]
for i in range(N):
    for j in range(N):
        now = student[matrix[i][j]]
        side = 0
        for s in range(4):
            ni, nj = i + dr[s], j + dc[s]
            if ni in range(N) and nj in range(N) and matrix[ni][nj] in now:
                side += 1
        ans += good[side]

print(ans)