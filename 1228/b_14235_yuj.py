import sys
import heapq
sys.stdin=open('input.txt')

# maxheap 사용
# def maxheap(j):
#     global heap
#
#     if j//2 in range(1, len(heap)):
#         if heap[j//2] < heap[j]:
#             heap[j//2], heap[j] = heap[j], heap[j//2]
#             maxheap(j//2)
#         return
#
#
# n = int(input())
# heap = [0]
# for _ in range(n):
#     presents = list(map(int, input().split()))
#
#     if presents[0] == 0:
#         if len(heap) == 1:
#             print(-1)
#         else:
#             print(heap.pop(1))
#             for j in range(1, len(heap)):
#                 maxheap(j)
#     else:
#         for i in range(presents[0]):
#             heap.append(presents[i+1])
#         for j in range(1, len(heap)):
#             maxheap(j)

heapq사용
n = int(input())
heap = []
for _ in range(n):
    presents = list(map(int, input().split()))
    if presents[0] == 0:
        if len(heap) == 0:
            print(-1)
        else:
            print(-heapq.heappop(heap))
    else:
        for i in range(presents[0]):
            heapq.heappush(heap, -presents[i+1])

# 리스트 사용
# n = int(input())
# heap = []
# for _ in range(n):
#     presents = list(map(int, input().split()))
#     if presents[0] == 0:
#         if not heap:
#             print(-1)
#         else:
#             print(heap.pop())
#     else:
#         heap.extend(presents[1:])
#         heap.sort()