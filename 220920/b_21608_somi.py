dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

N = int(input())
studentDict = dict()
desks = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(N * N):
    likeList = list(map(int, input().split()))
    studentDict[likeList[0]] = likeList[1:]

    maxLike = -1
    maxEmpty = -1
    desk_r = -1
    desk_c = -1

    for r in range(N):
        for c in range(N):
            if desks[r][c] == 0:  # 빈자리
                likeCnt = 0
                emptyCnt = 0

                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]

                    if 0 <= nr < N and 0 <= nc < N:
                        if desks[nr][nc] == 0:
                            emptyCnt += 1

                        elif desks[nr][nc] in likeList[1:]:
                            likeCnt += 1

                if (maxLike < likeCnt) or (maxLike == likeCnt and maxEmpty < emptyCnt):
                    maxLike = likeCnt
                    maxEmpty = emptyCnt
                    desk_r = r
                    desk_c = c

    desks[desk_r][desk_c] = likeList[0]


ans = 0

for j in range(N):
    for k in range(N):
        likes = studentDict[desks[j][k]]
        cnt = 0
        for i in range(4):
            nr = j + dr[i]
            nc = k + dc[i]

            if 0 <= nr < N and 0 <= nc < N and desks[nr][nc] in likes:
                cnt += 1

        if cnt:
            ans += 10 ** (cnt - 1)

print(ans)
