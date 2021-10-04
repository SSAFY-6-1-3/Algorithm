import sys
import heapq

sys.stdin = open('s_2930.txt')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    heap = []
    heapq._heapify_max(heap)
    result = []

    for _ in range(N):
        inp = list(map(int, input().split()))
        if inp[0] == 2:
            if heap:
                result.append(-heapq.heappop(heap)) # heapq는 최소 힙이라서 최대힙으로 사용하기 위해 -를 해서 사용
            else:
                result.append(-1)
        else:
            num = inp[1]
            heapq.heappush(heap, -num)
    print('#{}'.format(tc), *result)