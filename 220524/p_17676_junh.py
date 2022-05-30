from datetime import datetime, timedelta


def solution(lines):
    lines.sort()
    answer = 0
    times = []

    for line in lines:
        d, t, r = line.split()
        s = d + ' ' + t
        # 시간 데이터로 바꾸고, 1초로 범위를 잡기위해 0.5를 더한다(시작, 끝 시간을 0.5초씩 늘려서 1초 범위까지 커버하게)
        e = datetime.fromisoformat(s) + timedelta(seconds=0.5)
        # float로 바꿔서
        r = float(r.strip('s'))
        # 범위가 1초면 안되고 0.999로 잡아야 원래 시간까지 합쳐서 1초가 됨
        s = e - timedelta(seconds=r+0.999)

        times.append((s, e))

    # 각각의 시작, 끝 시간 중에
    for s, e in times:
        cnt = 0
        for os, oe in times:
            # 현재 요청의 시작이 다른 요청의 시작과 끝 사이에 있으면 +1
            if os <= s < oe :
                cnt += 1
        answer = max(answer, cnt)
        print(s, e)

    return answer



# print(solution(["2016-09-15 00:00:00.000 3s"])) #1
# print(solution(["2016-09-15 23:59:59.999 0.001s"])) #1
#
print(solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"])) #2
# 6.001 7
# print(solution(["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]))
#7