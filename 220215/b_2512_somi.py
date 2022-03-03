N = int(input())
plans = list(map(int, input().split()))
M = int(input())

start = 0
end = max(plans)
while start <= end:
    money = (start + end) // 2
    total = sum(map(lambda x: min(x, money), plans))
    if total <= M:
        start = money + 1
    else:
        end = money - 1
print(end)
