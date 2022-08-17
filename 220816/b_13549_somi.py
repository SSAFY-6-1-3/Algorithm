N, K = map(int, input().split())
q = [(N, 0)]
visited = set()
visited.add(N)
while q:
    now, time = q.pop(0)
    if now == K:
        print(time)
        break

    candidate = ((now * 2, 0), (now - 1, 1), (now + 1, 1))
    for c in candidate:
        if 0 <= c[0] <= 100000 and c[0] not in visited:
            q.append((c[0], time + c[1]))
            visited.add(c[0])

