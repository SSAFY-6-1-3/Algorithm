import heapq

N, K = map(int, input().split())
place = [0] * 200001
q = []
place[N] = 1
heapq.heappush(q, (0, N))
while q:
    time, now = heapq.heappop(q)
    if now == K:
        print(time)
        break
    if now*2 in range(200001) and not place[now*2]:
        place[now * 2] = 1
        heapq.heappush(q, (time, now*2))
    if now-1 in range(200001) and not place[now-1]:
        place[now - 1] = 1
        heapq.heappush(q, (time+1, now-1))
    if now+1 in range(200001) and not place[now+1]:
        place[now + 1] = 1
        heapq.heappush(q, (time+1, now+1))