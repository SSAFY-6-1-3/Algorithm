
def solution(n, wires):

    tree = [[False for _ in range(n+1)] for _ in range(n+1)]

    for wire in wires:
        a, b = wire
        tree[a][b] = tree[b][a] = True

    def wire_cut_dfs(w_a, w_b):
        stack = [1]
        idx = 0
        group = 1
        while idx < len(stack):
            a = stack[idx]
            for b in range(1, n+1):
                if (a==w_a and b==w_b) or (a==w_b and b==w_a): continue
                if tree[a][b] and b not in stack:
                    group += 1
                    stack.append(b)
            idx +=1

        return abs((n-group) - group)

    answer = n
    for wire in wires:
        answer = min(answer, wire_cut_dfs(wire[0], wire[1]))

    return answer



print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))