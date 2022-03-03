num = 1
while True:
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0:
        break

    else:
        ans = 0
        ans += L * (V // P)
        ans += min(V % P, L)
        print('Case {}: {}'.format(num, ans))
        num += 1