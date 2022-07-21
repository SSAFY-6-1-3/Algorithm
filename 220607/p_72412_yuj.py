from itertools import combinations

def solution(infos, queries):
    answer = []
    dic = {'': []}                  # '-'만 있는 조건 만족시키기위해서
    for info in infos:              # 맨 뒤의 점수만 빼고 str형태로 다 붙임
        info = info.split()
        temp = info[:-1]
        score = int(info[-1])
        dic[''].append(score)

        for i in range(1, 5):
            for comb in combinations(temp, i):  # 조건 조합으로 나올 수 있는 모든 경우의 수를 dic의 key로 설정
                temp_key = ''.join(comb)
                if temp_key in dic:
                    dic[temp_key].append(score)
                else:
                    dic[temp_key] = [score]

    for key in dic.keys():
        dic[key].sort()
    print(dic)
    for query in queries:
        query = query.split()
        temp_score = int(query[-1])
        temp_info = []
        for q in query[:-1]:
            if q not in ['and', '-']:
                temp_info.append(q)

        temp_str = ''.join(temp_info)

        cnt = 0
        if temp_str in dic:
            l = len(dic[temp_str])
            temp = l
            start, end = 0, l-1
            while start <= end:
                mid = (start + end) // 2
                if dic[temp_str][mid] >= temp_score:
                    end = mid - 1
                    temp = mid
                else:
                    start = mid + 1

            cnt = l-temp
        answer.append(cnt)
        print(temp_str)
        print(cnt)
    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))