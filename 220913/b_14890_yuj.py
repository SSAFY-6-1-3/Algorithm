def check(lst):
    checked = [0] * N
    idx = 1
    while idx < N:
        if abs(lst[idx] - lst[idx-1]) > 1:
            return 0
        elif lst[idx] - lst[idx-1] == 1:
            for k in range(1, L+1):
                prev = idx - k
                if prev in range(N) and not checked[prev] and lst[prev] == lst[idx-1]:
                    checked[prev] = 1
                else:
                    return 0
        elif lst[idx-1] - lst[idx] == 1:
            for k in range(L):
                next = idx + k
                if next in range(N) and lst[next] == lst[idx]:
                    checked[next] = 1
                else:
                    return 0
        idx += 1
    return 1

N, L = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for r in range(N):
    if check(matrix[r]):
        ans += 1
    tmp = []
    for c in range(N):
        tmp.append(matrix[c][r])
    if check(tmp):
        ans += 1
print(ans)