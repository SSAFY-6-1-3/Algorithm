def solution(N, stages):

    temp = [[] for _ in range(N)]
    # i(실패율을 구할 스테이지) 보다 stage 가 크거나 같은 개수가 도달한 수
    # i 보다 stage 가 큰 개수가 성공한 수
    for i in range(1, N+1):
        fail = 0
        challenge = 0
        for stage in stages:
            if i <= stage:
                challenge += 1
            if i == stage:
                fail += 1
        if challenge:
            temp[i-1] = [i, fail / challenge]
        else:
            temp[i-1] = [i, 0]

    answer = [0] * N
    idx = 0
    while idx != N:
        max_idx = 0
        for i in range(N):
            if temp[i][1] == -1:
                continue
            if temp[i][1] > temp[max_idx][1]:
                max_idx = i
        answer[idx] = temp[max_idx][0]
        temp[max_idx][1] = -1
        idx += 1

    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))
