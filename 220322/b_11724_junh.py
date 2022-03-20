import sys
input = sys.stdin.readline

N, M = map(int, input().split())
sets = [{i} for i in range(1, N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    a_s, b_s = 0, 0
    for i in range(len(sets)):
        if a in sets[i]:
            a_s = i
        if b in sets[i]:
            b_s = i

    if a_s == b_s: continue
    sets[a_s].update(sets[b_s])
    sets.pop(b_s)


print(len(sets))

