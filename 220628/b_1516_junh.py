import sys

input = sys.stdin.readline
N = int(input())

li = [None] + [list(map(int, input().split())) for _ in range(N)]
time = [0] * (N + 1)

def build(n):
    if not time[n] :
        time[n] = li[n][0]
        max_time = 0
        for i in range(1, len(li[n])):
            if li[n][i] == -1: break
            max_time = max(max_time, build(li[n][i]))
        time[n] += max_time

    return time[n]


for i in range(1, N+1):
    print(build(i))
