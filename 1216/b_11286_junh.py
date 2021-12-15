import sys
import heapq

input = sys.stdin.readline

pl_mi = {}

heap = []
heapq.heapify(heap)

N = int(input())
for _ in range(N):
    n = int(input())
    if n:
        heapq.heappush(heap, abs(n))
        if pl_mi.get(n) != None:
            pl_mi[n] += 1
        else:
            pl_mi[n] = 1
    else:
        if heap:
            popped = heapq.heappop(heap)
            if pl_mi.get(-popped) != None and pl_mi.get(-popped) > 0:
                pl_mi[-popped] -= 1
                print(-popped)
            else:
                pl_mi[popped] -= 1
                print(popped)
        else:
            print(0)











#
# def heap_insert(heap, n):
#     heap.append(n)
#     i = len(heap)-1
#     while i//2:
#         p = i//2
#         if abs(heap[p]) > abs(heap[i]):
#             heap[p], heap[i] = heap[i], heap[p]
#             i //= 2
#         elif abs(heap[p]) == abs(heap[i]) and heap[p] > heap[i]:
#             heap[p], heap[i] = heap[i], heap[p]
#             i //= 2
#         else:
#             return
# def heap_pop(heap):
#     if len(heap) == 1: return 0
#     elif len(heap) == 2: return heap.pop()
#     rtn = heap[1]
#     heap[1] = heap.pop()
#     heapify(heap)
#     return rtn
#
# def heapify(heap):
#     idx = 1
#     while idx * 2 < len(heap):
#         left, right = idx * 2, idx * 2 + 1
#
#         if right < len(heap):
#             if abs(heap[left]) < abs(heap[right]):
#                 target = left
#             elif abs(heap[left]) > abs(heap[right]):
#                 target = right
#             elif abs(heap[left]) == abs(heap[right]):
#                 if heap[left] <= heap[right]:
#                     target = left
#                 else:
#                     target = right
#         else:
#             target = left
#
#         if abs(heap[target]) < abs(heap[idx]) or (abs(heap[target] == abs(heap[idx])) and heap[target] < heap[idx]):
#             heap[idx], heap[target] = heap[target], heap[idx]
#             idx = target
#         else:
#             break
#
# N = int(input())
#
# abs_heap = [None]
#
# for _ in range(N):
#     n = int(input())
#     if n:
#         heap_insert(abs_heap, n)
#     else:
#         print(heap_pop(abs_heap))


