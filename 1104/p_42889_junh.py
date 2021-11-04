def solution(N, stages):
    answer = []
    stucks_clears = [[0, 0] for _ in range(N+1)]

    for stage in stages:
        if stage != N+1:
            stucks_clears[stage][0] +=1
        for k in range(1, min(stage, N)+1):
            stucks_clears[k][1] +=1

    max_stage = min(N, max(stages))

    ratios = [0] * (max_stage+1)
    for i in range(1, max_stage+1):
        ratios[i] = stucks_clears[i][0] / stucks_clears[i][1]

    ratios = list(enumerate(ratios))
    ratios.sort(reverse=True, key = lambda x: x[1])

    for ratio in ratios:
        if ratio[0]:
            answer.append(ratio[0])

    while len(answer) <N:                   # 아무도 도달 못한 단계 적어주기
        answer.append(len(answer)+1)

    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]	))
print(solution(4, [4,4,4,4,4]))