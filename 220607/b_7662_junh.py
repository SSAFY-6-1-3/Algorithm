import heapq
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    min_hp, max_hp = [], []
    min_p, max_p = {}, {}
    heapq.heapify(min_hp)
    heapq.heapify(max_hp)

    for _ in range(k):
        c, n = input().strip().split()
        n = int(n)

        if c == 'I':
            heapq.heappush(min_hp, n)
            heapq.heappush(max_hp, -n)
        elif n == 1 and max_hp:
            while max_hp:
                popped = -heapq.heappop(max_hp)
                if not min_p.get(popped, 0):
                    max_p[popped] = max_p.get(popped, 0) + 1
                    break
                else:
                    min_p[popped] -= 1
        elif n == -1 and min_hp:
            while min_hp:
                popped = heapq.heappop(min_hp)
                if not max_p.get(popped, 0):
                    min_p[popped] = min_p.get(popped, 0) + 1
                    break
                else:
                    max_p[popped] -= 1
            # popped = heapq.heappop(min_hp)

    for m in max_hp:
        m = -m
        if min_p.get(m, 0):
            min_p[m] -= 1
            heapq.heappop(max_hp)
        else:
            max_n = m
            break

    for m in min_hp:
        if max_p.get(m, 0):
            max_p[m] -= 1
            heapq.heappop(min_hp)
        else:
            min_n = m
            break

    if not min_hp or not max_hp:
        print('EMPTY')
    else:
        print(max_n, min_n)