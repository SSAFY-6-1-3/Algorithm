import sys

input = sys.stdin.readline
N = int(input())
switchs = [None] + list(map(int, input().split()))
M = int(input())

for _ in range(M):
    a, b = map(int, input().split())

    if a == 1:
        for i in range(b, N+1, b):
            switchs[i] = int(not switchs[i])
    else:
        for i in range(N//2 + 1):
            l, r = b-i, b+i
            if not 0 < l <= r < N+1 or switchs[l] != switchs[r]:
                break
            switchs[l] = switchs[r] = int(not switchs[l])

for i in range(1, N+1, 20):
    print(*switchs[i:min(i+20, N+1)])