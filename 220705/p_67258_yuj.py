def solution(gems):
    answer = []
    total = len(set(gems))
    dic = dict()
    start, end = 0, 0
    dic[gems[0]] = 1

    while True:
        while True:
            if gems[start] in dic and dic[gems[start]] > 1:
                dic[gems[start]] -= 1
                start += 1
            else:
                break

        if len(dic) == total:
            if not answer or (end-start) < answer[1]-answer[0]:
                answer = [start+1, end+1]

        end += 1
        if end == len(gems):
            break

        if gems[end] in dic:
            dic[gems[end]] += 1
        else:
            dic[gems[end]] = 1

    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))