import sys

sys.stdin = open('s_4013_input.txt')

def move(now, prev, dir):
    to_l, to_r = wheels[now][6], wheels[now][2]

    if dir == -1:
        wheels[now] = wheels[now][1:] + wheels[now][:1]
    else:
        wheels[now] = wheels[now][7:] + wheels[now][:7]

    if prev <= now and now < 4:

        if to_r != wheels[now+1][6]:
            move(now + 1, now, -dir)

    if prev >= now and now > 1:

        if to_l != wheels[now-1][2]:
            move(now - 1, now, -dir)


T = int(input())

for tc in range(1, T+1):
    K = int(input())
    wheels = [None]
    for _ in range(4):
        wheels.append(list(map(int, input().split())))

    for _ in range(K):
        w, d = map(int, input().split())
        move(w, w, d)

    point = 0
    for i in range(1, 5):
        point += wheels[i][0] * (2**(i-1))

    print('#{} {}'.format(tc, point))