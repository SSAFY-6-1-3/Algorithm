def cal(mid):
    res = 1
    total = mid
    for cost in costs:
        if total >= cost:
            total -= cost
        else:
            total = mid
            total -= cost
            res += 1
    return res

N, M = map(int, input().split())
costs = []
for _ in range(N):
    costs.append(int(input()))
start = max(costs)
end = sum(costs)
K = N * 10000
while start <= end:
    mid = (start + end) // 2
    cnt = cal(mid)
    # 최소 인출 금액이 클 수록 cnt가 커짐 -> 줄여야함
    if cnt <= M:
        K = min(mid, K)
        end = mid - 1
    else:
        start = mid + 1
print(K)