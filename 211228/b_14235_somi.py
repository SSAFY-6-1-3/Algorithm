import heapq

n = int(input())

heap = []
for _ in range(n):
    a = list(map(int, input().split()))

    if a[0] == 0:
        if not heap:
            print(-1)
        else:
            print(-heapq.heappop(heap))

    else:
        for num in a[1:]:
            heapq.heappush(heap, -num)
