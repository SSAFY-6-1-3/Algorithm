# 이분탐색

N, K = map(int, input().split())
strings = list(int(input()) for _ in range(N))

start = 1
end = max(strings)
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for string in strings:
        cnt += string // mid

    if cnt >= K:
        start = mid + 1
    else:
        end = mid - 1

print(end)