import sys
import heapq
input = sys.stdin.readline


def update_q(q):
    while q and not have_num[q[0][1]]:
        heapq.heappop(q)


T = int(input())
for _ in range(T):
    k = int(input())
    minQ = []
    maxQ = []
    have_num = list(False for _ in range(k))
    for i in range(k):
        cal = input()
        if 'D 1' in cal:
            update_q(maxQ)
            if maxQ:
                have_num[maxQ[0][1]] = False
                heapq.heappop(maxQ)

        elif 'D -1' in cal:
            update_q(minQ)
            if minQ:
                have_num[minQ[0][1]] = False
                heapq.heappop(minQ)

        elif cal[0] == 'I':
            heapq.heappush(minQ, (int(cal.split()[1]), i))
            heapq.heappush(maxQ, (-int(cal.split()[1]), i))
            have_num[i] = True

    update_q(minQ)
    update_q(maxQ)

    if minQ and maxQ:
        print(-maxQ[0][0], minQ[0][0])
    else:
        print('EMPTY')


