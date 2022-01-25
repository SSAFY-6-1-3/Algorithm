def solution(id_list, report, k):

    id_dict = {}  # id: [경고 횟수, 경고한 id]
    stop = []  # 정지당한 id
    for id in id_list:
        id_dict[id] = [0]

    for case in report:
        user, bad = case.split()  # 신고자, 대상

        if bad not in id_dict[user]: # 여러번 신고해도 1번만
            id_dict[user].append(bad)
            id_dict[bad][0] += 1
            if id_dict[bad][0] == k:
                stop.append(bad)

    answer = []
    for id in id_list:
        cnt = 0  # 경고한 id 중 몇 개가 정지 당했는 지 count
        for bad in stop:
            if bad in id_dict[id]:
                cnt += 1
        answer.append(cnt)

    return answer

print(solution(	["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))