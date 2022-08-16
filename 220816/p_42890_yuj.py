from itertools import combinations

def solution(relations):
    answer = 0
    nums = [j for j in range(len(relations[0]))]
    candidates = []

    # 최소성 확인
    # combs 집합 중에 부분집합인지 확인
    def minimal(comb):
        for candidate in candidates:
            if candidate.issubset(comb):
                return 0
        else:
            return 1

    # 유일성 확인
    def unique(comb):
        keys = set()
        for relation in relations:
            temp = ''
            for c in comb:
                temp += relation[c]
            keys.add(temp)
        if len(keys) == len(relations):
            candidates.append(comb)
            return 1
        return 0

    for i in range(1, len(relations[0])+1):
        for comb in combinations(nums, i):
            if minimal(set(comb)) and unique(set(comb)):
                answer += 1
    return answer

print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))