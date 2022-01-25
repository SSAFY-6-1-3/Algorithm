R, C = map(int, input().split())  # 행, 열 바꿔주기
K = int(input())

seats = list([0] * C for _ in range(R))

dr = [0, 1, 0, -1]  # 우하좌상
dc = [1, 0, -1, 0]

r, c = 0, -1  # 공연장 밖에서 시작
di = 0
num = 1

while num <= K:
    if R * C < K:
        print(0)
        break

    nr, nc = r + dr[di], c + dc[di]
    if 0 <= nr < R and 0 <= nc < C and not seats[nr][nc]:
        r, c = nr, nc
        seats[r][c] = num
        if num == K:
            print(r + 1, c + 1)
            break
        else:
            num += 1

    else:
        di = (di + 1) % 4

