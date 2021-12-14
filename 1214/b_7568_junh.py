
N = int(input())
li = [list(map(int, input().split()))+[1] for _ in range(N)]

answer = []

for a_idx in range(N):
    a = li[a_idx]
    for b_idx in range(a_idx, N):
        b = li[b_idx]
        if a[0]>b[0] and a[1]>b[1]:
            b[2] += 1
        elif a[0]<b[0] and a[1]<b[1]:
            a[2] += 1

for i in li:
    answer.append(i[2])
print(*answer)