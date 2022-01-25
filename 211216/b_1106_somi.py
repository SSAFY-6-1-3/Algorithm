
C, N = map(int, input().split())
max_cost = C * 100
customer = [max_cost] * (max_cost + 1)  # index가 고객 수, value가 비용
customer[0] = 0

for _ in range(N):
    cost, num = map(int, input().split())
    for i in range(num, max_cost + 1):
        customer[i] = min(customer[i], customer[i - num] + cost)

print(min(customer[C:]))