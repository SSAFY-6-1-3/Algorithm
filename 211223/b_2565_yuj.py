import sys
N = int(input())

lines = [list(map(int, input().split())) for _ in range(N)]
lines.sort()
result = [1] * N
for i in range(N):
    result[i] = 1
    for j in range(0, i):
        if lines[j][1] < lines[i][1]:
            result[i] = max(result[i], result[j]+1)

print(N-max(result))