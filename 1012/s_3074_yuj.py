import sys
sys.stdin=open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    counter = sorted(list(int(input()) for _ in range(N)))

    answer = []
    l, r = counter[0], counter[0] * M

    while l < r-1:
        mid = (l+r) // 2

        people = 0
        for c in counter:
            people += mid // c
        if people < M:
            l = mid
        else:
            r = mid

    print('#{} {}'.format(tc, r))