def solution(n, wires):

    tree = [[] for _ in range(n+1)]

    for wire in wires:
        a, b = wire
        tree[a].append(b)
        tree[b].append(a)

    return tree


    answer = -1
    return answer



print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))