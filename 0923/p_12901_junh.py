WEEKDAY = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
MONTH =[0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def solution(a, b):
    days = b
    for m in range(a):
        days += MONTH[m]
    answer = WEEKDAY[days % 7]
    return answer


print(solution(5, 24))