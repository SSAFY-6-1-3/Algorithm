import sys

sys.stdin = open('s_4466_input.txt')

def calc(n, k, scores):
    rtn = 0
    scores.sort(reverse=True)
    for i in range(k):
        rtn += scores[i]
    return rtn

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    scores = list(map(int, input().split()))
    print('#{} {}'.format(tc, calc(N, K, scores)))