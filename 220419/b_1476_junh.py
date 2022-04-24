
E, S, M = map(int, input().split())
# 15 28 19
N = 1

while True:
    if not (N-E)%15 and not (N-S)%28 and not (N-M) % 19:
        print(N)
        exit()
    N += 1