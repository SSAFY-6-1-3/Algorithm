import sys

input = sys.stdin.readline

def max_weight(N, ropes):
    wgt = ropes[0] * N

    for i in range(N):
        new_wgt = ropes[i] * (N-i)
        wgt = max(wgt, new_wgt)
    return wgt


N = int(input())
ropes = [int(input()) for _ in range(N)]
ropes.sort()
print(max_weight(N, ropes))