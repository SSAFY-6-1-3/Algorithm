N, M = map(int, input().split())
li = sorted(map(int, input().split()))

def dfs(permu):
    if len(permu) == M:
        print(*permu)
        return
    for n in li:
        if n not in permu:
            dfs(permu + [n])

dfs([])