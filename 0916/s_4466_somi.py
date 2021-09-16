import sys
sys.stdin = open('s_4466_input.txt')


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input(). split())
    scores = list(map(int, input().split()))

    # max_score = 0
    for i in range(K):  # 선택정렬 (0 ~ K 까지만, 내림차순으로)
        max_index = i

        for j in range(i + 1, N):
            if scores[max_index] < scores[j]:
                max_index = j
        scores[i], scores[max_index] = scores[max_index], scores[i]

        # max_score += scores[max_index] # 이건 왜...안될까

    max_score = sum(scores[:K])

    print('#{} {}'.format(tc, max_score))
