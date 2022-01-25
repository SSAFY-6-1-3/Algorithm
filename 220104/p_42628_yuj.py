import heapq
def solution(operations):
    min_heap = []                               # 최대힙, 최소힙 두 개 만들기 (최대, 최소 뺴기 위해)
    max_heap = []

    for operation in operations:
        alpha, num = map(str, operation.split())
        if alpha == 'I':
            heapq.heappush(min_heap, int(num))
            heapq.heappush(max_heap, -int(num))
        else:                                   # 리스트가 안 비어있을 때 최솟값 삭제
            if num == '-1' and min_heap:
                x = heapq.heappop(min_heap)
                max_heap.remove(-x)
                heapq.heapify(max_heap)         # remove하면 heap 구조가 깨져서 heapify 이용

            elif num == '1' and max_heap:       # 리스트가 안 비어있을 때 최댓값 삭제
               y = heapq.heappop(max_heap)
               min_heap.remove(-y)
               heapq.heapify(min_heap)
    if min_heap:
        answer = [max(min_heap), min(min_heap)]
    else:
        answer = [0, 0]
    return answer

operations = ["I 6", "I 2", "I 1", "I 4", "I 5", "I 3", "D 1", "I 7", "D -1", "I 6", "D -1", "D -1"]
print(solution(operations))