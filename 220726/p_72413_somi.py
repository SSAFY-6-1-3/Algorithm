def dijkstra(n, graph, start):
    distances = [20000000] * (n + 1)
    distances[start] = 0
    q = [(distances[start], start)]

    while q:
        current_distance, current_destination = q.pop(0)

        if distances[current_destination] < current_distance:
            continue
        for i in range(1, n + 1):
            new_distance = current_distance + graph[current_destination][i]
            if new_distance < distances[i]:
                distances[i] = new_distance
                q.append((new_distance, i))
    return distances


def solution(n, s, a, b, fares):
    answer = 20000000
    graph = list([20000000] * (n + 1) for _ in range(n + 1))
    for fare in fares:
        u, v, cost = fare
        graph[u][v] = cost
        graph[v][u] = cost

    min_graph = [[]]
    for i in range(1, n + 1):
        min_graph.append(dijkstra(n, graph, i))

    for j in range(1, n + 1):
        answer = min(answer, min_graph[s][j] + min_graph[j][a] + min_graph[j][b])

    return answer

print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))