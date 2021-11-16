import sys
sys.stdin=open('input.txt')

c, r = map(int, input().split())
n = int(input())
arr = [[0 for _ in range(c)] for _ in range(r)]

dx = [-1, 0, +1, 0]
dy = [0, +1, 0, -1]

if n <= r * c:
    cnt = 1
    x, y, k = r, 0, 0

    while cnt < n+1:

        nx, ny = x+dx[k], y+dy[k]

        if nx in range(r) and ny in range(c) and not arr[nx][ny]:
            arr[nx][ny] = cnt
            cnt += 1
            x, y = nx, ny
        else:
            k = (k+1) % 4

    print(y+1, r-x)

else:
    print(0)