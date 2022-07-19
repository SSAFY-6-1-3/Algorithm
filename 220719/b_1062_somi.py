from itertools import combinations

N, K = map(int, input().split())
base = {'a', 'n', 't', 'c', 'i'}
words = list(set(input()[4:-4]) - base for _ in range(N))
cnt = 0

if K < 5:
    print(cnt)
elif K == 26:
    print(N)
else:
    alpha = set(chr(i) for i in range(97, 123))
    alpha_to_learn = alpha - base
    # K - 5 만큼 배울 수 있음
    # 추가로 배울 수 있는 알파벳은 alpha_to_learn
    alpha_combs = combinations(list(alpha_to_learn), K - 5)

    for alpha_comb in alpha_combs:
        tmp_cnt = 0
        tmp_learn = set(alpha_comb)
        for word in words:
            # if len(word - tmp_learn) == 0:  # 시간초과
            if not word.difference(tmp_learn):
                tmp_cnt += 1
        cnt = max(cnt, tmp_cnt)
    print(cnt)
