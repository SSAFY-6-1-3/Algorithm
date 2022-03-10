N = int(input())
storage = []
max_L, max_H = 0, 0
for _ in range(N):
    L, H = map(int, input().split())
    max_L = max(L, max_L)
    max_H = max(H, max_H)
    storage.append([L, H])
sticks = [[0] * (max_L+1) for _ in range(max_H+1)]
for s in storage:
    l, h = s[0], s[1]
    for i in range(h):
        sticks[i][l] = 1

ans = 0
for x in range(max_H):
    for y in range(max_L):
        if sticks[x][y] == 0:
            ans += 1
        else:
            break

for r in range(max_H):
    for c in range(max_L, -1, -1):
        if sticks[r][c] == 0:
            ans += 1
        else:
            break

print(((max_L + 1) * max_H) - ans)