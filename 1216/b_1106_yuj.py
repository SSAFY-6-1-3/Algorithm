C, N = map(int, input().split())
dp = [0] + [float('inf')] * (2000)          # C보다 큰 값에서 최소일 수도 있어서 범위 길게 설정
lst = []
for _ in range(N):
    cost, p = map(int, input().split())
    lst.append([p, cost])

lst.sort()                                  # 인원 단위 작은 것부터 정렬

for p, cost in lst:
    for i in range(1, 2000):
        if i-p in range(2000):
            dp[i] = min(dp[i], dp[i-p]+cost)

print(min(dp[C::]))