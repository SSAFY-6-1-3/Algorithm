
N = int(input())
cards = list(map(int, input().split()))
if len(cards) == 2:
    print(max(cards))
    exit()

cards[1] = max(cards[0] + cards[1], cards[0] + cards[-1], cards[-1] + cards[1])
# 그받 그주, 밑받 그주, 그받 밑주
for i in range(2, N):
    if i % 2:
        cards[i] = max(cards[i - 2] + cards[i], cards[i - 1] + cards[i], cards[i - 1] + cards[-1])

    else:
        cards[i] += cards[i - 2]

print(max(cards[N - 2], cards[N - 3]))