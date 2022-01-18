def solution(n, stations, w):

    station_area = [(0,0)]  # 전파가 닿는 지역(시작점, 끝점)
    for station in stations:  # stations는 오름차순으로 정렬됨
        start = station - w
        if start < 0:
            start = 0
        end = station + w
        if end > n:
            end = n
        station_area.append((start, end))
    station_area.append((n + 1, n + 1))

    answer = 0
    for i in range(len(station_area) - 1):
        # 전파가 안 닿는 지역의 거리 / 전파전달 범위
        d, m = divmod(station_area[i + 1][0] - (station_area[i][1] + 1), (w * 2 + 1))

        if m >= 1:
            answer += d + 1
        else:
            answer += d

    return answer

solution(11, [4,11], 1)