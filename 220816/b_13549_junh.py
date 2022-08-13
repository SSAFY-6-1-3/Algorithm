from collections import deque

N, K = map(int, input().split())


def seek():
    if N > K:
        return N - K
    q = deque([(N, 0)])
    visited = {N,}
    max_n = 999999
    while q:
        now, step = q.popleft()

        if now >= max_n:
            continue
        for p in [now-1, now+1]:
            if p in visited: continue
            visited.add(p)

            if p == K:
                return step+1

            q.append((p, step+1))

        tmp = now
        while tmp < min(K, 100000) :
            tmp *= 2

            if tmp == K:
                return step
            if tmp in visited: continue
            visited.add(tmp)
            q.append((tmp, step))

            if K < tmp < max_n:
                max_n = tmp
                break
print(seek())