import sys

sys.stdin = open('s_3074.txt')

def check(fast, slow, li):
    answer = 0
    while fast <= slow:

        mid = (fast + slow)//2
        rst= sum(mid//desk for desk in li)

        if rst >= M:
            answer = mid
            slow = mid-1
        else:
            fast = mid+1
    return answer




T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    li = [int(input()) for _ in range(N)]
    min_sec = sum(1/k for k in li)
    min_sec = int(M / min_sec)
    print('#{} {}'.format(tc, check(min_sec, max(li)*M, li)))