from itertools import permutations

def solution(k, dungeons):
    answer = 0
    perms = list(permutations(dungeons, len(dungeons)))
    for perm in perms:
        total = k
        cnt = 0
        for idx in range(len(perm)):
            if answer > cnt + len(perm) - idx + 1:
                break
            if total >= perm[idx][0]:
                total -= perm[idx][1]
                cnt += 1
        answer = max(answer, cnt)

    return answer

print(solution(80, [[80,20],[50,40],[30,10]]))