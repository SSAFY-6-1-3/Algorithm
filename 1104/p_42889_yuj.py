def solution(N, stages):
    user = [0] * N                          # stage별 통과 못 한 인원
    for stage in stages:
        if stage < N+1:
            user[stage-1] += 1

    fail = [0] * N                          # 실패율 저장
    users = len(stages)
    for idx in range(N):
        if users:                           # 뒷 스테이지 전에 모두 실패해서 users가 0보다 작을 경우 분기
            fail[idx] = user[idx] / users
            users -= user[idx]
        else:
            fail[idx] = 0

    result = []
    while len(result) < N:                  # 큰 값부터 idx+1(stage)출력
        idx = fail.index(max(fail))
        result.append(idx+1)
        fail[idx] = -1

    return result

N, stages = 20, [1, 2, 2, 1, 3]
print(solution(N, stages))