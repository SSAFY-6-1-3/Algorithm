# 문제 잘못이해. 다시 풀기

def solution(n, t, m, timetable):
    answer = ''
    timetable.sort()
    now = timetable[0]
    p = len(timetable)
    if m <= p:
        tmp = timetable[-(p - m + 1)]
        if len(timetable[:timetable.index(tmp)]) + timetable.count(tmp) + 1 >= m:
            print(len(timetable[:timetable.index(tmp)]), timetable.count(tmp))
            tmp = int(tmp[:2]) * 60 + int(tmp[3:]) - 1
            h = str(tmp // 60).zfill(2)
            m = str(tmp % 60).zfill(2)
            answer = h + ':' + m
        else:
            answer = tmp
    else:
        answer = '09:00'
    return answer


print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))