def bfs(parent, visited, wire_list):
    q = [parent]
    cnt = 1
    visited[parent] = True
    while q:
        now = q.pop(0)
        for wire in wire_list[now]:
            if not visited[wire]:
                visited[now] = True
                cnt += 1
                q.append(wire)
    return cnt

def solution(n, wires):

    wires_list = [[] for _ in range(n + 1)]
    for w1, w2 in wires:
        wires_list[w1].append(w2)
        wires_list[w2].append(w1)

    answer = 100
    for w1, w2 in wires:
        visited = [False for _ in range(n + 1)]
        visited[w2] = True
        cnt1 = bfs(w1, visited, wires_list)
        cnt2 = n - cnt1
        answer = min(answer, abs(cnt1-cnt2))

    return answer

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))