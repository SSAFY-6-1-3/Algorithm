N = int(input())
dists = list(map(int, input().split()))
costs = list(map(int, input().split()))

now_cost = costs[0]
total_cost = 0
for i in range(1, N):
    total_cost += now_cost * dists[i-1]
    now_cost = min(now_cost, costs[i])

print(total_cost)

