# 시간 / 메모리 초과
import sys
sys.setrecursionlimit(10**6)


def write(name_idx, note):
    global ans

    if name_idx == n - 1:
        tmp = 0
        for i in range(len(note) - 1):
            tmp += note[i] ** 2
        ans = min(ans, tmp)
        return

    if sum(note) > ans:
        return

    if note[-1] >= names[name_idx] + 1:
        next_note = note[:]
        next_note[-1] -= names[name_idx] + 1
        write(name_idx + 1, next_note)

    next_note = note + [m - names[name_idx]]
    write(name_idx + 1, next_note)


n, m = map(int, input().split())
names = list(int(input()) for _ in range(n))
ans = m ** n
dp = list([m] * n for _ in range(m))
write(1, [m - names[0]])

print(ans)
