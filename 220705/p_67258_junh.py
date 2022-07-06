

def solution(gems):
    answer = [1, len(gems)+2]
    gem_set = set(gems)
    codes = {gem:-1 for gem in gem_set}

    for i in range(len(gems)):
        codes[gems[i]] = i
        start = min(codes.values())
        if start != -1 and i-start < answer[1]-answer[0]:
            answer = [start+1, i+1]

    return answer


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))