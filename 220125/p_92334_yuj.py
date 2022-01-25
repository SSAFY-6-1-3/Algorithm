def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {id: set() for id in id_list}
    reported_by = {id: set() for id in id_list}

    for names in report:
        a, b = map(str, names.split())
        reports[a].add(b)
        reported_by[b].add(a)

    for idx, id in enumerate(id_list):
        for person in reports[id]:
            if len(reported_by[person]) >= k:
                answer[idx] += 1

    return answer

print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))
print(solution(["con", "ryan"],["ryan con", "ryan con", "ryan con", "ryan con"], 3))