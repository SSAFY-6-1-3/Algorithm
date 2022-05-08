
dY = (0, 1, 0, -1)  # 좌 하 우 상 순서
dX = (-1, 0, 1, 0)
# 일단은 왼쪽 방향만 적어줌
sandmoves = [{
    (0, -1) : 0,
    (-1, -1) : 0.10,
    (1, -1) : 0.10,
    (-1, 0) : 0.07,
    (1, 0) : 0.07,
    (0, -2) : 0.05,
    (-2, 0) : 0.02,
    (2, 0) : 0.02,
    (-1, 1) : 0.01,
    (1, 1) : 0.01
}]

def make_sandmoves():   # 각 방향의 모래폭풍 만들기
    for d in range(1, 4):
        tmp = {}
        for p, v in sandmoves[0].items():
            y, x = p
            if d == 1:
                y, x = -x, y
            elif d == 2:
                y, x = y, -x
            elif d == 3:
                y, x = x, -y
            tmp[(y, x)] = v
        sandmoves.append(tmp)

def simul(mat, N):
    visited = [[False]*N for _ in range(N)]
    y, x = N//2, N//2   # 시작 위치
    d = 0               # 시작 방향
    cnt = 0             # 몇번 이동했는지
    outed = 0           # 격자 밖으로 나간 모래의 합

    while cnt < N**2:
        visited[y][x] = True
        now_storm = sandmoves[d]    # 현재 방향의 모래날리는 비율
        org_sand = mat[y][x]        # 현재 모래바람위치의 총 모래 양
        moved_sand = 0              # org에서 날라갈 모래 양
        ay, ax = 0, 0               # 모래바람이 바라보는 바로 앞 a좌표를 저장할 변수

        for k, v in now_storm.items():  # 모래가 떨어지는 모든 좌표에 대해서
            ry, rx = k  # 현재 위치에서의 상대좌표
            if not v:                   # value가 없으면 모래폭풍이 보고있는 바로 앞, 즉a 포인트의 상대위치
                ay, ax = y+ry, x+rx     # 절대위치만 저장해두고 continue
                continue

            my, mx = y+ry, x+rx   # 실제 모래가 떨어질 좌표

            move_sand = int(org_sand * v)               # 날아가야 할 모래의 양
            moved_sand += move_sand                     # 옮겨야할 모래에 추가

            if my in range(N) and mx in range(N):       # 떨어질 곳이 있으면 거기로 옮기고
                mat[my][mx] += move_sand
            else:                                       # 없으면 outed에 합산
                outed += move_sand

        org_sand -= moved_sand                          # 딴데로 날라간 모래 다 빼고
        if ay in range(N) and ax in range(N):           # a 좌표가 있으면 거기로 남은 모래를 다 옮긴다
            mat[ay][ax] += org_sand
        else:                                           # 없으면 outed로
            outed += org_sand
        mat[y][x] = 0                                   # 기존 위치의 모래는 다 날라갔으므로 0

        nD = (d+1)%4                                    # 일단 90도 돌려보고
        ny, nx = y+dY[nD], x+dX[nD]
        if not visited[ny][nx] and cnt:                 # 가능하면 방향 돌려서 글로 감, cnt가 0일때, 즉 제일 처음에는 무적권 직진
            d=nD
        else:                                           # visited때매 못가면 직진
            ny, nx = y+dY[d], x+dX[d]

        y, x = ny, nx                                   # 위치 옮기고 카운트+1
        cnt+=1

        # print(cnt)
        # print(y, x)
        # for i in range(N):
        #     print(*mat[i])
    return outed


make_sandmoves()
N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]

print(simul(mat, N))