def solution(id_list, report, k):
    n = len(id_list)
    answer = [0] * n
    reported = {}

    for rep in report:
        er, ed = rep.split(' ')

        if reported.get(ed):
            reported[ed].add(er)
        else:
            reported[ed] = {er}

    for ed in reported.values():
        if len(ed) >= k:
            for er in ed:
                idx = id_list.index(er)
                answer[idx] +=1

    return answer


print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))