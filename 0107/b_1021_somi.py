N, M = map(int, input().split())
locations = list(map(int, input().split()))
q = list(i for i in range(1, N + 1))

cnt = 0
for target in locations:
    idx = q.index(target)

    if q[0] == target:
        q.pop(0)

    elif idx < len(q) / 2:
        cnt += idx
        q = q[idx + 1:] + q[:idx]

    else:
        cnt += (len(q) - idx)
        q = q[idx + 1:] + q[:idx]


print(cnt)