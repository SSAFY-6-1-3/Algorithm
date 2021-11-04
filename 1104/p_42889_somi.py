def solution(N, stages):
    fail = [0] * (N + 2)
    for stage in stages:
        fail[stage] += 1


    user = len(stages)
    while user:
        for i in range(N + 2):
            fail_user = fail[i]
            if fail_user:
                fail[i] = fail[i] / user
                user -= fail_user

    result = [i[0] for i in sorted(enumerate(fail), reverse=True, key=lambda x: x[1])]
    result.remove(0)
    result.remove(N + 1)
    return result

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))