from collections import deque


def is_tree(s):
    q = deque([s])
    flag = True
    while q:
        now = q.popleft()
        if now in visited:
            flag = False
        visited.add(now)

        for nxt in graph[now]:
            if nxt in visited:
                continue
            q.append(nxt)

    return flag


t = 0
while True:
    t += 1
    n, m = map(int, input().split())
    if n == m == 0:
        break

    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        if a == b:
            continue
        graph[a].append(b)
        graph[b].append(a)

    visited = set()
    answer = 0
    for i in range(1, n+1):
        if i not in visited and is_tree(i):
            answer += 1

    if answer > 1:
        answer = f"A forest of {answer} trees."
    elif answer == 1:
        answer = "There is one tree."
    else:
        answer = "No trees."

    print(f"Case {t}: " + answer)
