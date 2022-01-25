T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    set_A = set(input().split())
    set_B = set(input().split())
    print('#{} {}'.format(tc, len(set_B.intersection(set_A))))
