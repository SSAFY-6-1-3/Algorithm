def solution(a, b):
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    mon = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    d_sum = 0
    for i in range(a):  # a-1월까지의 모든 일수 더하기
        d_sum += mon[i]
    d_sum = (d_sum + b - 1) % 7  # 요일이니까 7로 나눈 나머지 구하기
    answer = day[d_sum]
    return answer


print(solution(5, 24))
