from itertools import combinations

def solution(relation):
    keys = []
    items = [i for i in range(len(relation[0]))]  # 후보 키 인덱스
    for j in range(1, len(relation[0]) + 1):
        keys.extend((combinations(items, j)))

    candidate_key = set()
    for k in keys:
        # 최소성
        is_min = True
        for c in candidate_key:
            if set(c).issubset(k):
                is_min = False
                break
        if not is_min:
            continue

        # 유일성
        tmp_set = set(tuple(r[idx] for idx in k) for r in relation)
        if len(tmp_set) == len(relation):
            candidate_key.add(k)

    return len(candidate_key)

print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))