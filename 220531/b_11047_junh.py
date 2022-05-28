import sys

input = sys.stdin.readline

N, K = map(int, input().split())

coins = [int(input()) for _ in range(N)][::-1]
cnt = 0

for coin in coins:
    use = K // coin
    K -= use*coin
    cnt += use

print(cnt)
