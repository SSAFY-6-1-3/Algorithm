def quad(r, c, n):
    now = video[r][c]
    for x in range(r, r + n):
        for y in range(c, c + n):
            if now != video[x][y]:  # 0,1 섞여 있으면
                print('(', end='')
                n = n // 2
                quad(r, c, n)          # 왼쪽 위
                quad(r, c + n, n)      # 오른쪽 위
                quad(r + n, c, n)      # 왼쪽 아래
                quad(r + n, c + n, n)  # 오른쪽 아래
                print(')', end='')
                return

    print(now, end='')
    return

n = int(input())
video = [list(input()) for _ in range(n)]
quad(0, 0, n)