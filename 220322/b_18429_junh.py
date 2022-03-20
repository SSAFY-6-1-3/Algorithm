def exer(days, wgt, used):
    global ok
    if wgt < 500:
        return
    if days == N:
        ok += 1
        return

    for i in range(N):
        if i not in used:
            used.add(i)
            exer(days + 1, wgt - K + kits[i], used)
            used.remove(i)


N, K = map(int, input().split())

kits = sorted(map(int, input().split()), reverse=True)
ok = 0
exer(0, 500, set())
print(ok)


