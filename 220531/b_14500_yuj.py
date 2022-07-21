def move(i, j, temp, cnt):
    global answer, visited
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    if cnt == 3:
        answer = max(answer, temp)
        return

    elif cnt == 2:
        if temp + max_num < answer:
            return

    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        if ni in range(N) and nj in range(M) and [ni, nj] not in visited:
            visited.append([ni, nj])
            if cnt == 1:
                move(i, j, temp + matrix[ni][nj], cnt + 1)
            move(ni, nj, temp+matrix[ni][nj], cnt+1)
            visited.remove([ni, nj])

N, M = map(int, input().split())
matrix = list(list(map(int, input().split())) for _ in range(N))
max_num = max(map(max, matrix))
answer = 0
for i in range(N):
    for j in range(M):
        visited = [[i, j]]
        move(i, j, matrix[i][j], 0)

print(answer)