

def bfs(sy, sx, L, R, land):
    pass


def solut(N, L, R, land):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    uni = 0
    for r in range(N):
        for c in range(N):
            if visited[r][c]: continue
            uni += 1
            bfs(r, c, L, R, land)







N, L, R = map(int, input().split())

land = [list(map(int, input().split())) for _ in range(N)]

print(land)