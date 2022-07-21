# 메모리 초과
# from collections import deque
#
# N = int(input())
# q = deque([0]*N)
# print(q)
# for i in range(N):
#     numbers = map(int, input().split())
#     for number in numbers:
#         minv = min(q)
#         if number > minv:
#             for _ in range(N):
#                 num = q.popleft()
#                 if num == minv:
#                     break
#                 else:
#                     q.append(num)
#             q.append(number)
#
# print(min(q))
import heapq

N = int(input())
q = []
for i in range(N):
    numbers = map(int, input().split())
    for number in numbers:
        if len(q) < N:
            heapq.heappush(q, number)
        else:
            if q[0] < number:
                heapq.heappop(q)
                heapq.heappush(q, number)
print(q[0])