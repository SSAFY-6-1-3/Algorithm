from collections import deque
from copy import deepcopy

N, M = map(int, input().split())
dY = (1, 0, -1, 0)
dX = (0, 1, 0, -1)
org_mat = []
viruses = []
empty = 0
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        if line[j] == 0:
            empty += 1
        elif line[j] == 2:
            viruses.append((i, j))
    org_mat.append(line)

def bfs(comb):
    mat = deepcopy(org_mat)
    q = deque()
    for v in comb:
        virus = viruses[v]
        q.append(virus)
        mat[virus[0]][virus[1]] = 3
    left = empty
    sec = 0

    while q and left:
        tmp = deque()
        while q:
            y, x = q.popleft()

            for d in range(4):
                ny, nx = y + dY[d], x + dX[d]
                if ny not in range(N) or nx not in range(N) or mat[ny][nx] % 2:
                    continue
                if mat[ny][nx] == 0:
                    left -= 1
                mat[ny][nx] = 3
                tmp.append((ny, nx))
        q = tmp
        sec += 1
    if left:
        return float('inf')
    return sec


combs = deque([[i] for i in range(len(viruses))])
answer = float('inf')
while combs:
    comb = combs.pop()
    if len(comb) == M:
        answer = min(answer, bfs(comb))
    else:
        for i in range(comb[-1] + 1, len(viruses)):
            combs.append(comb + [i])
if answer == float('inf'):
    answer = -1
print(answer)

