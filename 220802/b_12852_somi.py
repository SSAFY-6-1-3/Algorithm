from collections import deque


def bfs(n):
    q = deque()
    q.append((n, [n]))

    while q:
        now, nums = q.popleft()

        if now == 1:
            return nums

        if not visited[now]:
            visited[now] = True
            if now % 3 == 0:
                q.append((now // 3, nums + [now // 3]))

            if now % 2 == 0:
                q.append((now // 2, nums + [now // 2]))

            q.append((now - 1, nums + [now - 1]))


N = int(input())
visited = [False] * (N + 1)
num_list = bfs(N)
print(len(num_list) - 1)
print(*num_list)
