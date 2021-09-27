import sys
sys.stdin = open('s_4466_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int,input().split())
    scores = sorted(list(map(int,input().split())))              # list 정렬
    max_score = 0

    for idx in range(1, K+1):                                   # 제일 큰 값 K개 더해서 최댓값 구하기
        max_score += scores[-idx]

    print('#{} {}'.format(tc, max_score))

