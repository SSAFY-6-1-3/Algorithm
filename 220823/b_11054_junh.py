N = int(input())
li = list(map(int, input().split()))

dp_l, dp_r = [1] * N, [1] * N

for i in range(N):
    for j in range(i + 1, N):
        if li[i] < li[j]:
            dp_l[j] = max(dp_l[j], dp_l[i] + 1)

        if li[N - 1 - i] < li[N - 1 - j]:
            dp_r[N - 1 - j] = max(dp_r[N - 1 - j], dp_r[N - 1 - i] + 1)

answer = 0
for i in range(N):
    answer = max(answer, dp_l[i] + dp_r[i] - 1)

print(answer)

