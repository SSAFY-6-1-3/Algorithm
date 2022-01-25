import sys
sys.stdin = open('s_13038_input.txt')


def get_day(i):
    attend = 0
    now = i
    day = 0

    while attend != n:
        if classes[now] == 1:
            attend += 1
        now = (now + 1) % 7
        day += 1

    return day


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    classes = list(map(int, input().split()))

    days = []
    for i in range(7):
        days.append(get_day(i))

    print('#{} {}'.format(tc, min(days)))
























