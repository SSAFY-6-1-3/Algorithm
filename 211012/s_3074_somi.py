def immigration(l, r):
    while l <= r:
        people = 0  # 심사 완료 한 사람 수
        # 해당 검색대에서 심사한 사람 수 = 총 소요 시간 / 해당 검색 대 소요 시간

        mid = (l + r) // 2

        for time in times:
            people += mid // time

        if people >= M:  # 초과 한 경우
            r = mid - 1

        else:  # 아직 시간 더 필요 한 경우
            l = mid + 1

    return l



T = int(input())
for tc in range(1, 1 + T):
    N, M = map(int, input().split())  # N : 총 심사대 / M : 사람 수
    times = [int(input()) for _ in range(N)]  # 입국 심사 소요 시간
    min_time, max_time = 1, max(times) * M  # max : 최악 소요 시간


    print('#{}'.format(tc), immigration(min_time, max_time))
