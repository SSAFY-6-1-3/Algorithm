from collections import deque

K = int(input())

li = deque()
g_mx, s_mx = 0,0

for i in range(6):
    li.append(int(input().split()[1]))

    if i%2:
        s_mx = max(s_mx, li[i])
    else:
        g_mx = max(g_mx, li[i])


while li[0] not in (g_mx, s_mx) or li[1] not in (g_mx, s_mx):
    li.append(li.popleft())


big = li[0] * li[1]
sml = li[3] * li[4]

print((big - sml) * K)
