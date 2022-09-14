# 메모리 초과나서 visited에 전 위치를 기록
import heapq

N, K = map(int, input().split())
q = [(0, N)]
maxv = max(N, K)
visited = [-1] * (2*maxv+1)
visited[N] = [N]
while q:
    time, now = heapq.heappop(q)
    if now == K:
        print(time)
        lst = [K]
        s = K
        while s != N:
            lst.append(visited[s])
            s = visited[s]
        print(*lst[::-1])
        break

    if now*2 in range(2*maxv+1) and visited[now * 2] == -1:
        heapq.heappush(q, (time + 1, now * 2))
        visited[now * 2] = now
    if now-1 in range(2*maxv+1) and visited[now - 1] == -1:
        heapq.heappush(q, (time + 1, now - 1))
        visited[now - 1] = now
    if now+1 in range(2*maxv+1) and visited[now + 1] == -1:
        heapq.heappush(q, (time + 1, now + 1))
        visited[now + 1] = now
