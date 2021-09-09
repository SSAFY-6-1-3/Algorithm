n = 3

answer = []
arr = list([0] * n for _ in range(n))
    # 하 우 대각선
dx = [+1, 0, -1]
dy = [0, +1, -1]

x, y = -1, 0     # 초기위치
cnt = 1
dir = 0         # 이동방향
number = 0
for num in range(n+1):
    number += num

while cnt < number+1:
    nx = x + dx[dir]
    ny = y + dy[dir]
    if 0<=nx<n and 0<=ny<n and arr[nx][ny]==0:
        arr[nx][ny] = cnt
        cnt += 1
        x = nx
        y = ny
    else:
        dir = (dir + 1) % 3
        # for i in range(3):
        #     if 0<=x+dx[i]<n and 0<=y+dy[i]<n and arr[x+dx[i]][y+dy[i]] == 0:
        #         dir = (dir+1) % 3
        #         break
        # else:
        #     break

for i in range(n):
    for j in range(n):
        if arr[i][j]:
            answer.append(arr[i][j])

print(answer)
