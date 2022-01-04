from collections import deque

N, M = map(int, input().split())
nums = list(map(int, input().split()))
deq = deque(list(i for i in range(1, N+1)))
result = 0                                     # pop 몇 번 했는지

for num in nums:
    left = 0
    for d in deq:
        if num == d:
            break
        else:
            left += 1
    right = N - left
    if left < right:
        for _ in range(left):
            deq.append(deq.popleft())
    else:
        for _ in range(right):
            deq.appendleft(deq.pop())
    result += min(left, right)
    deq.popleft()
    N -= 1

print(result)


