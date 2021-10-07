import sys
import heapq
sys.stdin=open('input.txt')

# def binarytree(n):
#
#     if n//2 >= 1:
#         if heap[n] > heap[n//2]:
#             heap[n], heap[n//2] = heap[n//2], heap[n]
#         binarytree(n-1)
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     heap = [0]
#     result = []
#     for _ in range(N):
#         cal = input()
#         if len(cal) == 1:
#             if not heap[1]:
#                 result.append(-1)
#             else:
#                 result.append(heap[1])
#             heap[1] = 0
#             binarytree(len(heap)-1)
#         else:
#             a, b = map(int, cal.split())
#             heap.append(b)
#             binarytree(len(heap)-1)
#
#     print('#{}'.format(tc), *result)
#

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    heap = []
    result = []
    for _ in range(N):
        cal = input()
        if len(cal) == 1:
            pass
            if not heap:
                result.append(-1)
            else:
                result.append(-heap[0])
                heapq.heappop(heap)
        else:
            a, b = map(int, cal.split())
            heapq.heappush(heap, -b)


    print('#{}'.format(tc), *result)