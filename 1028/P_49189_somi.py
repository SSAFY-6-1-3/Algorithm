def solution(n, edge):
    arr = [[] for _ in range(n + 1)]  # 인접 리스트
    for road in edge:
        arr[road[0]].append(road[1])
        arr[road[1]].append(road[0])

    dist = [0, 0] + [20000] * (n - 1)  # 2 ~ n번 노드까지 최댓값으로 초기화

    q = [[1, 0]]
    while q:
        now, distance = q. pop(0)
        for node in arr[now]:
            if dist[node] == 20000:  # 아직 방문하지 않은 노드
                q.append([node, distance + 1])

            dist[node] = min(dist[node], distance + 1)


    max_dist = max(dist)
    answer = dist.count(max_dist)
    return answer

n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, edge))