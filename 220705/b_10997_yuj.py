N = int(input())
if N == 1:
    print('*')
else:
    row = 3 * N + N-1
    matrix = [[' '] * (row-2) for _ in range(row)]
    x, y = row // 2 + 1, (row-2) // 2
    matrix[x][y] = '*'
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    cnt = 0
    star = 2
    flag = 0
    while True:
        if flag:
            break
        for _ in range(2):
            k = cnt % 4

            for _ in range(star):
                nx, ny = x+dx[k], y+dy[k]
                x, y = nx, ny
                matrix[x][y] = '*'
            cnt += 1
            if cnt == (N - 1) * 4 + 1:
                flag = 1
                break
        star += 2
    matrix[0] = ['*'] * (row-2)
    for i in range(row):
        if i == 1:
            print('*')
            continue
        temp = ''
        for j in range(row-2):
            print(matrix[i][j], end="")
        print('')