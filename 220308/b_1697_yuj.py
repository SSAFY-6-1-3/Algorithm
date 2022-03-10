from collections import deque
N, K = map(int, input().split())
deq = deque([(N, 0)])
visited = [0] * 100001

while True:
    now, time = deq.popleft()

    if now == K:
        print(time)
        break

    if not visited[now]:
        visited[now] = 1

        if now-1 >= 0:
            deq.append((now-1, time+1))
        if 2*now < 100001:
            deq.append((2*now, time+1))
        if now+1 < 100001:
            deq.append((now+1, time+1))