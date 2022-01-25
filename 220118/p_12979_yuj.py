def solution(n, stations, w):
    answer = 0
    needs = []                                          # 전파가 도달하지 않는 거리 저장
    for idx in range(len(stations)):
        if idx == 0:                                    # 맨 앞의 기지국일 경우 전파 도달하지 않는 거리 계산
            needs.append(stations[idx] - 1 - w)
        else:                                           # 기지국들 사이에 전파가 도달하지 않는 거리 계산
            needs.append(stations[idx] - stations[idx - 1] - 1 - (2 * w))
        if idx == len(stations) - 1:                    # 마지막 기지국일 경우 -> 맨 끝에서 마지막 기지국 사이에 거리 계산
            needs.append(n - stations[idx] - w)

    for need in needs:                                  # 기지국들 사이에 기지국이 몇 개 더 들어가야하는지 계산
        if need > 0:
            q = need // (2 * w + 1)  
            r = need % (2 * w + 1)                      # 총 전파거리보다 더 필요하면 기지국 한 개 더 추가
            if r:
                q += 1
            answer += q

    return answer


print(solution(11, [4, 11], 1))
print(solution(16, [9], 2))