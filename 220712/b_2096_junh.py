import sys

input = sys.stdin.readline

N = int(input())

start = list(map(int, input().split()))
maxs = start[:]
mins = start[:]

for i in range(1, N):
    now = list(map(int, input().split()))
    tmp_m = maxs[:]
    tmp_n = mins[:]
    mins = [900000]*3
    for j in range(3):
        for k in (-1, 0, 1):
            if j+k in range(3):
                maxs[j] = max(maxs[j], tmp_m[j+k] + now[j])
                mins[j] = min(mins[j], tmp_n[j+k] + now[j])

print(max(maxs), min(mins))
