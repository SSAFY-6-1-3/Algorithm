import sys

sys.stdin = open('s_12741_input.txt')

answer_st = ''
T = int(input())
for tc in range(1, T+1):
    a, b, c, d = map(int, input().split())
    start = max(a, c)
    end = min(b, d)
    if start < end:
        time = end - start
    else:
        time = 0
    # time = max(0, end - start)

    answer_st+='#{} {}\n'.format(tc, time)

print(answer_st)