def relationship(start):
    q = [start]
    kev = [0] * (N + 1)

    while q:
        now = q.pop(0)
        for p in friend[now]:
            if kev[p] == 0:
                q.append(p)
                kev[p] = kev[now] + 1
    return sum(kev)


N, M = map(int, input().split())

friend = list([] for _ in range(N + 1))
for _ in range(M):
    A, B = map(int, input().split())
    friend[A].append(B)
    friend[B].append(A)

result = [500000] * (N + 1)
for i in range(1, N + 1):
    cnt = relationship(i)
    result[i] = cnt

print(result.index(min(result)))