import math

def solution(n, stations, w):
    answer = 0

    width = 2*w + 1
    idx = 0

    for station in stations:
        start= max(0, station-w-1)
        answer += math.ceil((start - idx) / width)
        idx = min(n, station+w)
    answer += math.ceil((n-idx)/width)

    return answer

print(solution(11, [4, 11], 1))

