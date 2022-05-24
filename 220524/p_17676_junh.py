from datetime import datetime, timedelta
from collections import deque


def solution(lines):
    lines.sort()
    answer = 0
    q = []

    for line in lines:
        d, t, r = line.split()
        s = d + ' ' + t
        # 시간 데이터로 바꾸고
        s = datetime.fromisoformat(s) - timedelta(seconds=0.5)
        # float로 바꿔서
        r = float(r.strip('s')) + 0.999

        while q and s >= q[0]:
            # print(s)
            # print('pop', q[0])
            q.pop(0)


        q.append(s + timedelta(seconds=r))
        q.sort()
        answer = max(answer, len(q))
        # print(line)
        print(s, s+timedelta(seconds=r))
        # print(len(q))
    answer = max(answer, len(q))

    return answer



# print(solution(["2016-09-15 00:00:00.000 3s"])) #1
# print(solution(["2016-09-15 23:59:59.999 0.001s"])) #1

print(solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"])) #2
# 6.001 7
print(solution(["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]))
#7