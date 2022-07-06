import copy

di = [(0, 1), (1, 0), (0, -1), (-1, 0)]
cctv = {
    1: list([di[i]] for i in range(4)),
    2: [[di[0], di[2]], [di[1], di[3]]],
    3: list([di[i], di[(i + 1) % 4]] for i in range(4)),
    4: [[di[0], di[1], di[3]], [di[0], di[1], di[2]], [di[1], di[2], di[3]], [di[0], di[2], di[3]]],
    5: [di]
}


def count_blind(watched_office):  # 0만 count
    cnt = 0
    for i in range(N):
        for j in range(M):
            if not watched_office[i][j]:
                cnt += 1
    return cnt


def check_watched(r, c, direction, watched_office): 
    for d in direction:
        now_r = r + d[0]
        now_c = c + d[1]
        while 0 <= now_r < N and 0 <= now_c < M:
            if watched_office[now_r][now_c] == 6:
                break
            if watched_office[now_r][now_c] == 0:
                watched_office[now_r][now_c] = '#'
            now_r += d[0]
            now_c += d[1]

    return watched_office


def watch(spot_index, watched_office):
    global blind_spots

    if spot_index == cctv_cnt:
        cnt = count_blind(watched_office)
        blind_spots = min(blind_spots, cnt)
        return

    r, c = cctv_in_office[spot_index][0], cctv_in_office[spot_index][1]
    cctv_num = office[r][c]
    tmp_office = copy.deepcopy(watched_office)
    for direction in cctv[cctv_num]:
        checked_office = check_watched(r, c, direction, tmp_office)
        watch(spot_index + 1, checked_office)
        tmp_office = copy.deepcopy(watched_office)  # 49 줄 반영 안된 것으로


N, M = map(int, input().split())
office = []
cctv_in_office = list()  # cctv 좌표값 저장 리스트
for i in range(N):
    tmp = list(map(int, input().split()))
    office.append(tmp)
    for j in range(M):
        if tmp[j] in list(num for num in range(1, 6)):
            cctv_in_office.append((i, j))

cctv_cnt = len(cctv_in_office)
blind_spots = N * M + 1
watch(0, office)
print(blind_spots)