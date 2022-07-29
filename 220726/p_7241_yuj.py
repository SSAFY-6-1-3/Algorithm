# s->c, c->a, c->b를 구해서 더하기 (c는 중간지점)
# c 모든 경우의 수
def solution(n, s, a, b, fares):
    answer = float('inf')
    G = [[] for _ in range(n+1)]
    for fare in fares:
        G[fare[0]].append([fare[1], fare[2]])
        G[fare[1]].append([fare[0], fare[2]])

    def dijkstra(start):
        D = [float('inf')] * (n + 1)
        visited = [0] * (n + 1)
        D[start] = 0

        for _ in range(n):
            idx = -1
            minv = float('inf')
            for i in range(1, n+1):
                if not visited[i] and D[i] < minv:
                    idx = i
                    minv = D[i]
            visited[idx] = 1
            for v, val in G[idx]:
                if not visited[v] and D[idx] + val < D[v]:
                    D[v] = D[idx] + val
        return D

    d1 = dijkstra(s)
    for i in range(1, n+1):
        d2 = dijkstra(i)
        answer = min(answer, d1[i] + d2[a] + d2[b])
    return answer

print(solution(	6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(solution(6, 4, 5, 6, [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]))