
inp = list(map(int, input().split()))
N = inp[0]
moves = [(inp[1], 0, 1), (inp[2], 0, -1), (inp[3], 1, 0), (inp[4], -1, 0)]
answer = 0

def dfs(y, x, per, visited):
    global answer
    if len(visited) == N+1:
        answer += per
        return

    for d in range(4):
        mp, my, mx = moves[d]
        np = per * mp / 100
        ny, nx = y + my, x + mx

        if (ny, nx) in visited:
            continue
        visited.add((ny, nx))
        dfs(ny, nx, np, visited)
        visited.remove((ny, nx))

dfs(0, 0, 1, {(0, 0)})
print(answer)