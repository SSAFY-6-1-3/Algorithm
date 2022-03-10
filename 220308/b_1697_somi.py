N, K = map(int, input().split())

min = 100001
visited = [False for _ in range(min)]
visited[N] = True
q = [(N, 0)]

while q:
    now, time = q.pop(0)
    if now == K:
        print(time)
        break
    dir = [now + 1, now - 1, now * 2]
    for d in dir:
        if 0 <= d < min and not visited[d]:
            visited[d] = True
            q.append((d, time + 1))





