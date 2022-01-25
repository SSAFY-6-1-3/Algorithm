def solution(a, b):
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']

    # days = b
    # for i in range(a - 1):
    #     days += month[i]

    days = sum(month[:a - 1]) + b

    return day[days % 7]

print(solution(5, 24))