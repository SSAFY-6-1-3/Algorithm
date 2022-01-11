N, r, c = map(int, input().split())
cnt = 0

while N > 1:
    z = 2 ** (N - 1)
    if 0 <= r < z:
        if 0 <= c < z:
            pass
        else:
            cnt += (z * z)
            c -= z
    else:
        if 0 <= c < z:
            cnt += (z * z) * 2
            r -= z
        else:
            cnt += (z * z) * 3
            r -= z
            c -= z

    N -= 1

if r == 0:
    if c == 0:
        print(cnt)
    else:
        print(cnt + 1)
else:
    if c == 0:
        print(cnt + 2)
    else:
        print(cnt + 3)
