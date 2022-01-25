import sys

sys.stdin = open('s_4466_input.txt')

def calc(n, k, scores):
    rtn = 0
    scores.sort(reverse=True) # 역으로 정렬
    for i in range(k):
        rtn += scores[i] # 높은 순으로 k개 뽑아서 합침
    return rtn

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    scores = list(map(int, input().split()))
    print('#{} {}'.format(tc, calc(N, K, scores)))