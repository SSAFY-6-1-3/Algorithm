import sys
from itertools import combinations
sys.stdin=open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, B = map(int,input().split())
    height = list(map(int, input().split()))
    minv = B

    sum_result = []
    for _ in range(1, N+1):
        sum_result += (list(combinations(height, _)))

    for result in sum_result:
        if sum(result) >= B:
            if abs(sum(result) - B) < minv:
                minv = sum(result) - B


    print('#{} {}'.format(tc, minv))