import sys

input = sys.stdin.readline

dY = (1, 0, -1, 0)
dX = (0, 1, 0, -1)

def bfs(sy, sx, L, R, land, visited):
    visited[sy][sx] = True

    q = [(sy, sx)]
    qi = 0
    popul = 0

    while qi < len(q):

        y, x = q[qi]
        qi += 1

        popul += land[y][x]

        for d in range(4):
            ny, nx = y+dY[d], x+dX[d]
            if ny not in range(N) or nx not in range(N) or visited[ny][nx]:
                continue

            dif = abs(land[y][x] - land[ny][nx])
            if L <= dif <= R:
                q.append((ny, nx))
                visited[ny][nx] = True

    each_pop = popul // len(q)

    for y, x in q:
        land[y][x] = each_pop

    if len(q) > 1:
        return True
    return False


def solut(N, L, R, land):
    visited = [[False for _ in range(N)] for _ in range(N)]
    changed = False
    for r in range(N):
        for c in range(N):
            if visited[r][c]: continue
            if bfs(r, c, L, R, land, visited):
                changed = True

    if changed:
        return True
    return False



N, L, R = map(int, input().split())

land = [list(map(int, input().split())) for _ in range(N)]

day = 0
while True:
    if not solut(N, L, R, land):
        print(day)
        break
    day += 1