N = int(input())
cards = list(map(int, input().split()))

evens = [0] * (N // 2)
odds = [0] * (N // 2)

evens[0] = cards[0]
odds[0] = cards[1]
for i in range(1, N // 2):
    evens[i] = evens[i - 1] + cards[i * 2]
    odds[i] = odds[i - 1] + cards[i * 2 + 1]

jh_sum = [0] + evens
fr_sum = [0] + odds
ans = evens[-1]

for j in range(N):
    if j % 2:  # 상대방 순서
        tmp = jh_sum[j // 2 + 1] + (fr_sum[-2] - fr_sum[j // 2])
    else:  # 정훈 순서
        tmp = jh_sum[j // 2] + (fr_sum[-1] - fr_sum[j // 2])
    ans = max(ans, tmp)
print(ans)
