import sys

sys.stdin = open('2383.txt')


# def find_human_stairs():
#     humans = []
#     stairs = []
#     for i in range(N):
#         for j in range(N):
#             if maps[i][j] == 1:
#                 humans.append((i, j))
#             elif maps[i][j] > 1:
#                 stairs.append((i, j, maps[i][j]))
#
#     time_lst = []
#     for human in humans:
#         time = []
#         for stair in stairs:
#             temp = abs(human[0] - stair[0]) + abs(human[1] - stair[1]) + stair[2] + 1
#             time.append(temp)
#         time_lst.append(time)
#
#     return humans, stairs, time_lst
#
#
# T = int(input())
#
# for test_case in range(1, T+1):
#     N = int(input())
#     maps = [list(map(int, input().split())) for _ in range(N)]
#     h_lst, s_lst, t_lst = find_human_stairs()
#     print(f'#{test_case} {t_lst}')


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    room = [list(map(int, input().split())) for n in range(N)]

    people = []
    stair = []
    for i in range(N):
        for j in range(N):
            if room[i][j] == 1:
                people.append([i, j])
            elif room[i][j] >= 2:
                stair.append([i, j, room[i][j]])

    dis = []
    for i in people:
        pdis = []
        for j in stair:
            pdis.append(abs(i[0] - j[0]) + abs(i[1] - j[1]) + j[2] + 1)
        dis.append(pdis)

    res = []
    stair1 = 0
    stair2 = 0
    dis_index = 0
    for i in dis:
        if i[0] < i[1]:
            stair1 += 1
            res.append([i[0], dis_index])
        else:
            stair2 += 1
            res.append([i[1], dis_index])
        dis_index += 1

    res.sort()
    for i in res:
        if stair1 > 3:
            i[0] = min(i[0] + stair[0][2], dis[i[1]][1])
            stair1 -= 1
        if stair2 > 3:
            i[0] = min(i[0] + stair[1][2], dis[i[1]][0])
            stair2 -= 1

    time = []
    for i in res:
        time.append(i[0])

    print("#{} {}".format(tc, max(time)))
