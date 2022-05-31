N, K = map(int, input().split())
coins = list(int(input()) for _ in range(N))

idx = N - 1
cnt = 0
while K:
    if coins[idx] > K:
        idx -= 1
        continue
    cnt += (K // coins[idx])
    K %= coins[idx]
print(cnt)