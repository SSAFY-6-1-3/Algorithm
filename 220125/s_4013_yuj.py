import sys
sys.stdin=open('sample_input.txt')

# 반시계방향 돌기
def plus(n):
    for i in range(len(checks[n])):
        checks[n][i] = (checks[n][i]+1) % 8
    reds[n] = (reds[n]+1) % 8

# 시계방향 돌기
def minus(n):
    for i in range(len(checks[n])):
        checks[n][i] -= 1
        if checks[n][i] < 0:
            checks[n][i] = 7
    reds[n] = (reds[n]-1) % 8

def turn_left(num, clock):
    idx = [num]
    while num > 0:
        if wheels[num-1][checks[num-1][-1]] != wheels[num][checks[num][0]]:
            idx.append(num-1)
        else:
            break
        num -= 1

    for i in range(len(idx)):
        if clock:
            if i % 2:
                plus(idx[i])
            else:
                minus(idx[i])
        else:
            if i % 2:
                minus(idx[i])
            else:
                plus(idx[i])

def turn_right(num, clock):
    idx = [num]
    while num < 3:
        if wheels[num+1][checks[num+1][0]] != wheels[num][checks[num][-1]]:
            idx.append(num+1)
        else:
            break
        num += 1

    for i in range(len(idx)):
        if clock:
            if i % 2:
                plus(idx[i])
            else:
                minus(idx[i])
        else:
            if i % 2:
                minus(idx[i])
            else:
                plus(idx[i])

T = int(input())
for tc in range(1, T+1):
    K = int(input())
    scores = [1, 2, 4, 8]
    wheels = []
    for _ in range(4):
        wheels.append(list(map(int, input().split())))

    checks = [[2], [6, 2], [6, 2], [6]]
    reds = [0, 0, 0, 0]
    for _ in range(K):
        num, clock = map(int, input().split())
        if num-1 > 0:
            turn_left(num-1, clock)
        if num-1 < 3:
            turn_right(num-1, clock)

    result = 0

    for i in range(4):
        result += wheels[i][reds[i]] * scores[i]

    print('#{} {}'.format(tc, result))
