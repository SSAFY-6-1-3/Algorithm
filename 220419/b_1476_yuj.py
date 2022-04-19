E, S, M = map(int, input().split())
i, j, k = 1, 1, 1
ans = 1

while True:
    if i == E and j == S and k == M:
        break

    ans += 1
    i += 1
    j += 1
    k += 1
    if i == 16:
        i = 1
    if j == 29:
        j = 1
    if k == 20:
        k = 1

print(ans)