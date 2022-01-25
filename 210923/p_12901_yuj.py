def solution(a, b):
    week = ['FRI','SAT','SUN', 'MON', 'TUE', 'WED','THU']
    month_31 = [1, 3, 5, 7, 8, 10, 12]
    month_30 = [4, 6, 8, 9, 11]
    day = 0
    for month in range(1,a):
        if month in month_31:
            day += 31
        elif month in month_30:
            day += 30
        else:
            day += 29
    day += b-1
    return week[day%7]

a, b = 5, 24
print(solution(a,b))