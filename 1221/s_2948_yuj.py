import sys
sys.stdin=open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    result = set()
    for _ in range(2):
        result.update(list(map(str, input().split())))
    print('#{} {}'.format(tc, N+M-len(result)))