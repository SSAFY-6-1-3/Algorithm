import sys

input = sys.stdin.readline

def bfs(N, S, M):
    volumes = [set() for _ in range(N+1)]
    volumes[0].add(S)

    for song in range(N):
        for vol in volumes[song]:
            change = changes[song]
            if vol - change >= 0:
                volumes[song+1].add(vol - change)
            if vol + change <= M:
                volumes[song+1].add(vol + change)

    if not volumes[N]:
        return -1
    return max(volumes[N])


N, S, M = map(int, input().split())
changes = list(map(int, input().split()))
print(bfs(N, S, M))