import sys

sys.stdin = open('s_2948_input.txt')



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    A = set(input().split())
    B = set(input().split())
    ans = len(A.intersection(B))
    print('#{} {}'.format(tc, ans))
