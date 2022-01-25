import sys
sys.stdin = open('s_5550.txt')

T = int(input())
for tc in range(1, T + 1):
    frogs = input()
    sound = {
        'c': 0,
        'r': 1,
        'o': 2,
        'a': 3,
        'k': 4
    }
    croak = [0] * 5
    cnt = 0
    for alpha in frogs:
        index = sound[alpha]

        if alpha != 'k':
            croak[index] += 1

        if alpha != 'c':
            croak[index - 1] -= 1

            if croak[index - 1] == -1:
                cnt = -1
                break

        cnt = max(cnt, sum(croak))

    if croak != [0, 0, 0, 0, 0]:
        cnt = -1
    print('#{} {}'.format(tc, cnt))
