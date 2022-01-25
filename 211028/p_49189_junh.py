from collections import deque

def solution(n, edge):
    tree = [[] for _ in range(n+1)]
    for line in edge:
        a, b = line[0], line[1]     # 인접 행렬을 이용하니 시간초과가 났다.
        tree[a].append(b)
        tree[b].append(a)
    distance = [-1] * (n+1)
    distance[1] = 0
    q = deque([1])
    while q:
        node = q.popleft()
        dist = distance[node]
        for nxt in tree[node]:
            if distance[nxt] == -1:
                distance[nxt] = dist+1
                q.append(nxt)

    max_dist = max(distance)

    answer = 0
    for n in range(1, n+1):
        if distance[n] == max_dist:
            answer +=1
    return answer
    return answer




print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))