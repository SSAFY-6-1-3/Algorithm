import heapq

N, K = map(int, input().split())

def seek():
    if N > K:
        return N - K
    dp = [999999] * 100001
    q = [(0, N)]
    heapq.heapify(q)

    while q:
        step, now = heapq.heappop(q)
        if now == K:
            return step
        tmp = now
        while 0 < tmp <= 50000 :
            tmp *= 2

            if dp[tmp] > step:
                dp[tmp] = step
                heapq.heappush(q, (step, tmp))


        for p in [now-1, now+1]:
            if p not in range(100001) or dp[p] <= step + 1 : continue
            dp[p] = step + 1
            heapq.heappush(q, (step+1, p))

print(seek())