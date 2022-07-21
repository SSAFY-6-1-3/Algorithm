import heapq

T = int(input())
for _ in range(T):
    k = int(input())
    que = []
    for _ in range(k):
        iter, num = map(str, input().split())
        num = int(num)

        if iter == 'I':
            heapq.heappush(que, num)

        else:
            if num == 1 and que:
                heapq.heappop(que)

            elif num == -1 and que:
                heapq.heappop(-que)

    if que:
        print(f'{max(que)} {min(que)}')
    else:
        print('EMPTY')