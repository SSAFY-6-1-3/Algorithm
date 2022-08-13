from collections import deque


def solution(relation):

    def check(combi):
        c_set = set()
        for rel in relation:
            c_set.add(tuple([rel[c] for c in combi]))
        if len(c_set) == len(relation):
            return True
        return False

    answer = 0
    length = len(relation[0])
    q = deque([{i} for i in range(length)])

    used = []
    while q:
        comb = q.popleft()

        for u in used:
            if u.issubset(comb):
                break
        else:
            if check(comb):
                used.append(comb)
                answer += 1
            else:
                for i in range(max(comb)+1, length):
                    q.append(comb.union({i}))

    return answer

print(solution([["100", "ryan", "music", "2", 1], ["200", "apeach", "math", "2", 2], ["300", "tube", "computer", "3", 3], ["400", "con", "computer", "4", 4], ["500", "muzi", "music", "3", 5], ["600", "apeach", "music", "2", 6]]))