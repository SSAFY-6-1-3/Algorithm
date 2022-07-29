from collections import deque


def solution(n, s, a, b, fares):
    tree = [[0]*(n+1) for _ in range(n+1)]

    for aa, bb, d in fares:
        tree[aa][bb] = tree[bb][aa] = d

    def bfs(dep, dest):
        q = deque([(dep, 0)])
        visited = [float('inf')] * (n+1)

        while q:
            now, cost = q.popleft()

            for nxt in range(1, n+1):
                if not tree[now][nxt]:
                    continue
                new_cost = cost + tree[now][nxt]
                if visited[nxt] <= new_cost:
                    continue

                visited[nxt] = new_cost
                if dest and nxt == dest:
                    continue
                q.append((nxt, new_cost))

        if dep == dest:
            visited[dep] = 0
        return visited

    from_s = bfs(s, None)
    answer = from_s[a] + from_s[b]
    for mid in range(1, n+1):
        from_mid = bfs(mid, mid)
        answer = min(answer, from_s[mid]+from_mid[a]+from_mid[b])
    return answer





print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(solution(6, 4, 5, 6, [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]))
