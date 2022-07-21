def all(x, y, d):
    temp = 0
    # 위, 오른쪽, 아래, 왼쪽
    direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    x += direction[d][0]
    y += direction[d][1]

    while x in range(N) and y in range(M):
        if matrix[x][y] == 6:
            break
        elif matrix[x][y] == 0:
            matrix[x][y] = '#'
            temp += 1
        x += direction[d][0]
        y += direction[d][1]
    return temp

def move(x, y, d, checked):
    temp = []
    # 위, 오른쪽, 아래, 왼쪽
    direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    x += direction[d][0]
    y += direction[d][1]

    while x in range(N) and y in range(M):
        if matrix[x][y] == 6:
            break
        elif matrix[x][y] == 0 and [x, y] not in checked:
            temp.append([x, y])
        x += direction[d][0]
        y += direction[d][1]
    return temp


def watch(s, checked):
    global ans

    if s == len(lst):
        ans = max(ans, len(checked))
        return

    if matrix[lst[s][0]][lst[s][1]] == 1:
        for k in range(4):
            watch(s+1, checked + move(lst[s][0], lst[s][1], k, checked))

    if matrix[lst[s][0]][lst[s][1]] == 2:
        dir = [[1, 3], [0, 2]]
        for k in range(2):
            two = []
            two += move(lst[s][0], lst[s][1], dir[k][0], checked)
            two += move(lst[s][0], lst[s][1], dir[k][1], checked)
            watch(s+1, checked + two)

    if matrix[lst[s][0]][lst[s][1]] == 3:
        dir = [[0, 1], [1, 2], [2, 3], [3, 0]]
        for k in range(4):
            three = []
            three += move(lst[s][0], lst[s][1], dir[k][0], checked)
            three += move(lst[s][0], lst[s][1], dir[k][1], checked)
            watch(s+1, checked + three)

    if matrix[lst[s][0]][lst[s][1]] == 4:
        dir = [[0, 1, 2], [1, 2, 3], [0, 1, 3], [0, 2, 3]]
        for k in range(4):
            four = []
            four += move(lst[s][0], lst[s][1], dir[k][0], checked)
            four += move(lst[s][0], lst[s][1], dir[k][1], checked)
            four += move(lst[s][0], lst[s][1], dir[k][2], checked)
            watch(s+1, checked + four)

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
lst = []
five = []
wall = 0
for i in range(N):
    for j in range(M):
        if 0 < matrix[i][j] < 5:
            lst.append([i, j])
        elif matrix[i][j] == 5:
            five.append([i, j])
        elif matrix[i][j] == 6:
            wall += 1

for f in five:
    for num in range(4):
        wall += all(f[0], f[1], num)

ans = 0
checked = [0] * len(lst)
watch(0, [])
ans += len(lst) + wall + len(five)
print(N*M - ans)


