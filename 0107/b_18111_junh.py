from statistics import mean
import sys

input = sys.stdin.readline

def solution(N, M, B, avg, mat):
    time = 0
    inv = B
    for i in range(N):
        for j in range(M):

            if mat[i][j] < avg:
                block = avg - mat[i][j]
                time += block
                inv -= block
            else:           # elif X, else
                block = mat[i][j] - avg
                time += block * 2
                inv += block
            if min_time < time:
                return float('inf')

    if inv >=0 :
        return time
    else:
        return float('inf')


N, M, B = map(int, input().split())


mat = [list(map(int, input().split())) for _ in range(N)]
min_h = min(map(min, mat))
max_h = max(map(max, mat))
avg = round(mean(map(mean, mat)))

min_time = float('inf')
min_avg = 0
for h in range(max_h, min_h-1, -1):
    new_time = solution(N, M, B, h, mat)
    if new_time < min_time:
        min_time = new_time
        min_avg = h

print(min_time, min_avg)
