WEEKDAY = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
MONTH =[0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def solution(a, b):
    days = b # 일 수에
    for m in range(a):
        days += MONTH[m] # 받은 월까지의 일 수를 더 한다.
    answer = WEEKDAY[days % 7] # 7로 %연산
    return answer


print(solution(5, 24))